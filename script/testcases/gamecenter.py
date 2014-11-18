#!/usr/bin/python
# -*- coding:utf-8 -*- 
import unittest
from uiautomatorplug.android import device as d

THIRD_APK = ('com.togic.livevideo', 'net.myvst.v2')

class GameCenterTest(unittest.TestCase):
    def setUp(self):
        """
        called before  each test method start.
        """
        d.wakeup()
        for i in xrange(3):
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.press('home')
        for i in xrange(3):
            d.press('back')
            d.sleep(1)
        self.split_tag = '='
        before_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
        if ''.join(before_install).find('=') == -1:
            self.split_tag = ':'
        del_apk = [ apk for apk  in [i.split(self.split_tag)[1] for i in before_install] if apk not in THIRD_APK]
        for apk in del_apk:
            d.server.adb.cmd('shell pm uninstall %s' % apk)
            d.sleep(3)
        self.before_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()

    def tearDown(self):
        """
        called after each test method end or exception occur.
        """
        self.after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
        del_apk = [i.split(self.split_tag)[1] for i in self.after_install if i not in self.before_install]
        for apk in del_apk:
            d.server.adb.cmd('shell pm uninstall %s' % apk)
            d.sleep(3)
        for i in xrange(5):
            d.press('back')
            d.sleep(1)
        d.press('home')
        d.press('home') 

    def testInstallAndUninstallGame(self):
        """
        launch  app store and exit
       """
        assert d(text="游戏中心").exists, 'Game Center icon not found!'
        d(text="游戏中心").sibling(className='android.view.View').click.wait()
        assert d(packageName="com.xiaomi.mibox.gamecenter", text="推荐").wait.exists(timeout=20000), 'Launch Game Center failed!'
        d.sleep(5)
        d.press('left')
        d.sleep(2)
        d.press('left')
        d.sleep(2)
        d.press('left')
        d.sleep(2)
        d.press('down')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('right')
        d.sleep(2)
        d.press('enter')
        d.sleep(3)
        #if d(resourceId='com.xiaomi.mibox.gamecenter:id/update', text='打开').wait.exists(timeout=5000):
        if d(className='android.widget.Button', text='启 动').wait.exists(timeout=5000):
            #uninstall except third default APK
            current_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            del_apk = [ apk for apk  in [i.split(self.split_tag)[1] for i in current_install] if apk not in THIRD_APK]
            for apk in del_apk:
                d.server.adb.cmd('shell pm uninstall %s' % apk)
                d.sleep(3)
        elif d(className='android.widget.Button', text='安 装').exists:
            d(className='android.widget.Button', text='安 装').click.wait()
            assert d(className='android.widget.Button', text='安 装').wait.gone(timeout=5000), 'button 安 装 should not exists on screen!'
            assert d(packageName='com.xiaomi.mibox.gamecenter', text='正在下载').wait.exists(timeout=10000), '正在下载 should exists on screen!'
            assert d(className='android.widget.Button', text='启 动').wait.exists(timeout=600000), 'install game failed in 5 minutes!'
            d.sleep(3)
            after_install = d.server.adb.cmd('shell pm list package -3').communicate()[0].split()
            del_apk = [i.split(self.split_tag)[1] for i in after_install if i not in self.before_install]
            for apk in del_apk:
                d.server.adb.cmd('shell pm uninstall %s' % apk)
                d.sleep(3)
            assert d(className='android.widget.Button', text='安 装').wait.exists(timeout=18000), 'uninstall game failed'
            d.press('back')
            assert d(resourceId='android:id/content').child(text="推荐").wait.exists(timeout=5000), 'game main screen not found!'
        else:
            assert False, 'game preview screen not appear!'
        d.press('back')
