# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME


if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyKingKeltner import KkStrategy
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    
    # 创建回测引擎
    engine = BacktestingEngine()
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20130101')
    engine.setEndDate('20171001')
    # 设置产品相关参数
    
    engine.setSlippage(0.2)     # 股指1跳
    engine.setRate(0.3/10000)   # 万0.3
    engine.setSize(300)         # 股指合约大小
    engine.setPriceTick(0.2)    # 股指最小价格变动

    # 设置使用的历史数据库
    engine.setDatabase(MINUTE_DB_NAME, 'rb0000')

    d = {
        'fastWindow':3,
        "slowWindow":4,
        }
    print ("  "+'argument' + str(d))

    engine.initStrategy(DoubleMaStrategy, d)

    # 开始跑回测
    engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()

    engine.clearBacktestingResult()
    

    
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

    # dict = {}
    # from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    # for fastWindow in range(3,30):    
    #     for slowWindow in range(fastWindow+1,50):
    #         # 在引擎中创建策略对象
    #         d = {
    #             'fastWindow':fastWindow,
    #             "slowWindow":slowWindow,
    #             }
    #         print ("  "+'argument' + str(d))

    #         engine.initStrategy(DoubleMaStrategy, d)

    #         # 开始跑回测
    #         engine.runBacktesting()

    #         # 显示回测结果
    #         d_r = engine.showBacktestingResult()
    #         dict[str(d)] = d_r['annualInterestRate']
    #         engine.clearBacktestingResult()

    # print(dict)
