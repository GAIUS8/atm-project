from django.core.management.base import BaseCommand
from calculus.models import RawData, Population, UpdateRecord
from decimal import Decimal
import random, datetime, pprint


class Command(BaseCommand):
    def handle(self, *args, **options):
        # 랜덤한 숫자 6개를 만든다 1~ 45개 중 중복이 안되게 45개를 뽑는다. - 한 1000개쯤 뽑아서 이걸 평가해서 제일 높은 점수 상위 5개를 가져온다.
        # 해당 번호가 얼마나 당첨될지 평가한다.
        # 번호 평가 모형을 설계해야 한다.

        # 각 개별 숫자들에 대한 평가
        # ex) 1과 친한 숫자는 뭐 2,3과 친한 숫자는 뭐
        # 1부터 45까지 몇번나왔는지 가중치 0.1
        # 1,2 조합이 몇번 나왔는지 가중치 0.2
        # 1,2,3 조합이 몇번 나왔는지 가중치 0.3
        # 봄345 여름678 가을91011 겨울1212인지 봄1 여름2 가을3 겨울4
        
        last_update = UpdateRecord.objects.last()
        is_go = False
        is_first = False
        start_day = None
        if not last_update:
            is_go = True
            is_first = True
            start_day = RawData.objects.order_by('date_local').first().date_local
            print("Raw DATA first input")
        else:
            date_local_raw_db = RawData.objects.order_by('-date_local').first().date_local
            latest_updated_day = last_update.last_snyc_date
            if date_local_raw_db > latest_updated_day:
                is_go = True
                start_day = latest_updated_day
                print("RAW DATA ADDED!! NEW UPDATE!!")
            else:
                print("ALREADY UPDATED!")
        
        # Population 생성 및 업데이트
        if is_go:
            if is_first:
                dataset = RawData.objects.filter(date_local__gte=start_day).values_list('date_local', 'num1','num2', 'num3', 'num4', 'num5', 'num6')
            else:
                dataset = RawData.objects.filter(date_local__gt=start_day).values_list('date_local', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6')

            latest_date = RawData.objects.order_by('date_local').last().date_local

            for data in dataset:
                month = data[0].month
                if month in (3, 4, 5):
                    season = 1
                elif month in (6, 7, 8):
                    season = 2
                elif month in (9, 10, 11):
                    season = 4
                else:
                    season = 4
    
                data = data[1:]
                name_list = ['{i}:::::'.format(i=i) for i in data] + \
                            ['{i}:{j}::::'.format(i=i, j=j) for i in data for j in data[data.index(i):] if i != j] + \
                            ['{}:{}:{}:::'.format(i, j, k) for i in data for j in data[data.index(i):] for k in data[data.index(j):] if i != j and j != k] + \
                            ['{}:{}:{}:{}::'.format(i,j,k,l) for i in data for j in data[data.index(i):] for k in data[data.index(j):] for l in data[data.index(k):] if i != j and j != k and k != l] + \
                            ['{}:{}:{}:{}:{}:'.format(i,j,k,l,h) for i in data for j in data[data.index(i):] for k in data[data.index(j):] for l in data[data.index(k):] for h in data[data.index(l):] if i != j and j != k and k != l and l != h] + \
                            ['{}:{}:{}:{}:{}:{}'.format(data[0], data[1], data[2], data[3], data[4], data[5])]
                
                for name in name_list:
                    try:
                        depth = name.split(':').index('')
                    except ValueError:
                        depth = 6
                    query = Population.objects.filter(name=name, season=season).first()
                    if not query:
                        Population.objects.create(
                            name=name,
                            counts=1,
                            depth=depth,
                            season=season,
                        )
                    else:
                        query.counts = query.counts + 1
                        query.save(update_fields=['counts'])
            
            UpdateRecord.objects.create(
                last_snyc_date=latest_date,
            )
        # make random number
        candidate_list = self.make_candidates
        
        # season evaluation model
        evaluated_list = []
        month = datetime.datetime.now().month
        if month in (3, 4, 5):
            season_now = 1
        elif month in (6, 7, 8):
            season_now = 2
        elif month in (9, 10, 11):
            season_now = 4
        else:
            season_now = 4
            
        name_base_dict, name_season_base_dict = self.population_settings
        
        for candidate in candidate_list:
            name_list = ['{i}:::::'.format(i=i) for i in candidate] + \
                        ['{i}:{j}::::'.format(i=i, j=j) for i in candidate for j in candidate[candidate.index(i):] if i != j] + \
                        ['{}:{}:{}:::'.format(i, j, k) for i in candidate for j in candidate[candidate.index(i):] for k in candidate[candidate.index(j):] if i != j and j != k] + \
                        ['{}:{}:{}:{}::'.format(i, j, k, l) for i in candidate for j in candidate[candidate.index(i):] for k in candidate[candidate.index(j):] for l in candidate[candidate.index(k):] if i != j and j != k and k != l] + \
                        ['{}:{}:{}:{}:{}:'.format(i, j, k, l, h) for i in candidate for j in candidate[candidate.index(i):] for k in candidate[candidate.index(j):] for l in candidate[candidate.index(k):] for h in candidate[candidate.index(l):] if i != j and j != k and k != l and l != h] + \
                        ['{}:{}:{}:{}:{}:{}'.format(candidate[0], candidate[1], candidate[2], candidate[3], candidate[4], candidate[5])]
            
            score_chart = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

            for name in name_list:
                try:
                    depth = name.split(':').index('')
                except ValueError:
                    depth = 6
                
                if depth == 6 and name in name_base_dict:
                    pass
                else:
                    try:
                        record = name_season_base_dict[(name, season_now)]
                        score_chart['{}'.format(depth)] = score_chart['{}'.format(depth)] + record['counts']
                    except KeyError:
                        score_chart['{}'.format(depth)] = 0
         
            total_score = Decimal(score_chart["1"])/Decimal(45) * Decimal(0.01) + \
                          Decimal(score_chart["2"])/Decimal(45*44) * Decimal(0.31) + \
                          Decimal(score_chart["3"])/Decimal(45*44*43) * Decimal(0.31) + \
                          Decimal(score_chart["4"])/Decimal(45*44*43*42) * Decimal(0.31) + \
                          Decimal(score_chart["5"])/Decimal(45*44*43*42*41) * Decimal(0.06)
            
            evaluated_list.append((total_score, candidate))
        
        evaluated_list.sort(reverse=True)
        result = []
        temp = []
        for index, last_test in enumerate(evaluated_list):
            if index == 0:
                temp.append(last_test[1][0])
                result.append(last_test)
            elif len(result) < 10:
                if last_test[1][0] in temp:
                    pass
                else:
                    temp.append(last_test[1][0])
                    result.append(last_test)
            else:
                break
            
        pprint.pprint(result)
    
    @property
    def make_candidates(self):
        candidates = []
        sample = [i for i in range(1, 46)]
        while len(candidates) < 30000:
            result = random.sample(sample, 6)
            result.sort()
            if result in candidates:
                pass
            else:
                candidates.append(result)
        return candidates
    
    @property
    def population_settings(self):
        basic = Population.objects.all().values()
        name_base_dict = {}
        name_season_base_dict = {}
        for record in basic:
            name_base_dict[record['name']] = record
            name_season_base_dict[(record['name'], record['season'])] = record
        
        return name_base_dict, name_season_base_dict
