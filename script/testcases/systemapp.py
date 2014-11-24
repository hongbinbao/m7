#!/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from uiautomatorplug.android import device as d

class SystemAppTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        d.wakeup()
        for i in xrange(3): 
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.sleep(1)
        d.press('home')
        d.sleep(1)
        for i in xrange(3):
            d.press('back')
            d.sleep(1)

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        for i in xrange(5):
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.sleep(1)
        d.press('home')
        d.sleep(1)

    def  testLaunchAndExitVideo(self):
        assert d(text="在线影视", packageName='com.xiaomi.tv.desktop').exists, 'Online Video icon not found!'
        #d(text="在线影视", packageName='com.xiaomi.tv.desktop').sibling(className='android.view.View').click.wait()
        d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=0).click.wait()
        d.sleep(10)
        if  d.find('menu_hot_highlight_focus3.png', threshold=0.05, timeout=30) :
            pass
        elif  d.find('menu_hot_highlight_nofocus3.png', threshold=0.05, timeout=30):
            pass
        elif  d.find('menu_hot_highlight_focus2.png', threshold=0.05, timeout=30):
            pass
        elif  d.find('menu_hot_highlight_nofocus2.png', threshold=0.05, timeout=30) :
            pass
        elif  d.find('menu_hot_highlight_focus.png', threshold=0.05, timeout=30):
            pass
        elif  d.find('menu_hot_highlight_nofocus.png', threshold=0.05, timeout=30) :
            pass
        else:
            assert False, 'open online video failed!' 
        d.press('back')
        assert d(text="在线影视").wait.exists(timeout=15000), 'exit from online video failed!'

    def testLaunchAndExitGameCenter(self):
        """
        launch  app store and exit
       """
        assert d(text="游戏中心", packageName='com.xiaomi.tv.desktop').exists, 'Game Center icon not found!'
       #d(text="游戏中心", packageName='com.xiaomi.tv.desktop').sibling(className='android.view.View').click.wait() 
        d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=1).click.wait()
        assert d(resourceId='android:id/content').child(text="推荐").wait.exists(timeout=20000), 'Launch Game Center failed!'
        d.press('home') 
        assert d(text="游戏中心", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from Game Center failed!'

    def testLaunchAndExitAppStore(self):
        """
        launch  app store and exit
       """
        assert d(text="应用商店", packageName='com.xiaomi.tv.desktop').exists, 'App Store icon not found!'
        #d(text="应用商店", packageName='com.xiaomi.tv.desktop').sibling(className='android.view.View').click.wait()
        d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=2).click.wait()
        assert d(resourceId='com.xiaomi.mitv.appstore:id/tv_tab_indicator', text='推荐').wait.exists(timeout=15000), 'launch App Store failed!'
        #assert d(resourceId='com.xiaomi.mitv.appstore:id/tv_tab_recommend', text='推荐').wait.exists(timeout=15000), 'launch App Store failed!'
        d.press('back')
        assert d(text="应用商店", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from App Store failed!'

    def testLaunchAndExitSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="图像与声音").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="关于").wait.exists(timeout=5000), 'open setting failed!'
        d.press('back') 
        assert d(text="小米盒子设置").wait.exists(timeout=15000), 'exit from MiBox Setting failed!'

    def testLaunchCommonSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="通用设置").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('down')
        d.sleep(1)
        d.press('enter')
        assert d(text="盒子系统的相关设置").wait.exists(timeout=5000), 'launch common setting failed'
        d.press('back')
        assert d(text="通用设置").wait.exists(timeout=5000), 'back to setting failed!'


    def testLaunchGrapAudioSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="图像与声音").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('enter')
        assert d(text="盒子图像和声音设置").wait.exists(timeout=5000), 'launch GrapAudio setting failed'
        d.press('back')
        assert d(text="图像与声音").wait.exists(timeout=5000), 'back to setting failed!'

    def testLaunchSecuritySetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="图像与声音").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('enter')
        assert d(text="盒子系统的帐户与安全设置").wait.exists(timeout=5000), 'launch Security setting failed'
        d.press('back')
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'back to setting failed!'

    def testLaunchAboutSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="关于").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('down')
        d.sleep(1)
        d.press('enter')
        assert d(text="本机的相关信息").wait.exists(timeout=5000), 'launch About setting failed'
        d.press('back')
        assert d(text="关于").wait.exists(timeout=5000), 'back to setting failed!'

    def testLaunchSystemUpdateSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="系统升级").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('down')
        d.sleep(1)
        d.press('right')
        d.sleep(1)
        d.press('enter')
        assert d(textContains="当前版本").wait.exists(timeout=5000), 'launch SystemUpdate setting failed'
        d.press('back')
        assert d(text="系统升级").wait.exists(timeout=5000), 'back to setting failed!'

    def testLaunchNetworkSetting(self):
        """
        launch  app store and exit
       """
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').exists, 'MiBox Setting icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=1).click.wait()
        d(text="小米盒子设置", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(text="帐户与安全").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        assert d(text="系统升级").wait.exists(timeout=5000), 'launch MiBox setting failed!'
        d.press('up')
        d.sleep(1)
        d.press('up')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('left')
        d.sleep(1)
        d.press('enter')
        assert d(textContains="网络的相关设置").wait.exists(timeout=5000), 'launch Network setting failed'
        d.press('back')
        assert d(text="系统升级").wait.exists(timeout=5000), 'back to setting failed!'

    def testLaunchAndExitMediaExplorer(self):
        for i in xrange(6):
            d.press('right')
            d.sleep(1)
        assert d(text="高清播放器", packageName='com.xiaomi.tv.desktop').exists, 'Media Explorer icon not found!'
        d(text="高清播放器", packageName='com.xiaomi.tv.desktop').click.wait()
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=5).click.wait()
        #assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/entry_name', text='设备').wait.exists(timeout=10000), 'launch Media Explorer failed!'
        #assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/entry_name', text="视频").wait.exists(timeout=10000), 'launch Media Explorer failed!'
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/dev', text='设备').wait.exists(timeout=18000), 'launch Media Explorer failed!'
        assert d(resourceId='com.xiaomi.mitv.mediaexplorer:id/video', text="视频").wait.exists(timeout=18000), 'launch Media Explorer failed!'       
        d.press('back')
        d.sleep(3)
        d.press('back')
        assert d(text="应用商店", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from Media Explorer failed!'

    def testLaunchAndExitCloudGallery(self):
        """
        launch  app store and exit
       """
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(text="云相册", packageName='com.xiaomi.tv.desktop').exists, 'Cloud Gallery icon not found!'
        #d(resourceId="com.xiaomi.tv.desktop:id/bottom_layer").child(index=3).child(index=5).click.wait()
        d(text="云相册", packageName='com.xiaomi.tv.desktop').click.wait()
        assert d(packageName="com.duokan.cloudalbum", resourceId="android:id/content").wait.exists(timeout=20000), 'launch cloud gallery failed!'
        d.press('back')
        assert d(text="云相册", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from cloud gallery failed!'

    def  testLaunchAndExitFM(self):
        for i in xrange(8):
            d.press('right')
            d.sleep(1)
        assert d(text="网络电台", packageName='com.xiaomi.tv.desktop').exists, 'FM app icon not found!'
        d(text="网络电台", packageName='com.xiaomi.tv.desktop').click.wait()
        d.sleep(10)
        assert d(resourceId='com.xiaomi.mimusic:id/play_btn').child(className='android.widget.ImageView').wait.exists(timeout=30000), 'Open FM failed!'
        d.sleep(10)
        d.press('back')
        d.sleep(2)
        d.press('back')
        assert d(text="网络电台", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from FM failed!'

    def testLaunchAndExitMiracast(self):
        for i in xrange(4):
            d.press('right')
            d.sleep(1)
        assert d(text="无线显示", packageName='com.xiaomi.tv.desktop').exists, 'Miracast icon not found!'
        d(text="无线显示", packageName='com.xiaomi.tv.desktop').click.wait()
        d.press('back')
        assert d(text="无线显示", packageName='com.xiaomi.tv.desktop').wait.exists(timeout=15000), 'exit from Miracast failed!'

    def testWifiOpenAndClose(self):
        d.start_activity('--activity-clear-task', component='com.android.settings/.Settings')
        d(text="无线和网络").wait.exists(timeout=2000)
        #d(className="android.widget.ListView", resourceId="android:id/list").child(text='WLAN').click.wait()
        #d(text="WLAN").click.wait()
        d.press('enter')
        d(resourceId='android:id/action_bar').child(text='WLAN').wait.exists(timeout=3000)
        if d(className='android.widget.Switch', text='打开').exists:
            d.press('right')
            d.sleep(2)
            d.press('up')
            d.sleep(2)
            for i in xrange(10):
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='关闭').wait.exists(timeout=3000), 'wifi close failed!'
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi open failed!' 
                assert d(resourceId='android:id/list').child(text='已连接').wait.exists(timeout=20000), 'wifi connect failed!' 
        elif d(className='android.widget.Switch', text='关闭').exists:
            d.press('right')
            d.sleep(2)
            d.press('up')
            d.sleep(2)
            for i in xrange(10):           
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi close failed!'
                assert d(resourceId='android:id/list').child(text='已连接').wait.exists(timeout=20000), 'wifi connect failed!' 
                d.press('enter')
                assert d(resourceId='android:id/action_bar').child(text='打开').wait.exists(timeout=3000), 'wifi open failed!'
