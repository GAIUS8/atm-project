from django.core.management.base import BaseCommand
from calculus.models import RawData


class Command(BaseCommand):
    def handle(self, *args, **options):
        f = open("bubble_jack_raw_data.csv", "r")

        is_first = True
        while True:
             line = f.readline()
             if is_first:
                 is_first = False
                 pass
             else:
                 data_list = line.split(',')
                 RawData.objects.create(
                     round=data_list[0],
                     date_local=data_list[1],
                     num1=data_list[2],
                     num2=data_list[3],
                     num3=data_list[4],
                     num4=data_list[5],
                     num5=data_list[6],
                     num6=data_list[7],
                     bonus=data_list[8],
                     first_win=int(data_list[9]),
                     second_win=int(data_list[10]),
                     third_win=int(data_list[11]),
                     fourth_win=int(data_list[12]),
                     last_win=int(data_list[13]),
                 )
             if not line:
                break
        f.close()
