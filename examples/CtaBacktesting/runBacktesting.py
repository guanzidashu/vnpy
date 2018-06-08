# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME
import numpy as np


if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyPosDoubleMa import DoubleMaPosStrategy

    # 创建回测引擎
    engine = BacktestingEngine()
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20130101')
    engine.setEndDate('20171001')
    # 设置产品相关参数
    
    engine.setSlippage(0.0)     # 股指1跳
    engine.setRate(0.3/10000)   # 万0.3
    # engine.setSize(300)         # 股指合约大小
    engine.setPriceTick(0.2)    # 股指最小价格变动
    engine.setMarginRatio(1)

    # # 设置使用的历史数据库
    engine.setDatabase(MINUTE_DB_NAME, 'rb0000')

    # d = {
    #     'fastWindow':20,
    #     "slowWindow":90,
    #     }
    # print ("  "+'argument' + str(d))

    # engine.initStrategy(DoubleMaPosStrategy, d)

    # # 开始跑回测
    # engine.runBacktesting()
    # print("xxxxx")
    # # 显示回测结果
    # engine.showBacktestingResult()

    # engine.clearBacktestingResult()
    

    
    # for kkDev in range(1,2):
    #     # 在引擎中创建策略对象
    #     d = {
    #         "kkLength":31,
    #         'kkDev':kkDev/10.0
    #         }
    #     print ("  "+'argument' + str(d))

    #     engine.initStrategy(KkStrategy, d)

    #     # 开始跑回测
    #     engine.runBacktesting()

    #     # 显示回测结果
    #     engine.showBacktestingResult()

    #     engine.clearBacktestingResult()
    x = 10 
    y = 20
    step = 5
    dict = {}
    array = np.zeros((x-1,y-1))
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    for fastWindow in range(step,x*step,step):    
        for slowWindow in range(fastWindow+step,fastWindow + y*step, step):
            # 在引擎中创建策略对象
            d = {
                'fastWindow':fastWindow,
                "slowWindow":slowWindow,
                }
            print ("  "+'argument' + str(d))

            engine.initStrategy(DoubleMaPosStrategy, d)

            # 开始跑回测
            engine.runBacktesting()

            # 显示回测结果
            d_r = engine.showBacktestingResult()
            dict[str(d)] = int(d_r['annualInterestRate']*100)
            array[fastWindow/step-1][(slowWindow - fastWindow)/step-1] = int(d_r['annualInterestRate']*100)
            engine.clearBacktestingResult()
            print(dict)


    print(dict)
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import json


    # for dic in dict:
         

    # y = np.array(list)
    # y = y.reshape((5,8))
    # df = pd.DataFrame(array,columns=[x for x in 'abcdefgh'])
    df = pd.DataFrame(array, columns=range(step, y*(step), step), index=range(step,x*(step),step))

    sns.heatmap(df,annot=True)
    plt.show()


