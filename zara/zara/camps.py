# from django.core.management.base import BaseCommand
# from django.utils import timezone
import json
import os
import pprint
import re
import copy
# from django.contrib import messages
from facebook_business import FacebookSession
from facebook_business import FacebookAdsApi
from facebook_business.adobjects.campaign import Campaign as AdCampaign
from facebook_business.adobjects.adaccountuser import AdAccountUser as AdUser
from facebook_business.adobjects.adaccount import AdAccount
# from django.db.models import Count, Sum, Avg
# from django.db.models import Q
# from dashboard.models import Campaign
from datetime import date, datetime
from dateutil.relativedelta import relativedelta as relativedelta


pp = pprint.PrettyPrinter(indent=4)
this_dir = os.path.dirname(__file__)
config_filename = os.path.join(this_dir, '../../config.json')

config_file = open(config_filename)
config = json.load(config_file)
config_file.close()

### Setup session and api objects
session = FacebookSession(
    config['app_id'],
    config['app_secret'],
    config['access_token'],
)
api = FacebookAdsApi(session)

class Command(BaseCommand):
    help = 'Gets Campaign data from Facebook'
    # def add_arguments(self, parser):
    #     parser.add_argument('insta', nargs='+', type=str)

    def handle(self, *args, **kwargs):
        FacebookAdsApi.set_default_api(api)

        # print('\n\n\n********** Reading objects example. **********\n')

        # Pro tip: Use list(me.get_ad_accounts()) to make a list out of
        # all the elements out of the iterator
        business_account = AdAccount(config['act_id'])
        business_account.remote_read(fields=[AdAccount.Field.tos_accepted])

        camp = business_account.get_campaigns()

        # for attr, value in camp.__dict__.items():
        #     print(attr, 'campaign_name')
        for campaign in camp:
            get_camp_insights = campaign.get_insights(fields=[
                                    'campaign_name',
                                    'impressions',
                                    'clicks',
                                    'unique_clicks',
                                    'actions',
                                    'spend',
                                    'cpm',
                                    
                                ]) 
                
            # print("Testing "+str(get_camp_insights))
            if (bool(get_camp_insights)==True):
                client = get_camp_insights[0]['campaign_name']
                # print(get_camp_insights)
                imp_ressions = get_camp_insights[0]['impressions']
                spend = get_camp_insights[0]['spend']
                date_start = get_camp_insights[0]['date_start']
                date_stop = get_camp_insights[0]['date_stop']
                client = client.replace(' - ','@@')
                
                split_array = client.split('@@')
                
                damo = date.today()
                
                bill_month = '{:02}'.format(damo.month)
                bill_year = '{:04}'.format(damo.year)
                bill_date = '0'

                for value in split_array:
                    if 'BD' in value:
                        if len(value)==3 or len(value)==4:
                            bill_date = value.replace('BD','')
                            # bill_date = bill_year+'-'+bill_month+'-'+bill_date
                            if bill_month == '02' and bill_date > '28':
                                bill_date = '28'
                            bill_date = bill_year+'-'+bill_month+'-'+bill_date
                    else:
                        continue
                if split_array[0][1:5] == 'TEST':
                    client_id = '9876'
                else:
                    client_id = (re.findall(r'\d+', client.split('@@')[0])[0])
                client_name = (client.split('@@')[0].split('] ')[1].strip())                
                try:
                    if 'for ' in client:
                        target_impressions = int((re.findall(r'\d+',client.split('for ')[1])[0]))
                    else:
                        target_impressions = int((re.findall(r'\d+',client.split('@@')[1])[0]))
                except:
                    target_impressions = 0

                status = 'na'

                days = (datetime.now().date() - datetime.strptime(bill_date, "%Y-%m-%d").date()).days
                if days < 0:
                    bill_datea = datetime.strptime(bill_date, "%Y-%m-%d")
                    bill_dateaa = bill_datea + relativedelta(months=-1)
                    days = (datetime.now() - bill_dateaa).days

            
                days_range_dict = {15:10,16:20,17:30,18:40,19:50,20:60,21:70,22:80,23:90,24:100}
                
                if target_impressions>0:
                    get_percent = (int(imp_ressions)/target_impressions)*100
                    #print(days_range_dict)
                    if get_percent>250:
                        status = 'co'
                    elif get_percent>=120 and get_percent <=250:
                        status = 'ov'
                    elif days > 17 and days < 25:
                        if get_percent<120 and days > 14 and days < 25:
                            if(days_range_dict[days]):
                                status = 'ot'
                            else:
                                status = 'cu'
                        else:
                            status = 'cu'
                    elif get_percent<120 and days > 14 and days < 25:
                        if(days_range_dict[days]):
                            status = 'ot'
                        elif days > 14 and days < 18:
                            if(days_range_dict[days]):
                                status = 'un'
                    elif days > 9 and days < 15:
                        if imp_ressions==0:
                            status = 'un'
                    else:
                        pass
                else:
                    get_percent = 0
                    pass

                # print(status)

                app_tag = 'resultli'
                data = {
                    'spend' : spend,
                    'target_impressions' : target_impressions,
                    'date_start' : date_start,
                    'date_stop' :date_stop,
                    'impressions' : imp_ressions,
                    'client_id': client_id,
                    'client_name' : client_name,
                    'bill_date' : bill_date,
                    'percentage' : get_percent,
                    'status':status,
                    'app_tag': app_tag,
                    'days':days
                    }

                
                print(data)
                # instance = Campaign(**data)
                # instance.save()
                # print(instance)
                    