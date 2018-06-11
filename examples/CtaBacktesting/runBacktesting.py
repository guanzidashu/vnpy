# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME,DAILY_DB_NAME
import numpy as np


if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyPosDoubleMa import DoubleMaPosStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyPosMa import MaPosStrategy


    # 创建回测引擎
    engine = BacktestingEngine()
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20130101')
    engine.setEndDate('20171001')
    # 设置产品相关参数
    
    engine.setSlippage(0.0)     # 股指1跳
    engine.setRate(1.6/10000)   # 万0.3
    # engine.setSize(300)         # 股指合约大小
    engine.setPriceTick(0.2)    # 股指最小价格变动
    engine.setMarginRatio(1)

    # 设置使用的历史数据库
    engine.setDatabase(MINUTE_DB_NAME, 'IF0000')

    # d = {
    #     'fastWindow':35,
    #     "slowWindow":70,
    #     }
    # print ("  "+'argument' + str(d))

    # engine.initStrategy(MaPosStrategy, d)

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

    x_start = 1
    y_start = 1
    x = 15 
    y = 40
    step = 5
    dict = {}
    array = np.zeros((x-1,y-2))
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    for fastWindow in range(x_start*step,x*step,step):    
        for slowWindow in range(max(fastWindow+step,y_start*step),y*step, step):
            # 在引擎中创建策略对象
            d = {
                'fastWindow':fastWindow,
                "slowWindow":slowWindow,
                }
            print ("  "+'argument' + str(d))

            engine.initStrategy(MaPosStrategy, d)

            # 开始跑回测
            engine.runBacktesting()

            # 显示回测结果
            d_r = engine.showBacktestingResult()
            dict[str(d)] = int(d_r['annualInterestRate']*100)
            array[fastWindow/step-1][slowWindow/step-2] = int(d_r['annualInterestRate']*100)
            engine.clearBacktestingResult()
            print(dict)


    print(dict)
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns
    import json



    df = pd.DataFrame(array, columns=range(2*step, y*(step), step), index=range(step,x*(step),step))

    sns.heatmap(df,annot=True)
    plt.savefig(str(x)+ "_"+str(y)+'IFhuadianemaDoubleMaPosStrategy.png')

    plt.show()


    # from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
    # from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    # from vnpy.trader.app.ctaStrategy.strategy.strategyPosDoubleMa import DoubleMaPosStrategy

    # # 创建回测引擎
    # engine = BacktestingEngine()
    # # 设置引擎的回测模式为K线
    # engine.setBacktestingMode(engine.BAR_MODE)

    # # 设置回测用的数据起始日期
    # engine.setStartDate('20090327')
    # engine.setEndDate('20180611')
    # # 设置产品相关参数
    
    # engine.setSlippage(0)     # 股指1跳
    # engine.setRate(0/10000)   # 万1.6
    # # engine.setSize(300)         # 股指合约大小
    # engine.setPriceTick(0.2)    # 股指最小价格变动
    # engine.setMarginRatio(1)

    # # 设置使用的历史数据库
    # engine.setDatabase(DAILY_DB_NAME, 'rb0000')

    # d = {
    #     'fastWindow':54,
    #     "slowWindow":72,
    #     }
    # print ("  "+'argument' + str(d))

    # engine.initStrategy(DoubleMaPosStrategy, d)

    # # 开始跑回测
    # engine.runBacktesting()
    # print("xxxxx")
    # # 显示回测结果
    # engine.showBacktestingResult()

    # engine.clearBacktestingResult()


    # x = 6 
    # y = 35
    # step = 1
    # dict = {}
    # array = np.zeros((x-1,y-2))
    # from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    # for fastWindow in range(step+1,x*step,step):    
    #     for slowWindow in range(fastWindow+step,y*step, step):
    #         # 在引擎中创建策略对象
    #         d = {
    #             'fastWindow':fastWindow,
    #             "slowWindow":slowWindow,
    #             }
    #         print ("  "+'argument' + str(d))

    #         engine.initStrategy(DoubleMaPosStrategy, d)

    #         # 开始跑回测
    #         engine.runBacktesting()

    #         # 显示回测结果
    #         d_r = engine.showBacktestingResult()
    #         dict[str(d)] = int(d_r['annualInterestRate']*100)
    #         array[fastWindow/step-1][slowWindow/step-2] = int(d_r['annualInterestRate']*100)
    #         engine.clearBacktestingResult()
    #         print(dict)


    # print(dict)
    # import pandas as pd
    # import matplotlib.pyplot as plt
    # import seaborn as sns
    # import json



    # df = pd.DataFrame(array, columns=range(2*step, y*(step), step), index=range(step,x*(step),step))

    # sns.heatmap(df,annot=True)
    # plt.savefig(str(x)+ "_"+str(y)+'rbdayhuadianemaDoubleMaPosStrategy.png')

    # plt.show()