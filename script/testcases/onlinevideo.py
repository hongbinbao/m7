#!/usr/bin/python
# -*- coding:utf-8 -*- 

import unittest
import random
from uiautomatorplug.android import device as d

class OnlineVideoTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        #a watcher to aviod dialog block test
        d.watcher("AUTO_FC_WHEN_ANR").when(text="稍后升级").click(text="稍后升级")
        d.watcher("EXIT_VST_THIRD_APP").when(textContains="退出，真的不看了").click(text="退出，真的不看了")
        d.watcher("EXIT_SOHU_APP").when(textContains="主人，您真的要离开吗？记得常来看我呀").click(text="确定")
        d.watcher("PASS_NOTIFICATION").when(textContains="确认").click(text="确认")
        d.watcher("PASS_VST_UPDATE1").when(textContains="稍后更新").click(text="稍后更新")
        d.watcher("PASS_TOGIC_UPDATE").when(packageName='com.togic.livevideo', textContains="已阅读").press('enter','enter')
        d.watcher("PASS_VST_UPDATE2").when(textContains='根据国家现行政策规定').press('enter')
        d.watcher("PASS_ANR").when(textContains='关闭吗').click(text='确定')
        d.watcher("PASS_FC").when(textContains='停止运行').click(text='确定')
        d.wakeup()
        for i in xrange(3): 
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.sleep(1)
        d.press('home')
        for i in xrange(2):
            d.press('back')
            d.sleep(1)
    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        d.watchers.remove("AUTO_FC_WHEN_ANR")
        d.watchers.remove("EXIT_VST_THIRD_APP")
        d.watchers.remove("EXIT_SOHU_APP")
        d.watchers.remove("PASS_NOTIFICATION")
        d.watchers.remove("PASS_VST_UPDATE1")
        d.watchers.remove("PASS_VST_UPDATE2")
        d.watchers.remove("PASS_TOGIC_UPDATE")
        d.watchers.remove("PASS_ANR")
        d.watchers.remove("PASS_FC")
        for i in xrange(4):
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.sleep(1)
        d.press('home') 

    def testPlayOnlineVideo(self):
        """
        play video from "online video" and play 180 seconds
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视",  packageName='com.xiaomi.tv.desktop').exists, 'Online Video icon not found!'
        d(text="在线影视",  packageName='com.xiaomi.tv.desktop').sibling(className='android.view.View').click.wait()
        assert d(packageName="com.duokan.duokantv", resourceId="android:id/content").wait.exists(timeout=20000), 'launch online video failed!'
        for i in xrange(30):
            d.press('left')
            d.sleep(1)
        if  d.find('menu_hot_highlight_focus3.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus3.png', threshold=0.05, timeout=30):
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        elif  d.find('menu_hot_highlight_focus2.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus2.png', threshold=0.05, timeout=30) :
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        elif  d.find('menu_hot_highlight_focus.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus.png', threshold=0.05, timeout=30) :
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        else:
            assert False, "unable to get the matched picture!"
        d.expect('video_preview_sub_shoucang2.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        d.sleep(5)
        assert d(resourceId='com.xiaomi.mitv.player:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #play duration
        d.sleep(300)
        assert not d(textContains='播放失败').exists, 'video paly failed!'
        assert not d(textContains='无法获取视频地址').exists, 'unable to get video address!'
        #assert not d(textContains="正在读取视频信息").exists, 'reading video information!'        
        d.press('back')
        d.sleep(5)
        #d.expect('video_preview_sub_shoucang2.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayOnlineVideoLong(self):
        """
        play video from "online video" and play 1200 seconds
        """
        #d.start_activity('--activity-clear-task', component='com.duokan.duokantv/.MainActivity')
        assert d(text="在线影视",  packageName='com.xiaomi.tv.desktop').exists, 'Online Video icon not found!'
        d(text="在线影视",  packageName='com.xiaomi.tv.desktop').sibling(className='android.view.View').click.wait()
        assert d(packageName="com.duokan.duokantv", resourceId="android:id/content").wait.exists(timeout=20000), 'launch online video failed!'
        for i in xrange(30):
            d.press('left')
            d.sleep(1)
        if  d.find('menu_hot_highlight_focus3.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus3.png', threshold=0.05, timeout=30):
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        elif  d.find('menu_hot_highlight_focus2.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus2.png', threshold=0.05, timeout=30) :
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        elif  d.find('menu_hot_highlight_focus.png', threshold=0.05, timeout=30):
            d.press('down')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(3)
            d.press('enter') 
            d.sleep(5)
        elif  d.find('menu_hot_highlight_nofocus.png', threshold=0.05, timeout=30) :
            d.press('right')
            d.sleep(3)
            d.press('right')
            d.sleep(5)
            d.press('enter')
            d.sleep(5)
        else:
            assert False, "unable to get the matched picture!"
        d.expect('video_preview_sub_shoucang2.png', threshold=0.05 ,timeout=30)
        d.sleep(2)
        d.press('enter')
        d.sleep(10)
        assert d(resourceId='com.xiaomi.mitv.player:id/main_frame').wait.exists(timeout=30000), 'video not start!'
        #assert not d.find('video_preview_sub_shoucang.png', timeout=30), 'video not start!'
        #play duration
        d.sleep(600)
        assert not d(textContains='播放失败').exists, 'video paly failed!'
        assert not d(textContains='无法获取视频地址').exists, 'unable to get video address!'
        #assert not d(textContains="正在读取视频信息").exists, 'reading video information!'
        d.press('back')
        d.sleep(5)
        #d.expect('video_preview_sub_shoucang2.png', threshold=0.05 , timeout=30)
        d.press('back')

    def testPlayVideoFromVSTClient(self):
        """
        Suma: play a video from VST client
        Step1: click  "Togic" icon 
        Step2: verify the new screen was luanched successfully
        Step3: click a video label randomlly
        Step4: verify the new screen was luanched successfully
        Step4: click "play" icon  to play the video and play 300 sescondsvideo.
        """
        #APP1 VST
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(textContains="VST全聚合", packageName="com.xiaomi.tv.desktop").wait.exists(timeout=3000), "VST全聚合 not found on home screen"
        #d.start_activity('--activity-clear-task', component='net.myvst.v2/com.vst.itv52.v1.LancherActivity')
        d.start_activity('--activity-clear-task', component='net.myvst.v2/com.vst.itv52.v1.LancherActivity')
        #d(text="VST全聚合", packageName="com.xiaomi.tv.desktop").sibling(className='android.view.View').click.wait()
        assert d(text="推荐").wait.exists(timeout=30000), "VST-推荐 not found on screen"
        d.sleep(5)
        d.press('down')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('enter') 
        assert d(text="收藏").wait.exists(timeout=20000), "VST-收藏 not found on screen"
        d.press('enter')
        d.sleep(30)
        assert d(className='android.view.View').wait.exists(timeout=20000), 'VST-播放视频 未开始！'
        #play duration
        d.sleep(600)
        d.press('back')
        d.press('back')
        d.sleep(5)
        assert d(text="收藏").wait.exists(timeout=20000), "VST-收藏 not found on screen after stopping playing"
        d.press('back') 
        assert d(text="推荐").wait.exists(timeout=20000), "VST-推荐 not found on screen"
        d.press('back')
        d.sleep(2)
        d.press('enter')
        ##return to home and idle 30 seconds
        #d.sleep(10)
        #verify exit to home screen
        assert d(packageName="com.xiaomi.tv.desktop").wait.exists(timeout=10000), "fail to exit from VST!"

    def testPlayVideoFromTogicClient(self):
        """
        Suma: play a video from Togic client
        Step1: click  "Togic" icon 
        Step2: verify the new screen was luanched successfully
        Step3: click a video label randomlly
        Step4: verify the new screen was luanched successfully
        Step4: click "play" icon  to play the video and play 300 sesconds
        """
        #APP2 TOGIC
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(textContains="泰捷视频", packageName="com.xiaomi.tv.desktop").wait.exists(timeout=3000), "泰捷视频-图标 not found on home screen"
        d.start_activity('--activity-clear-task', component='com.togic.livevideo/com.togic.launcher.SplashActivity')
        assert d(packageName='com.togic.livevideo', text='影视').wait.exists(timeout=30000), "泰捷-影视菜单 not found on screen"
        d.sleep(5)
        if d(text='影视').focused:
            d.press('down')
            d.sleep(1)
        else:
            for i in xrange(16):
                d.press('left')
                d.sleep(1)
            if d(text='影视').focused:
                d.press('down')
                d.sleep(1)
        d.press('right')
        d.sleep(1)           
        d.press('right')
        d.sleep(1)
        d.press('enter')
        ##assert into film view
        ##play video
        d.sleep(3)
        assert d(resourceId='com.togic.livevideo:id/logo_text',text='电影').wait.exists(timeout=20000), '泰捷-电影-电影 界面进入失败！'
        assert d(text='最新电影').wait.exists(timeout=20000), '泰捷-电影-电影 列表无法获取！'
        #网络连接失败，请检查网络！com.togic.livevideo:id/empty_result
        for h in xrange(random.randint(0, 5)):
            d.press('right')
            d.sleep(1)
        for v in xrange(random.randint(0, 5)):
            d.press('down')
            d.sleep(1)           
        d.press('enter')
        d.sleep(5)
        assert d(resourceId='com.togic.livevideo:id/play',text='播放').wait.exists(timeout=30000), '泰捷-电影-电影-播放 进入失败！'
        #d(resourceId='com.togic.livevideo:id/play',text='播放').click()
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('enter')
        d.sleep(50)
        assert d(resourceId='com.togic.livevideo:id/video_layout').wait.exists(timeout=20000), '泰捷-电影-电影-播放-电影开始 失败！'
        #play duration
        d.sleep(600)
        ##return to home and idle 30 seconds
        for i in xrange(8):
            d.press('back')
            d.sleep(1)
        #exit to home screen
        assert d(packageName="com.xiaomi.tv.desktop").wait.exists(timeout=10000), "fail to exit from 泰捷!"


    def testPlayVideoBetweenApp_short(self):
        """
        Suma: play a video between VST and TOGIC. play 300 seconds for each video.
        Step1: click  "VST" and "TOGIC"
        Step2: verify the new screen was luanched successfully
        Step3: click the top video
        Step4: verify the new screen was luanched successfully
        Step4: click "play  icon"  to play the video.
        """
        #APP1 VST
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(textContains="VST全聚合", packageName="com.xiaomi.tv.desktop").wait.exists(timeout=3000), "VST全聚合 not found on home screen"
        #d.start_activity('--activity-clear-task', component='net.myvst.v2/com.vst.itv52.v1.LancherActivity')
        d.start_activity('--activity-clear-task', component='net.myvst.v2/com.vst.itv52.v1.LancherActivity')
        #d(text="VST全聚合", packageName="com.xiaomi.tv.desktop").sibling(className='android.view.View').click.wait()
        assert d(text="推荐").wait.exists(timeout=30000), "VST-推荐 not found on screen"
        d.sleep(5)
        d.press('down')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('enter') 
        assert d(text="收藏").wait.exists(timeout=20000), "VST-收藏 not found on screen"
        d.press('enter')
        d.sleep(30)
        assert d(className='android.view.View').wait.exists(timeout=20000), 'VST-播放视频 未开始！'
        #play duration
        d.sleep(600)
        d.press('back')
        d.press('back')
        d.sleep(5)
        assert d(text="收藏").wait.exists(timeout=20000), "VST-收藏 not found on screen after stopping playing"
        d.press('back') 
        assert d(text="推荐").wait.exists(timeout=20000), "VST-推荐 not found on screen"
        d.press('back')
        d.sleep(2)
        d.press('enter')
        #verify exit to home screen
        assert d(packageName="com.xiaomi.tv.desktop").wait.exists(timeout=10000), "fail to exit from VST!"

        ####switch to APP2
        #APP2 TOGIC
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(textContains="泰捷视频", packageName="com.xiaomi.tv.desktop").wait.exists(timeout=3000), "泰捷视频-图标 not found on home screen"
        d.start_activity('--activity-clear-task', component='com.togic.livevideo/com.togic.launcher.SplashActivity')
        assert d(packageName='com.togic.livevideo', text='影视').wait.exists(timeout=30000), "泰捷-影视菜单 not found on screen"
        d.sleep(5)
        if d(text='影视').focused:
            d.press('down')
            d.sleep(1)
        else:
            for i in xrange(16):
                d.press('left')
                d.sleep(1)
            if d(text='影视').focused:
                d.press('down')
                d.sleep(1)
        d.press('right')
        d.sleep(1)           
        d.press('right')
        d.sleep(1)
        d.press('enter')
        ##assert into film view
        ##play video
        d.sleep(3)
        assert d(resourceId='com.togic.livevideo:id/logo_text',text='电影').wait.exists(timeout=20000), '泰捷-电影-电影 界面进入失败！'
        assert d(text='最新电影').wait.exists(timeout=20000), '泰捷-电影-电影 列表无法获取！'
        #网络连接失败，请检查网络！com.togic.livevideo:id/empty_result
        for h in xrange(random.randint(0, 5)):
            d.press('right')
            d.sleep(1)
        for v in xrange(random.randint(0, 5)):
            d.press('down')
            d.sleep(1)           
        d.press('enter')
        d.sleep(5)
        assert d(resourceId='com.togic.livevideo:id/play',text='播放').wait.exists(timeout=30000), '泰捷-电影-电影-播放 进入失败！'
        #d(resourceId='com.togic.livevideo:id/play',text='播放').click()
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('enter')
        d.sleep(50)
        assert d(resourceId='com.togic.livevideo:id/video_layout').wait.exists(timeout=20000), '泰捷-电影-电影-播放-电影开始 失败！'
        #play duration
        d.sleep(600)
        ##return to home and idle 30 seconds
        for i in xrange(8):
            d.press('back')
            d.sleep(1)
        #exit to home screen
        assert d(packageName="com.xiaomi.tv.desktop").wait.exists(timeout=10000), "fail to exit from 泰捷!"




