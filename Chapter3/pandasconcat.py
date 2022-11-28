'''2022.10.23 study'''
import numpy as np
import pandas as pd

def main() :
    '''pandas4 main'''
    pop = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv')
    areas = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv')
    abbrevs = pd.read_csv('https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv')
    
    # print(pop.head())
    # print(areas.head())
    # print(abbrevs.head())
    merged = pd.merge(pop, abbrevs, how='outer', left_on='state/region', right_on='abbreviation')
    merged = merged.drop(columns = 'abbreviation', axis = 1)
    # print(merged.head())
    
    #아래는 해당 정보에서 null인 부분이 있는지
    # print(merged.isnull().any())
    # print(merged[merged['population'].isnull()].head())
    
    #여기는 state-abbrev에서 없는 데이터를 체크하고 해당 데이터를 연결하는 작업
    merged.loc[merged['state'].isnull(), 'state/region'].unique()
    merged.loc[merged['state/region'] == 'PR', 'state'] = 'Puerto Rico'
    merged.loc[merged['state/region'] == 'USA', 'state'] = 'United States'
    #print(merged.isnull().any())
    
    #abbrev 까지 추가
    final = pd.merge(merged, areas, on='state', how='left')
    #print(final.head())
    
    #United States 전체에 대한 데이터는 없으니 삭제
    #print(final['state'][final['area (sq. mi)'].isnull()].unique())
    
    final.dropna(inplace=True)
    print(final.head())
    
    #year 2010, ages = total 에 대한 데이터만 추출
    data2010 = final.query("year == 2010 & ages == 'total'")
    #print(data2010.head())
    
    data2010.set_index('state', inplace=True)
    density = data2010['population'] / data2010['area (sq. mi)']
    density.sort_values(ascending=False, inplace=True)
    #print(density.head())

def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c : [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)

if __name__ == "__main__" :
    main()
    