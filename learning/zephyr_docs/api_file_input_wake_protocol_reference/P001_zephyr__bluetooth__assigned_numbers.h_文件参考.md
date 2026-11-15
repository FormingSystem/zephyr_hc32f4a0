---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-1
title: zephyr__bluetooth__assigned_numbers.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_zephyr\_\_bluetooth\_\_assigned\_numbers.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/assigned__numbers_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙分配编号（Bluetooth Assigned Numbers）、代码和标识符。

<a id="details"></a>

```c
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

蓝牙分配编号（Bluetooth Assigned Numbers）、代码和标识符。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 1.1\_宏定义（Macros）

<a id="r_gac1251f8a35b5e343eeeff87f22f8ab10"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN 1
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gac1251f8a35b5e343eeeff87f22f8ab10)。

支持的最小声道数（Channel Count）。

<a id="r_gad91341739d394f92ffc4988b614f47b6"></a>

```c
#define BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX 8
```

相关声明：[BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gad91341739d394f92ffc4988b614f47b6)。

支持的最大声道数（Channel Count）。

<a id="r_gaa3bf677a479a90793f28a5a3ed69c7e0"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MIN 4U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_LEN_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaa3bf677a479a90793f28a5a3ed69c7e0)。

广播名称（Broadcast Name）的最小长度，单位为八位字节（Octet）。

<a id="r_gaa2fafcbb6a826c3f4cee16ebb545dad6"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_LEN_MAX 128U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_LEN_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaa2fafcbb6a826c3f4cee16ebb545dad6)。

广播名称（Broadcast Name）的最大长度，单位为八位字节（Octet）。

<a id="r_gaaf50689c66f41dee1f4fab02893c4a1b"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MIN 4U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_CHAR_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaaf50689c66f41dee1f4fab02893c4a1b)。

广播名称（Broadcast Name）的最少字符数。

<a id="r_gaaabef5f2a77ea0ca60156eef80175311"></a>

```c
#define BT_AUDIO_BROADCAST_NAME_CHAR_MAX 32U
```

相关声明：[BT_AUDIO_BROADCAST_NAME_CHAR_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaaabef5f2a77ea0ca60156eef80175311)。

广播名称（Broadcast Name）的最多字符数。

<a id="r_ga6320f86aab9b227385bdf52a9ff3985b"></a>

```c
#define BT_AUDIO_CONTEXT_TYPE_ANY
```

相关声明：[BT_AUDIO_CONTEXT_TYPE_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga6320f86aab9b227385bdf52a9ff3985b)。

任意已知上下文（Context）。

<a id="r_ga90688f158fe999ed3aa9c759c8245fcc"></a>

```c
#define BT_AUDIO_LOCATION_ANY
```

相关声明：[BT_AUDIO_LOCATION_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga90688f158fe999ed3aa9c759c8245fcc)。

任意已知位置（Location）。

<a id="define-members-0"></a>

### 外观编号（Appearance Numbers）

最后修改于 2023-01-05（Last Modified）。

<a id="r_gafd1c9ca638a362a01897792e5a00a0c5"></a>

```c
#define BT_APPEARANCE_UNKNOWN 0x0000
```

相关声明：[BT_APPEARANCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafd1c9ca638a362a01897792e5a00a0c5)。

通用未知设备（Generic Unknown）。

<a id="r_gae7061e78f960563af6e1b3dea71655a9"></a>

```c
#define BT_APPEARANCE_GENERIC_PHONE 0x0040
```

相关声明：[BT_APPEARANCE_GENERIC_PHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae7061e78f960563af6e1b3dea71655a9)。

通用电话（Generic Phone）。

<a id="r_ga6b74ad86efc0e9a745f2c9e64079b1cd"></a>

```c
#define BT_APPEARANCE_GENERIC_COMPUTER 0x0080
```

相关声明：[BT_APPEARANCE_GENERIC_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6b74ad86efc0e9a745f2c9e64079b1cd)。

通用计算机（Generic Computer）。

<a id="r_ga1aa0565ca7e00e3a1aa8968e0a7f1bef"></a>

```c
#define BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION 0x0081
```

相关声明：[BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)。

台式工作站（Desktop Workstation）。

<a id="r_gab71a3c3f836561ac7bd8e52f5e01c769"></a>

```c
#define BT_APPEARANCE_COMPUTER_SERVER_CLASS 0x0082
```

相关声明：[BT_APPEARANCE_COMPUTER_SERVER_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab71a3c3f836561ac7bd8e52f5e01c769)。

服务器级计算机（Server-class Computer）。

<a id="r_ga55ce2ad96a153ed6bdfd841276145c28"></a>

```c
#define BT_APPEARANCE_COMPUTER_LAPTOP 0x0083
```

相关声明：[BT_APPEARANCE_COMPUTER_LAPTOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga55ce2ad96a153ed6bdfd841276145c28)。

笔记本电脑（Laptop）。

<a id="r_gab64312ea16f03c5998db4429b194b8b0"></a>

```c
#define BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA 0x0084
```

相关声明：[BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab64312ea16f03c5998db4429b194b8b0)。

翻盖式手持电脑／个人数字助理（Handheld PC/PDA (clamshell)）。

<a id="r_ga9340ed60911fc7c5aab7d317b6925c10"></a>

```c
#define BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA 0x0085
```

相关声明：[BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9340ed60911fc7c5aab7d317b6925c10)。

掌上电脑／个人数字助理（Palm­size PC/PDA）。

<a id="r_ga7c6667ba4c68dec380a548ba9530c110"></a>

```c
#define BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER 0x0086
```

相关声明：[BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7c6667ba4c68dec380a548ba9530c110)。

手表大小的可穿戴计算机（Wearable computer (watch size)）。

<a id="r_ga11bc881cb5f88956edbf2bb2fe5b358c"></a>

```c
#define BT_APPEARANCE_COMPUTER_TABLET 0x0087
```

相关声明：[BT_APPEARANCE_COMPUTER_TABLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga11bc881cb5f88956edbf2bb2fe5b358c)。

平板电脑（Tablet）。

<a id="r_ga36187d2651d08c4b3e17c36565a2d3c9"></a>

```c
#define BT_APPEARANCE_COMPUTER_DOCKING_STATION 0x0088
```

相关声明：[BT_APPEARANCE_COMPUTER_DOCKING_STATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga36187d2651d08c4b3e17c36565a2d3c9)。

扩展坞（Docking Station）。

<a id="r_gaa4d962ad8661c28ed48f5cf8cd75ad6e"></a>

```c
#define BT_APPEARANCE_COMPUTER_ALL_IN_ONE 0x0089
```

相关声明：[BT_APPEARANCE_COMPUTER_ALL_IN_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa4d962ad8661c28ed48f5cf8cd75ad6e)。

一体机（All in One）。

<a id="r_ga53e8eff26f2020b1fc89b21684e54698"></a>

```c
#define BT_APPEARANCE_COMPUTER_BLADE_SERVER 0x008A
```

相关声明：[BT_APPEARANCE_COMPUTER_BLADE_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga53e8eff26f2020b1fc89b21684e54698)。

刀片服务器（Blade Server）。

<a id="r_ga073dca362cabfd2a07cdc1cb787a0f58"></a>

```c
#define BT_APPEARANCE_COMPUTER_CONVERTIBLE 0x008B
```

相关声明：[BT_APPEARANCE_COMPUTER_CONVERTIBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga073dca362cabfd2a07cdc1cb787a0f58)。

可翻转电脑（Convertible）。

<a id="r_ga8f35f76cc9de4170006669d6e9e7d72a"></a>

```c
#define BT_APPEARANCE_COMPUTER_DETACHABLE 0x008C
```

相关声明：[BT_APPEARANCE_COMPUTER_DETACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8f35f76cc9de4170006669d6e9e7d72a)。

可拆卸电脑（Detachable）。

<a id="r_ga6ae353795476853bc3be2196ed220aa7"></a>

```c
#define BT_APPEARANCE_COMPUTER_IOT_GATEWAY 0x008D
```

相关声明：[BT_APPEARANCE_COMPUTER_IOT_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ae353795476853bc3be2196ed220aa7)。

物联网网关（IoT Gateway）。

<a id="r_ga3c47c11f56eabec15e960662c64f6fcb"></a>

```c
#define BT_APPEARANCE_COMPUTER_MINI_PC 0x008E
```

相关声明：[BT_APPEARANCE_COMPUTER_MINI_PC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3c47c11f56eabec15e960662c64f6fcb)。

迷你电脑（Mini PC）。

<a id="r_gabb53daf3eb4ac9ba0cbb1614056ee214"></a>

```c
#define BT_APPEARANCE_COMPUTER_STICK_PC 0x008F
```

相关声明：[BT_APPEARANCE_COMPUTER_STICK_PC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabb53daf3eb4ac9ba0cbb1614056ee214)。

棒式电脑（Stick PC）。

<a id="r_ga0c512fd6aa5d35e78f02176073f5f121"></a>

```c
#define BT_APPEARANCE_GENERIC_WATCH 0x00C0
```

相关声明：[BT_APPEARANCE_GENERIC_WATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0c512fd6aa5d35e78f02176073f5f121)。

通用手表（Generic Watch）。

<a id="r_gaca9cc93d768145ec3d87b88740954b50"></a>

```c
#define BT_APPEARANCE_SPORTS_WATCH 0x00C1
```

相关声明：[BT_APPEARANCE_SPORTS_WATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca9cc93d768145ec3d87b88740954b50)。

运动手表（Sports Watch）。

<a id="r_gaa5662d4a544b034243faa45245a9728b"></a>

```c
#define BT_APPEARANCE_SMARTWATCH 0x00C2
```

相关声明：[BT_APPEARANCE_SMARTWATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa5662d4a544b034243faa45245a9728b)。

智能手表（Smartwatch）。

<a id="r_ga100d26d6b9e9a3af925d64c0b006c6bd"></a>

```c
#define BT_APPEARANCE_GENERIC_CLOCK 0x0100
```

相关声明：[BT_APPEARANCE_GENERIC_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga100d26d6b9e9a3af925d64c0b006c6bd)。

通用时钟（Generic Clock）。

<a id="r_ga0a21cb58861a48875002af38ee82ac08"></a>

```c
#define BT_APPEARANCE_GENERIC_DISPLAY 0x0140
```

相关声明：[BT_APPEARANCE_GENERIC_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a21cb58861a48875002af38ee82ac08)。

通用显示器（Generic Display）。

<a id="r_ga0b47897768b27d26b8687dd2ab28703b"></a>

```c
#define BT_APPEARANCE_GENERIC_REMOTE 0x0180
```

相关声明：[BT_APPEARANCE_GENERIC_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0b47897768b27d26b8687dd2ab28703b)。

通用遥控器（Generic Remote Control）。

<a id="r_gab2b5f6385662519a2ece8fb654a6194b"></a>

```c
#define BT_APPEARANCE_GENERIC_EYEGLASSES 0x01C0
```

相关声明：[BT_APPEARANCE_GENERIC_EYEGLASSES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab2b5f6385662519a2ece8fb654a6194b)。

通用眼镜（Generic Eye-glasses）。

<a id="r_gaca6d810977e6da1a3174ee2b6b36662d"></a>

```c
#define BT_APPEARANCE_GENERIC_TAG 0x0200
```

相关声明：[BT_APPEARANCE_GENERIC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca6d810977e6da1a3174ee2b6b36662d)。

通用标签（Generic Tag）。

<a id="r_gaf73b11c4dbf366a854b4c68e802e3c1c"></a>

```c
#define BT_APPEARANCE_GENERIC_KEYRING 0x0240
```

相关声明：[BT_APPEARANCE_GENERIC_KEYRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf73b11c4dbf366a854b4c68e802e3c1c)。

通用钥匙圈（Generic Keyring）。

<a id="r_ga17e94209c0c96b5ca039b1613de0d05e"></a>

```c
#define BT_APPEARANCE_GENERIC_MEDIA_PLAYER 0x0280
```

相关声明：[BT_APPEARANCE_GENERIC_MEDIA_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga17e94209c0c96b5ca039b1613de0d05e)。

通用媒体播放器（Generic Media Player）。

<a id="r_gadca19a01611ca83e18156bb540dd96c1"></a>

```c
#define BT_APPEARANCE_GENERIC_BARCODE_SCANNER 0x02C0
```

相关声明：[BT_APPEARANCE_GENERIC_BARCODE_SCANNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadca19a01611ca83e18156bb540dd96c1)。

通用条码扫描器（Generic Barcode Scanner）。

<a id="r_ga2e0fde88d83e1f4533d69c8dc472255f"></a>

```c
#define BT_APPEARANCE_GENERIC_THERMOMETER 0x0300
```

相关声明：[BT_APPEARANCE_GENERIC_THERMOMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2e0fde88d83e1f4533d69c8dc472255f)。

通用温度计（Generic Thermometer）。

<a id="r_ga54283061a207491dcfced899c0fc3008"></a>

```c
#define BT_APPEARANCE_THERMOMETER_EAR 0x0301
```

相关声明：[BT_APPEARANCE_THERMOMETER_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga54283061a207491dcfced899c0fc3008)。

耳温计（Ear Thermometer）。

<a id="r_gac5bdf195b81215932848151d765e84d6"></a>

```c
#define BT_APPEARANCE_GENERIC_HEART_RATE 0x0340
```

相关声明：[BT_APPEARANCE_GENERIC_HEART_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac5bdf195b81215932848151d765e84d6)。

通用心率传感器（Generic Heart Rate Sensor）。

<a id="r_ga895f6570a09f3eee8d821eca57cdeb03"></a>

```c
#define BT_APPEARANCE_HEART_RATE_BELT 0x0341
```

相关声明：[BT_APPEARANCE_HEART_RATE_BELT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga895f6570a09f3eee8d821eca57cdeb03)。

心率带（Heart Rate Belt）。

<a id="r_ga3ab7a9595e00208a9e6a56dca99b56c2"></a>

```c
#define BT_APPEARANCE_GENERIC_BLOOD_PRESSURE 0x0380
```

相关声明：[BT_APPEARANCE_GENERIC_BLOOD_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3ab7a9595e00208a9e6a56dca99b56c2)。

通用血压设备（Generic Blood Pressure）。

<a id="r_ga55c3e67d27c8fd8ae06880ccdd9259ce"></a>

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_ARM 0x0381
```

相关声明：[BT_APPEARANCE_BLOOD_PRESSURE_ARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga55c3e67d27c8fd8ae06880ccdd9259ce)。

臂式血压设备（Arm Blood Pressure）。

<a id="r_ga89684ca0544a400293b663cdf0063cfa"></a>

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_WRIST 0x0382
```

相关声明：[BT_APPEARANCE_BLOOD_PRESSURE_WRIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga89684ca0544a400293b663cdf0063cfa)。

腕式血压设备（Wrist Blood Pressure）。

<a id="r_gaf2050baedf0863ec37177dd2ef872d39"></a>

```c
#define BT_APPEARANCE_GENERIC_HID 0x03C0
```

相关声明：[BT_APPEARANCE_GENERIC_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf2050baedf0863ec37177dd2ef872d39)。

通用人机接口设备（Generic Human Interface Device）。

<a id="r_gaa74af272423a80d5489ed8cf6c3ee66c"></a>

```c
#define BT_APPEARANCE_HID_KEYBOARD 0x03C1
```

相关声明：[BT_APPEARANCE_HID_KEYBOARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa74af272423a80d5489ed8cf6c3ee66c)。

键盘（Keyboard）。

<a id="r_ga3b6ba8ffe424db08583186c448e37149"></a>

```c
#define BT_APPEARANCE_HID_MOUSE 0x03C2
```

相关声明：[BT_APPEARANCE_HID_MOUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3b6ba8ffe424db08583186c448e37149)。

鼠标（Mouse）。

<a id="r_ga2f9f15df2260a1307f5142f37437bf0c"></a>

```c
#define BT_APPEARANCE_HID_JOYSTICK 0x03C3
```

相关声明：[BT_APPEARANCE_HID_JOYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2f9f15df2260a1307f5142f37437bf0c)。

操纵杆（Joystick）。

<a id="r_ga770336524e74d106cb18354f9dbfad76"></a>

```c
#define BT_APPEARANCE_HID_GAMEPAD 0x03C4
```

相关声明：[BT_APPEARANCE_HID_GAMEPAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga770336524e74d106cb18354f9dbfad76)。

游戏手柄（Gamepad）。

<a id="r_gacac11dcb96ab60963a1118e171a731de"></a>

```c
#define BT_APPEARANCE_HID_DIGITIZER_TABLET 0x03C5
```

相关声明：[BT_APPEARANCE_HID_DIGITIZER_TABLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacac11dcb96ab60963a1118e171a731de)。

数字化绘图板（Digitizer Tablet）。

<a id="r_gaa03c3b4d7ea8211748316146afab8bd4"></a>

```c
#define BT_APPEARANCE_HID_CARD_READER 0x03C6
```

相关声明：[BT_APPEARANCE_HID_CARD_READER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa03c3b4d7ea8211748316146afab8bd4)。

读卡器（Card Reader）。

<a id="r_ga002a1d7965b23ec62c8a196f4e5452d9"></a>

```c
#define BT_APPEARANCE_HID_DIGITAL_PEN 0x03C7
```

相关声明：[BT_APPEARANCE_HID_DIGITAL_PEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga002a1d7965b23ec62c8a196f4e5452d9)。

数字笔（Digital Pen）。

<a id="r_gaf88f83afd454fe88dd7146e10ef6d35e"></a>

```c
#define BT_APPEARANCE_HID_BARCODE_SCANNER 0x03C8
```

相关声明：[BT_APPEARANCE_HID_BARCODE_SCANNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf88f83afd454fe88dd7146e10ef6d35e)。

条码扫描器（Barcode Scanner）。

<a id="r_gaee207f9434bce7d0f7e096bf3b37a01c"></a>

```c
#define BT_APPEARANCE_HID_TOUCHPAD 0x03C9
```

相关声明：[BT_APPEARANCE_HID_TOUCHPAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaee207f9434bce7d0f7e096bf3b37a01c)。

触摸板（Touchpad）。

<a id="r_gae415dd9e8d620dfd1981719f4ed2d796"></a>

```c
#define BT_APPEARANCE_HID_PRESENTATION_REMOTE 0x03CA
```

相关声明：[BT_APPEARANCE_HID_PRESENTATION_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae415dd9e8d620dfd1981719f4ed2d796)。

演示遥控器（Presentation Remote）。

<a id="r_ga209645f7445873beb50c388cc82aff2a"></a>

```c
#define BT_APPEARANCE_GENERIC_GLUCOSE 0x0400
```

相关声明：[BT_APPEARANCE_GENERIC_GLUCOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga209645f7445873beb50c388cc82aff2a)。

通用血糖仪（Generic Glucose Meter）。

<a id="r_ga9cf19d97db0c4c5b8473b72809b51d42"></a>

```c
#define BT_APPEARANCE_GENERIC_WALKING 0x0440
```

相关声明：[BT_APPEARANCE_GENERIC_WALKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9cf19d97db0c4c5b8473b72809b51d42)。

通用跑步／步行传感器（Generic Running Walking Sensor）。

<a id="r_gad748f5dc2e0622353d6159c3a3e4241b"></a>

```c
#define BT_APPEARANCE_WALKING_IN_SHOE 0x0441
```

相关声明：[BT_APPEARANCE_WALKING_IN_SHOE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad748f5dc2e0622353d6159c3a3e4241b)。

鞋内跑步／步行传感器（In-Shoe Running Walking Sensor）。

<a id="r_ga0a4541459ba8b41a3938c5b8d35b1c8c"></a>

```c
#define BT_APPEARANCE_WALKING_ON_SHOE 0x0442
```

相关声明：[BT_APPEARANCE_WALKING_ON_SHOE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a4541459ba8b41a3938c5b8d35b1c8c)。

鞋面跑步／步行传感器（On-Shoe Running Walking Sensor）。

<a id="r_gad211a7e2f11dc7effe3ba28e8c4f7092"></a>

```c
#define BT_APPEARANCE_WALKING_ON_HIP 0x0443
```

相关声明：[BT_APPEARANCE_WALKING_ON_HIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad211a7e2f11dc7effe3ba28e8c4f7092)。

髋部佩戴式跑步／步行传感器（On-Hip Running Walking Sensor）。

<a id="r_ga7a0463b9b0df37bce80cada38b10ee54"></a>

```c
#define BT_APPEARANCE_GENERIC_CYCLING 0x0480
```

相关声明：[BT_APPEARANCE_GENERIC_CYCLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7a0463b9b0df37bce80cada38b10ee54)。

通用骑行设备（Generic Cycling）。

<a id="r_ga3e81dce23c3d005a9b48ff83c7b8f896"></a>

```c
#define BT_APPEARANCE_CYCLING_COMPUTER 0x0481
```

相关声明：[BT_APPEARANCE_CYCLING_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3e81dce23c3d005a9b48ff83c7b8f896)。

自行车码表（Cycling Computer）。

<a id="r_ga16fb08fa70272252ab6b2d3a5aec485a"></a>

```c
#define BT_APPEARANCE_CYCLING_SPEED 0x0482
```

相关声明：[BT_APPEARANCE_CYCLING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga16fb08fa70272252ab6b2d3a5aec485a)。

速度传感器（Speed Sensor）。

<a id="r_ga71dc370aad015e88fce7c3e758c647ed"></a>

```c
#define BT_APPEARANCE_CYCLING_CADENCE 0x0483
```

相关声明：[BT_APPEARANCE_CYCLING_CADENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga71dc370aad015e88fce7c3e758c647ed)。

踏频传感器（Cadence Sensor）。

<a id="r_ga02fd9566d9b932aeaa1163d312fbc4d8"></a>

```c
#define BT_APPEARANCE_CYCLING_POWER 0x0484
```

相关声明：[BT_APPEARANCE_CYCLING_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga02fd9566d9b932aeaa1163d312fbc4d8)。

功率传感器（Power Sensor）。

<a id="r_ga48d8f2a285795785f8f51ce220d46371"></a>

```c
#define BT_APPEARANCE_CYCLING_SPEED_CADENCE 0x0485
```

相关声明：[BT_APPEARANCE_CYCLING_SPEED_CADENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga48d8f2a285795785f8f51ce220d46371)。

速度与踏频传感器（Speed and Cadence Sensor）。

<a id="r_ga5e16df5eefcae8556dfc387135e2b1b6"></a>

```c
#define BT_APPEARANCE_GENERIC_CONTROL_DEVICE 0x04C0
```

相关声明：[BT_APPEARANCE_GENERIC_CONTROL_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5e16df5eefcae8556dfc387135e2b1b6)。

通用控制设备（Generic Control Device）。

<a id="r_gac53247d00e3da69595274e0b94fa670f"></a>

```c
#define BT_APPEARANCE_CONTROL_SWITCH 0x04C1
```

相关声明：[BT_APPEARANCE_CONTROL_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac53247d00e3da69595274e0b94fa670f)。

开关（Switch）。

<a id="r_gad30c40df58e160128893e545a11ab44c"></a>

```c
#define BT_APPEARANCE_CONTROL_MULTI_SWITCH 0x04C2
```

相关声明：[BT_APPEARANCE_CONTROL_MULTI_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad30c40df58e160128893e545a11ab44c)。

多联开关（Multi-switch）。

<a id="r_ga52dfd2858663b7ab624f0c4b08cee7dc"></a>

```c
#define BT_APPEARANCE_CONTROL_BUTTON 0x04C3
```

相关声明：[BT_APPEARANCE_CONTROL_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga52dfd2858663b7ab624f0c4b08cee7dc)。

按钮（Button）。

<a id="r_gaa849d890c000defcaf29893296c86cc5"></a>

```c
#define BT_APPEARANCE_CONTROL_SLIDER 0x04C4
```

相关声明：[BT_APPEARANCE_CONTROL_SLIDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa849d890c000defcaf29893296c86cc5)。

滑块（Slider）。

<a id="r_ga946b6a8bb49bf0b5cd3ded93ee8dfe89"></a>

```c
#define BT_APPEARANCE_CONTROL_ROTARY_SWITCH 0x04C5
```

相关声明：[BT_APPEARANCE_CONTROL_ROTARY_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)。

旋转开关（Rotary Switch）。

<a id="r_ga4d5763288557e7b7f6da0f3e9831171d"></a>

```c
#define BT_APPEARANCE_CONTROL_TOUCH_PANEL 0x04C6
```

相关声明：[BT_APPEARANCE_CONTROL_TOUCH_PANEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4d5763288557e7b7f6da0f3e9831171d)。

触摸面板（Touch Panel）。

<a id="r_ga979ca0f4febeaa55daec07e2b3b0179e"></a>

```c
#define BT_APPEARANCE_CONTROL_SINGLE_SWITCH 0x04C7
```

相关声明：[BT_APPEARANCE_CONTROL_SINGLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga979ca0f4febeaa55daec07e2b3b0179e)。

单联开关（Single Switch）。

<a id="r_gac1c80dbb8aaa327b6125bf632692c3be"></a>

```c
#define BT_APPEARANCE_CONTROL_DOUBLE_SWITCH 0x04C8
```

相关声明：[BT_APPEARANCE_CONTROL_DOUBLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac1c80dbb8aaa327b6125bf632692c3be)。

双联开关（Double Switch）。

<a id="r_gaa532fd1bd67c2c5b72822704a62df143"></a>

```c
#define BT_APPEARANCE_CONTROL_TRIPLE_SWITCH 0x04C9
```

相关声明：[BT_APPEARANCE_CONTROL_TRIPLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa532fd1bd67c2c5b72822704a62df143)。

三联开关（Triple Switch）。

<a id="r_gaea669671a53b3df5b1aa4c43e5bde9b9"></a>

```c
#define BT_APPEARANCE_CONTROL_BATTERY_SWITCH 0x04CA
```

相关声明：[BT_APPEARANCE_CONTROL_BATTERY_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaea669671a53b3df5b1aa4c43e5bde9b9)。

电池供电开关（Battery Switch）。

<a id="r_gadec2907a822e302d5027f162ef9ce4b6"></a>

```c
#define BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH 0x04CB
```

相关声明：[BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadec2907a822e302d5027f162ef9ce4b6)。

能量采集开关（Energy Harvesting Switch）。

<a id="r_ga9bb358864e1388cc00502b5586ec581f"></a>

```c
#define BT_APPEARANCE_CONTROL_PUSH_BUTTON 0x04CC
```

相关声明：[BT_APPEARANCE_CONTROL_PUSH_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9bb358864e1388cc00502b5586ec581f)。

按压按钮（Push Button）。

<a id="r_gac4727ec720344ece687256ac517800e7"></a>

```c
#define BT_APPEARANCE_GENERIC_NETWORK_DEVICE 0x0500
```

相关声明：[BT_APPEARANCE_GENERIC_NETWORK_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac4727ec720344ece687256ac517800e7)。

通用网络设备（Generic Network Device）。

<a id="r_ga265ba959769d56f42ff621a20e193aba"></a>

```c
#define BT_APPEARANCE_NETWORK_ACCESS_POINT 0x0501
```

相关声明：[BT_APPEARANCE_NETWORK_ACCESS_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga265ba959769d56f42ff621a20e193aba)。

接入点（Access Point）。

<a id="r_gadcc3d795579a731ae03ade14d5193408"></a>

```c
#define BT_APPEARANCE_NETWORK_MESH_DEVICE 0x0502
```

相关声明：[BT_APPEARANCE_NETWORK_MESH_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadcc3d795579a731ae03ade14d5193408)。

网状网络设备（Mesh Device）。

<a id="r_gad4c5f5840a8caba73d55b0138e506bd0"></a>

```c
#define BT_APPEARANCE_NETWORK_MESH_PROXY 0x0503
```

相关声明：[BT_APPEARANCE_NETWORK_MESH_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad4c5f5840a8caba73d55b0138e506bd0)。

网状网络代理（Mesh Network Proxy）。

<a id="r_gab3241fe012482e716c3f18e2962ca15d"></a>

```c
#define BT_APPEARANCE_GENERIC_SENSOR 0x0540
```

相关声明：[BT_APPEARANCE_GENERIC_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab3241fe012482e716c3f18e2962ca15d)。

通用传感器（Generic Sensor）。

<a id="r_gab49b84183136e9b65ba2e1f5490a79ed"></a>

```c
#define BT_APPEARANCE_SENSOR_MOTION 0x0541
```

相关声明：[BT_APPEARANCE_SENSOR_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab49b84183136e9b65ba2e1f5490a79ed)。

运动传感器（Motion Sensor）。

<a id="r_gaacb0779499ad4aaa83f0b6303460caf8"></a>

```c
#define BT_APPEARANCE_SENSOR_AIR_QUALITY 0x0542
```

相关声明：[BT_APPEARANCE_SENSOR_AIR_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaacb0779499ad4aaa83f0b6303460caf8)。

空气质量传感器（Air quality Sensor）。

<a id="r_ga5e072a902bf145dc2b00dbd1c8a64b52"></a>

```c
#define BT_APPEARANCE_SENSOR_TEMPERATURE 0x0543
```

相关声明：[BT_APPEARANCE_SENSOR_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5e072a902bf145dc2b00dbd1c8a64b52)。

温度传感器（Temperature Sensor）。

<a id="r_ga2deff206602e1e0784af9456ef8abd5b"></a>

```c
#define BT_APPEARANCE_SENSOR_HUMIDITY 0x0544
```

相关声明：[BT_APPEARANCE_SENSOR_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2deff206602e1e0784af9456ef8abd5b)。

湿度传感器（Humidity Sensor）。

<a id="r_ga2cbac5e931080f1f5cb3c9bb4c73e9d8"></a>

```c
#define BT_APPEARANCE_SENSOR_LEAK 0x0545
```

相关声明：[BT_APPEARANCE_SENSOR_LEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)。

泄漏传感器（Leak Sensor）。

<a id="r_gaeedc0612f8ca171aec061cf02ee907e4"></a>

```c
#define BT_APPEARANCE_SENSOR_SMOKE 0x0546
```

相关声明：[BT_APPEARANCE_SENSOR_SMOKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeedc0612f8ca171aec061cf02ee907e4)。

烟雾传感器（Smoke Sensor）。

<a id="r_ga8e8b7834c82c42a0076300aca20c2d35"></a>

```c
#define BT_APPEARANCE_SENSOR_OCCUPANCY 0x0547
```

相关声明：[BT_APPEARANCE_SENSOR_OCCUPANCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e8b7834c82c42a0076300aca20c2d35)。

占用传感器（Occupancy Sensor）。

<a id="r_gac71e281cf1b8d1b6535623ec34c7d63f"></a>

```c
#define BT_APPEARANCE_SENSOR_CONTACT 0x0548
```

相关声明：[BT_APPEARANCE_SENSOR_CONTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac71e281cf1b8d1b6535623ec34c7d63f)。

接触传感器（Contact Sensor）。

<a id="r_ga0e60b365f871c17c0015ffcf8bc1646e"></a>

```c
#define BT_APPEARANCE_SENSOR_CARBON_MONOXIDE 0x0549
```

相关声明：[BT_APPEARANCE_SENSOR_CARBON_MONOXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0e60b365f871c17c0015ffcf8bc1646e)。

一氧化碳传感器（Carbon Monoxide Sensor）。

<a id="r_ga34ed8c9aefe34d5030209f073c9ecd24"></a>

```c
#define BT_APPEARANCE_SENSOR_CARBON_DIOXIDE 0x054A
```

相关声明：[BT_APPEARANCE_SENSOR_CARBON_DIOXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga34ed8c9aefe34d5030209f073c9ecd24)。

二氧化碳传感器（Carbon Dioxide Sensor）。

<a id="r_ga622508f9b051ed0320700b01967f6446"></a>

```c
#define BT_APPEARANCE_SENSOR_AMBIENT_LIGHT 0x054B
```

相关声明：[BT_APPEARANCE_SENSOR_AMBIENT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga622508f9b051ed0320700b01967f6446)。

环境光传感器（Ambient Light Sensor）。

<a id="r_gaca0cfcd560fa4133c0bc62a61d2874c7"></a>

```c
#define BT_APPEARANCE_SENSOR_ENERGY 0x054C
```

相关声明：[BT_APPEARANCE_SENSOR_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca0cfcd560fa4133c0bc62a61d2874c7)。

能量传感器（Energy Sensor）。

<a id="r_ga8106142ddb6445e7462137e032e50854"></a>

```c
#define BT_APPEARANCE_SENSOR_COLOR_LIGHT 0x054D
```

相关声明：[BT_APPEARANCE_SENSOR_COLOR_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8106142ddb6445e7462137e032e50854)。

彩色光传感器（Color Light Sensor）。

<a id="r_ga380da83e3a69de3fd5091cdc89f7fcbc"></a>

```c
#define BT_APPEARANCE_SENSOR_RAIN 0x054E
```

相关声明：[BT_APPEARANCE_SENSOR_RAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga380da83e3a69de3fd5091cdc89f7fcbc)。

雨量传感器（Rain Sensor）。

<a id="r_ga425115e6c251a9c493c98d79f659077d"></a>

```c
#define BT_APPEARANCE_SENSOR_FIRE 0x054F
```

相关声明：[BT_APPEARANCE_SENSOR_FIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga425115e6c251a9c493c98d79f659077d)。

火灾传感器（Fire Sensor）。

<a id="r_gaa710c0666d8b5bf1e1230672cbbf55fa"></a>

```c
#define BT_APPEARANCE_SENSOR_WIND 0x0550
```

相关声明：[BT_APPEARANCE_SENSOR_WIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa710c0666d8b5bf1e1230672cbbf55fa)。

风传感器（Wind Sensor）。

<a id="r_ga6d3447e24d5d75051b81998fd9ad8bfe"></a>

```c
#define BT_APPEARANCE_SENSOR_PROXIMITY 0x0551
```

相关声明：[BT_APPEARANCE_SENSOR_PROXIMITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6d3447e24d5d75051b81998fd9ad8bfe)。

接近传感器（Proximity Sensor）。

<a id="r_gaeec9666dbdb31e9302a25aaa536f3180"></a>

```c
#define BT_APPEARANCE_SENSOR_MULTI 0x0552
```

相关声明：[BT_APPEARANCE_SENSOR_MULTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeec9666dbdb31e9302a25aaa536f3180)。

多传感器（Multi-Sensor）。

<a id="r_gaf9a9c0191ec175d14061058cf3da163c"></a>

```c
#define BT_APPEARANCE_SENSOR_FLUSH_MOUNTED 0x0553
```

相关声明：[BT_APPEARANCE_SENSOR_FLUSH_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf9a9c0191ec175d14061058cf3da163c)。

嵌入安装式传感器（Flush Mounted Sensor）。

<a id="r_gadfb6808db5a7060316b724c24c8ceaf8"></a>

```c
#define BT_APPEARANCE_SENSOR_CEILING_MOUNTED 0x0554
```

相关声明：[BT_APPEARANCE_SENSOR_CEILING_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadfb6808db5a7060316b724c24c8ceaf8)。

吸顶安装式传感器（Ceiling Mounted Sensor）。

<a id="r_gae564900f0517d393ceffcca8d27f6e45"></a>

```c
#define BT_APPEARANCE_SENSOR_WALL_MOUNTED 0x0555
```

相关声明：[BT_APPEARANCE_SENSOR_WALL_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae564900f0517d393ceffcca8d27f6e45)。

壁挂安装式传感器（Wall Mounted Sensor）。

<a id="r_ga90237753920702380321e9f858344741"></a>

```c
#define BT_APPEARANCE_MULTISENSOR 0x0556
```

相关声明：[BT_APPEARANCE_MULTISENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga90237753920702380321e9f858344741)。

多传感器（Multisensor）。

<a id="r_ga7238d3a45f9e62f0189db9d7eeac4d15"></a>

```c
#define BT_APPEARANCE_SENSOR_ENERGY_METER 0x0557
```

相关声明：[BT_APPEARANCE_SENSOR_ENERGY_METER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7238d3a45f9e62f0189db9d7eeac4d15)。

能量计（Energy Meter）。

<a id="r_gaae8f95ef639cb7d5e97063eed710a07d"></a>

```c
#define BT_APPEARANCE_SENSOR_FLAME_DETECTOR 0x0558
```

相关声明：[BT_APPEARANCE_SENSOR_FLAME_DETECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaae8f95ef639cb7d5e97063eed710a07d)。

火焰探测器（Flame Detector）。

<a id="r_ga4d0877a3cd9b7efebbaa5fd8a988a2a3"></a>

```c
#define BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE 0x0559
```

相关声明：[BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)。

车辆胎压传感器（Vehicle Tire Pressure Sensor）。

<a id="r_gae01be867f730c06b59fcb03289ae66d7"></a>

```c
#define BT_APPEARANCE_GENERIC_LIGHT_FIXTURES 0x0580
```

相关声明：[BT_APPEARANCE_GENERIC_LIGHT_FIXTURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae01be867f730c06b59fcb03289ae66d7)。

通用照明灯具（Generic Light Fixtures）。

<a id="r_gae1b2b535754f9cdc24c4a6cee63ef5cb"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_WALL 0x0581
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_WALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae1b2b535754f9cdc24c4a6cee63ef5cb)。

壁灯（Wall Light）。

<a id="r_ga2d77fb5f5ed9a43771186ecc5693da8f"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CEILING 0x0582
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CEILING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2d77fb5f5ed9a43771186ecc5693da8f)。

吸顶灯（Ceiling Light）。

<a id="r_ga57bb461b0ddd045d21d7fbd3843fbabb"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOR 0x0583
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_FLOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga57bb461b0ddd045d21d7fbd3843fbabb)。

落地灯（Floor Light）。

<a id="r_gadc48840b6590a89593a5d17fbdb1e9e9"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CABINET 0x0584
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CABINET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadc48840b6590a89593a5d17fbdb1e9e9)。

橱柜灯（Cabinet Light）。

<a id="r_ga2f37bf95ea6057b999bbf2cf94016e5d"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DESK 0x0585
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2f37bf95ea6057b999bbf2cf94016e5d)。

桌灯（Desk Light）。

<a id="r_gaa57b538ecad380ad77354e0cd9576e5b"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_TROFFER 0x0586
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_TROFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa57b538ecad380ad77354e0cd9576e5b)。

嵌入式格栅灯（Troffer Light）。

<a id="r_ga336147b54406237e25d8cf9ed152928b"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PENDANT 0x0587
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_PENDANT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga336147b54406237e25d8cf9ed152928b)。

吊灯（Pendant Light）。

<a id="r_ga583b7432ba6ac4cc078d3a069e3a54e1"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND 0x0588
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga583b7432ba6ac4cc078d3a069e3a54e1)。

地埋灯（In-ground Light）。

<a id="r_gab41f8b6f1ff0f624bb6666ef2ac6dab3"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOD 0x0589
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_FLOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab41f8b6f1ff0f624bb6666ef2ac6dab3)。

泛光灯（Flood Light）。

<a id="r_ga83f50305a23250e5e2cef5004762e122"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER 0x058A
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga83f50305a23250e5e2cef5004762e122)。

水下灯（Underwater Light）。

<a id="r_ga20a7b241f292475d70626a38d983886c"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH 0x058B
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga20a7b241f292475d70626a38d983886c)。

带灯柱桩（Bollard with Light）。

<a id="r_ga7c5811bd50d9f78e67e3e56faa432aae"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY 0x058C
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7c5811bd50d9f78e67e3e56faa432aae)。

步道灯（Pathway Light）。

<a id="r_ga348e64ffe0f3d6301dd8c911f70ead68"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_GARDEN 0x058D
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_GARDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga348e64ffe0f3d6301dd8c911f70ead68)。

庭院灯（Garden Light）。

<a id="r_ga0da0cbeebd2b20bf28dfc06def016068"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP 0x058E
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0da0cbeebd2b20bf28dfc06def016068)。

杆顶灯（Pole-top Light）。

<a id="r_ga58e1989c99b5a223a318a716d62f6e2b"></a>

```c
#define BT_APPEARANCE_SPOT_LIGHT 0x058F
```

相关声明：[BT_APPEARANCE_SPOT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga58e1989c99b5a223a318a716d62f6e2b)。

聚光灯（Spotlight）。

<a id="r_ga5388daf123e629d6f7a0b9af13fbc366"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LINEAR 0x0590
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_LINEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5388daf123e629d6f7a0b9af13fbc366)。

线性灯（Linear Light）。

<a id="r_gac938fb03553d2d3c27b50af2a9a1ac48"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_STREET 0x0591
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_STREET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac938fb03553d2d3c27b50af2a9a1ac48)。

路灯（Street Light）。

<a id="r_ga1bf2889f7a8a7ae363bc1d4355ee8d65"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_SHELVES 0x0592
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_SHELVES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1bf2889f7a8a7ae363bc1d4355ee8d65)。

货架灯（Shelves Light）。

<a id="r_ga8f98c2d32664a6e03ebc2a43ae1eb52a"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BAY 0x0593
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8f98c2d32664a6e03ebc2a43ae1eb52a)。

工矿灯（Bay Light）。

<a id="r_ga3f687f994ffff2ce70b81a992195d210"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT 0x0594
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3f687f994ffff2ce70b81a992195d210)。

紧急出口灯（Emergency Exit Light）。

<a id="r_ga35a90a4e3bfef7b0cfec0d5fa7b36c4a"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER 0x0595
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)。

照明控制器（Light Controller）。

<a id="r_gac2b6de99b4e87f7c40063ba844c75ead"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DRIVER 0x0596
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac2b6de99b4e87f7c40063ba844c75ead)。

灯具驱动器（Light Driver）。

<a id="r_ga8325830f2c977dc238a9ca1b9837803e"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BULB 0x0597
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BULB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8325830f2c977dc238a9ca1b9837803e)。

灯泡（Bulb）。

<a id="r_gafc924bbc1b6aff0130c2be3d5fe59e33"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY 0x0598
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc924bbc1b6aff0130c2be3d5fe59e33)。

低棚灯（Low-bay Light）。

<a id="r_ga738e87008c6a64450bb7ec22dbcdd113"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY 0x0599
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga738e87008c6a64450bb7ec22dbcdd113)。

高棚灯（High-bay Light）。

<a id="r_ga82cc89321c4f4ffbf3ef25eff624943c"></a>

```c
#define BT_APPEARANCE_GENERIC_FAN 0x05C0
```

相关声明：[BT_APPEARANCE_GENERIC_FAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga82cc89321c4f4ffbf3ef25eff624943c)。

通用风扇（Generic Fan）。

<a id="r_ga8cd83cd08846ac276cc65f31333ee62e"></a>

```c
#define BT_APPEARANCE_FAN_CEILING 0x05C1
```

相关声明：[BT_APPEARANCE_FAN_CEILING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8cd83cd08846ac276cc65f31333ee62e)。

吊扇（Ceiling Fan）。

<a id="r_ga32dd73ffa211d632617018aa510b89c4"></a>

```c
#define BT_APPEARANCE_FAN_AXIAL 0x05C2
```

相关声明：[BT_APPEARANCE_FAN_AXIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga32dd73ffa211d632617018aa510b89c4)。

轴流风扇（Axial Fan）。

<a id="r_ga1e842c97b90678908f4d18c86c1227c2"></a>

```c
#define BT_APPEARANCE_FAN_EXHAUST 0x05C3
```

相关声明：[BT_APPEARANCE_FAN_EXHAUST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1e842c97b90678908f4d18c86c1227c2)。

排气扇（Exhaust Fan）。

<a id="r_ga2e54f8de862435f2dbd7f56b98615c84"></a>

```c
#define BT_APPEARANCE_FAN_PEDESTAL 0x05C4
```

相关声明：[BT_APPEARANCE_FAN_PEDESTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2e54f8de862435f2dbd7f56b98615c84)。

落地风扇（Pedestal Fan）。

<a id="r_gaa9e17b8b5e06d2fb365bf152e0cbef5d"></a>

```c
#define BT_APPEARANCE_FAN_DESK 0x05C5
```

相关声明：[BT_APPEARANCE_FAN_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa9e17b8b5e06d2fb365bf152e0cbef5d)。

桌面风扇（Desk Fan）。

<a id="r_ga498be79799cb778c9df6629411fe32ad"></a>

```c
#define BT_APPEARANCE_FAN_WALL 0x05C6
```

相关声明：[BT_APPEARANCE_FAN_WALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga498be79799cb778c9df6629411fe32ad)。

壁扇（Wall Fan）。

<a id="r_gaf1f01946f6acadcaf719d3d7cc06e55f"></a>

```c
#define BT_APPEARANCE_GENERIC_HVAC 0x0600
```

相关声明：[BT_APPEARANCE_GENERIC_HVAC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf1f01946f6acadcaf719d3d7cc06e55f)。

通用暖通空调设备（Generic HVAC）。

<a id="r_ga33055b50c10bfc713b18823fca525488"></a>

```c
#define BT_APPEARANCE_HVAC_THERMOSTAT 0x0601
```

相关声明：[BT_APPEARANCE_HVAC_THERMOSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga33055b50c10bfc713b18823fca525488)。

恒温器（Thermostat）。

<a id="r_gaf55f3f3f07cc78509e7fe19cea6cea4e"></a>

```c
#define BT_APPEARANCE_HVAC_HUMIDIFIER 0x0602
```

相关声明：[BT_APPEARANCE_HVAC_HUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf55f3f3f07cc78509e7fe19cea6cea4e)。

加湿器（Humidifier）。

<a id="r_gaa3b96e44638048b8891a2dece29f4b3f"></a>

```c
#define BT_APPEARANCE_HVAC_DEHUMIDIFIER 0x0603
```

相关声明：[BT_APPEARANCE_HVAC_DEHUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa3b96e44638048b8891a2dece29f4b3f)。

除湿机（De-humidifier）。

<a id="r_gacef9145f435d10cbf5a775b9a2c9b756"></a>

```c
#define BT_APPEARANCE_HVAC_HEATER 0x0604
```

相关声明：[BT_APPEARANCE_HVAC_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacef9145f435d10cbf5a775b9a2c9b756)。

加热器（Heater）。

<a id="r_gad90f108f3d33d68e27ac545cdb520f18"></a>

```c
#define BT_APPEARANCE_HVAC_RADIATOR 0x0605
```

相关声明：[BT_APPEARANCE_HVAC_RADIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad90f108f3d33d68e27ac545cdb520f18)。

散热暖气片（Radiator）。

<a id="r_gacc28a1bc1a809c574019455de4ac9d0b"></a>

```c
#define BT_APPEARANCE_HVAC_BOILER 0x0606
```

相关声明：[BT_APPEARANCE_HVAC_BOILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacc28a1bc1a809c574019455de4ac9d0b)。

锅炉（Boiler）。

<a id="r_gaead4ebeabb8855111ab9080aca4e035a"></a>

```c
#define BT_APPEARANCE_HVAC_HEAT_PUMP 0x0607
```

相关声明：[BT_APPEARANCE_HVAC_HEAT_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaead4ebeabb8855111ab9080aca4e035a)。

热泵（Heat Pump）。

<a id="r_ga50c5df52d8471fc8e1dc65e31079566d"></a>

```c
#define BT_APPEARANCE_HVAC_INFRARED_HEATER 0x0608
```

相关声明：[BT_APPEARANCE_HVAC_INFRARED_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga50c5df52d8471fc8e1dc65e31079566d)。

红外加热器（Infrared Heater）。

<a id="r_gad43d27ff96a7fba1ed7d5e20ebd472d9"></a>

```c
#define BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER 0x0609
```

相关声明：[BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad43d27ff96a7fba1ed7d5e20ebd472d9)。

辐射板式加热器（Radiant Panel Heater）。

<a id="r_ga2a044c3369ed48d216707f6e6a541a23"></a>

```c
#define BT_APPEARANCE_HVAC_FAN_HEATER 0x060A
```

相关声明：[BT_APPEARANCE_HVAC_FAN_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2a044c3369ed48d216707f6e6a541a23)。

暖风机（Fan Heater）。

<a id="r_ga182ade4b2c8f4705ba132248e504bb95"></a>

```c
#define BT_APPEARANCE_HVAC_AIR_CURTAIN 0x060B
```

相关声明：[BT_APPEARANCE_HVAC_AIR_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga182ade4b2c8f4705ba132248e504bb95)。

空气幕（Air Curtain）。

<a id="r_gaa13ae6496d47df2be0a0692a28806007"></a>

```c
#define BT_APPEARANCE_GENERIC_AIR_CONDITIONING 0x0640
```

相关声明：[BT_APPEARANCE_GENERIC_AIR_CONDITIONING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa13ae6496d47df2be0a0692a28806007)。

通用空调设备（Generic Air Conditioning）。

<a id="r_ga0b552243744bc598467421555e935cd0"></a>

```c
#define BT_APPEARANCE_GENERIC_HUMIDIFIER 0x0680
```

相关声明：[BT_APPEARANCE_GENERIC_HUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0b552243744bc598467421555e935cd0)。

通用加湿器（Generic Humidifier）。

<a id="r_ga8ea92ea92ca4e2bad4e5e2baba1271dd"></a>

```c
#define BT_APPEARANCE_GENERIC_HEATING 0x06C0
```

相关声明：[BT_APPEARANCE_GENERIC_HEATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8ea92ea92ca4e2bad4e5e2baba1271dd)。

通用供暖设备（Generic Heating）。

<a id="r_ga05b0b91c74aed5bc73a92f336bdae33a"></a>

```c
#define BT_APPEARANCE_HEATING_RADIATOR 0x06C1
```

相关声明：[BT_APPEARANCE_HEATING_RADIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga05b0b91c74aed5bc73a92f336bdae33a)。

散热暖气片（Radiator）。

<a id="r_gac1abc9ae0b8ede2197720ea9e67b692e"></a>

```c
#define BT_APPEARANCE_HEATING_BOILER 0x06C2
```

相关声明：[BT_APPEARANCE_HEATING_BOILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac1abc9ae0b8ede2197720ea9e67b692e)。

锅炉（Boiler）。

<a id="r_ga99537968fdc7e680d922ca309fba7678"></a>

```c
#define BT_APPEARANCE_HEATING_HEAT_PUMP 0x06C3
```

相关声明：[BT_APPEARANCE_HEATING_HEAT_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga99537968fdc7e680d922ca309fba7678)。

热泵（Heat Pump）。

<a id="r_ga8e40496a351c7ec5ea836805925f1e13"></a>

```c
#define BT_APPEARANCE_HEATING_INFRARED_HEATER 0x06C4
```

相关声明：[BT_APPEARANCE_HEATING_INFRARED_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e40496a351c7ec5ea836805925f1e13)。

红外加热器（Infrared Heater）。

<a id="r_ga46fe051c7e50492dba5ae824e154cf69"></a>

```c
#define BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER 0x06C5
```

相关声明：[BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga46fe051c7e50492dba5ae824e154cf69)。

辐射板式加热器（Radiant Panel Heater）。

<a id="r_ga995ca18db114ea062df0d76c9e241937"></a>

```c
#define BT_APPEARANCE_HEATING_FAN_HEATER 0x06C6
```

相关声明：[BT_APPEARANCE_HEATING_FAN_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga995ca18db114ea062df0d76c9e241937)。

暖风机（Fan Heater）。

<a id="r_gac74bc8e109f5d9b4c0988ee6378ed471"></a>

```c
#define BT_APPEARANCE_HEATING_AIR_CURTAIN 0x06C7
```

相关声明：[BT_APPEARANCE_HEATING_AIR_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac74bc8e109f5d9b4c0988ee6378ed471)。

空气幕（Air Curtain）。

<a id="r_gac856a99a5db04dc20229a6e60a18d310"></a>

```c
#define BT_APPEARANCE_GENERIC_ACCESS_CONTROL 0x0700
```

相关声明：[BT_APPEARANCE_GENERIC_ACCESS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac856a99a5db04dc20229a6e60a18d310)。

通用门禁控制设备（Generic Access Control）。

<a id="r_ga8e21f7df9d789b7c3aa6f7dab500df8c"></a>

```c
#define BT_APPEARANCE_CONTROL_ACCESS_DOOR 0x0701
```

相关声明：[BT_APPEARANCE_CONTROL_ACCESS_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e21f7df9d789b7c3aa6f7dab500df8c)。

出入门（Access Door）。

<a id="r_ga39134568b56c1d33e6567c893eb441f1"></a>

```c
#define BT_APPEARANCE_CONTROL_GARAGE_DOOR 0x0702
```

相关声明：[BT_APPEARANCE_CONTROL_GARAGE_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39134568b56c1d33e6567c893eb441f1)。

车库门（Garage Door）。

<a id="r_ga2b6c7987ee4040216a385e665ff92321"></a>

```c
#define BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR 0x0703
```

相关声明：[BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2b6c7987ee4040216a385e665ff92321)。

紧急出口门（Emergency Exit Door）。

<a id="r_gac2f588b6202e9d6140ec682cfe45f65d"></a>

```c
#define BT_APPEARANCE_CONTROL_ACCESS_LOCK 0x0704
```

相关声明：[BT_APPEARANCE_CONTROL_ACCESS_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac2f588b6202e9d6140ec682cfe45f65d)。

门禁锁（Access Lock）。

<a id="r_ga321d63ead349c0a83ef289bd2e4efb33"></a>

```c
#define BT_APPEARANCE_CONTROL_ELEVATOR 0x0705
```

相关声明：[BT_APPEARANCE_CONTROL_ELEVATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga321d63ead349c0a83ef289bd2e4efb33)。

电梯（Elevator）。

<a id="r_gaedc6415432862889e7f002fc9ef46b74"></a>

```c
#define BT_APPEARANCE_CONTROL_WINDOW 0x0706
```

相关声明：[BT_APPEARANCE_CONTROL_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaedc6415432862889e7f002fc9ef46b74)。

窗户（Window）。

<a id="r_gab2a476a90f20576c0a1784fdc1e5e633"></a>

```c
#define BT_APPEARANCE_CONTROL_ENTRANCE_GATE 0x0707
```

相关声明：[BT_APPEARANCE_CONTROL_ENTRANCE_GATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab2a476a90f20576c0a1784fdc1e5e633)。

入口大门（Entrance Gate）。

<a id="r_ga29d07ce1101740b5f6f980660e405278"></a>

```c
#define BT_APPEARANCE_CONTROL_DOOR_LOCK 0x0708
```

相关声明：[BT_APPEARANCE_CONTROL_DOOR_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga29d07ce1101740b5f6f980660e405278)。

门锁（Door Lock）。

<a id="r_ga824236ba19c7f54d06b9abcd7df8c767"></a>

```c
#define BT_APPEARANCE_CONTROL_LOCKER 0x0709
```

相关声明：[BT_APPEARANCE_CONTROL_LOCKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga824236ba19c7f54d06b9abcd7df8c767)。

储物柜（Locker）。

<a id="r_ga414b202e93d1db533853093d66603720"></a>

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE 0x0740
```

相关声明：[BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga414b202e93d1db533853093d66603720)。

通用电动设备（Generic Motorized Device）。

<a id="r_ga376ef909868a5c273b71d1c372755707"></a>

```c
#define BT_APPEARANCE_MOTORIZED_GATE 0x0741
```

相关声明：[BT_APPEARANCE_MOTORIZED_GATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga376ef909868a5c273b71d1c372755707)。

电动大门（Motorized Gate）。

<a id="r_ga338de5523abf3fd81e913f3cdb4a31b6"></a>

```c
#define BT_APPEARANCE_MOTORIZED_AWNING 0x0742
```

相关声明：[BT_APPEARANCE_MOTORIZED_AWNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga338de5523abf3fd81e913f3cdb4a31b6)。

遮阳篷（Awning）。

<a id="r_gaaa39c48ed2d6edd5650743b82154462b"></a>

```c
#define BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES 0x0743
```

相关声明：[BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaaa39c48ed2d6edd5650743b82154462b)。

百叶帘或遮阳帘（Blinds or Shades）。

<a id="r_ga53f6a4df5ccc2117525952be2e174ddc"></a>

```c
#define BT_APPEARANCE_MOTORIZED_CURTAINS 0x0744
```

相关声明：[BT_APPEARANCE_MOTORIZED_CURTAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga53f6a4df5ccc2117525952be2e174ddc)。

窗帘（Curtains）。

<a id="r_ga5f32cab5c7a155fffbe0c33cadfef31a"></a>

```c
#define BT_APPEARANCE_MOTORIZED_SCREEN 0x0745
```

相关声明：[BT_APPEARANCE_MOTORIZED_SCREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5f32cab5c7a155fffbe0c33cadfef31a)。

屏障（Screen）。

<a id="r_gadae82e45d9aafd34cafd3f0e793b1b24"></a>

```c
#define BT_APPEARANCE_GENERIC_POWER_DEVICE 0x0780
```

相关声明：[BT_APPEARANCE_GENERIC_POWER_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadae82e45d9aafd34cafd3f0e793b1b24)。

通用电源设备（Generic Power Device）。

<a id="r_gad9efd19e2c95525a3972c8b0f0417449"></a>

```c
#define BT_APPEARANCE_POWER_OUTLET 0x0781
```

相关声明：[BT_APPEARANCE_POWER_OUTLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad9efd19e2c95525a3972c8b0f0417449)。

电源插座（Power Outlet）。

<a id="r_ga2c5bd38d4eeb1aad2d29b004390a6d18"></a>

```c
#define BT_APPEARANCE_POWER_STRIP 0x0782
```

相关声明：[BT_APPEARANCE_POWER_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2c5bd38d4eeb1aad2d29b004390a6d18)。

电源插排（Power Strip）。

<a id="r_ga0d9aadc19f5f5f484769b225164866e4"></a>

```c
#define BT_APPEARANCE_POWER_PLUG 0x0783
```

相关声明：[BT_APPEARANCE_POWER_PLUG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d9aadc19f5f5f484769b225164866e4)。

插头（Plug）。

<a id="r_ga07acce808c9cf2b5e84aacd65e8f256d"></a>

```c
#define BT_APPEARANCE_POWER_SUPPLY 0x0784
```

相关声明：[BT_APPEARANCE_POWER_SUPPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga07acce808c9cf2b5e84aacd65e8f256d)。

电源（Power Supply）。

<a id="r_ga31842298741c822dcebba942453975c6"></a>

```c
#define BT_APPEARANCE_POWER_LED_DRIVER 0x0785
```

相关声明：[BT_APPEARANCE_POWER_LED_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga31842298741c822dcebba942453975c6)。

LED 驱动器（LED Driver）。

<a id="r_ga7de26016aa039e3e72ddd61653e1c1d8"></a>

```c
#define BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR 0x0786
```

相关声明：[BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7de26016aa039e3e72ddd61653e1c1d8)。

荧光灯控制装置（Fluorescent Lamp Gear）。

<a id="r_ga6396b1d813c9764bdfe92c4f2ba961b1"></a>

```c
#define BT_APPEARANCE_POWER_HID_LAMP_GEAR 0x0787
```

相关声明：[BT_APPEARANCE_POWER_HID_LAMP_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6396b1d813c9764bdfe92c4f2ba961b1)。

高强度气体放电灯控制装置（HID Lamp Gear）。

<a id="r_ga5d6b28b9660d2357e2af2bf0ceab9c18"></a>

```c
#define BT_APPEARANCE_POWER_CHARGE_CASE 0x0788
```

相关声明：[BT_APPEARANCE_POWER_CHARGE_CASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5d6b28b9660d2357e2af2bf0ceab9c18)。

充电盒（Charge Case）。

<a id="r_gab6a5ac3941a5707f052126810a7f22e0"></a>

```c
#define BT_APPEARANCE_POWER_POWER_BANK 0x0789
```

相关声明：[BT_APPEARANCE_POWER_POWER_BANK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab6a5ac3941a5707f052126810a7f22e0)。

移动电源（Power Bank）。

<a id="r_gacb3340c5193588eea2d42fe1bef443d0"></a>

```c
#define BT_APPEARANCE_GENERIC_LIGHT_SOURCE 0x07C0
```

相关声明：[BT_APPEARANCE_GENERIC_LIGHT_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacb3340c5193588eea2d42fe1bef443d0)。

通用光源（Generic Light Source）。

<a id="r_gafed8531ffde21d0ad6e8d477d64496f0"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB 0x07C1
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafed8531ffde21d0ad6e8d477d64496f0)。

白炽灯泡（Incandescent Light Bulb）。

<a id="r_ga66bf91b8a25ac88a0fd6ab9456201de1"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP 0x07C2
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga66bf91b8a25ac88a0fd6ab9456201de1)。

LED 灯（LED Lamp）。

<a id="r_ga1babd2989112bafb5819235fe5b6c556"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP 0x07C3
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1babd2989112bafb5819235fe5b6c556)。

高强度气体放电灯（HID Lamp）。

<a id="r_ga39957a77aa54255ab3a06441e422e7e3"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP 0x07C4
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39957a77aa54255ab3a06441e422e7e3)。

荧光灯（Fluorescent Lamp）。

<a id="r_ga242d324cf5cf33e4edd5cf33e8c3c89b"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY 0x07C5
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga242d324cf5cf33e4edd5cf33e8c3c89b)。

LED 阵列（LED Array）。

<a id="r_ga8449006920ed1fdd562c702ee2e16a21"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY 0x07C6
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8449006920ed1fdd562c702ee2e16a21)。

多色 LED 阵列（Multi-Color LED Array）。

<a id="r_gaf47bce54f4ae1915cd64c3c2d254e353"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN 0x07C7
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf47bce54f4ae1915cd64c3c2d254e353)。

低压卤素灯（Low voltage halogen）。

<a id="r_gaed4400a94dae4f536a456cc55eb6f6d5"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_OLED 0x07C8
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_OLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaed4400a94dae4f536a456cc55eb6f6d5)。

有机发光二极管（Organic light emitting diode）。

<a id="r_ga1e70d961fca2719243c866464132684c"></a>

```c
#define BT_APPEARANCE_GENERIC_WINDOW_COVERING 0x0800
```

相关声明：[BT_APPEARANCE_GENERIC_WINDOW_COVERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1e70d961fca2719243c866464132684c)。

通用窗户遮蔽物（Generic Window Covering）。

<a id="r_ga37614ae63c8287bc4bd0c9a5bf00502e"></a>

```c
#define BT_APPEARANCE_WINDOW_SHADES 0x0801
```

相关声明：[BT_APPEARANCE_WINDOW_SHADES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga37614ae63c8287bc4bd0c9a5bf00502e)。

遮阳窗帘（Window Shades）。

<a id="r_ga717efaeab0329ded066567761b9983a7"></a>

```c
#define BT_APPEARANCE_WINDOW_BLINDS 0x0802
```

相关声明：[BT_APPEARANCE_WINDOW_BLINDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga717efaeab0329ded066567761b9983a7)。

百叶窗帘（Window Blinds）。

<a id="r_ga9945bb52a9ee3268efda7d5e05421e12"></a>

```c
#define BT_APPEARANCE_WINDOW_AWNING 0x0803
```

相关声明：[BT_APPEARANCE_WINDOW_AWNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9945bb52a9ee3268efda7d5e05421e12)。

窗户遮阳篷（Window Awning）。

<a id="r_ga20352e58e6cec63efbb6beaa75c0e330"></a>

```c
#define BT_APPEARANCE_WINDOW_CURTAIN 0x0804
```

相关声明：[BT_APPEARANCE_WINDOW_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga20352e58e6cec63efbb6beaa75c0e330)。

窗帘（Window Curtain）。

<a id="r_ga7ead13b128fbc50be3f5c101fb1383cb"></a>

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER 0x0805
```

相关声明：[BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7ead13b128fbc50be3f5c101fb1383cb)。

外置百叶窗（Exterior Shutter）。

<a id="r_ga0a0b87095177af0560a540e545c97f42"></a>

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN 0x0806
```

相关声明：[BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a0b87095177af0560a540e545c97f42)。

外置遮阳屏（Exterior Screen）。

<a id="r_ga32bb0f06096ce5259676a31342b9f0d9"></a>

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SINK 0x0840
```

相关声明：[BT_APPEARANCE_GENERIC_AUDIO_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga32bb0f06096ce5259676a31342b9f0d9)。

通用音频接收端（Generic Audio Sink）。

<a id="r_gabcb109c4660a177494329faf353406f4"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER 0x0841
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabcb109c4660a177494329faf353406f4)。

独立扬声器（Standalone Speaker）。

<a id="r_ga93e3a858b2efabea72a8855a28ad21c2"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_SOUNDBAR 0x0842
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_SOUNDBAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga93e3a858b2efabea72a8855a28ad21c2)。

条形音箱（Soundbar）。

<a id="r_ga666aed968e9a0f9566edcc1bcba0bfbd"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER 0x0843
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga666aed968e9a0f9566edcc1bcba0bfbd)。

书架式音箱（Bookshelf Speaker）。

<a id="r_ga6b3ddddf1de7d95a15aa6194ddc656ee"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER 0x0844
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6b3ddddf1de7d95a15aa6194ddc656ee)。

支架式音箱（Standmounted Speaker）。

<a id="r_gadd82602d251aa555a06123ef0388d1b1"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE 0x0845
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadd82602d251aa555a06123ef0388d1b1)。

免提电话（Speakerphone）。

<a id="r_gac85b90f2585044d0efa61191dba3c596"></a>

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SOURCE 0x0880
```

相关声明：[BT_APPEARANCE_GENERIC_AUDIO_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac85b90f2585044d0efa61191dba3c596)。

通用音频源（Generic Audio Source）。

<a id="r_ga6dd1354de34ed79702d9d7878d859fcb"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE 0x0881
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6dd1354de34ed79702d9d7878d859fcb)。

麦克风（Microphone）。

<a id="r_gaa8d5a95cb181e27efb2409d5dce3da57"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_ALARM 0x0882
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa8d5a95cb181e27efb2409d5dce3da57)。

警报器（Alarm）。

<a id="r_ga748b4fa86145f3950069ed44cde8cacb"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BELL 0x0883
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BELL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga748b4fa86145f3950069ed44cde8cacb)。

铃（Bell）。

<a id="r_ga3415afbd526b29b5bbafc1ac889bd371"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_HORN 0x0884
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_HORN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3415afbd526b29b5bbafc1ac889bd371)。

号角（Horn）。

<a id="r_ga35ecc1a1051379010123582c82e9b31c"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE 0x0885
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga35ecc1a1051379010123582c82e9b31c)。

广播设备（Broadcasting Device）。

<a id="r_ga48fc37d769211cba1e6121e670b02e25"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK 0x0886
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga48fc37d769211cba1e6121e670b02e25)。

服务台（Service Desk）。

<a id="r_ga6ad3ee00ed05c8a7ed182df5c82a5af4"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_KIOSK 0x0887
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_KIOSK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ad3ee00ed05c8a7ed182df5c82a5af4)。

自助服务终端（Kiosk）。

<a id="r_gaad0fe38e5246c55cc562729448b9f390"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM 0x0888
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaad0fe38e5246c55cc562729448b9f390)。

广播室（Broadcasting Room）。

<a id="r_gac8ab0549f83c9d6b68dc4dd75cfe7b1e"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM 0x0889
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)。

礼堂（Auditorium）。

<a id="r_ga49328394fd7505da9476d4d62ae60c03"></a>

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE 0x08C0
```

相关声明：[BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga49328394fd7505da9476d4d62ae60c03)。

通用机动车辆（Generic Motorized Vehicle）。

<a id="r_ga6257291ed3e6d09ce6197e2081b36d04"></a>

```c
#define BT_APPEARANCE_VEHICLE_CAR 0x08C1
```

相关声明：[BT_APPEARANCE_VEHICLE_CAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6257291ed3e6d09ce6197e2081b36d04)。

汽车（Car）。

<a id="r_ga31ff643e1efccffd9ba73c793f63837c"></a>

```c
#define BT_APPEARANCE_VEHICLE_LARGE_GOODS 0x08C2
```

相关声明：[BT_APPEARANCE_VEHICLE_LARGE_GOODS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga31ff643e1efccffd9ba73c793f63837c)。

大型货运车辆（Large Goods Vehicle）。

<a id="r_ga68ade931a12e5d9e9863decad3d8de9e"></a>

```c
#define BT_APPEARANCE_VEHICLE_TWO_WHEELED 0x08C3
```

相关声明：[BT_APPEARANCE_VEHICLE_TWO_WHEELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga68ade931a12e5d9e9863decad3d8de9e)。

两轮车辆（2-Wheeled Vehicle）。

<a id="r_gaa71eaa4fd0eef66a794475cb44aaf397"></a>

```c
#define BT_APPEARANCE_VEHICLE_MOTORBIKE 0x08C4
```

相关声明：[BT_APPEARANCE_VEHICLE_MOTORBIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa71eaa4fd0eef66a794475cb44aaf397)。

摩托车（Motorbike）。

<a id="r_gae082982b90d94404b69c57987d8a2c5a"></a>

```c
#define BT_APPEARANCE_VEHICLE_SCOOTER 0x08C5
```

相关声明：[BT_APPEARANCE_VEHICLE_SCOOTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae082982b90d94404b69c57987d8a2c5a)。

踏板车（Scooter）。

<a id="r_ga18b0231dbd97d8871f685774f9e1b4e1"></a>

```c
#define BT_APPEARANCE_VEHICLE_MOPED 0x08C6
```

相关声明：[BT_APPEARANCE_VEHICLE_MOPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga18b0231dbd97d8871f685774f9e1b4e1)。

轻便摩托车（Moped）。

<a id="r_ga8159dfd6933a2a5fdb2c72da9623bc2e"></a>

```c
#define BT_APPEARANCE_VEHICLE_THREE_WHEELED 0x08C7
```

相关声明：[BT_APPEARANCE_VEHICLE_THREE_WHEELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8159dfd6933a2a5fdb2c72da9623bc2e)。

三轮车辆（3-Wheeled Vehicle）。

<a id="r_gac22a0476760c42eb8f00b36b74361c5e"></a>

```c
#define BT_APPEARANCE_VEHICLE_LIGHT 0x08C8
```

相关声明：[BT_APPEARANCE_VEHICLE_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac22a0476760c42eb8f00b36b74361c5e)。

轻型车辆（Light Vehicle）。

<a id="r_ga03e3660bdc2e439126f2f8df8ea335ee"></a>

```c
#define BT_APPEARANCE_VEHICLE_QUAD_BIKE 0x08C9
```

相关声明：[BT_APPEARANCE_VEHICLE_QUAD_BIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga03e3660bdc2e439126f2f8df8ea335ee)。

四轮摩托车（Quad Bike）。

<a id="r_ga0cf473bbf07d4576ab9f0116ca48f161"></a>

```c
#define BT_APPEARANCE_VEHICLE_MINIBUS 0x08CA
```

相关声明：[BT_APPEARANCE_VEHICLE_MINIBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0cf473bbf07d4576ab9f0116ca48f161)。

小型客车（Minibus）。

<a id="r_ga0da02a18987c653a3232c28a3e4908f7"></a>

```c
#define BT_APPEARANCE_VEHICLE_BUS 0x08CB
```

相关声明：[BT_APPEARANCE_VEHICLE_BUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0da02a18987c653a3232c28a3e4908f7)。

公共汽车（Bus）。

<a id="r_gabde7af9f7c25d56f5fb9643398273526"></a>

```c
#define BT_APPEARANCE_VEHICLE_TROLLEY 0x08CC
```

相关声明：[BT_APPEARANCE_VEHICLE_TROLLEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabde7af9f7c25d56f5fb9643398273526)。

电车（Trolley）。

<a id="r_gaa149e56e4b4a1b6dde821fbdac3d9c32"></a>

```c
#define BT_APPEARANCE_VEHICLE_AGRICULTURAL 0x08CD
```

相关声明：[BT_APPEARANCE_VEHICLE_AGRICULTURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa149e56e4b4a1b6dde821fbdac3d9c32)。

农业车辆（Agricultural Vehicle）。

<a id="r_gafcb3909bf61bb130f8c0a217e69477b8"></a>

```c
#define BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN 0x08CE
```

相关声明：[BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafcb3909bf61bb130f8c0a217e69477b8)。

露营车／拖挂式旅居车（Camper/Caravan）。

<a id="r_ga9366a994d42c88490313380d419b2a8e"></a>

```c
#define BT_APPEARANCE_VEHICLE_RECREATIONAL 0x08CF
```

相关声明：[BT_APPEARANCE_VEHICLE_RECREATIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9366a994d42c88490313380d419b2a8e)。

休闲车辆／自行式房车（Recreational Vehicle/Motor Home）。

<a id="r_gac08b31ff9b618b19e4c1b43ae2056b5f"></a>

```c
#define BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE 0x0900
```

相关声明：[BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac08b31ff9b618b19e4c1b43ae2056b5f)。

通用家用电器（Generic Domestic Appliance）。

<a id="r_gad02c3dc8fa1321b14ee70264a36c4950"></a>

```c
#define BT_APPEARANCE_APPLIANCE_REFRIGERATOR 0x0901
```

相关声明：[BT_APPEARANCE_APPLIANCE_REFRIGERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad02c3dc8fa1321b14ee70264a36c4950)。

冰箱（Refrigerator）。

<a id="r_ga6ec2458a171142a5e22ec339d23a5a0c"></a>

```c
#define BT_APPEARANCE_APPLIANCE_FREEZER 0x0902
```

相关声明：[BT_APPEARANCE_APPLIANCE_FREEZER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ec2458a171142a5e22ec339d23a5a0c)。

冷冻柜（Freezer）。

<a id="r_ga7a48c5a07e677167ae10412ed2c1040b"></a>

```c
#define BT_APPEARANCE_APPLIANCE_OVEN 0x0903
```

相关声明：[BT_APPEARANCE_APPLIANCE_OVEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7a48c5a07e677167ae10412ed2c1040b)。

烤箱（Oven）。

<a id="r_gabaac12b866cd29547165331333e8be3d"></a>

```c
#define BT_APPEARANCE_APPLIANCE_MICROWAVE 0x0904
```

相关声明：[BT_APPEARANCE_APPLIANCE_MICROWAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabaac12b866cd29547165331333e8be3d)。

微波炉（Microwave）。

<a id="r_ga5b0d9632cb2ed4afd856f05a1e857394"></a>

```c
#define BT_APPEARANCE_APPLIANCE_TOASTER 0x0905
```

相关声明：[BT_APPEARANCE_APPLIANCE_TOASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5b0d9632cb2ed4afd856f05a1e857394)。

烤面包机（Toaster）。

<a id="r_ga1febcada2c95105648831094a4de6a8d"></a>

```c
#define BT_APPEARANCE_APPLIANCE_WASHING_MACHINE 0x0906
```

相关声明：[BT_APPEARANCE_APPLIANCE_WASHING_MACHINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1febcada2c95105648831094a4de6a8d)。

洗衣机（Washing Machine）。

<a id="r_gaac26996e0de10b16e24900a08c1098f5"></a>

```c
#define BT_APPEARANCE_APPLIANCE_DRYER 0x0907
```

相关声明：[BT_APPEARANCE_APPLIANCE_DRYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaac26996e0de10b16e24900a08c1098f5)。

烘干机（Dryer）。

<a id="r_gac601c74c6132decf13527bdacbc5a08b"></a>

```c
#define BT_APPEARANCE_APPLIANCE_COFFEE_MAKER 0x0908
```

相关声明：[BT_APPEARANCE_APPLIANCE_COFFEE_MAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac601c74c6132decf13527bdacbc5a08b)。

咖啡机（Coffee maker）。

<a id="r_gaeb66941a8e8b38ed0ea47305da157e24"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_IRON 0x0909
```

相关声明：[BT_APPEARANCE_APPLIANCE_CLOTHES_IRON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeb66941a8e8b38ed0ea47305da157e24)。

电熨斗（Clothes iron）。

<a id="r_ga6a9885e9a2133c0732d056ecd63313ad"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CURLING_IRON 0x090A
```

相关声明：[BT_APPEARANCE_APPLIANCE_CURLING_IRON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6a9885e9a2133c0732d056ecd63313ad)。

卷发棒（Curling iron）。

<a id="r_ga15be0164f5883558fb61c9cb9679b78f"></a>

```c
#define BT_APPEARANCE_APPLIANCE_HAIR_DRYER 0x090B
```

相关声明：[BT_APPEARANCE_APPLIANCE_HAIR_DRYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga15be0164f5883558fb61c9cb9679b78f)。

吹风机（Hair dryer）。

<a id="r_ga46d5f18bb8c764c43af97fddcec4a1ec"></a>

```c
#define BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER 0x090C
```

相关声明：[BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga46d5f18bb8c764c43af97fddcec4a1ec)。

吸尘器（Vacuum cleaner）。

<a id="r_ga423e85d0816a4bd0205f4d8188e6c406"></a>

```c
#define BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER 0x090D
```

相关声明：[BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga423e85d0816a4bd0205f4d8188e6c406)。

扫地机器人（Robotic vacuum cleaner）。

<a id="r_ga78511e0ef7d509deeba65352e7f81ad8"></a>

```c
#define BT_APPEARANCE_APPLIANCE_RICE_COOKER 0x090E
```

相关声明：[BT_APPEARANCE_APPLIANCE_RICE_COOKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga78511e0ef7d509deeba65352e7f81ad8)。

电饭煲（Rice cooker）。

<a id="r_ga0292c6123b655964311d0e6027b5af20"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER 0x090F
```

相关声明：[BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0292c6123b655964311d0e6027b5af20)。

挂烫机（Clothes steamer）。

<a id="r_gabad761094a16873dcebbc6238825d84b"></a>

```c
#define BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE 0x0940
```

相关声明：[BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabad761094a16873dcebbc6238825d84b)。

通用可穿戴音频设备（Generic Wearable Audio Device）。

<a id="r_gab480735e2ba8db23d2668ea3a2137214"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD 0x0941
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab480735e2ba8db23d2668ea3a2137214)。

耳塞式耳机（Earbud）。

<a id="r_ga8bd98ba3a4c1cbf8dbf8235d9ad0f943"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET 0x0942
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)。

带麦克风耳机（Headset）。

<a id="r_gae420044380309abba1b9570d26735315"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES 0x0943
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae420044380309abba1b9570d26735315)。

头戴式耳机（Headphones）。

<a id="r_ga59ea8ff5efec7a19bce8440e7ae78a1e"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND 0x0944
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga59ea8ff5efec7a19bce8440e7ae78a1e)。

颈挂式耳机（Neck Band）。

<a id="r_ga24c9bcf9646ec5049abf310b31ab355e"></a>

```c
#define BT_APPEARANCE_GENERIC_AIRCRAFT 0x0980
```

相关声明：[BT_APPEARANCE_GENERIC_AIRCRAFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga24c9bcf9646ec5049abf310b31ab355e)。

通用航空器（Generic Aircraft）。

<a id="r_ga6f1d2fb56f53ac5317b024d7487b8742"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_LIGHT 0x0981
```

相关声明：[BT_APPEARANCE_AIRCRAFT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6f1d2fb56f53ac5317b024d7487b8742)。

轻型飞机（Light Aircraft）。

<a id="r_gad2d0b1c4b710e50127049ec4cd299396"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_MICROLIGHT 0x0982
```

相关声明：[BT_APPEARANCE_AIRCRAFT_MICROLIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad2d0b1c4b710e50127049ec4cd299396)。

超轻型飞机（Microlight）。

<a id="r_ga6f827322066333fe926f0912099e6903"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_PARAGLIDER 0x0983
```

相关声明：[BT_APPEARANCE_AIRCRAFT_PARAGLIDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6f827322066333fe926f0912099e6903)。

滑翔伞（Paraglider）。

<a id="r_gae7be5c3bf9ad97e34d6c62bb791c39c0"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER 0x0984
```

相关声明：[BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae7be5c3bf9ad97e34d6c62bb791c39c0)。

大型客机（Large Passenger Aircraft）。

<a id="r_gadb3b07d6c3d3f679b15069fdd8d4e1ee"></a>

```c
#define BT_APPEARANCE_GENERIC_AV_EQUIPMENT 0x09C0
```

相关声明：[BT_APPEARANCE_GENERIC_AV_EQUIPMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadb3b07d6c3d3f679b15069fdd8d4e1ee)。

通用音视频设备（Generic AV Equipment）。

<a id="r_ga7294c7b26ac8da3b9800c91ec824ad22"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER 0x09C1
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7294c7b26ac8da3b9800c91ec824ad22)。

放大器（Amplifier）。

<a id="r_gac826e2e5326d1aa5fdd7ebf55fe395e6"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RECEIVER 0x09C2
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac826e2e5326d1aa5fdd7ebf55fe395e6)。

接收机（Receiver）。

<a id="r_gad60d1a387a1c62218baa3044e5acc3db"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RADIO 0x09C3
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad60d1a387a1c62218baa3044e5acc3db)。

收音机（Radio）。

<a id="r_ga7ccf41932861fa5f33d12060a12d5aa7"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TUNER 0x09C4
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_TUNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7ccf41932861fa5f33d12060a12d5aa7)。

调谐器（Tuner）。

<a id="r_ga69417cb3e9c434e751483328d6134cdf"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE 0x09C5
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga69417cb3e9c434e751483328d6134cdf)。

唱盘（Turntable）。

<a id="r_ga6c9ad45a9b22a94ae0cce16bfe749a33"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER 0x09C6
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6c9ad45a9b22a94ae0cce16bfe749a33)。

CD 播放器（CD Player）。

<a id="r_ga02681af8d755c701d9caef3f89a5c35a"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER 0x09C7
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga02681af8d755c701d9caef3f89a5c35a)。

DVD 播放器（DVD Player）。

<a id="r_ga1394bc80927fb8db4eef1786111c65c7"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER 0x09C8
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1394bc80927fb8db4eef1786111c65c7)。

蓝光播放器（Bluray Player）。

<a id="r_gaa01c862bff9aaaad09ed925da60fcb25"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER 0x09C9
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa01c862bff9aaaad09ed925da60fcb25)。

光盘播放器（Optical Disc Player）。

<a id="r_gad0ac86cf291b781b772fa9e85dda283a"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX 0x09CA
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad0ac86cf291b781b772fa9e85dda283a)。

机顶盒（Set-Top Box）。

<a id="r_ga44b70b2f515416baf686b1e127ef4375"></a>

```c
#define BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT 0x0A00
```

相关声明：[BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga44b70b2f515416baf686b1e127ef4375)。

通用显示设备（Generic Display Equipment）。

<a id="r_ga9a6684aa8677575625e049fa0da2c26c"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION 0x0A01
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9a6684aa8677575625e049fa0da2c26c)。

电视机（Television）。

<a id="r_gabbcb0fbbeb6423052db9d5e04410499c"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR 0x0A02
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabbcb0fbbeb6423052db9d5e04410499c)。

监视器（Monitor）。

<a id="r_gaa98f5139c99b46515746fb76e9ae7f9b"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR 0x0A03
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa98f5139c99b46515746fb76e9ae7f9b)。

投影仪（Projector）。

<a id="r_gadb5595a41edf5974e03649a675618b7b"></a>

```c
#define BT_APPEARANCE_GENERIC_HEARING_AID 0x0A40
```

相关声明：[BT_APPEARANCE_GENERIC_HEARING_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadb5595a41edf5974e03649a675618b7b)。

通用助听器（Generic Hearing aid）。

<a id="r_ga28cc6555937d9d5a9e8ae0079fc8a534"></a>

```c
#define BT_APPEARANCE_HEARING_AID_IN_EAR 0x0A41
```

相关声明：[BT_APPEARANCE_HEARING_AID_IN_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga28cc6555937d9d5a9e8ae0079fc8a534)。

耳内式助听器（In-ear hearing aid）。

<a id="r_ga1fa6231e14dcfa90a5518e61f0e4e302"></a>

```c
#define BT_APPEARANCE_HEARING_AID_BEHIND_EAR 0x0A42
```

相关声明：[BT_APPEARANCE_HEARING_AID_BEHIND_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1fa6231e14dcfa90a5518e61f0e4e302)。

耳后式助听器（Behind-ear hearing aid）。

<a id="r_ga82ba79bd9fd04a3fbdb6d8b4e35e3877"></a>

```c
#define BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT 0x0A43
```

相关声明：[BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)。

人工耳蜗（Cochlear Implant）。

<a id="r_gaca727b215a8277d921c0a3bfeccb3f14"></a>

```c
#define BT_APPEARANCE_GENERIC_GAMING 0x0A80
```

相关声明：[BT_APPEARANCE_GENERIC_GAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca727b215a8277d921c0a3bfeccb3f14)。

通用游戏设备（Generic Gaming）。

<a id="r_ga8fbaf0fced0cce12e08c4a516351b166"></a>

```c
#define BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE 0x0A81
```

相关声明：[BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8fbaf0fced0cce12e08c4a516351b166)。

家用电子游戏机（Home Video Game Console）。

<a id="r_ga39ad633d1795af4546bd930d0e799447"></a>

```c
#define BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE 0x0A82
```

相关声明：[BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39ad633d1795af4546bd930d0e799447)。

便携式掌上游戏机（Portable handheld console）。

<a id="r_gabc243c7449804749704c1862db286eab"></a>

```c
#define BT_APPEARANCE_GENERIC_SIGNAGE 0x0AC0
```

相关声明：[BT_APPEARANCE_GENERIC_SIGNAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabc243c7449804749704c1862db286eab)。

通用标识设备（Generic Signage）。

<a id="r_gace31a591ef3b5f0812e4cbf417a2205a"></a>

```c
#define BT_APPEARANCE_SIGNAGE_DIGITAL 0x0AC1
```

相关声明：[BT_APPEARANCE_SIGNAGE_DIGITAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gace31a591ef3b5f0812e4cbf417a2205a)。

数字标牌（Digital Signage）。

<a id="r_gaa4674b06751edf98fa88ede568a68ad4"></a>

```c
#define BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL 0x0AC2
```

相关声明：[BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa4674b06751edf98fa88ede568a68ad4)。

电子标签（Electronic Label）。

<a id="r_ga93ee753bf3b8819239041c065eaf024f"></a>

```c
#define BT_APPEARANCE_GENERIC_PULSE_OXIMETER 0x0C40
```

相关声明：[BT_APPEARANCE_GENERIC_PULSE_OXIMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga93ee753bf3b8819239041c065eaf024f)。

通用脉搏血氧仪（Generic Pulse Oximeter）。

<a id="r_ga8a298130c73299b6079dae3065954c0c"></a>

```c
#define BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP 0x0C41
```

相关声明：[BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8a298130c73299b6079dae3065954c0c)。

指夹式脉搏血氧仪（Fingertip Pulse Oximeter）。

<a id="r_gaebcadd5c37e6d87903e2cb97e03aeb7d"></a>

```c
#define BT_APPEARANCE_PULSE_OXIMETER_WRIST 0x0C42
```

相关声明：[BT_APPEARANCE_PULSE_OXIMETER_WRIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaebcadd5c37e6d87903e2cb97e03aeb7d)。

腕戴式脉搏血氧仪（Wrist Worn Pulse Oximeter）。

<a id="r_ga1aec23cd4f531a57260c7c8faf9caf40"></a>

```c
#define BT_APPEARANCE_GENERIC_WEIGHT_SCALE 0x0C80
```

相关声明：[BT_APPEARANCE_GENERIC_WEIGHT_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1aec23cd4f531a57260c7c8faf9caf40)。

通用体重秤（Generic Weight Scale）。

<a id="r_ga7387d717c77b38374e981991278aeb1c"></a>

```c
#define BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE 0x0CC0
```

相关声明：[BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7387d717c77b38374e981991278aeb1c)。

通用个人助行设备（Generic Personal Mobility Device）。

<a id="r_ga7966ec64cafe708fe94a7c323fbe3713"></a>

```c
#define BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR 0x0CC1
```

相关声明：[BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7966ec64cafe708fe94a7c323fbe3713)。

电动轮椅（Powered Wheelchair）。

<a id="r_ga21f21a73f355ffaa408376ca4fc802a8"></a>

```c
#define BT_APPEARANCE_MOBILITY_SCOOTER 0x0CC2
```

相关声明：[BT_APPEARANCE_MOBILITY_SCOOTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga21f21a73f355ffaa408376ca4fc802a8)。

助行代步车（Mobility Scooter）。

<a id="r_gab77dd4cfe254df84cbe0b8d45247e198"></a>

```c
#define BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR 0x0D00
```

相关声明：[BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab77dd4cfe254df84cbe0b8d45247e198)。

连续血糖监测仪（Continuous Glucose Monitor）。

<a id="r_ga481169a27fab19628f81a68af31d543c"></a>

```c
#define BT_APPEARANCE_GENERIC_INSULIN_PUMP 0x0D40
```

相关声明：[BT_APPEARANCE_GENERIC_INSULIN_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga481169a27fab19628f81a68af31d543c)。

通用胰岛素泵（Generic Insulin Pump）。

<a id="r_ga63512439364307259010bededf7bfd8b"></a>

```c
#define BT_APPEARANCE_INSULIN_PUMP_DURABLE 0x0D41
```

相关声明：[BT_APPEARANCE_INSULIN_PUMP_DURABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga63512439364307259010bededf7bfd8b)。

耐用型胰岛素泵（Insulin Pump, durable pump）。

<a id="r_ga0979695247b96321e5a8b6869d09227a"></a>

```c
#define BT_APPEARANCE_INSULIN_PUMP_PATCH 0x0D44
```

相关声明：[BT_APPEARANCE_INSULIN_PUMP_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0979695247b96321e5a8b6869d09227a)。

贴片式胰岛素泵（Insulin Pump, patch pump）。

<a id="r_ga1562514d0182e8862edad570b7a346e6"></a>

```c
#define BT_APPEARANCE_INSULIN_PEN 0x0D48
```

相关声明：[BT_APPEARANCE_INSULIN_PEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1562514d0182e8862edad570b7a346e6)。

胰岛素笔（Insulin Pen）。

<a id="r_ga08453eebe2ae8f53deddaa64a029c2b5"></a>

```c
#define BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY 0x0D80
```

相关声明：[BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga08453eebe2ae8f53deddaa64a029c2b5)。

通用药物输送设备（Generic Medication Delivery）。

<a id="r_ga1332c44cc3371fa9006993d03ba4ae12"></a>

```c
#define BT_APPEARANCE_GENERIC_SPIROMETER 0x0DC0
```

相关声明：[BT_APPEARANCE_GENERIC_SPIROMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1332c44cc3371fa9006993d03ba4ae12)。

通用肺量计（Generic Spirometer）。

<a id="r_ga42b9d596efb757b209f080a8c33f3723"></a>

```c
#define BT_APPEARANCE_SPIROMETER_HANDHELD 0x0DC1
```

相关声明：[BT_APPEARANCE_SPIROMETER_HANDHELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga42b9d596efb757b209f080a8c33f3723)。

手持式肺量计（Handheld Spirometer）。

<a id="r_ga0d39ca2892bd96013b8c82111eecc1cb"></a>

```c
#define BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS 0x1440
```

相关声明：[BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d39ca2892bd96013b8c82111eecc1cb)。

通用户外运动设备（Generic Outdoor Sports Activity）。

<a id="r_ga30c97d6f5bff1a4a67e4f59eb4d49d2d"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION 0x1441
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)。

位置显示器（Location Display）。

<a id="r_ga52b6c51c9afcbbba12d9d3cae824f4a7"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV 0x1442
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga52b6c51c9afcbbba12d9d3cae824f4a7)。

位置与导航显示器（Location and Navigation Display）。

<a id="r_gadf053353789183d1b1c3ca13ad98559f"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD 0x1443
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadf053353789183d1b1c3ca13ad98559f)。

定位模块（Location Pod）。

<a id="r_ga8fbc7782099e724febb712ee108e8cba"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV 0x1444
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8fbc7782099e724febb712ee108e8cba)。

定位与导航模块（Location and Navigation Pod）。

<a id="define-members-1"></a>

### 通用数据类型（Common Data Types）

<a id="r_ga396b92d418fcb8263895e420b9df3df2"></a>

```c
#define BT_DATA_FLAGS 0x01
```

相关声明：[BT_DATA_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga396b92d418fcb8263895e420b9df3df2)。

广播数据标志（AD flags）。

<a id="r_ga6c725bd3d31c159a4d046561dbca38ba"></a>

```c
#define BT_DATA_UUID16_SOME 0x02
```

相关声明：[`BT_DATA_UUID16_SOME`：部分 16 位 UUID（Some 16-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6c725bd3d31c159a4d046561dbca38ba)。

16 位 UUID 列表，尚有更多条目（16-bit UUID, more available）。

<a id="r_ga0d55063b9ad321b5c530a0012337df8a"></a>

```c
#define BT_DATA_UUID16_ALL 0x03
```

相关声明：[BT_DATA_UUID16_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d55063b9ad321b5c530a0012337df8a)。

16 位 UUID 列表，已全部列出（16-bit UUID, all listed）。

<a id="r_ga2486a6748490ba57e442ca15223482ef"></a>

```c
#define BT_DATA_UUID32_SOME 0x04
```

相关声明：[`BT_DATA_UUID32_SOME`：部分 32 位 UUID（Some 32-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2486a6748490ba57e442ca15223482ef)。

32 位 UUID 列表，尚有更多条目（32-bit UUID, more available）。

<a id="r_gaaf825c3e4686e572a35ddd46ee6fe2e8"></a>

```c
#define BT_DATA_UUID32_ALL 0x05
```

相关声明：[BT_DATA_UUID32_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaaf825c3e4686e572a35ddd46ee6fe2e8)。

32 位 UUID 列表，已全部列出（32-bit UUID, all listed）。

<a id="r_ga5c4f7fc1b93c611e95f735330fba243b"></a>

```c
#define BT_DATA_UUID128_SOME 0x06
```

相关声明：[`BT_DATA_UUID128_SOME`：部分 128 位 UUID（Some 128-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5c4f7fc1b93c611e95f735330fba243b)。

128 位 UUID 列表，尚有更多条目（128-bit UUID, more available）。

<a id="r_gaafcade3dbbcb4005f4590e994f91884b"></a>

```c
#define BT_DATA_UUID128_ALL 0x07
```

相关声明：[BT_DATA_UUID128_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaafcade3dbbcb4005f4590e994f91884b)。

128 位 UUID 列表，已全部列出（128-bit UUID, all listed）。

<a id="r_gafc509b33a8d2dd9124f6893eadbe1662"></a>

```c
#define BT_DATA_NAME_SHORTENED 0x08
```

相关声明：[`BT_DATA_NAME_SHORTENED`：缩短名称（Shortened Name）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc509b33a8d2dd9124f6893eadbe1662)。

缩短名称（Shortened name）。

<a id="r_gab94a7c5689d296acf47f976538056ab5"></a>

```c
#define BT_DATA_NAME_COMPLETE 0x09
```

相关声明：[BT_DATA_NAME_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab94a7c5689d296acf47f976538056ab5)。

完整名称（Complete name）。

<a id="r_ga4988c17578c4cf76fcdd9d44e1c931b0"></a>

```c
#define BT_DATA_TX_POWER 0x0a
```

相关声明：[BT_DATA_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4988c17578c4cf76fcdd9d44e1c931b0)。

发射功率（Tx Power）。

<a id="r_ga152c3028a2befcc4caf40aa6590c80b7"></a>

```c
#define BT_DATA_DEVICE_CLASS 0x0d
```

相关声明：[BT_DATA_DEVICE_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga152c3028a2befcc4caf40aa6590c80b7)。

设备类别（Class of Device）。

<a id="r_ga053c8bb0aedd01b3dd3f6154f4b49999"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_HASH_C192 0x0e
```

相关声明：[BT_DATA_SIMPLE_PAIRING_HASH_C192](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga053c8bb0aedd01b3dd3f6154f4b49999)。

简单配对哈希 C-192（Simple Pairing Hash C-192）。

<a id="r_ga280f1f96c5204960fe034c9ddaf194ec"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_RAND_C192 0x0f
```

相关声明：[BT_DATA_SIMPLE_PAIRING_RAND_C192](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga280f1f96c5204960fe034c9ddaf194ec)。

简单配对随机数 R-192（Simple Pairing Randomizer R-192）。

<a id="r_gac9402c597e5b4497f4bcd22d5177cc23"></a>

```c
#define BT_DATA_DEVICE_ID 0x10
```

相关声明：[BT_DATA_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac9402c597e5b4497f4bcd22d5177cc23)。

设备 ID 配置文件（Device ID (Profile)）。

<a id="r_ga5014acb2fe8e76b855b55bf98abe6d05"></a>

```c
#define BT_DATA_SM_TK_VALUE 0x10
```

相关声明：[BT_DATA_SM_TK_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5014acb2fe8e76b855b55bf98abe6d05)。

安全管理器临时密钥值（Security Manager TK Value）。

<a id="r_gaa12c742d1c955036aa3f55e84df69890"></a>

```c
#define BT_DATA_SM_OOB_FLAGS 0x11
```

相关声明：[BT_DATA_SM_OOB_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa12c742d1c955036aa3f55e84df69890)。

安全管理器带外标志（Security Manager OOB Flags）。

<a id="r_gabcf872eafc60c21287f6be63174dc7c8"></a>

```c
#define BT_DATA_PERIPHERAL_INT_RANGE 0x12
```

相关声明：[BT_DATA_PERIPHERAL_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabcf872eafc60c21287f6be63174dc7c8)。

外设连接间隔范围（Peripheral Connection Interval Range）。

<a id="r_ga2ad4d2ec2ff29c0aad5159de12d3f741"></a>

```c
#define BT_DATA_SOLICIT16 0x14
```

相关声明：[BT_DATA_SOLICIT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2ad4d2ec2ff29c0aad5159de12d3f741)。

服务征询 UUID，16 位（Solicit UUIDs, 16-bit）。

<a id="r_ga217df3f70846e86fa09e5605d5acd291"></a>

```c
#define BT_DATA_SOLICIT128 0x15
```

相关声明：[BT_DATA_SOLICIT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga217df3f70846e86fa09e5605d5acd291)。

服务征询 UUID，128 位（Solicit UUIDs, 128-bit）。

<a id="r_ga76990dda919688b369decaf9d3606b32"></a>

```c
#define BT_DATA_SVC_DATA16 0x16
```

相关声明：[BT_DATA_SVC_DATA16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga76990dda919688b369decaf9d3606b32)。

服务数据，16 位 UUID（Service data, 16-bit UUID）。

<a id="r_gacb867f0436d38c5c80e3426ca6247a46"></a>

```c
#define BT_DATA_PUB_TARGET_ADDR 0x17
```

相关声明：[BT_DATA_PUB_TARGET_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacb867f0436d38c5c80e3426ca6247a46)。

公共目标地址（Public Target Address）。

<a id="r_ga3d9097d8f53213ccafc152c51ad6fdbd"></a>

```c
#define BT_DATA_RAND_TARGET_ADDR 0x18
```

相关声明：[BT_DATA_RAND_TARGET_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3d9097d8f53213ccafc152c51ad6fdbd)。

随机目标地址（Random Target Address）。

<a id="r_ga67fc721da05758b7d7a36aecaa035fac"></a>

```c
#define BT_DATA_GAP_APPEARANCE 0x19
```

相关声明：[BT_DATA_GAP_APPEARANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga67fc721da05758b7d7a36aecaa035fac)。

通用访问配置文件外观值（GAP appearance）。

<a id="r_ga6fd8c0f32bbcb97aaafee51fda0b601e"></a>

```c
#define BT_DATA_ADV_INT 0x1a
```

相关声明：[BT_DATA_ADV_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6fd8c0f32bbcb97aaafee51fda0b601e)。

广播间隔（Advertising Interval）。

<a id="r_gad9e8a273239fa160a6b2797ef5563a94"></a>

```c
#define BT_DATA_LE_BT_DEVICE_ADDRESS 0x1b
```

相关声明：[BT_DATA_LE_BT_DEVICE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad9e8a273239fa160a6b2797ef5563a94)。

低功耗蓝牙设备地址（LE Bluetooth Device Address）。

<a id="r_ga255c7cb16eb24b95fa0f531fc4574273"></a>

```c
#define BT_DATA_LE_ROLE 0x1c
```

相关声明：[BT_DATA_LE_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga255c7cb16eb24b95fa0f531fc4574273)。

低功耗蓝牙角色（LE Role）。

<a id="r_ga324f91521eacd1e9d579c9d52d02eb06"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_HASH 0x1d
```

相关声明：[BT_DATA_SIMPLE_PAIRING_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga324f91521eacd1e9d579c9d52d02eb06)。

简单配对哈希 C256（Simple Pairing Hash C256）。

<a id="r_gad7e7dd2d3a972e53f9e5e80627bd07e6"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_RAND 0x1e
```

相关声明：[BT_DATA_SIMPLE_PAIRING_RAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad7e7dd2d3a972e53f9e5e80627bd07e6)。

简单配对随机数 R256（Simple Pairing Randomizer R256）。

<a id="r_ga76e7e8971ed841b87fda08793a00b14f"></a>

```c
#define BT_DATA_SOLICIT32 0x1f
```

相关声明：[BT_DATA_SOLICIT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga76e7e8971ed841b87fda08793a00b14f)。

服务征询 UUID，32 位（Solicit UUIDs, 32-bit）。

<a id="r_ga7d411a723ff2f038c3b7a1e09c88cb3d"></a>

```c
#define BT_DATA_SVC_DATA32 0x20
```

相关声明：[BT_DATA_SVC_DATA32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7d411a723ff2f038c3b7a1e09c88cb3d)。

服务数据，32 位 UUID（Service data, 32-bit UUID）。

<a id="r_gaa53847910515d9488b490f17a4fdf0d1"></a>

```c
#define BT_DATA_SVC_DATA128 0x21
```

相关声明：[BT_DATA_SVC_DATA128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa53847910515d9488b490f17a4fdf0d1)。

服务数据，128 位 UUID（Service data, 128-bit UUID）。

<a id="r_ga883dda02c157f0de8157b1c5f66aafd0"></a>

```c
#define BT_DATA_LE_SC_CONFIRM_VALUE 0x22
```

相关声明：[BT_DATA_LE_SC_CONFIRM_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga883dda02c157f0de8157b1c5f66aafd0)。

低功耗安全连接确认值（LE SC Confirmation Value）。

<a id="r_gacbc31c67684e3c68481501cf89f9ec68"></a>

```c
#define BT_DATA_LE_SC_RANDOM_VALUE 0x23
```

相关声明：[BT_DATA_LE_SC_RANDOM_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacbc31c67684e3c68481501cf89f9ec68)。

低功耗安全连接随机值（LE SC Random Value）。

<a id="r_ga3c6a5903cc4a46aaf0b30a0de0179403"></a>

```c
#define BT_DATA_URI 0x24
```

相关声明：[BT_DATA_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3c6a5903cc4a46aaf0b30a0de0179403)。

统一资源标识符（URI）。

<a id="r_ga0f29f9d8f5a336af430f0a603e87e995"></a>

```c
#define BT_DATA_INDOOR_POS 0x25
```

相关声明：[BT_DATA_INDOOR_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0f29f9d8f5a336af430f0a603e87e995)。

室内定位（Indoor Positioning）。

<a id="r_ga8e9ccc669ee545152b2d9b3120692d55"></a>

```c
#define BT_DATA_TRANS_DISCOVER_DATA 0x26
```

相关声明：[BT_DATA_TRANS_DISCOVER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e9ccc669ee545152b2d9b3120692d55)。

传输发现数据（Transport Discovery Data）。

<a id="r_ga207bc1e5405a4fd3f39863a2cb304ebc"></a>

```c
#define BT_DATA_LE_SUPPORTED_FEATURES 0x27
```

相关声明：[BT_DATA_LE_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga207bc1e5405a4fd3f39863a2cb304ebc)。

低功耗蓝牙支持的特性（LE Supported Features）。

<a id="r_gae3eb96c0f127b6417d7cad288faaaceb"></a>

```c
#define BT_DATA_CHANNEL_MAP_UPDATE_IND 0x28
```

相关声明：[BT_DATA_CHANNEL_MAP_UPDATE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae3eb96c0f127b6417d7cad288faaaceb)。

信道映射更新指示（Channel Map Update Indication）。

<a id="r_gafc5984d58b0b54ee824dd83bc78dfbe9"></a>

```c
#define BT_DATA_MESH_PROV 0x29
```

相关声明：[BT_DATA_MESH_PROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc5984d58b0b54ee824dd83bc78dfbe9)。

网状网络配置协议数据单元（Mesh Provisioning PDU）。

<a id="r_gac351c67ab58520b796fa713602d9f602"></a>

```c
#define BT_DATA_MESH_MESSAGE 0x2a
```

相关声明：[BT_DATA_MESH_MESSAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac351c67ab58520b796fa713602d9f602)。

网状网络协议数据单元（Mesh Networking PDU）。

<a id="r_ga59cc479be1f6c61a4a47aa6f479fe67a"></a>

```c
#define BT_DATA_MESH_BEACON 0x2b
```

相关声明：[BT_DATA_MESH_BEACON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga59cc479be1f6c61a4a47aa6f479fe67a)。

网状网络信标（Mesh Beacon）。

<a id="r_ga16feb94cd09c04d020450f61646f5486"></a>

```c
#define BT_DATA_BIG_INFO 0x2c
```

相关声明：[BT_DATA_BIG_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga16feb94cd09c04d020450f61646f5486)。

广播等时组信息（BIGInfo）。

<a id="r_ga72d2e55819db593a6db77579ebfe1e9d"></a>

```c
#define BT_DATA_BROADCAST_CODE 0x2d
```

相关声明：[BT_DATA_BROADCAST_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga72d2e55819db593a6db77579ebfe1e9d)。

广播码（Broadcast Code）。

<a id="r_ga122da4184d606ae140f8a311aaebeedd"></a>

```c
#define BT_DATA_CSIS_RSI 0x2e
```

相关声明：[BT_DATA_CSIS_RSI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga122da4184d606ae140f8a311aaebeedd)。

协调集识别服务随机集 ID 类型（CSIS Random Set ID type）。

<a id="r_gad4ac2e0de80dddcacc4ca6d25765eebd"></a>

```c
#define BT_DATA_ADV_INT_LONG 0x2f
```

相关声明：[BT_DATA_ADV_INT_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad4ac2e0de80dddcacc4ca6d25765eebd)。

长广播间隔（Advertising Interval long）。

<a id="r_ga7d781791bc85fe3c7ea839ff617ee6e7"></a>

```c
#define BT_DATA_BROADCAST_NAME 0x30
```

相关声明：[BT_DATA_BROADCAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7d781791bc85fe3c7ea839ff617ee6e7)。

广播名称（Broadcast Name）。

<a id="r_ga41d5c898144e89b6035f92ff506f38a3"></a>

```c
#define BT_DATA_ENCRYPTED_AD_DATA 0x31
```

相关声明：[BT_DATA_ENCRYPTED_AD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga41d5c898144e89b6035f92ff506f38a3)。

加密广播数据（Encrypted Advertising Data）。

<a id="r_ga14a8b1cf9d6c1c9749443a012731d39c"></a>

```c
#define BT_DATA_PAWR_TIMING_INFO 0x32
```

相关声明：[BT_DATA_PAWR_TIMING_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga14a8b1cf9d6c1c9749443a012731d39c)。

周期广播响应时序信息（Periodic Advertising Response Timing Info）。

<a id="r_ga90c7a1175148f3a56b04dc0b29525a4d"></a>

```c
#define BT_DATA_ESL 0x34
```

相关声明：[BT_DATA_ESL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga90c7a1175148f3a56b04dc0b29525a4d)。

电子货架标签配置文件（Electronic Shelf Label Profile）。

<a id="r_gaecab0c77f9f912c16c264e7eaf2e4707"></a>

```c
#define BT_DATA_3D_INFO 0x3D
```

相关声明：[BT_DATA_3D_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaecab0c77f9f912c16c264e7eaf2e4707)。

三维信息数据（3D Information Data）。

<a id="r_ga63b846807bff632b1cdd49b1e46e63b4"></a>

```c
#define BT_DATA_MANUFACTURER_DATA 0xff
```

相关声明：[BT_DATA_MANUFACTURER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga63b846807bff632b1cdd49b1e46e63b4)。

厂商专用数据（Manufacturer Specific Data）。

<a id="define-members-2"></a>

### 标志数据类型的取值（Flags data type values）

<a id="r_ga36191ee000a2098fd679c398b31e0906"></a>

```c
#define BT_LE_AD_LIMITED 0x01
```

相关声明：[BT_LE_AD_LIMITED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga36191ee000a2098fd679c398b31e0906)。

有限可发现模式（Limited Discoverable）。

<a id="r_ga13d9b4a24e2a8b58402bfb21f8b782c8"></a>

```c
#define BT_LE_AD_GENERAL 0x02
```

相关声明：[BT_LE_AD_GENERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga13d9b4a24e2a8b58402bfb21f8b782c8)。

通用可发现模式（General Discoverable）。

<a id="r_gabf5725f481cb73cbd974f3653c904bc9"></a>

```c
#define BT_LE_AD_NO_BREDR 0x04
```

相关声明：[BT_LE_AD_NO_BREDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabf5725f481cb73cbd974f3653c904bc9)。

不支持基本速率／增强数据率（BR/EDR not supported）。

<a id="define-members-3"></a>

### 基础模型（Foundation Models）

<a id="r_ga004d8d1be55b2aec56abbeeca1d118d8"></a>

```c
#define BT_MESH_MODEL_ID_CFG_SRV 0x0000
```

相关声明：[BT_MESH_MODEL_ID_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga004d8d1be55b2aec56abbeeca1d118d8)。

配置服务器（Configuration Server）。

<a id="r_ga3f8442dcd1a110ea0d0023f50057139f"></a>

```c
#define BT_MESH_MODEL_ID_CFG_CLI 0x0001
```

相关声明：[BT_MESH_MODEL_ID_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3f8442dcd1a110ea0d0023f50057139f)。

配置客户端（Configuration Client）。

<a id="r_ga6416216348d7186f91175ca50bb8c903"></a>

```c
#define BT_MESH_MODEL_ID_HEALTH_SRV 0x0002
```

相关声明：[BT_MESH_MODEL_ID_HEALTH_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga6416216348d7186f91175ca50bb8c903)。

健康服务器（Health Server）。

<a id="r_gab58b85b7a77feeb579973177c12bb446"></a>

```c
#define BT_MESH_MODEL_ID_HEALTH_CLI 0x0003
```

相关声明：[BT_MESH_MODEL_ID_HEALTH_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gab58b85b7a77feeb579973177c12bb446)。

健康客户端（Health Client）。

<a id="r_ga9c7d1c5dfb87a5ce50c08747af47414f"></a>

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_SRV 0x0004
```

相关声明：[BT_MESH_MODEL_ID_REMOTE_PROV_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9c7d1c5dfb87a5ce50c08747af47414f)。

远程配网服务器（Remote Provisioning Server）。

<a id="r_gaf373eb4d8af5d6bee76a821bd4d5e48c"></a>

```c
#define BT_MESH_MODEL_ID_REMOTE_PROV_CLI 0x0005
```

相关声明：[BT_MESH_MODEL_ID_REMOTE_PROV_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf373eb4d8af5d6bee76a821bd4d5e48c)。

远程配网客户端（Remote Provisioning Client）。

<a id="r_ga599d00e9d63ade6ed1a6803579c1e16e"></a>

```c
#define BT_MESH_MODEL_ID_BRG_CFG_SRV 0x0008
```

相关声明：[BT_MESH_MODEL_ID_BRG_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga599d00e9d63ade6ed1a6803579c1e16e)。

桥接配置服务器（Bridge Configuration Sever），原文将 Server 写作 Sever。

<a id="r_ga9c776b4befd21c15f4867d906f631257"></a>

```c
#define BT_MESH_MODEL_ID_BRG_CFG_CLI 0x0009
```

相关声明：[BT_MESH_MODEL_ID_BRG_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9c776b4befd21c15f4867d906f631257)。

桥接配置客户端（Bridge Configuration Client）。

<a id="r_gacca0e355982935cfbde46a06b09a7bec"></a>

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_SRV 0x000a
```

相关声明：[BT_MESH_MODEL_ID_PRIV_BEACON_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gacca0e355982935cfbde46a06b09a7bec)。

私有信标服务器（Private Beacon Server）。

<a id="r_gab3b21cbee4e11319a6e0ba3b02b24a91"></a>

```c
#define BT_MESH_MODEL_ID_PRIV_BEACON_CLI 0x000b
```

相关声明：[BT_MESH_MODEL_ID_PRIV_BEACON_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gab3b21cbee4e11319a6e0ba3b02b24a91)。

私有信标客户端（Private Beacon Client）。

<a id="r_ga1e9d8be1d2e65d2977aea0306b015258"></a>

```c
#define BT_MESH_MODEL_ID_SAR_CFG_SRV 0x000e
```

相关声明：[BT_MESH_MODEL_ID_SAR_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga1e9d8be1d2e65d2977aea0306b015258)。

分段与重组配置服务器（SAR Configuration Server）。

<a id="r_gaf214eb7eef3530919432b62ff9b353c3"></a>

```c
#define BT_MESH_MODEL_ID_SAR_CFG_CLI 0x000f
```

相关声明：[BT_MESH_MODEL_ID_SAR_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf214eb7eef3530919432b62ff9b353c3)。

分段与重组配置客户端（SAR Configuration Client）。

<a id="r_ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a"></a>

```c
#define BT_MESH_MODEL_ID_OP_AGG_SRV 0x0010
```

相关声明：[BT_MESH_MODEL_ID_OP_AGG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)。

操作码聚合器服务器（Opcodes Aggregator Server）。

<a id="r_gabac62a77e7d2d7677af21c33c8629187"></a>

```c
#define BT_MESH_MODEL_ID_OP_AGG_CLI 0x0011
```

相关声明：[BT_MESH_MODEL_ID_OP_AGG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gabac62a77e7d2d7677af21c33c8629187)。

操作码聚合器客户端（Opcodes Aggregator Client）。

<a id="r_gaec3abd6a0bd7b07a71fe5ed6a7a6931a"></a>

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV 0x0012
```

相关声明：[BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)。

大型组成数据服务器（Large Composition Data Server）。

<a id="r_ga729d67e4183457932e4c837d65abd842"></a>

```c
#define BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI 0x0013
```

相关声明：[BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga729d67e4183457932e4c837d65abd842)。

大型组成数据客户端（Large Composition Data Client）。

<a id="r_ga165bc198dadaa0d534ec82eb8192ebc0"></a>

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV 0x0014
```

相关声明：[BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga165bc198dadaa0d534ec82eb8192ebc0)。

请求PDU重放保护列表配置服务器（Solicitation PDU RPL Configuration Server）。

<a id="r_ga6e747dd364bcfaa368e37c5f01afd530"></a>

```c
#define BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI 0x0015
```

相关声明：[BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga6e747dd364bcfaa368e37c5f01afd530)。

请求PDU重放保护列表配置客户端（Solicitation PDU RPL Configuration Client）。

<a id="r_gaddc0bd645180a57cb9cd36745b84f7a1"></a>

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV 0x000c
```

相关声明：[BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaddc0bd645180a57cb9cd36745b84f7a1)。

私有代理服务器（Private Proxy Server）。

<a id="r_gadd36546fb2cb6d1c731f7ae7674af6a7"></a>

```c
#define BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI 0x000d
```

相关声明：[BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadd36546fb2cb6d1c731f7ae7674af6a7)。

私有代理客户端（Private Proxy Client）。

<a id="define-members-4"></a>

### Mesh模型规范中的模型（Models from the Mesh Model Specification）

<a id="r_ga83e1ed5398d513cfeb900e41655aa4d8"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_SRV 0x1000
```

相关声明：[BT_MESH_MODEL_ID_GEN_ONOFF_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga83e1ed5398d513cfeb900e41655aa4d8)。

通用开关服务器（Generic OnOff Server）。

<a id="r_ga4f0eee2569b518a5e4250f5b7b294fed"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ONOFF_CLI 0x1001
```

相关声明：[BT_MESH_MODEL_ID_GEN_ONOFF_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4f0eee2569b518a5e4250f5b7b294fed)。

通用开关客户端（Generic OnOff Client）。

<a id="r_ga7f10a8332b1406c3ad628b9679e1d7cb"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_SRV 0x1002
```

相关声明：[BT_MESH_MODEL_ID_GEN_LEVEL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga7f10a8332b1406c3ad628b9679e1d7cb)。

通用级别服务器（Generic Level Server）。

<a id="r_ga462c578845a17b20cdb3e008f74f93a6"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LEVEL_CLI 0x1003
```

相关声明：[BT_MESH_MODEL_ID_GEN_LEVEL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga462c578845a17b20cdb3e008f74f93a6)。

通用级别客户端（Generic Level Client）。

<a id="r_ga004d5ec0870d47a8d37182e5b0c089a5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV 0x1004
```

相关声明：[BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga004d5ec0870d47a8d37182e5b0c089a5)。

通用默认过渡时间服务器（Generic Default Transition Time Server）。

<a id="r_gafa1c6a7d857fe13a139ce2242b4e62f5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI 0x1005
```

相关声明：[BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gafa1c6a7d857fe13a139ce2242b4e62f5)。

通用默认过渡时间客户端（Generic Default Transition Time Client）。

<a id="r_ga09ac731fff09146ec68557f00e8294e0"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV 0x1006
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga09ac731fff09146ec68557f00e8294e0)。

通用电源开关服务器（Generic Power OnOff Server）。

<a id="r_ga2a6dad18792ba7f1d81d6c9a1c65f90a"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV 0x1007
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2a6dad18792ba7f1d81d6c9a1c65f90a)。

通用电源开关设置服务器（Generic Power OnOff Setup Server）。

<a id="r_ga9f6544f7b87f39d0792ea2de13cd45f1"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI 0x1008
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9f6544f7b87f39d0792ea2de13cd45f1)。

通用电源开关客户端（Generic Power OnOff Client）。

<a id="r_gadd30afe63f89e9c1778e56f722fd82f9"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV 0x1009
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadd30afe63f89e9c1778e56f722fd82f9)。

通用功率级别服务器（Generic Power Level Server）。

<a id="r_ga1ff6ec64ce3a86d1cfd00fc98e89c0a5"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV 0x100a
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)。

通用功率级别设置服务器（Generic Power Level Setup Server）。

<a id="r_ga8420454c35afc12c62ede55942f3b6d3"></a>

```c
#define BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI 0x100b
```

相关声明：[BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8420454c35afc12c62ede55942f3b6d3)。

通用功率级别客户端（Generic Power Level Client）。

<a id="r_gacf891135f54fb1fbb62beb812235619e"></a>

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_SRV 0x100c
```

相关声明：[BT_MESH_MODEL_ID_GEN_BATTERY_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gacf891135f54fb1fbb62beb812235619e)。

通用电池服务器（Generic Battery Server）。

<a id="r_ga34bb3d4839e9685ec55f8285aac9a79f"></a>

```c
#define BT_MESH_MODEL_ID_GEN_BATTERY_CLI 0x100d
```

相关声明：[BT_MESH_MODEL_ID_GEN_BATTERY_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga34bb3d4839e9685ec55f8285aac9a79f)。

通用电池客户端（Generic Battery Client）。

<a id="r_gad516f513c5c942fbfee65b85332b105e"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SRV 0x100e
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad516f513c5c942fbfee65b85332b105e)。

通用位置服务器（Generic Location Server）。

<a id="r_ga240d1ed34b7341627773cce862f85620"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV 0x100f
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga240d1ed34b7341627773cce862f85620)。

通用位置设置服务器（Generic Location Setup Server）。

<a id="r_ga8fa01ddb1f4de4d61500bb650243390d"></a>

```c
#define BT_MESH_MODEL_ID_GEN_LOCATION_CLI 0x1010
```

相关声明：[BT_MESH_MODEL_ID_GEN_LOCATION_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8fa01ddb1f4de4d61500bb650243390d)。

通用位置客户端（Generic Location Client）。

<a id="r_ga3cc6862e9c72f9282055c5cda2343c89"></a>

```c
#define BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV 0x1011
```

相关声明：[BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3cc6862e9c72f9282055c5cda2343c89)。

通用管理员属性服务器（Generic Admin Property Server）。

<a id="r_ga32e09ddfebd2e8b22da9a3102e116aae"></a>

```c
#define BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV 0x1012
```

相关声明：[BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga32e09ddfebd2e8b22da9a3102e116aae)。

通用制造商属性服务器（Generic Manufacturer Property Server）。

<a id="r_ga4b7b6a4b47e87de94ccf11ef1abd64b9"></a>

```c
#define BT_MESH_MODEL_ID_GEN_USER_PROP_SRV 0x1013
```

相关声明：[BT_MESH_MODEL_ID_GEN_USER_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4b7b6a4b47e87de94ccf11ef1abd64b9)。

通用用户属性服务器（Generic User Property Server）。

<a id="r_ga20906658018ef26114d8a6656c258f62"></a>

```c
#define BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV 0x1014
```

相关声明：[BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga20906658018ef26114d8a6656c258f62)。

通用客户端属性服务器（Generic Client Property Server）。

<a id="r_ga69455e5b1e6def3d909c4bb6e0dee9ae"></a>

```c
#define BT_MESH_MODEL_ID_GEN_PROP_CLI 0x1015
```

相关声明：[BT_MESH_MODEL_ID_GEN_PROP_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga69455e5b1e6def3d909c4bb6e0dee9ae)。

通用属性客户端（Generic Property Client）。

<a id="r_ga3e0dcb14f46f6076e5b1b114b977f630"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_SRV 0x1100
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3e0dcb14f46f6076e5b1b114b977f630)。

传感器服务器（Sensor Server）。

<a id="r_gad10780bfc1c16866fa28de750e56bec3"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_SETUP_SRV 0x1101
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad10780bfc1c16866fa28de750e56bec3)。

传感器设置服务器（Sensor Setup Server）。

<a id="r_ga8f1e4ff66d388627dbe91b2f8d4ed358"></a>

```c
#define BT_MESH_MODEL_ID_SENSOR_CLI 0x1102
```

相关声明：[BT_MESH_MODEL_ID_SENSOR_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8f1e4ff66d388627dbe91b2f8d4ed358)。

传感器客户端（Sensor Client）。

<a id="r_ga93fbf1c661a75d70fdbd2a599353eb94"></a>

```c
#define BT_MESH_MODEL_ID_TIME_SRV 0x1200
```

相关声明：[BT_MESH_MODEL_ID_TIME_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga93fbf1c661a75d70fdbd2a599353eb94)。

时间服务器（Time Server）。

<a id="r_ga2725121dc8c2c21c0ee469fe4348f45f"></a>

```c
#define BT_MESH_MODEL_ID_TIME_SETUP_SRV 0x1201
```

相关声明：[BT_MESH_MODEL_ID_TIME_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2725121dc8c2c21c0ee469fe4348f45f)。

时间设置服务器（Time Setup Server）。

<a id="r_ga500df90af7989794c5d72e760e5e65c6"></a>

```c
#define BT_MESH_MODEL_ID_TIME_CLI 0x1202
```

相关声明：[BT_MESH_MODEL_ID_TIME_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga500df90af7989794c5d72e760e5e65c6)。

时间客户端（Time Client）。

<a id="r_gaaa5554e3d48ae101596476e6bd6caf67"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_SRV 0x1203
```

相关声明：[BT_MESH_MODEL_ID_SCENE_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaaa5554e3d48ae101596476e6bd6caf67)。

场景服务器（Scene Server）。

<a id="r_gaa3b08fc8788684abb960fa3516726264"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_SETUP_SRV 0x1204
```

相关声明：[BT_MESH_MODEL_ID_SCENE_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa3b08fc8788684abb960fa3516726264)。

场景设置服务器（Scene Setup Server）。

<a id="r_gad60472aa004a8a913aeb63ef62c45857"></a>

```c
#define BT_MESH_MODEL_ID_SCENE_CLI 0x1205
```

相关声明：[BT_MESH_MODEL_ID_SCENE_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad60472aa004a8a913aeb63ef62c45857)。

场景客户端（Scene Client）。

<a id="r_ga82b723752e240f22b9bcc8dc3dd10eb9"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SRV 0x1206
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga82b723752e240f22b9bcc8dc3dd10eb9)。

调度器服务器（Scheduler Server）。

<a id="r_ga3dbec5a3b82cb25a142c4bc851e3fe0e"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV 0x1207
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3dbec5a3b82cb25a142c4bc851e3fe0e)。

调度器设置服务器（Scheduler Setup Server）。

<a id="r_gac743b26cf7e746b16302c25e8cd56221"></a>

```c
#define BT_MESH_MODEL_ID_SCHEDULER_CLI 0x1208
```

相关声明：[BT_MESH_MODEL_ID_SCHEDULER_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gac743b26cf7e746b16302c25e8cd56221)。

调度器客户端（Scheduler Client）。

<a id="r_ga16df49e84e84d0ae4a6ab5d5f3f1b2b6"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV 0x1300
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)。

灯光亮度服务器（Light Lightness Server）。

<a id="r_gadb93b2ed2256a5c9c3f66237841b1bf5"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV 0x1301
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadb93b2ed2256a5c9c3f66237841b1bf5)。

灯光亮度设置服务器（Light Lightness Setup Server）。

<a id="r_ga960055723dec7b3b366efa7c49cafc2e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI 0x1302
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga960055723dec7b3b366efa7c49cafc2e)。

灯光亮度客户端（Light Lightness Client）。

<a id="r_gaa9a211341c5b3283b9b0e0842adef053"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SRV 0x1303
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa9a211341c5b3283b9b0e0842adef053)。

灯光色温与亮度服务器（Light CTL Server）。

<a id="r_ga28ac69b2dbeec70bae4bd3c0381e9e93"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV 0x1304
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga28ac69b2dbeec70bae4bd3c0381e9e93)。

灯光色温与亮度设置服务器（Light CTL Setup Server）。

<a id="r_ga58fc8d99b746b0061177ac5d95341da1"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_CLI 0x1305
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga58fc8d99b746b0061177ac5d95341da1)。

灯光色温与亮度客户端（Light CTL Client）。

<a id="r_gafcb1f1ea20bb78b78a9ead4bfdbe3e47"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV 0x1306
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)。

灯光色温服务器（Light CTL Temperature Server）。

<a id="r_gaa0ddc753a226060d014dcd368feab17e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SRV 0x1307
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa0ddc753a226060d014dcd368feab17e)。

灯光色相、饱和度与亮度服务器（Light HSL Server）。

<a id="r_ga574d3ba3f629bdbffc8f15db931a263a"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV 0x1308
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga574d3ba3f629bdbffc8f15db931a263a)。

灯光色相、饱和度与亮度设置服务器（Light HSL Setup Server）。

<a id="r_ga2d111a352322be8e33ba0cba0feb3f0c"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_CLI 0x1309
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2d111a352322be8e33ba0cba0feb3f0c)。

灯光色相、饱和度与亮度客户端（Light HSL Client）。

<a id="r_ga865952346db9336a255c71bcb5f09774"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV 0x130a
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga865952346db9336a255c71bcb5f09774)。

灯光HSL色相服务器（Light HSL Hue Server）。

<a id="r_gae55004e70670a8711e18e9c9b3428720"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV 0x130b
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gae55004e70670a8711e18e9c9b3428720)。

灯光HSL饱和度服务器（Light HSL Saturation Server）。

<a id="r_ga29e1a90f166d88b6773d9b7ccf08e1c7"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SRV 0x130c
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga29e1a90f166d88b6773d9b7ccf08e1c7)。

灯光色度与亮度服务器（Light xyL Server）。

<a id="r_ga4addae460d6b3c0a914198695b3e31ea"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV 0x130d
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4addae460d6b3c0a914198695b3e31ea)。

灯光色度与亮度设置服务器（Light xyL Setup Server）。

<a id="r_ga0ca4d9997e6016b5c27f42549d42a99d"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_XYL_CLI 0x130e
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_XYL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga0ca4d9997e6016b5c27f42549d42a99d)。

灯光色度与亮度客户端（Light xyL Client）。

<a id="r_ga789412252034939539ba45e4bf21e3e2"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SRV 0x130f
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga789412252034939539ba45e4bf21e3e2)。

灯光亮度控制服务器（Light LC Server）。

<a id="r_ga436358740bb64d845aa4d849d462a12e"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV 0x1310
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga436358740bb64d845aa4d849d462a12e)。

灯光亮度控制设置服务器（Light LC Setup Server）。

<a id="r_gaadd48b07e1eb53df24df40b7ea412e90"></a>

```c
#define BT_MESH_MODEL_ID_LIGHT_LC_CLI 0x1311
```

相关声明：[BT_MESH_MODEL_ID_LIGHT_LC_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaadd48b07e1eb53df24df40b7ea412e90)。

灯光亮度控制客户端（Light LC Client）。

<a id="define-members-5"></a>

### Mesh二进制大对象传输模型规范中的模型（Models from the Mesh Binary Large Object Transfer Model Specification）

<a id="r_gae85d4cf7aad4e94582c24f79d6f60904"></a>

```c
#define BT_MESH_MODEL_ID_BLOB_SRV 0x1400
```

相关声明：[BT_MESH_MODEL_ID_BLOB_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gae85d4cf7aad4e94582c24f79d6f60904)。

二进制大对象传输服务器（BLOB Transfer Server）。

<a id="r_ga17e2e59a1344e623fe9fec6e27b7f22e"></a>

```c
#define BT_MESH_MODEL_ID_BLOB_CLI 0x1401
```

相关声明：[BT_MESH_MODEL_ID_BLOB_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga17e2e59a1344e623fe9fec6e27b7f22e)。

二进制大对象传输客户端（BLOB Transfer Client）。

<a id="define-members-6"></a>

### Mesh设备固件更新模型规范中的模型（Models from the Mesh Device Firmware Update Model Specification）

<a id="r_ga0215c2c8cd16ab6536ea243864f9604e"></a>

```c
#define BT_MESH_MODEL_ID_DFU_SRV 0x1402
```

相关声明：[BT_MESH_MODEL_ID_DFU_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga0215c2c8cd16ab6536ea243864f9604e)。

固件更新服务器（Firmware Update Server）。

<a id="r_gaf477a37238ec577000a646af40862ee1"></a>

```c
#define BT_MESH_MODEL_ID_DFU_CLI 0x1403
```

相关声明：[BT_MESH_MODEL_ID_DFU_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf477a37238ec577000a646af40862ee1)。

固件更新客户端（Firmware Update Client）。

<a id="r_gaf4309dea32d05274f8f3a6ea45faba38"></a>

```c
#define BT_MESH_MODEL_ID_DFD_SRV 0x1404
```

相关声明：[BT_MESH_MODEL_ID_DFD_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf4309dea32d05274f8f3a6ea45faba38)。

固件分发服务器（Firmware Distribution Server）。

<a id="r_ga87d3b5cc207dc3b51e85c9594bb98cad"></a>

```c
#define BT_MESH_MODEL_ID_DFD_CLI 0x1405
```

相关声明：[BT_MESH_MODEL_ID_DFD_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga87d3b5cc207dc3b51e85c9594bb98cad)。

固件分发客户端（Firmware Distribution Client）。

<a id="define-members-7"></a>

### 公司标识符（Company Identifiers，参见 Bluetooth Assigned Numbers）

<a id="r_ga6bbf21c05f24d2c2c710be9bcf05af5f"></a>

```c
#define BT_COMP_ID_LF 0x05f1
```

相关声明：[BT_COMP_ID_LF](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6bbf21c05f24d2c2c710be9bcf05af5f)。

Linux 基金会（The Linux Foundation）。

<a id="define-members-8"></a>

### 已定义的基本速率设备类别值（Defined BR Class of Device (CoD) values）

<a id="r_gaa8793a9bc39bf833124c8c961e441a43"></a>

```c
#define BT_COD(major_service, major_device, minor_device)
```

相关声明：[BT_COD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa8793a9bc39bf833124c8c961e441a43)。

<a id="r_gaf2c925e431eec42930101a72b00a7283"></a>

```c
#define BT_COD_VALID(cod)
```

相关声明：[BT_COD_VALID](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf2c925e431eec42930101a72b00a7283)。

<a id="r_gab598bdad77874748f74187aa32049ea6"></a>

```c
#define BT_COD_MAJOR_SERVICE_CLASSES(cod)
```

相关声明：[BT_COD_MAJOR_SERVICE_CLASSES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab598bdad77874748f74187aa32049ea6)。

<a id="r_ga129895b48ad9071017a2e97335ec6d2b"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS(cod)
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga129895b48ad9071017a2e97335ec6d2b)。

<a id="r_gadcf892b98d0924ea8a78d4b8b588bddb"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS(cod)
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadcf892b98d0924ea8a78d4b8b588bddb)。

<a id="define-members-9"></a>

### 主服务类别（Major Service Classes）

<a id="r_ga01883ae9792f486644dc96dd0559c72d"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER BIT(13)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga01883ae9792f486644dc96dd0559c72d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

有限可发现模式服务类别（Limited Discoverable Mode service class）。

<a id="r_ga031275c4187717b7556c4f0a7e16126a"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_LE_AUDIO BIT(14)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_LE_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga031275c4187717b7556c4f0a7e16126a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

低功耗音频服务类别（LE Audio service class）。

<a id="r_ga18cbe8ede63ed6c3396aabf01c97c672"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_RESERVED BIT(15)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_RESERVED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga18cbe8ede63ed6c3396aabf01c97c672)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

保留服务类别（Reserved service class）。

<a id="r_ga9fa4505b17dc53c22c9ac3fde9743e29"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_POSITIONING BIT(16)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_POSITIONING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9fa4505b17dc53c22c9ac3fde9743e29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

定位服务类别（Positioning service class）。

<a id="r_ga262412d5459d96d7f64a3d13db4906d2"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_NETWORKING BIT(17)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_NETWORKING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga262412d5459d96d7f64a3d13db4906d2)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

联网服务类别（Networking service class）。

<a id="r_ga6f959f962a9054102b4bbfe5b7248dd5"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_RENDERING BIT(18)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_RENDERING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6f959f962a9054102b4bbfe5b7248dd5)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

呈现服务类别（Rendering service class）。

<a id="r_ga35cd970ddcba07d98e9e42863ee155f9"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_CAPTURING BIT(19)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_CAPTURING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga35cd970ddcba07d98e9e42863ee155f9)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

采集服务类别（Capturing service class）。

<a id="r_ga17cf278f25d45040991ef2d60dafb456"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER BIT(20)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga17cf278f25d45040991ef2d60dafb456)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

对象传输服务类别（Object Transfer service class）。

<a id="r_ga2c70ab983a099e74a89aaaff02c086d0"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_AUDIO BIT(21)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2c70ab983a099e74a89aaaff02c086d0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

音频服务类别（Audio service class）。

<a id="r_ga2bca689e747d06869b3e86dbe7e10253"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_TELEPHONY BIT(22)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_TELEPHONY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2bca689e747d06869b3e86dbe7e10253)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

电话服务类别（Telephony service class）。

<a id="r_gafb44e9944c2f84d45d448975c1ab0300"></a>

```c
#define BT_COD_MAJOR_SVC_CLASS_INFORMATION BIT(23)
```

相关声明：[BT_COD_MAJOR_SVC_CLASS_INFORMATION](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafb44e9944c2f84d45d448975c1ab0300)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

信息服务类别（Information service class）。

<a id="define-members-10"></a>

### 主设备类别（Major Device Class）

<a id="r_ga9e57c7be37bc489c6ec4e35bf26e5718"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS 0x00
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9e57c7be37bc489c6ec4e35bf26e5718)。

杂项主设备类别（Miscellaneous major device class）。

<a id="r_ga41f24363507a81975e1a1de8068bcd86"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_COMPUTER 0x01
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_COMPUTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga41f24363507a81975e1a1de8068bcd86)。

计算机主设备类别（Computer major device class）。

<a id="r_gaf4e20997428ae008b48f1eee3f150633"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PHONE 0x02
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_PHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf4e20997428ae008b48f1eee3f150633)。

电话主设备类别（Phone major device class）。

<a id="r_ga341edcc0340d6d2d5ba3c76beeab1c93"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK 0x03
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga341edcc0340d6d2d5ba3c76beeab1c93)。

局域网／网络接入点主设备类别（LAN/Network Access Point major device class）。

<a id="r_ga88281290c9641477d5e19b321f489e85"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO 0x04
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga88281290c9641477d5e19b321f489e85)。

音频／视频主设备类别（Audio/Video major device class）。

<a id="r_ga71cb552a1ba251492456a3862a70321b"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL 0x05
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga71cb552a1ba251492456a3862a70321b)。

外设主设备类别（Peripheral major device class）。

<a id="r_gabd6b43f20dba80d46238567f8026a405"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_IMAGING 0x06
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_IMAGING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gabd6b43f20dba80d46238567f8026a405)。

成像主设备类别（Imaging major device class）。

<a id="r_ga832d46c3654018a272f167e8d2f028c2"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_WEARABLE 0x07
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_WEARABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga832d46c3654018a272f167e8d2f028c2)。

可穿戴主设备类别（Wearable major device class）。

<a id="r_ga6af01f93fadb4ded2c0e7d74acdfa9a2"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_TOY 0x08
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_TOY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6af01f93fadb4ded2c0e7d74acdfa9a2)。

玩具主设备类别（Toy major device class）。

<a id="r_ga7493589ba4918239c7714b12f4044c48"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_HEALTH 0x09
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_HEALTH](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7493589ba4918239c7714b12f4044c48)。

健康主设备类别（Health major device class）。

<a id="r_ga81690fb90860176fc17fed8625fed486"></a>

```c
#define BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED 0x1F
```

相关声明：[BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga81690fb90860176fc17fed8625fed486)。

未分类的主设备类别（Uncategorized major device class）。

<a id="define-members-11"></a>

### 次设备类别：计算机主类别（Minor Device Class - Computer Major Class）

<a id="r_ga47d7e27a9da20b27c0483ab50db3590d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga47d7e27a9da20b27c0483ab50db3590d)。

未分类的计算机次设备类别（Uncategorized computer minor device class）。

<a id="r_gae1a285e3787132a97edf7adb53963880"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae1a285e3787132a97edf7adb53963880)。

台式工作站计算机次设备类别（Desktop workstation computer minor device class）。

<a id="r_ga6d009b3670bfa0de1ed30c2ec87f8918"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6d009b3670bfa0de1ed30c2ec87f8918)。

服务器级计算机次设备类别（Server-class computer minor device class）。

<a id="r_ga60f70b01f651baab797b79ee5c7b94aa"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga60f70b01f651baab797b79ee5c7b94aa)。

笔记本计算机次设备类别（Laptop computer minor device class）。

<a id="r_gad8af957eeafefca10f2538b2e09c7bd3"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad8af957eeafefca10f2538b2e09c7bd3)。

手持 PC／个人数字助理计算机次设备类别（Handheld PC/PDA computer minor device class）。

<a id="r_gab5eb08bfa138cbfd55ffa2774a38fd9f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab5eb08bfa138cbfd55ffa2774a38fd9f)。

掌上 PC／个人数字助理计算机次设备类别（Palm-sized PC/PDA computer minor device class）。

<a id="r_gaec2dc76edfa8a7edc6ce990be1658e54"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaec2dc76edfa8a7edc6ce990be1658e54)。

可穿戴计算机次设备类别（Wearable computer minor device class）。

<a id="r_ga0a98088245313a02c7dfbfdb39784632"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga0a98088245313a02c7dfbfdb39784632)。

平板计算机次设备类别（Tablet computer minor device class）。

<a id="define-members-12"></a>

### 次设备类别：电话主类别（Minor Device Class - Phone Major Class）

<a id="r_ga86dd6474cad2c148c4bf2273707f3bca"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga86dd6474cad2c148c4bf2273707f3bca)。

未分类的电话次设备类别（Uncategorized phone minor device class）。

<a id="r_gaf3796e468def379157c2cf02a356b578"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf3796e468def379157c2cf02a356b578)。

蜂窝电话次设备类别（Cellular phone minor device class）。

<a id="r_gacce21d82143f430ff2bac1608b42b7e1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gacce21d82143f430ff2bac1608b42b7e1)。

无绳电话次设备类别（Cordless phone minor device class）。

<a id="r_gad74d69e9ec7a82b128df0a6ad33bfc65"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad74d69e9ec7a82b128df0a6ad33bfc65)。

智能手机次设备类别（Smartphone minor device class）。

<a id="r_ga708f325406d16fbcb96f0a311ad6f12f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga708f325406d16fbcb96f0a311ad6f12f)。

有线调制解调器或语音网关电话次设备类别（Wired modem or voice gateway phone minor device class）。

<a id="r_gad711cb8a9d53d428f4aef9da0605c27e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad711cb8a9d53d428f4aef9da0605c27e)。

通用综合业务数字网接入电话次设备类别（Common ISDN access phone minor device class）。

<a id="define-members-13"></a>

### 次设备类别：局域网／网络主类别：服务利用率（Minor Device Class - LAN/Network Major Class - Service Utilization）

<a id="r_gacf4f30af8af17254d8557c2102e82930"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gacf4f30af8af17254d8557c2102e82930)。

局域网服务利用率：完全可用（LAN service utilization: fully available）。

<a id="r_gaa48c789f29f33b7f129bbd593ab336fe"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa48c789f29f33b7f129bbd593ab336fe)。

局域网服务利用率：已使用 1–17%（LAN service utilization: 1-17% utilized）。

<a id="r_gab19bf6c95fbe0d3aa4923323b67c2f0c"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab19bf6c95fbe0d3aa4923323b67c2f0c)。

局域网服务利用率：已使用 17–33%（LAN service utilization: 17-33% utilized）。

<a id="r_ga17e2dd35fb4fd37f45757515a03df565"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga17e2dd35fb4fd37f45757515a03df565)。

局域网服务利用率：已使用 33–50%（LAN service utilization: 33-50% utilized）。

<a id="r_gaecb741bfc498bacfbd4c9059b3551e2f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaecb741bfc498bacfbd4c9059b3551e2f)。

局域网服务利用率：已使用 50–67%（LAN service utilization: 50-67% utilized）。

<a id="r_gaf296fcfd14235a0762a4565ff265e6be"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf296fcfd14235a0762a4565ff265e6be)。

局域网服务利用率：已使用 67–83%（LAN service utilization: 67-83% utilized）。

<a id="r_ga7a740756ba4dbc8770f4cdf5af2d1fa5"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7a740756ba4dbc8770f4cdf5af2d1fa5)。

局域网服务利用率：已使用 83–99%（LAN service utilization: 83-99% utilized）。

<a id="r_gafb3f26abffdd158cfd117aefa06a31bb"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafb3f26abffdd158cfd117aefa06a31bb)。

局域网服务利用率：无可用服务（LAN service utilization: no service available）。

<a id="define-members-14"></a>

### 次设备类别：局域网／网络主类别：设备类型（Minor Device Class - LAN/Network Major Class - Device Type）

<a id="r_gab4af4c15266ce0f24f2f61d0578f346a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab4af4c15266ce0f24f2f61d0578f346a)。

未分类的局域网／网络设备类型（Uncategorized LAN/network device type）。

<a id="r_ga245357d925ffde5ce1d7d038bd661097"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga245357d925ffde5ce1d7d038bd661097)。

次设备类别：音频／视频主类别（Minor Device Class - Audio/Video Major Class）。

<a id="r_gaa79054d26b530834da97412ffc6a6d76"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa79054d26b530834da97412ffc6a6d76)。

可穿戴耳麦音频／视频次设备类别（Wearable headset audio/video minor device class）。

<a id="r_gaea20dcaaf0dcf2914b1ede0e657ad233"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaea20dcaaf0dcf2914b1ede0e657ad233)。

免提音频／视频次设备类别（Handsfree audio/video minor device class）。

<a id="r_ga6c71bd324c442918d05b2ba176549f78"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6c71bd324c442918d05b2ba176549f78)。

麦克风音频／视频次设备类别（Microphone audio/video minor device class）。

<a id="r_ga419c36342136f5ea827d2889ed666d4c"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga419c36342136f5ea827d2889ed666d4c)。

扬声器音频／视频次设备类别（Loudspeaker audio/video minor device class）。

<a id="r_ga6adf41d4cadabdca21bb1191ae0951f5"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6adf41d4cadabdca21bb1191ae0951f5)。

耳机音频／视频次设备类别（Headphones audio/video minor device class）。

<a id="r_gac50804ea808e6e83686ad973d187bf9d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gac50804ea808e6e83686ad973d187bf9d)。

便携音频设备的音频／视频次设备类别（Portable audio audio/video minor device class）。

<a id="r_ga8f60c01b2da107da93e8b873b03be337"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8f60c01b2da107da93e8b873b03be337)。

汽车音响的音频／视频次设备类别（Car audio audio/video minor device class）。

<a id="r_ga3a7182ce71c7ae49330475c0093e7665"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga3a7182ce71c7ae49330475c0093e7665)。

机顶盒音频／视频次设备类别（Set-top box audio/video minor device class）。

<a id="r_ga7ec413fa38b2e0ddcdb0cacfb9565d2a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO 0x0A
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7ec413fa38b2e0ddcdb0cacfb9565d2a)。

高保真音响的音频／视频次设备类别（HiFi audio audio/video minor device class）。

<a id="r_gafa6100bcc07e04e7177b34336a523c6a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR 0x0B
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafa6100bcc07e04e7177b34336a523c6a)。

录像机音频／视频次设备类别（VCR audio/video minor device class）。

<a id="r_ga4ee160425ba1d2fa7f7ab9f360eb51ea"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA 0x0C
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4ee160425ba1d2fa7f7ab9f360eb51ea)。

视频摄像机音频／视频次设备类别（Video camera audio/video minor device class）。

<a id="r_ga9cb9ddf5ac2d9e132b1504bb35fba5e7"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER 0x0D
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9cb9ddf5ac2d9e132b1504bb35fba5e7)。

便携式摄录机音频／视频次设备类别（Camcorder audio/video minor device class）。

<a id="r_ga7bb6a3801475a076153529859d607254"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR 0x0E
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7bb6a3801475a076153529859d607254)。

视频监视器音频／视频次设备类别（Video monitor audio/video minor device class）。

<a id="r_ga5a20841438980c2fcf408974782c9f6e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER 0x0F
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5a20841438980c2fcf408974782c9f6e)。

视频显示器与扬声器音频／视频次设备类别（Video display and loudspeaker audio/video minor device class）。

<a id="r_ga07f3ddf991a1de0ef1a5e4bc80f87ae9"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING 0x10
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga07f3ddf991a1de0ef1a5e4bc80f87ae9)。

视频会议音频／视频次设备类别（Video conferencing audio/video minor device class）。

<a id="r_ga67798be9a45da9d23993851dc47b8015"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY 0x12
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga67798be9a45da9d23993851dc47b8015)。

游戏玩具音频／视频次设备类别（Gaming toy audio/video minor device class）。

<a id="define-members-15"></a>

### 次设备类别：外设主类别：输入设备类型（Minor Device Class - Peripheral Major Class - Input Device Type）

<a id="r_ga4b48d9b5ef8fdddd11f1cb528e826d79"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4b48d9b5ef8fdddd11f1cb528e826d79)。

外设输入：无键盘，无指点设备（Peripheral input: no keyboard, no pointing device）。

<a id="r_gab648e64338834e0f986415603a7ee01a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab648e64338834e0f986415603a7ee01a)。

外设输入：键盘（Peripheral input: keyboard）。

<a id="r_ga71c43b86fa8d01d45d11bea0bb56ee63"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga71c43b86fa8d01d45d11bea0bb56ee63)。

外设输入：指点设备（Peripheral input: pointing device）。

<a id="r_ga4c26cacb0efe86dd586cacb48f7f9798"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4c26cacb0efe86dd586cacb48f7f9798)。

外设输入：键盘与指点设备组合（Peripheral input: combo keyboard and pointing device）。

<a id="define-members-16"></a>

### 次设备类别：外设主类别：设备类型（Minor Device Class - Peripheral Major Class - Device Type）

<a id="r_gadd57844cdd2d6ff59ea8371b64c0786a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadd57844cdd2d6ff59ea8371b64c0786a)。

未分类的外设设备类型（Uncategorized peripheral device type）。

<a id="r_gae7ceeea12447c03b901704165f815d2a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae7ceeea12447c03b901704165f815d2a)。

操纵杆外设设备类型（Joystick peripheral device type）。

<a id="r_gaae4e0e78d28b915f7be42640aab41802"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaae4e0e78d28b915f7be42640aab41802)。

游戏手柄外设设备类型（Gamepad peripheral device type）。

<a id="r_ga55dc4b9ce33c7254ade2b32124bd5a52"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga55dc4b9ce33c7254ade2b32124bd5a52)。

遥控器外设设备类型（Remote control peripheral device type）。

<a id="r_ga6115e1fc2619c95bcf7a50e657347c8b"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6115e1fc2619c95bcf7a50e657347c8b)。

传感设备外设类型（Sensing device peripheral device type）。

<a id="r_ga8b21b9c98bb8ec187bb7be661c875048"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8b21b9c98bb8ec187bb7be661c875048)。

数字化绘图板外设设备类型（Digitizer tablet peripheral device type）。

<a id="r_ga8b23f0432923353c1425244780c2cd4a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8b23f0432923353c1425244780c2cd4a)。

读卡器外设设备类型（Card reader peripheral device type）。

<a id="r_ga7a8bec17a83efabcf83a3a0848fbd286"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7a8bec17a83efabcf83a3a0848fbd286)。

数字笔外设设备类型（Digital pen peripheral device type）。

<a id="r_ga3cff5d97f27e3725217f332dbd1e15ef"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga3cff5d97f27e3725217f332dbd1e15ef)。

手持扫描仪外设设备类型（Handheld scanner peripheral device type）。

<a id="r_ga2e603791c7467731fcd8e5ef521405fc"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2e603791c7467731fcd8e5ef521405fc)。

手持手势输入外设设备类型（Handheld gestural input peripheral device type）。

<a id="define-members-17"></a>

### 次设备类别：成像主类别（Minor Device Class - Imaging Major Class）。

<a id="r_gaeb931c305948fa843853f9f418c71d45"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaeb931c305948fa843853f9f418c71d45)。

次设备类别：成像主类别（Minor Device Class - Imaging Major Class）。

<a id="r_ga238b06f556138d4bab338ff1375a1021"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga238b06f556138d4bab338ff1375a1021)。

成像相机设备（Imaging camera device）。

<a id="r_ga6eb468819358a83906f40f2f64c344ae"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6eb468819358a83906f40f2f64c344ae)。

成像扫描仪设备（Imaging scanner device）。

<a id="r_gaf6a4be11446739a2aede1adf4d4fda77"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf6a4be11446739a2aede1adf4d4fda77)。

成像打印机设备（Imaging printer device）。

<a id="r_ga5010b99a3111775447ac89f169d824af"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5010b99a3111775447ac89f169d824af)。

次设备类别：成像主类别中的未分类设备（Minor Device Class - Imaging Major Class Uncategorized）。

<a id="define-members-18"></a>

### 次设备类别：可穿戴主类别（Minor Device Class - Wearable Major Class）

<a id="r_gae879842e986be1f78b1a6afdd06f267e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae879842e986be1f78b1a6afdd06f267e)。

可穿戴耳麦设备（Wearable headset device）。

<a id="r_ga2c68dc5a8fe4252bc2c743f05f9d4e96"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2c68dc5a8fe4252bc2c743f05f9d4e96)。

可穿戴寻呼机设备（Wearable pager device）。

<a id="r_ga9a7d4d0b3645f38a9888beb2ec994fe1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9a7d4d0b3645f38a9888beb2ec994fe1)。

可穿戴夹克设备（Wearable jacket device）。

<a id="r_ga091efe28aab4b90f3552d56704b2a886"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga091efe28aab4b90f3552d56704b2a886)。

可穿戴头盔设备（Wearable helmet device）。

<a id="r_gaea4e865414b40d9b370951a328dc0c36"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaea4e865414b40d9b370951a328dc0c36)。

可穿戴眼镜设备（Wearable glasses device）。

<a id="define-members-19"></a>

### 次设备类别：玩具主类别（Minor Device Class - Toy Major Class）

<a id="r_gaf527b4a6353fc0e110033f1661342a80"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf527b4a6353fc0e110033f1661342a80)。

玩具机器人设备（Toy robot device）。

<a id="r_ga236dedbc75b174d221173080e734227e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga236dedbc75b174d221173080e734227e)。

玩具车辆设备（Toy vehicle device）。

<a id="r_gaf22179ae786663d350c7dfa9a25671b0"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf22179ae786663d350c7dfa9a25671b0)。

玩具娃娃设备（Toy doll device）。

<a id="r_gae51ab020f0a58a7468e79b33cf5888d2"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae51ab020f0a58a7468e79b33cf5888d2)。

玩具控制器设备（Toy controller device）。

<a id="r_ga4305ed742e35f7d21d97d6ca8a228776"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_TOY_GAME 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_TOY_GAME](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4305ed742e35f7d21d97d6ca8a228776)。

玩具游戏设备（Toy game device）。

<a id="define-members-20"></a>

### 次设备类别：健康主类别（Minor Device Class - Health Major Class）

<a id="r_ga98a4f1577322dd14790bda9ce8b28661"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED 0x00
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga98a4f1577322dd14790bda9ce8b28661)。

未定义的健康设备（Undefined health device）。

<a id="r_gadc1ba5de00271e2663dc52770acbf1f1"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR 0x01
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadc1ba5de00271e2663dc52770acbf1f1)。

血压监测健康设备（Blood pressure monitor health device）。

<a id="r_ga60998708af979e1c02d8a0d6373500c8"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER 0x02
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga60998708af979e1c02d8a0d6373500c8)。

温度计健康设备（Thermometer health device）。

<a id="r_ga8c6cb016bdd1a5f50258c671f7528f8e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE 0x03
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8c6cb016bdd1a5f50258c671f7528f8e)。

体重秤健康设备（Weighing scale health device）。

<a id="r_ga5c9e6a84ff76bfc8c12750e9b133861a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER 0x04
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5c9e6a84ff76bfc8c12750e9b133861a)。

血糖仪健康设备（Glucose meter health device）。

<a id="r_gabe9f5e78c7321d8a2ff1752fe41d124d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER 0x05
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gabe9f5e78c7321d8a2ff1752fe41d124d)。

脉搏血氧仪健康设备（Pulse oximeter health device）。

<a id="r_ga94863d500f1a576eb3d818209196d12e"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR 0x06
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga94863d500f1a576eb3d818209196d12e)。

心率／脉搏监测健康设备（Heart/pulse monitor health device）。

<a id="r_gad6577d566fd17b126611583b4379ad01"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY 0x07
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad6577d566fd17b126611583b4379ad01)。

健康数据展示设备（Health data display device）。

<a id="r_ga6e50e1316332ba4e5da2fd81c6e65ef7"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER 0x08
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6e50e1316332ba4e5da2fd81c6e65ef7)。

计步器健康设备（Step counter health device）。

<a id="r_gad34ed19a24a0b2a300b8e31c5a7ce798"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER 0x09
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad34ed19a24a0b2a300b8e31c5a7ce798)。

身体成分分析仪健康设备（Body composition analyzer health device）。

<a id="r_ga746b3b863fb6250cd990099b014f063f"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR 0x0A
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga746b3b863fb6250cd990099b014f063f)。

峰值流量监测健康设备（Peak flow monitor health device）。

<a id="r_ga4b376213b25611ff4bcf8cb7c7483a3a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR 0x0B
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4b376213b25611ff4bcf8cb7c7483a3a)。

用药监测健康设备（Medication monitor health device）。

<a id="r_gaabd014dab3f24d38b8aabda2ae7e5ff4"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS 0x0C
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaabd014dab3f24d38b8aabda2ae7e5ff4)。

膝关节假体健康设备（Knee prosthesis health device）。

<a id="r_ga25315720692627e093a25df80d5b487d"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS 0x0D
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga25315720692627e093a25df80d5b487d)。

踝关节假体健康设备（Ankle prosthesis health device）。

<a id="r_ga308d6b8f3ed8cefccbca002ede932218"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER 0x0E
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga308d6b8f3ed8cefccbca002ede932218)。

通用健康管理器设备（Generic health manager device）。

<a id="r_ga5fd6e3a6703d961259bd563ca6379c9a"></a>

```c
#define BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE 0x0F
```

相关声明：[BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5fd6e3a6703d961259bd563ca6379c9a)。

个人移动辅助健康设备（Personal mobility health device）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_ga4bf3f820b493361a9a3b393d0282420f"></a>

```c
enum bt_bearer_tech { BT_BEARER_TECH_3G = 0x01 , BT_BEARER_TECH_4G = 0x02 , BT_BEARER_TECH_LTE = 0x03 , BT_BEARER_TECH_WIFI = 0x04 , BT_BEARER_TECH_5G = 0x05 , BT_BEARER_TECH_GSM = 0x06 , BT_BEARER_TECH_CDMA = 0x07 , BT_BEARER_TECH_2G = 0x08 , BT_BEARER_TECH_WCDMA = 0x09 }
```

相关声明：[bt_bearer_tech](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga4bf3f820b493361a9a3b393d0282420f)、[BT_BEARER_TECH_3G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e)、[BT_BEARER_TECH_4G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29)、[BT_BEARER_TECH_LTE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64)、[BT_BEARER_TECH_WIFI](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c)、[BT_BEARER_TECH_5G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24)、[BT_BEARER_TECH_GSM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a)、[BT_BEARER_TECH_CDMA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328)、[BT_BEARER_TECH_2G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8)、[BT_BEARER_TECH_WCDMA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa)。

有效承载技术（Bearer Technology）值的枚举。

<a id="r_gaf58823a56eb36cfd22e582ab1ea3d015"></a>

```c
enum bt_audio_codec_cap_type { BT_AUDIO_CODEC_CAP_TYPE_FREQ = 0x01 , BT_AUDIO_CODEC_CAP_TYPE_DURATION = 0x02 , BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT = 0x03 , BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN = 0x04 , BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT = 0x05 }
```

相关声明：[bt_audio_codec_cap_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaf58823a56eb36cfd22e582ab1ea3d015)、[BT_AUDIO_CODEC_CAP_TYPE_FREQ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)、[BT_AUDIO_CODEC_CAP_TYPE_DURATION](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)、[BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)、[BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)、[BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)。

编解码器能力（Codec Capability）类型。

<a id="r_gaafc1106d5d305874ee2f540c850ff5b4"></a>

```c
enum bt_audio_codec_cap_freq { BT_AUDIO_CODEC_CAP_FREQ_8KHZ = (1UL << (0)) , BT_AUDIO_CODEC_CAP_FREQ_11KHZ = (1UL << (1)) , BT_AUDIO_CODEC_CAP_FREQ_16KHZ = (1UL << (2)) , BT_AUDIO_CODEC_CAP_FREQ_22KHZ = (1UL << (3)) , BT_AUDIO_CODEC_CAP_FREQ_24KHZ = (1UL << (4)) , BT_AUDIO_CODEC_CAP_FREQ_32KHZ = (1UL << (5)) , BT_AUDIO_CODEC_CAP_FREQ_44KHZ = (1UL << (6)) , BT_AUDIO_CODEC_CAP_FREQ_48KHZ = (1UL << (7)) , BT_AUDIO_CODEC_CAP_FREQ_88KHZ = (1UL << (8)) , BT_AUDIO_CODEC_CAP_FREQ_96KHZ = (1UL << (9)) , BT_AUDIO_CODEC_CAP_FREQ_176KHZ = (1UL << (10)) , BT_AUDIO_CODEC_CAP_FREQ_192KHZ = (1UL << (11)) , BT_AUDIO_CODEC_CAP_FREQ_384KHZ = (1UL << (12)) , BT_AUDIO_CODEC_CAP_FREQ_ANY }
```

相关声明：[bt_audio_codec_cap_freq](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaafc1106d5d305874ee2f540c850ff5b4)、[BT_AUDIO_CODEC_CAP_FREQ_8KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)、[BT_AUDIO_CODEC_CAP_FREQ_11KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)、[BT_AUDIO_CODEC_CAP_FREQ_16KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)、[BT_AUDIO_CODEC_CAP_FREQ_22KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)、[BT_AUDIO_CODEC_CAP_FREQ_24KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)、[BT_AUDIO_CODEC_CAP_FREQ_32KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)、[BT_AUDIO_CODEC_CAP_FREQ_44KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)、[BT_AUDIO_CODEC_CAP_FREQ_48KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)、[BT_AUDIO_CODEC_CAP_FREQ_88KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)、[BT_AUDIO_CODEC_CAP_FREQ_96KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)、[BT_AUDIO_CODEC_CAP_FREQ_176KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)、[BT_AUDIO_CODEC_CAP_FREQ_192KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)、[BT_AUDIO_CODEC_CAP_FREQ_384KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)、[BT_AUDIO_CODEC_CAP_FREQ_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)。

支持的频率（Frequency）位域。

<a id="r_gaf37e8e19f956afb3c3a413cbaa1a21f5"></a>

```c
enum bt_audio_codec_cap_frame_dur { BT_AUDIO_CODEC_CAP_DURATION_7_5 = (1UL << (0)) , BT_AUDIO_CODEC_CAP_DURATION_10 = (1UL << (1)) , BT_AUDIO_CODEC_CAP_DURATION_ANY , BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5 = (1UL << (4)) , BT_AUDIO_CODEC_CAP_DURATION_PREFER_10 = (1UL << (5)) }
```

相关声明：[bt_audio_codec_cap_frame_dur](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)、[BT_AUDIO_CODEC_CAP_DURATION_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)、[BT_AUDIO_CODEC_CAP_DURATION_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)、[BT_AUDIO_CODEC_CAP_DURATION_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)、[BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)、[BT_AUDIO_CODEC_CAP_DURATION_PREFER_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)。

支持的帧时长（Frame Duration）位域。

<a id="r_gae695b5d17359967703f2509db1671fa5"></a>

```c
enum bt_audio_codec_cap_chan_count { BT_AUDIO_CODEC_CAP_CHAN_COUNT_1 = (1UL << (0)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_2 = (1UL << (1)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_3 = (1UL << (2)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_4 = (1UL << (3)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_5 = (1UL << (4)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_6 = (1UL << (5)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_7 = (1UL << (6)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_8 = (1UL << (7)) , BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY }
```

相关声明：[bt_audio_codec_cap_chan_count](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gae695b5d17359967703f2509db1671fa5)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_1](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_2](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_3](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_4](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_6](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_7](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_8](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)、[BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)。

音频能力（Audio Capability）支持的声道数位域。

<a id="r_ga9230ec4d7518bd243207ba2decb1a974"></a>

```c
enum bt_audio_codec_cfg_type { BT_AUDIO_CODEC_CFG_FREQ = 0x01 , BT_AUDIO_CODEC_CFG_DURATION = 0x02 , BT_AUDIO_CODEC_CFG_CHAN_ALLOC = 0x03 , BT_AUDIO_CODEC_CFG_FRAME_LEN = 0x04 , BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU = 0x05 }
```

相关声明：[bt_audio_codec_cfg_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga9230ec4d7518bd243207ba2decb1a974)、[BT_AUDIO_CODEC_CFG_FREQ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)、[BT_AUDIO_CODEC_CFG_DURATION](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)、[BT_AUDIO_CODEC_CFG_CHAN_ALLOC](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)、[BT_AUDIO_CODEC_CFG_FRAME_LEN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)、[BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)。

编解码器配置（Codec Configuration）类型。

<a id="r_ga8e99fb678cc011bb8c9f6e1858bae0d7"></a>

```c
enum bt_audio_codec_cfg_freq { BT_AUDIO_CODEC_CFG_FREQ_8KHZ = 0x01 , BT_AUDIO_CODEC_CFG_FREQ_11KHZ = 0x02 , BT_AUDIO_CODEC_CFG_FREQ_16KHZ = 0x03 , BT_AUDIO_CODEC_CFG_FREQ_22KHZ = 0x04 , BT_AUDIO_CODEC_CFG_FREQ_24KHZ = 0x05 , BT_AUDIO_CODEC_CFG_FREQ_32KHZ = 0x06 , BT_AUDIO_CODEC_CFG_FREQ_44KHZ = 0x07 , BT_AUDIO_CODEC_CFG_FREQ_48KHZ = 0x08 , BT_AUDIO_CODEC_CFG_FREQ_88KHZ = 0x09 , BT_AUDIO_CODEC_CFG_FREQ_96KHZ = 0x0a , BT_AUDIO_CODEC_CFG_FREQ_176KHZ = 0x0b , BT_AUDIO_CODEC_CFG_FREQ_192KHZ = 0x0c , BT_AUDIO_CODEC_CFG_FREQ_384KHZ = 0x0d }
```

相关声明：[bt_audio_codec_cfg_freq](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)、[BT_AUDIO_CODEC_CFG_FREQ_8KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)、[BT_AUDIO_CODEC_CFG_FREQ_11KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)、[BT_AUDIO_CODEC_CFG_FREQ_16KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)、[BT_AUDIO_CODEC_CFG_FREQ_22KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)、[BT_AUDIO_CODEC_CFG_FREQ_24KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)、[BT_AUDIO_CODEC_CFG_FREQ_32KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)、[BT_AUDIO_CODEC_CFG_FREQ_44KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)、[BT_AUDIO_CODEC_CFG_FREQ_48KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)、[BT_AUDIO_CODEC_CFG_FREQ_88KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)、[BT_AUDIO_CODEC_CFG_FREQ_96KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)、[BT_AUDIO_CODEC_CFG_FREQ_176KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)、[BT_AUDIO_CODEC_CFG_FREQ_192KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)、[BT_AUDIO_CODEC_CFG_FREQ_384KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)。

编解码器配置的采样频率（Sampling Frequency）。

<a id="r_ga83701b5eadfcbc9b84dc0b1a85ebeb74"></a>

```c
enum bt_audio_codec_cfg_frame_dur { BT_AUDIO_CODEC_CFG_DURATION_7_5 = 0x00 , BT_AUDIO_CODEC_CFG_DURATION_10 = 0x01 }
```

相关声明：[bt_audio_codec_cfg_frame_dur](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)、[BT_AUDIO_CODEC_CFG_DURATION_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)、[BT_AUDIO_CODEC_CFG_DURATION_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)。

编解码器配置的帧时长（Frame Duration）。

<a id="r_gafb379ffa88388cc1397960155bbb2ab3"></a>

```c
enum bt_audio_context { BT_AUDIO_CONTEXT_TYPE_NONE = 0 , BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED = (1UL << (0)) , BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL = (1UL << (1)) , BT_AUDIO_CONTEXT_TYPE_MEDIA = (1UL << (2)) , BT_AUDIO_CONTEXT_TYPE_GAME = (1UL << (3)) , BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL = (1UL << (4)) , BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS = (1UL << (5)) , BT_AUDIO_CONTEXT_TYPE_LIVE = (1UL << (6)) , BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS = (1UL << (7)) , BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS = (1UL << (8)) , BT_AUDIO_CONTEXT_TYPE_RINGTONE = (1UL << (9)) , BT_AUDIO_CONTEXT_TYPE_ALERTS = (1UL << (10)) , BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM = (1UL << (11)) }
```

相关声明：[bt_audio_context](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gafb379ffa88388cc1397960155bbb2ab3)、[BT_AUDIO_CONTEXT_TYPE_NONE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)、[BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)、[BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)、[BT_AUDIO_CONTEXT_TYPE_MEDIA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)、[BT_AUDIO_CONTEXT_TYPE_GAME](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)、[BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)、[BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)、[BT_AUDIO_CONTEXT_TYPE_LIVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)、[BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)、[BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)、[BT_AUDIO_CONTEXT_TYPE_RINGTONE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)、[BT_AUDIO_CONTEXT_TYPE_ALERTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)、[BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)。

通用音频（Generic Audio）的音频上下文类型（Audio Context Type）。

<a id="r_ga6d4aff1f93dc0b902e4b5d1355f15760"></a>

```c
enum bt_audio_parental_rating { BT_AUDIO_PARENTAL_RATING_NO_RATING = 0x00 , BT_AUDIO_PARENTAL_RATING_AGE_ANY = 0x01 , BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE = 0x02 , BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE = 0x03 , BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE = 0x04 , BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE = 0x05 , BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE = 0x06 , BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE = 0x07 , BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE = 0x08 , BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE = 0x09 , BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE = 0x0A , BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE = 0x0B , BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE = 0x0C , BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE = 0x0D , BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE = 0x0E , BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE = 0x0F }
```

相关声明：[bt_audio_parental_rating](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga6d4aff1f93dc0b902e4b5d1355f15760)、[BT_AUDIO_PARENTAL_RATING_NO_RATING](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)、[BT_AUDIO_PARENTAL_RATING_AGE_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)、[BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)、[BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)、[BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)、[BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)、[BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)、[BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)、[BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)、[BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)、[BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)、[BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)、[BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)、[BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)、[BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)、[BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的家长分级（Parental Rating）。

<a id="r_ga16d403ec4db7be997682331ad365ff5f"></a>

```c
enum bt_audio_active_state { BT_AUDIO_ACTIVE_STATE_DISABLED = 0x00 , BT_AUDIO_ACTIVE_STATE_ENABLED = 0x01 }
```

相关声明：[bt_audio_active_state](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga16d403ec4db7be997682331ad365ff5f)、[BT_AUDIO_ACTIVE_STATE_DISABLED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)、[BT_AUDIO_ACTIVE_STATE_ENABLED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的音频活动状态（Audio Active State）。

<a id="r_ga207fbf0fbca9b24cba02c7f1d184e7f5"></a>

```c
enum bt_audio_assisted_listening_stream { BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED = 0x00 }
```

相关声明：[bt_audio_assisted_listening_stream](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga207fbf0fbca9b24cba02c7f1d184e7f5)、[BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285)。

通用音频分配编号（Generic Audio Assigned Numbers，bluetooth.com）定义的辅助聆听流（Assisted Listening Stream）。

<a id="r_gab53d0dd62bceff97cf8eed7d8cf80354"></a>

```c
enum bt_audio_metadata_type { BT_AUDIO_METADATA_TYPE_PREF_CONTEXT = 0x01 , BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT = 0x02 , BT_AUDIO_METADATA_TYPE_PROGRAM_INFO = 0x03 , BT_AUDIO_METADATA_TYPE_LANG = 0x04 , BT_AUDIO_METADATA_TYPE_CCID_LIST = 0x05 , BT_AUDIO_METADATA_TYPE_PARENTAL_RATING = 0x06 , BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI = 0x07 , BT_AUDIO_METADATA_TYPE_AUDIO_STATE = 0x08 , BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE = 0x09 , BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM = 0x0A , BT_AUDIO_METADATA_TYPE_BROADCAST_NAME = 0x0B , BT_AUDIO_METADATA_TYPE_EXTENDED = 0xFE , BT_AUDIO_METADATA_TYPE_VENDOR = 0xFF }
```

相关声明：[bt_audio_metadata_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gab53d0dd62bceff97cf8eed7d8cf80354)、[BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)、[BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)、[BT_AUDIO_METADATA_TYPE_PROGRAM_INFO](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)、[BT_AUDIO_METADATA_TYPE_LANG](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)、[BT_AUDIO_METADATA_TYPE_CCID_LIST](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)、[BT_AUDIO_METADATA_TYPE_PARENTAL_RATING](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)、[BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)、[BT_AUDIO_METADATA_TYPE_AUDIO_STATE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)、[BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)、[BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)、[BT_AUDIO_METADATA_TYPE_BROADCAST_NAME](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)、[BT_AUDIO_METADATA_TYPE_EXTENDED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)、[BT_AUDIO_METADATA_TYPE_VENDOR](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)。

编解码器元数据（Codec Metadata）类型 ID。

<a id="r_ga61230848c02098352320fe751332c4e8"></a>

```c
enum bt_audio_location { BT_AUDIO_LOCATION_MONO_AUDIO = 0 , BT_AUDIO_LOCATION_FRONT_LEFT = (1UL << (0)) , BT_AUDIO_LOCATION_FRONT_RIGHT = (1UL << (1)) , BT_AUDIO_LOCATION_FRONT_CENTER = (1UL << (2)) , BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1 = (1UL << (3)) , BT_AUDIO_LOCATION_BACK_LEFT = (1UL << (4)) , BT_AUDIO_LOCATION_BACK_RIGHT = (1UL << (5)) , BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER = (1UL << (6)) , BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER = (1UL << (7)) , BT_AUDIO_LOCATION_BACK_CENTER = (1UL << (8)) , BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2 = (1UL << (9)) , BT_AUDIO_LOCATION_SIDE_LEFT = (1UL << (10)) , BT_AUDIO_LOCATION_SIDE_RIGHT = (1UL << (11)) , BT_AUDIO_LOCATION_TOP_FRONT_LEFT = (1UL << (12)) , BT_AUDIO_LOCATION_TOP_FRONT_RIGHT = (1UL << (13)) , BT_AUDIO_LOCATION_TOP_FRONT_CENTER = (1UL << (14)) , BT_AUDIO_LOCATION_TOP_CENTER = (1UL << (15)) , BT_AUDIO_LOCATION_TOP_BACK_LEFT = (1UL << (16)) , BT_AUDIO_LOCATION_TOP_BACK_RIGHT = (1UL << (17)) , BT_AUDIO_LOCATION_TOP_SIDE_LEFT = (1UL << (18)) , BT_AUDIO_LOCATION_TOP_SIDE_RIGHT = (1UL << (19)) , BT_AUDIO_LOCATION_TOP_BACK_CENTER = (1UL << (20)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER = (1UL << (21)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT = (1UL << (22)) , BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT = (1UL << (23)) , BT_AUDIO_LOCATION_FRONT_LEFT_WIDE = (1UL << (24)) , BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE = (1UL << (25)) , BT_AUDIO_LOCATION_LEFT_SURROUND = (1UL << (26)) , BT_AUDIO_LOCATION_RIGHT_SURROUND = (1UL << (27)) }
```

相关声明：[bt_audio_location](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga61230848c02098352320fe751332c4e8)、[BT_AUDIO_LOCATION_MONO_AUDIO](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)、[BT_AUDIO_LOCATION_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)、[BT_AUDIO_LOCATION_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)、[BT_AUDIO_LOCATION_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)、[BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)、[BT_AUDIO_LOCATION_BACK_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)、[BT_AUDIO_LOCATION_BACK_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)、[BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)、[BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)、[BT_AUDIO_LOCATION_BACK_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)、[BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)、[BT_AUDIO_LOCATION_SIDE_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)、[BT_AUDIO_LOCATION_SIDE_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)、[BT_AUDIO_LOCATION_TOP_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)、[BT_AUDIO_LOCATION_TOP_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)、[BT_AUDIO_LOCATION_TOP_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)、[BT_AUDIO_LOCATION_TOP_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)、[BT_AUDIO_LOCATION_TOP_BACK_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)、[BT_AUDIO_LOCATION_TOP_BACK_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)、[BT_AUDIO_LOCATION_TOP_SIDE_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)、[BT_AUDIO_LOCATION_TOP_SIDE_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)、[BT_AUDIO_LOCATION_TOP_BACK_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)、[BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)、[BT_AUDIO_LOCATION_FRONT_LEFT_WIDE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)、[BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)、[BT_AUDIO_LOCATION_LEFT_SURROUND](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)、[BT_AUDIO_LOCATION_RIGHT_SURROUND](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)。

蓝牙音频（BT Audio）的位置（Location）值。


## 1.3\_原页交叉引用（Cross References）

- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_socket_ethernet_reference/P001_assigned_numbers.h_源码浏览.md)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gac1251f8a35b5e343eeeff87f22f8ab10)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gad91341739d394f92ffc4988b614f47b6)
- [BT_AUDIO_BROADCAST_NAME_LEN_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaa3bf677a479a90793f28a5a3ed69c7e0)
- [BT_AUDIO_BROADCAST_NAME_LEN_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaa2fafcbb6a826c3f4cee16ebb545dad6)
- [BT_AUDIO_BROADCAST_NAME_CHAR_MIN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaaf50689c66f41dee1f4fab02893c4a1b)
- [BT_AUDIO_BROADCAST_NAME_CHAR_MAX](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaaabef5f2a77ea0ca60156eef80175311)
- [BT_AUDIO_CONTEXT_TYPE_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga6320f86aab9b227385bdf52a9ff3985b)
- [BT_AUDIO_LOCATION_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga90688f158fe999ed3aa9c759c8245fcc)
- [BT_APPEARANCE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafd1c9ca638a362a01897792e5a00a0c5)
- [BT_APPEARANCE_GENERIC_PHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae7061e78f960563af6e1b3dea71655a9)
- [BT_APPEARANCE_GENERIC_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6b74ad86efc0e9a745f2c9e64079b1cd)
- [BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)
- [BT_APPEARANCE_COMPUTER_SERVER_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab71a3c3f836561ac7bd8e52f5e01c769)
- [BT_APPEARANCE_COMPUTER_LAPTOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga55ce2ad96a153ed6bdfd841276145c28)
- [BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab64312ea16f03c5998db4429b194b8b0)
- [BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9340ed60911fc7c5aab7d317b6925c10)
- [BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7c6667ba4c68dec380a548ba9530c110)
- [BT_APPEARANCE_COMPUTER_TABLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga11bc881cb5f88956edbf2bb2fe5b358c)
- [BT_APPEARANCE_COMPUTER_DOCKING_STATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga36187d2651d08c4b3e17c36565a2d3c9)
- [BT_APPEARANCE_COMPUTER_ALL_IN_ONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa4d962ad8661c28ed48f5cf8cd75ad6e)
- [BT_APPEARANCE_COMPUTER_BLADE_SERVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga53e8eff26f2020b1fc89b21684e54698)
- [BT_APPEARANCE_COMPUTER_CONVERTIBLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga073dca362cabfd2a07cdc1cb787a0f58)
- [BT_APPEARANCE_COMPUTER_DETACHABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8f35f76cc9de4170006669d6e9e7d72a)
- [BT_APPEARANCE_COMPUTER_IOT_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ae353795476853bc3be2196ed220aa7)
- [BT_APPEARANCE_COMPUTER_MINI_PC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3c47c11f56eabec15e960662c64f6fcb)
- [BT_APPEARANCE_COMPUTER_STICK_PC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabb53daf3eb4ac9ba0cbb1614056ee214)
- [BT_APPEARANCE_GENERIC_WATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0c512fd6aa5d35e78f02176073f5f121)
- [BT_APPEARANCE_SPORTS_WATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca9cc93d768145ec3d87b88740954b50)
- [BT_APPEARANCE_SMARTWATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa5662d4a544b034243faa45245a9728b)
- [BT_APPEARANCE_GENERIC_CLOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga100d26d6b9e9a3af925d64c0b006c6bd)
- [BT_APPEARANCE_GENERIC_DISPLAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a21cb58861a48875002af38ee82ac08)
- [BT_APPEARANCE_GENERIC_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0b47897768b27d26b8687dd2ab28703b)
- [BT_APPEARANCE_GENERIC_EYEGLASSES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab2b5f6385662519a2ece8fb654a6194b)
- [BT_APPEARANCE_GENERIC_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca6d810977e6da1a3174ee2b6b36662d)
- [BT_APPEARANCE_GENERIC_KEYRING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf73b11c4dbf366a854b4c68e802e3c1c)
- [BT_APPEARANCE_GENERIC_MEDIA_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga17e94209c0c96b5ca039b1613de0d05e)
- [BT_APPEARANCE_GENERIC_BARCODE_SCANNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadca19a01611ca83e18156bb540dd96c1)
- [BT_APPEARANCE_GENERIC_THERMOMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2e0fde88d83e1f4533d69c8dc472255f)
- [BT_APPEARANCE_THERMOMETER_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga54283061a207491dcfced899c0fc3008)
- [BT_APPEARANCE_GENERIC_HEART_RATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac5bdf195b81215932848151d765e84d6)
- [BT_APPEARANCE_HEART_RATE_BELT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga895f6570a09f3eee8d821eca57cdeb03)
- [BT_APPEARANCE_GENERIC_BLOOD_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3ab7a9595e00208a9e6a56dca99b56c2)
- [BT_APPEARANCE_BLOOD_PRESSURE_ARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga55c3e67d27c8fd8ae06880ccdd9259ce)
- [BT_APPEARANCE_BLOOD_PRESSURE_WRIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga89684ca0544a400293b663cdf0063cfa)
- [BT_APPEARANCE_GENERIC_HID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf2050baedf0863ec37177dd2ef872d39)
- [BT_APPEARANCE_HID_KEYBOARD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa74af272423a80d5489ed8cf6c3ee66c)
- [BT_APPEARANCE_HID_MOUSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3b6ba8ffe424db08583186c448e37149)
- [BT_APPEARANCE_HID_JOYSTICK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2f9f15df2260a1307f5142f37437bf0c)
- [BT_APPEARANCE_HID_GAMEPAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga770336524e74d106cb18354f9dbfad76)
- [BT_APPEARANCE_HID_DIGITIZER_TABLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacac11dcb96ab60963a1118e171a731de)
- [BT_APPEARANCE_HID_CARD_READER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa03c3b4d7ea8211748316146afab8bd4)
- [BT_APPEARANCE_HID_DIGITAL_PEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga002a1d7965b23ec62c8a196f4e5452d9)
- [BT_APPEARANCE_HID_BARCODE_SCANNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf88f83afd454fe88dd7146e10ef6d35e)
- [BT_APPEARANCE_HID_TOUCHPAD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaee207f9434bce7d0f7e096bf3b37a01c)
- [BT_APPEARANCE_HID_PRESENTATION_REMOTE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae415dd9e8d620dfd1981719f4ed2d796)
- [BT_APPEARANCE_GENERIC_GLUCOSE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga209645f7445873beb50c388cc82aff2a)
- [BT_APPEARANCE_GENERIC_WALKING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9cf19d97db0c4c5b8473b72809b51d42)
- [BT_APPEARANCE_WALKING_IN_SHOE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad748f5dc2e0622353d6159c3a3e4241b)
- [BT_APPEARANCE_WALKING_ON_SHOE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a4541459ba8b41a3938c5b8d35b1c8c)
- [BT_APPEARANCE_WALKING_ON_HIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad211a7e2f11dc7effe3ba28e8c4f7092)
- [BT_APPEARANCE_GENERIC_CYCLING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7a0463b9b0df37bce80cada38b10ee54)
- [BT_APPEARANCE_CYCLING_COMPUTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3e81dce23c3d005a9b48ff83c7b8f896)
- [BT_APPEARANCE_CYCLING_SPEED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga16fb08fa70272252ab6b2d3a5aec485a)
- [BT_APPEARANCE_CYCLING_CADENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga71dc370aad015e88fce7c3e758c647ed)
- [BT_APPEARANCE_CYCLING_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga02fd9566d9b932aeaa1163d312fbc4d8)
- [BT_APPEARANCE_CYCLING_SPEED_CADENCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga48d8f2a285795785f8f51ce220d46371)
- [BT_APPEARANCE_GENERIC_CONTROL_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5e16df5eefcae8556dfc387135e2b1b6)
- [BT_APPEARANCE_CONTROL_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac53247d00e3da69595274e0b94fa670f)
- [BT_APPEARANCE_CONTROL_MULTI_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad30c40df58e160128893e545a11ab44c)
- [BT_APPEARANCE_CONTROL_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga52dfd2858663b7ab624f0c4b08cee7dc)
- [BT_APPEARANCE_CONTROL_SLIDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa849d890c000defcaf29893296c86cc5)
- [BT_APPEARANCE_CONTROL_ROTARY_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)
- [BT_APPEARANCE_CONTROL_TOUCH_PANEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4d5763288557e7b7f6da0f3e9831171d)
- [BT_APPEARANCE_CONTROL_SINGLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga979ca0f4febeaa55daec07e2b3b0179e)
- [BT_APPEARANCE_CONTROL_DOUBLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac1c80dbb8aaa327b6125bf632692c3be)
- [BT_APPEARANCE_CONTROL_TRIPLE_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa532fd1bd67c2c5b72822704a62df143)
- [BT_APPEARANCE_CONTROL_BATTERY_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaea669671a53b3df5b1aa4c43e5bde9b9)
- [BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadec2907a822e302d5027f162ef9ce4b6)
- [BT_APPEARANCE_CONTROL_PUSH_BUTTON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9bb358864e1388cc00502b5586ec581f)
- [BT_APPEARANCE_GENERIC_NETWORK_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac4727ec720344ece687256ac517800e7)
- [BT_APPEARANCE_NETWORK_ACCESS_POINT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga265ba959769d56f42ff621a20e193aba)
- [BT_APPEARANCE_NETWORK_MESH_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadcc3d795579a731ae03ade14d5193408)
- [BT_APPEARANCE_NETWORK_MESH_PROXY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad4c5f5840a8caba73d55b0138e506bd0)
- [BT_APPEARANCE_GENERIC_SENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab3241fe012482e716c3f18e2962ca15d)
- [BT_APPEARANCE_SENSOR_MOTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab49b84183136e9b65ba2e1f5490a79ed)
- [BT_APPEARANCE_SENSOR_AIR_QUALITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaacb0779499ad4aaa83f0b6303460caf8)
- [BT_APPEARANCE_SENSOR_TEMPERATURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5e072a902bf145dc2b00dbd1c8a64b52)
- [BT_APPEARANCE_SENSOR_HUMIDITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2deff206602e1e0784af9456ef8abd5b)
- [BT_APPEARANCE_SENSOR_LEAK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)
- [BT_APPEARANCE_SENSOR_SMOKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeedc0612f8ca171aec061cf02ee907e4)
- [BT_APPEARANCE_SENSOR_OCCUPANCY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e8b7834c82c42a0076300aca20c2d35)
- [BT_APPEARANCE_SENSOR_CONTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac71e281cf1b8d1b6535623ec34c7d63f)
- [BT_APPEARANCE_SENSOR_CARBON_MONOXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0e60b365f871c17c0015ffcf8bc1646e)
- [BT_APPEARANCE_SENSOR_CARBON_DIOXIDE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga34ed8c9aefe34d5030209f073c9ecd24)
- [BT_APPEARANCE_SENSOR_AMBIENT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga622508f9b051ed0320700b01967f6446)
- [BT_APPEARANCE_SENSOR_ENERGY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca0cfcd560fa4133c0bc62a61d2874c7)
- [BT_APPEARANCE_SENSOR_COLOR_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8106142ddb6445e7462137e032e50854)
- [BT_APPEARANCE_SENSOR_RAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga380da83e3a69de3fd5091cdc89f7fcbc)
- [BT_APPEARANCE_SENSOR_FIRE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga425115e6c251a9c493c98d79f659077d)
- [BT_APPEARANCE_SENSOR_WIND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa710c0666d8b5bf1e1230672cbbf55fa)
- [BT_APPEARANCE_SENSOR_PROXIMITY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6d3447e24d5d75051b81998fd9ad8bfe)
- [BT_APPEARANCE_SENSOR_MULTI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeec9666dbdb31e9302a25aaa536f3180)
- [BT_APPEARANCE_SENSOR_FLUSH_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf9a9c0191ec175d14061058cf3da163c)
- [BT_APPEARANCE_SENSOR_CEILING_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadfb6808db5a7060316b724c24c8ceaf8)
- [BT_APPEARANCE_SENSOR_WALL_MOUNTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae564900f0517d393ceffcca8d27f6e45)
- [BT_APPEARANCE_MULTISENSOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga90237753920702380321e9f858344741)
- [BT_APPEARANCE_SENSOR_ENERGY_METER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7238d3a45f9e62f0189db9d7eeac4d15)
- [BT_APPEARANCE_SENSOR_FLAME_DETECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaae8f95ef639cb7d5e97063eed710a07d)
- [BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)
- [BT_APPEARANCE_GENERIC_LIGHT_FIXTURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae01be867f730c06b59fcb03289ae66d7)
- [BT_APPEARANCE_LIGHT_FIXTURES_WALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae1b2b535754f9cdc24c4a6cee63ef5cb)
- [BT_APPEARANCE_LIGHT_FIXTURES_CEILING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2d77fb5f5ed9a43771186ecc5693da8f)
- [BT_APPEARANCE_LIGHT_FIXTURES_FLOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga57bb461b0ddd045d21d7fbd3843fbabb)
- [BT_APPEARANCE_LIGHT_FIXTURES_CABINET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadc48840b6590a89593a5d17fbdb1e9e9)
- [BT_APPEARANCE_LIGHT_FIXTURES_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2f37bf95ea6057b999bbf2cf94016e5d)
- [BT_APPEARANCE_LIGHT_FIXTURES_TROFFER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa57b538ecad380ad77354e0cd9576e5b)
- [BT_APPEARANCE_LIGHT_FIXTURES_PENDANT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga336147b54406237e25d8cf9ed152928b)
- [BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga583b7432ba6ac4cc078d3a069e3a54e1)
- [BT_APPEARANCE_LIGHT_FIXTURES_FLOOD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab41f8b6f1ff0f624bb6666ef2ac6dab3)
- [BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga83f50305a23250e5e2cef5004762e122)
- [BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga20a7b241f292475d70626a38d983886c)
- [BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7c5811bd50d9f78e67e3e56faa432aae)
- [BT_APPEARANCE_LIGHT_FIXTURES_GARDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga348e64ffe0f3d6301dd8c911f70ead68)
- [BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0da0cbeebd2b20bf28dfc06def016068)
- [BT_APPEARANCE_SPOT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga58e1989c99b5a223a318a716d62f6e2b)
- [BT_APPEARANCE_LIGHT_FIXTURES_LINEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5388daf123e629d6f7a0b9af13fbc366)
- [BT_APPEARANCE_LIGHT_FIXTURES_STREET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac938fb03553d2d3c27b50af2a9a1ac48)
- [BT_APPEARANCE_LIGHT_FIXTURES_SHELVES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1bf2889f7a8a7ae363bc1d4355ee8d65)
- [BT_APPEARANCE_LIGHT_FIXTURES_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8f98c2d32664a6e03ebc2a43ae1eb52a)
- [BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3f687f994ffff2ce70b81a992195d210)
- [BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)
- [BT_APPEARANCE_LIGHT_FIXTURES_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac2b6de99b4e87f7c40063ba844c75ead)
- [BT_APPEARANCE_LIGHT_FIXTURES_BULB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8325830f2c977dc238a9ca1b9837803e)
- [BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc924bbc1b6aff0130c2be3d5fe59e33)
- [BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga738e87008c6a64450bb7ec22dbcdd113)
- [BT_APPEARANCE_GENERIC_FAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga82cc89321c4f4ffbf3ef25eff624943c)
- [BT_APPEARANCE_FAN_CEILING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8cd83cd08846ac276cc65f31333ee62e)
- [BT_APPEARANCE_FAN_AXIAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga32dd73ffa211d632617018aa510b89c4)
- [BT_APPEARANCE_FAN_EXHAUST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1e842c97b90678908f4d18c86c1227c2)
- [BT_APPEARANCE_FAN_PEDESTAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2e54f8de862435f2dbd7f56b98615c84)
- [BT_APPEARANCE_FAN_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa9e17b8b5e06d2fb365bf152e0cbef5d)
- [BT_APPEARANCE_FAN_WALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga498be79799cb778c9df6629411fe32ad)
- [BT_APPEARANCE_GENERIC_HVAC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf1f01946f6acadcaf719d3d7cc06e55f)
- [BT_APPEARANCE_HVAC_THERMOSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga33055b50c10bfc713b18823fca525488)
- [BT_APPEARANCE_HVAC_HUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf55f3f3f07cc78509e7fe19cea6cea4e)
- [BT_APPEARANCE_HVAC_DEHUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa3b96e44638048b8891a2dece29f4b3f)
- [BT_APPEARANCE_HVAC_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacef9145f435d10cbf5a775b9a2c9b756)
- [BT_APPEARANCE_HVAC_RADIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad90f108f3d33d68e27ac545cdb520f18)
- [BT_APPEARANCE_HVAC_BOILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacc28a1bc1a809c574019455de4ac9d0b)
- [BT_APPEARANCE_HVAC_HEAT_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaead4ebeabb8855111ab9080aca4e035a)
- [BT_APPEARANCE_HVAC_INFRARED_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga50c5df52d8471fc8e1dc65e31079566d)
- [BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad43d27ff96a7fba1ed7d5e20ebd472d9)
- [BT_APPEARANCE_HVAC_FAN_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2a044c3369ed48d216707f6e6a541a23)
- [BT_APPEARANCE_HVAC_AIR_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga182ade4b2c8f4705ba132248e504bb95)
- [BT_APPEARANCE_GENERIC_AIR_CONDITIONING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa13ae6496d47df2be0a0692a28806007)
- [BT_APPEARANCE_GENERIC_HUMIDIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0b552243744bc598467421555e935cd0)
- [BT_APPEARANCE_GENERIC_HEATING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8ea92ea92ca4e2bad4e5e2baba1271dd)
- [BT_APPEARANCE_HEATING_RADIATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga05b0b91c74aed5bc73a92f336bdae33a)
- [BT_APPEARANCE_HEATING_BOILER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac1abc9ae0b8ede2197720ea9e67b692e)
- [BT_APPEARANCE_HEATING_HEAT_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga99537968fdc7e680d922ca309fba7678)
- [BT_APPEARANCE_HEATING_INFRARED_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e40496a351c7ec5ea836805925f1e13)
- [BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga46fe051c7e50492dba5ae824e154cf69)
- [BT_APPEARANCE_HEATING_FAN_HEATER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga995ca18db114ea062df0d76c9e241937)
- [BT_APPEARANCE_HEATING_AIR_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac74bc8e109f5d9b4c0988ee6378ed471)
- [BT_APPEARANCE_GENERIC_ACCESS_CONTROL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac856a99a5db04dc20229a6e60a18d310)
- [BT_APPEARANCE_CONTROL_ACCESS_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e21f7df9d789b7c3aa6f7dab500df8c)
- [BT_APPEARANCE_CONTROL_GARAGE_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39134568b56c1d33e6567c893eb441f1)
- [BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2b6c7987ee4040216a385e665ff92321)
- [BT_APPEARANCE_CONTROL_ACCESS_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac2f588b6202e9d6140ec682cfe45f65d)
- [BT_APPEARANCE_CONTROL_ELEVATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga321d63ead349c0a83ef289bd2e4efb33)
- [BT_APPEARANCE_CONTROL_WINDOW](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaedc6415432862889e7f002fc9ef46b74)
- [BT_APPEARANCE_CONTROL_ENTRANCE_GATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab2a476a90f20576c0a1784fdc1e5e633)
- [BT_APPEARANCE_CONTROL_DOOR_LOCK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga29d07ce1101740b5f6f980660e405278)
- [BT_APPEARANCE_CONTROL_LOCKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga824236ba19c7f54d06b9abcd7df8c767)
- [BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga414b202e93d1db533853093d66603720)
- [BT_APPEARANCE_MOTORIZED_GATE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga376ef909868a5c273b71d1c372755707)
- [BT_APPEARANCE_MOTORIZED_AWNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga338de5523abf3fd81e913f3cdb4a31b6)
- [BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaaa39c48ed2d6edd5650743b82154462b)
- [BT_APPEARANCE_MOTORIZED_CURTAINS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga53f6a4df5ccc2117525952be2e174ddc)
- [BT_APPEARANCE_MOTORIZED_SCREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5f32cab5c7a155fffbe0c33cadfef31a)
- [BT_APPEARANCE_GENERIC_POWER_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadae82e45d9aafd34cafd3f0e793b1b24)
- [BT_APPEARANCE_POWER_OUTLET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad9efd19e2c95525a3972c8b0f0417449)
- [BT_APPEARANCE_POWER_STRIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2c5bd38d4eeb1aad2d29b004390a6d18)
- [BT_APPEARANCE_POWER_PLUG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d9aadc19f5f5f484769b225164866e4)
- [BT_APPEARANCE_POWER_SUPPLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga07acce808c9cf2b5e84aacd65e8f256d)
- [BT_APPEARANCE_POWER_LED_DRIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga31842298741c822dcebba942453975c6)
- [BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7de26016aa039e3e72ddd61653e1c1d8)
- [BT_APPEARANCE_POWER_HID_LAMP_GEAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6396b1d813c9764bdfe92c4f2ba961b1)
- [BT_APPEARANCE_POWER_CHARGE_CASE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5d6b28b9660d2357e2af2bf0ceab9c18)
- [BT_APPEARANCE_POWER_POWER_BANK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab6a5ac3941a5707f052126810a7f22e0)
- [BT_APPEARANCE_GENERIC_LIGHT_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacb3340c5193588eea2d42fe1bef443d0)
- [BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafed8531ffde21d0ad6e8d477d64496f0)
- [BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga66bf91b8a25ac88a0fd6ab9456201de1)
- [BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1babd2989112bafb5819235fe5b6c556)
- [BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39957a77aa54255ab3a06441e422e7e3)
- [BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga242d324cf5cf33e4edd5cf33e8c3c89b)
- [BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8449006920ed1fdd562c702ee2e16a21)
- [BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaf47bce54f4ae1915cd64c3c2d254e353)
- [BT_APPEARANCE_LIGHT_SOURCE_OLED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaed4400a94dae4f536a456cc55eb6f6d5)
- [BT_APPEARANCE_GENERIC_WINDOW_COVERING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1e70d961fca2719243c866464132684c)
- [BT_APPEARANCE_WINDOW_SHADES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga37614ae63c8287bc4bd0c9a5bf00502e)
- [BT_APPEARANCE_WINDOW_BLINDS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga717efaeab0329ded066567761b9983a7)
- [BT_APPEARANCE_WINDOW_AWNING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9945bb52a9ee3268efda7d5e05421e12)
- [BT_APPEARANCE_WINDOW_CURTAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga20352e58e6cec63efbb6beaa75c0e330)
- [BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7ead13b128fbc50be3f5c101fb1383cb)
- [BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0a0b87095177af0560a540e545c97f42)
- [BT_APPEARANCE_GENERIC_AUDIO_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga32bb0f06096ce5259676a31342b9f0d9)
- [BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabcb109c4660a177494329faf353406f4)
- [BT_APPEARANCE_AUDIO_SINK_SOUNDBAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga93e3a858b2efabea72a8855a28ad21c2)
- [BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga666aed968e9a0f9566edcc1bcba0bfbd)
- [BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6b3ddddf1de7d95a15aa6194ddc656ee)
- [BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadd82602d251aa555a06123ef0388d1b1)
- [BT_APPEARANCE_GENERIC_AUDIO_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac85b90f2585044d0efa61191dba3c596)
- [BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6dd1354de34ed79702d9d7878d859fcb)
- [BT_APPEARANCE_AUDIO_SOURCE_ALARM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa8d5a95cb181e27efb2409d5dce3da57)
- [BT_APPEARANCE_AUDIO_SOURCE_BELL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga748b4fa86145f3950069ed44cde8cacb)
- [BT_APPEARANCE_AUDIO_SOURCE_HORN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3415afbd526b29b5bbafc1ac889bd371)
- [BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga35ecc1a1051379010123582c82e9b31c)
- [BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga48fc37d769211cba1e6121e670b02e25)
- [BT_APPEARANCE_AUDIO_SOURCE_KIOSK](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ad3ee00ed05c8a7ed182df5c82a5af4)
- [BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaad0fe38e5246c55cc562729448b9f390)
- [BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)
- [BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga49328394fd7505da9476d4d62ae60c03)
- [BT_APPEARANCE_VEHICLE_CAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6257291ed3e6d09ce6197e2081b36d04)
- [BT_APPEARANCE_VEHICLE_LARGE_GOODS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga31ff643e1efccffd9ba73c793f63837c)
- [BT_APPEARANCE_VEHICLE_TWO_WHEELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga68ade931a12e5d9e9863decad3d8de9e)
- [BT_APPEARANCE_VEHICLE_MOTORBIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa71eaa4fd0eef66a794475cb44aaf397)
- [BT_APPEARANCE_VEHICLE_SCOOTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae082982b90d94404b69c57987d8a2c5a)
- [BT_APPEARANCE_VEHICLE_MOPED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga18b0231dbd97d8871f685774f9e1b4e1)
- [BT_APPEARANCE_VEHICLE_THREE_WHEELED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8159dfd6933a2a5fdb2c72da9623bc2e)
- [BT_APPEARANCE_VEHICLE_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac22a0476760c42eb8f00b36b74361c5e)
- [BT_APPEARANCE_VEHICLE_QUAD_BIKE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga03e3660bdc2e439126f2f8df8ea335ee)
- [BT_APPEARANCE_VEHICLE_MINIBUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0cf473bbf07d4576ab9f0116ca48f161)
- [BT_APPEARANCE_VEHICLE_BUS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0da02a18987c653a3232c28a3e4908f7)
- [BT_APPEARANCE_VEHICLE_TROLLEY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabde7af9f7c25d56f5fb9643398273526)
- [BT_APPEARANCE_VEHICLE_AGRICULTURAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa149e56e4b4a1b6dde821fbdac3d9c32)
- [BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafcb3909bf61bb130f8c0a217e69477b8)
- [BT_APPEARANCE_VEHICLE_RECREATIONAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9366a994d42c88490313380d419b2a8e)
- [BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac08b31ff9b618b19e4c1b43ae2056b5f)
- [BT_APPEARANCE_APPLIANCE_REFRIGERATOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad02c3dc8fa1321b14ee70264a36c4950)
- [BT_APPEARANCE_APPLIANCE_FREEZER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6ec2458a171142a5e22ec339d23a5a0c)
- [BT_APPEARANCE_APPLIANCE_OVEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7a48c5a07e677167ae10412ed2c1040b)
- [BT_APPEARANCE_APPLIANCE_MICROWAVE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabaac12b866cd29547165331333e8be3d)
- [BT_APPEARANCE_APPLIANCE_TOASTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5b0d9632cb2ed4afd856f05a1e857394)
- [BT_APPEARANCE_APPLIANCE_WASHING_MACHINE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1febcada2c95105648831094a4de6a8d)
- [BT_APPEARANCE_APPLIANCE_DRYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaac26996e0de10b16e24900a08c1098f5)
- [BT_APPEARANCE_APPLIANCE_COFFEE_MAKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac601c74c6132decf13527bdacbc5a08b)
- [BT_APPEARANCE_APPLIANCE_CLOTHES_IRON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaeb66941a8e8b38ed0ea47305da157e24)
- [BT_APPEARANCE_APPLIANCE_CURLING_IRON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6a9885e9a2133c0732d056ecd63313ad)
- [BT_APPEARANCE_APPLIANCE_HAIR_DRYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga15be0164f5883558fb61c9cb9679b78f)
- [BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga46d5f18bb8c764c43af97fddcec4a1ec)
- [BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga423e85d0816a4bd0205f4d8188e6c406)
- [BT_APPEARANCE_APPLIANCE_RICE_COOKER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga78511e0ef7d509deeba65352e7f81ad8)
- [BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0292c6123b655964311d0e6027b5af20)
- [BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabad761094a16873dcebbc6238825d84b)
- [BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab480735e2ba8db23d2668ea3a2137214)
- [BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)
- [BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae420044380309abba1b9570d26735315)
- [BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga59ea8ff5efec7a19bce8440e7ae78a1e)
- [BT_APPEARANCE_GENERIC_AIRCRAFT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga24c9bcf9646ec5049abf310b31ab355e)
- [BT_APPEARANCE_AIRCRAFT_LIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6f1d2fb56f53ac5317b024d7487b8742)
- [BT_APPEARANCE_AIRCRAFT_MICROLIGHT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad2d0b1c4b710e50127049ec4cd299396)
- [BT_APPEARANCE_AIRCRAFT_PARAGLIDER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6f827322066333fe926f0912099e6903)
- [BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae7be5c3bf9ad97e34d6c62bb791c39c0)
- [BT_APPEARANCE_GENERIC_AV_EQUIPMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadb3b07d6c3d3f679b15069fdd8d4e1ee)
- [BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7294c7b26ac8da3b9800c91ec824ad22)
- [BT_APPEARANCE_AV_EQUIPMENT_RECEIVER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac826e2e5326d1aa5fdd7ebf55fe395e6)
- [BT_APPEARANCE_AV_EQUIPMENT_RADIO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad60d1a387a1c62218baa3044e5acc3db)
- [BT_APPEARANCE_AV_EQUIPMENT_TUNER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7ccf41932861fa5f33d12060a12d5aa7)
- [BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga69417cb3e9c434e751483328d6134cdf)
- [BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6c9ad45a9b22a94ae0cce16bfe749a33)
- [BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga02681af8d755c701d9caef3f89a5c35a)
- [BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1394bc80927fb8db4eef1786111c65c7)
- [BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa01c862bff9aaaad09ed925da60fcb25)
- [BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad0ac86cf291b781b772fa9e85dda283a)
- [BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga44b70b2f515416baf686b1e127ef4375)
- [BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga9a6684aa8677575625e049fa0da2c26c)
- [BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabbcb0fbbeb6423052db9d5e04410499c)
- [BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa98f5139c99b46515746fb76e9ae7f9b)
- [BT_APPEARANCE_GENERIC_HEARING_AID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadb5595a41edf5974e03649a675618b7b)
- [BT_APPEARANCE_HEARING_AID_IN_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga28cc6555937d9d5a9e8ae0079fc8a534)
- [BT_APPEARANCE_HEARING_AID_BEHIND_EAR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1fa6231e14dcfa90a5518e61f0e4e302)
- [BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)
- [BT_APPEARANCE_GENERIC_GAMING](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaca727b215a8277d921c0a3bfeccb3f14)
- [BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8fbaf0fced0cce12e08c4a516351b166)
- [BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga39ad633d1795af4546bd930d0e799447)
- [BT_APPEARANCE_GENERIC_SIGNAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabc243c7449804749704c1862db286eab)
- [BT_APPEARANCE_SIGNAGE_DIGITAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gace31a591ef3b5f0812e4cbf417a2205a)
- [BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa4674b06751edf98fa88ede568a68ad4)
- [BT_APPEARANCE_GENERIC_PULSE_OXIMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga93ee753bf3b8819239041c065eaf024f)
- [BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8a298130c73299b6079dae3065954c0c)
- [BT_APPEARANCE_PULSE_OXIMETER_WRIST](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaebcadd5c37e6d87903e2cb97e03aeb7d)
- [BT_APPEARANCE_GENERIC_WEIGHT_SCALE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1aec23cd4f531a57260c7c8faf9caf40)
- [BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7387d717c77b38374e981991278aeb1c)
- [BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7966ec64cafe708fe94a7c323fbe3713)
- [BT_APPEARANCE_MOBILITY_SCOOTER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga21f21a73f355ffaa408376ca4fc802a8)
- [BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab77dd4cfe254df84cbe0b8d45247e198)
- [BT_APPEARANCE_GENERIC_INSULIN_PUMP](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga481169a27fab19628f81a68af31d543c)
- [BT_APPEARANCE_INSULIN_PUMP_DURABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga63512439364307259010bededf7bfd8b)
- [BT_APPEARANCE_INSULIN_PUMP_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0979695247b96321e5a8b6869d09227a)
- [BT_APPEARANCE_INSULIN_PEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1562514d0182e8862edad570b7a346e6)
- [BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga08453eebe2ae8f53deddaa64a029c2b5)
- [BT_APPEARANCE_GENERIC_SPIROMETER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga1332c44cc3371fa9006993d03ba4ae12)
- [BT_APPEARANCE_SPIROMETER_HANDHELD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga42b9d596efb757b209f080a8c33f3723)
- [BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d39ca2892bd96013b8c82111eecc1cb)
- [BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)
- [BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga52b6c51c9afcbbba12d9d3cae824f4a7)
- [BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gadf053353789183d1b1c3ca13ad98559f)
- [BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8fbc7782099e724febb712ee108e8cba)
- [BT_DATA_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga396b92d418fcb8263895e420b9df3df2)
- [`BT_DATA_UUID16_SOME`：部分 16 位 UUID（Some 16-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6c725bd3d31c159a4d046561dbca38ba)
- [BT_DATA_UUID16_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0d55063b9ad321b5c530a0012337df8a)
- [`BT_DATA_UUID32_SOME`：部分 32 位 UUID（Some 32-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2486a6748490ba57e442ca15223482ef)
- [BT_DATA_UUID32_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaaf825c3e4686e572a35ddd46ee6fe2e8)
- [`BT_DATA_UUID128_SOME`：部分 128 位 UUID（Some 128-bit UUIDs）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5c4f7fc1b93c611e95f735330fba243b)
- [BT_DATA_UUID128_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaafcade3dbbcb4005f4590e994f91884b)
- [`BT_DATA_NAME_SHORTENED`：缩短名称（Shortened Name）。](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc509b33a8d2dd9124f6893eadbe1662)
- [BT_DATA_NAME_COMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gab94a7c5689d296acf47f976538056ab5)
- [BT_DATA_TX_POWER](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga4988c17578c4cf76fcdd9d44e1c931b0)
- [BT_DATA_DEVICE_CLASS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga152c3028a2befcc4caf40aa6590c80b7)
- [BT_DATA_SIMPLE_PAIRING_HASH_C192](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga053c8bb0aedd01b3dd3f6154f4b49999)
- [BT_DATA_SIMPLE_PAIRING_RAND_C192](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga280f1f96c5204960fe034c9ddaf194ec)
- [BT_DATA_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac9402c597e5b4497f4bcd22d5177cc23)
- [BT_DATA_SM_TK_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga5014acb2fe8e76b855b55bf98abe6d05)
- [BT_DATA_SM_OOB_FLAGS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa12c742d1c955036aa3f55e84df69890)
- [BT_DATA_PERIPHERAL_INT_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabcf872eafc60c21287f6be63174dc7c8)
- [BT_DATA_SOLICIT16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga2ad4d2ec2ff29c0aad5159de12d3f741)
- [BT_DATA_SOLICIT128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga217df3f70846e86fa09e5605d5acd291)
- [BT_DATA_SVC_DATA16](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga76990dda919688b369decaf9d3606b32)
- [BT_DATA_PUB_TARGET_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacb867f0436d38c5c80e3426ca6247a46)
- [BT_DATA_RAND_TARGET_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3d9097d8f53213ccafc152c51ad6fdbd)
- [BT_DATA_GAP_APPEARANCE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga67fc721da05758b7d7a36aecaa035fac)
- [BT_DATA_ADV_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga6fd8c0f32bbcb97aaafee51fda0b601e)
- [BT_DATA_LE_BT_DEVICE_ADDRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad9e8a273239fa160a6b2797ef5563a94)
- [BT_DATA_LE_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga255c7cb16eb24b95fa0f531fc4574273)
- [BT_DATA_SIMPLE_PAIRING_HASH](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga324f91521eacd1e9d579c9d52d02eb06)
- [BT_DATA_SIMPLE_PAIRING_RAND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad7e7dd2d3a972e53f9e5e80627bd07e6)
- [BT_DATA_SOLICIT32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga76e7e8971ed841b87fda08793a00b14f)
- [BT_DATA_SVC_DATA32](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7d411a723ff2f038c3b7a1e09c88cb3d)
- [BT_DATA_SVC_DATA128](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaa53847910515d9488b490f17a4fdf0d1)
- [BT_DATA_LE_SC_CONFIRM_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga883dda02c157f0de8157b1c5f66aafd0)
- [BT_DATA_LE_SC_RANDOM_VALUE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gacbc31c67684e3c68481501cf89f9ec68)
- [BT_DATA_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga3c6a5903cc4a46aaf0b30a0de0179403)
- [BT_DATA_INDOOR_POS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga0f29f9d8f5a336af430f0a603e87e995)
- [BT_DATA_TRANS_DISCOVER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga8e9ccc669ee545152b2d9b3120692d55)
- [BT_DATA_LE_SUPPORTED_FEATURES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga207bc1e5405a4fd3f39863a2cb304ebc)
- [BT_DATA_CHANNEL_MAP_UPDATE_IND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gae3eb96c0f127b6417d7cad288faaaceb)
- [BT_DATA_MESH_PROV](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gafc5984d58b0b54ee824dd83bc78dfbe9)
- [BT_DATA_MESH_MESSAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gac351c67ab58520b796fa713602d9f602)
- [BT_DATA_MESH_BEACON](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga59cc479be1f6c61a4a47aa6f479fe67a)
- [BT_DATA_BIG_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga16feb94cd09c04d020450f61646f5486)
- [BT_DATA_BROADCAST_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga72d2e55819db593a6db77579ebfe1e9d)
- [BT_DATA_CSIS_RSI](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga122da4184d606ae140f8a311aaebeedd)
- [BT_DATA_ADV_INT_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gad4ac2e0de80dddcacc4ca6d25765eebd)
- [BT_DATA_BROADCAST_NAME](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga7d781791bc85fe3c7ea839ff617ee6e7)
- [BT_DATA_ENCRYPTED_AD_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga41d5c898144e89b6035f92ff506f38a3)
- [BT_DATA_PAWR_TIMING_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga14a8b1cf9d6c1c9749443a012731d39c)
- [BT_DATA_ESL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga90c7a1175148f3a56b04dc0b29525a4d)
- [BT_DATA_3D_INFO](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gaecab0c77f9f912c16c264e7eaf2e4707)
- [BT_DATA_MANUFACTURER_DATA](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga63b846807bff632b1cdd49b1e46e63b4)
- [BT_LE_AD_LIMITED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga36191ee000a2098fd679c398b31e0906)
- [BT_LE_AD_GENERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#ga13d9b4a24e2a8b58402bfb21f8b782c8)
- [BT_LE_AD_NO_BREDR](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html#gabf5725f481cb73cbd974f3653c904bc9)
- [BT_MESH_MODEL_ID_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga004d8d1be55b2aec56abbeeca1d118d8)
- [BT_MESH_MODEL_ID_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3f8442dcd1a110ea0d0023f50057139f)
- [BT_MESH_MODEL_ID_HEALTH_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga6416216348d7186f91175ca50bb8c903)
- [BT_MESH_MODEL_ID_HEALTH_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gab58b85b7a77feeb579973177c12bb446)
- [BT_MESH_MODEL_ID_REMOTE_PROV_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9c7d1c5dfb87a5ce50c08747af47414f)
- [BT_MESH_MODEL_ID_REMOTE_PROV_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf373eb4d8af5d6bee76a821bd4d5e48c)
- [BT_MESH_MODEL_ID_BRG_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga599d00e9d63ade6ed1a6803579c1e16e)
- [BT_MESH_MODEL_ID_BRG_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9c776b4befd21c15f4867d906f631257)
- [BT_MESH_MODEL_ID_PRIV_BEACON_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gacca0e355982935cfbde46a06b09a7bec)
- [BT_MESH_MODEL_ID_PRIV_BEACON_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gab3b21cbee4e11319a6e0ba3b02b24a91)
- [BT_MESH_MODEL_ID_SAR_CFG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga1e9d8be1d2e65d2977aea0306b015258)
- [BT_MESH_MODEL_ID_SAR_CFG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf214eb7eef3530919432b62ff9b353c3)
- [BT_MESH_MODEL_ID_OP_AGG_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga5cf2bb09e5eaa299cfc6b7fe4ed66e9a)
- [BT_MESH_MODEL_ID_OP_AGG_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gabac62a77e7d2d7677af21c33c8629187)
- [BT_MESH_MODEL_ID_LARGE_COMP_DATA_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaec3abd6a0bd7b07a71fe5ed6a7a6931a)
- [BT_MESH_MODEL_ID_LARGE_COMP_DATA_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga729d67e4183457932e4c837d65abd842)
- [BT_MESH_MODEL_ID_SOL_PDU_RPL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga165bc198dadaa0d534ec82eb8192ebc0)
- [BT_MESH_MODEL_ID_SOL_PDU_RPL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga6e747dd364bcfaa368e37c5f01afd530)
- [BT_MESH_MODEL_ID_ON_DEMAND_PROXY_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaddc0bd645180a57cb9cd36745b84f7a1)
- [BT_MESH_MODEL_ID_ON_DEMAND_PROXY_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadd36546fb2cb6d1c731f7ae7674af6a7)
- [BT_MESH_MODEL_ID_GEN_ONOFF_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga83e1ed5398d513cfeb900e41655aa4d8)
- [BT_MESH_MODEL_ID_GEN_ONOFF_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4f0eee2569b518a5e4250f5b7b294fed)
- [BT_MESH_MODEL_ID_GEN_LEVEL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga7f10a8332b1406c3ad628b9679e1d7cb)
- [BT_MESH_MODEL_ID_GEN_LEVEL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga462c578845a17b20cdb3e008f74f93a6)
- [BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga004d5ec0870d47a8d37182e5b0c089a5)
- [BT_MESH_MODEL_ID_GEN_DEF_TRANS_TIME_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gafa1c6a7d857fe13a139ce2242b4e62f5)
- [BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga09ac731fff09146ec68557f00e8294e0)
- [BT_MESH_MODEL_ID_GEN_POWER_ONOFF_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2a6dad18792ba7f1d81d6c9a1c65f90a)
- [BT_MESH_MODEL_ID_GEN_POWER_ONOFF_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga9f6544f7b87f39d0792ea2de13cd45f1)
- [BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadd30afe63f89e9c1778e56f722fd82f9)
- [BT_MESH_MODEL_ID_GEN_POWER_LEVEL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga1ff6ec64ce3a86d1cfd00fc98e89c0a5)
- [BT_MESH_MODEL_ID_GEN_POWER_LEVEL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8420454c35afc12c62ede55942f3b6d3)
- [BT_MESH_MODEL_ID_GEN_BATTERY_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gacf891135f54fb1fbb62beb812235619e)
- [BT_MESH_MODEL_ID_GEN_BATTERY_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga34bb3d4839e9685ec55f8285aac9a79f)
- [BT_MESH_MODEL_ID_GEN_LOCATION_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad516f513c5c942fbfee65b85332b105e)
- [BT_MESH_MODEL_ID_GEN_LOCATION_SETUPSRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga240d1ed34b7341627773cce862f85620)
- [BT_MESH_MODEL_ID_GEN_LOCATION_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8fa01ddb1f4de4d61500bb650243390d)
- [BT_MESH_MODEL_ID_GEN_ADMIN_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3cc6862e9c72f9282055c5cda2343c89)
- [BT_MESH_MODEL_ID_GEN_MANUFACTURER_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga32e09ddfebd2e8b22da9a3102e116aae)
- [BT_MESH_MODEL_ID_GEN_USER_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4b7b6a4b47e87de94ccf11ef1abd64b9)
- [BT_MESH_MODEL_ID_GEN_CLIENT_PROP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga20906658018ef26114d8a6656c258f62)
- [BT_MESH_MODEL_ID_GEN_PROP_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga69455e5b1e6def3d909c4bb6e0dee9ae)
- [BT_MESH_MODEL_ID_SENSOR_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3e0dcb14f46f6076e5b1b114b977f630)
- [BT_MESH_MODEL_ID_SENSOR_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad10780bfc1c16866fa28de750e56bec3)
- [BT_MESH_MODEL_ID_SENSOR_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga8f1e4ff66d388627dbe91b2f8d4ed358)
- [BT_MESH_MODEL_ID_TIME_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga93fbf1c661a75d70fdbd2a599353eb94)
- [BT_MESH_MODEL_ID_TIME_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2725121dc8c2c21c0ee469fe4348f45f)
- [BT_MESH_MODEL_ID_TIME_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga500df90af7989794c5d72e760e5e65c6)
- [BT_MESH_MODEL_ID_SCENE_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaaa5554e3d48ae101596476e6bd6caf67)
- [BT_MESH_MODEL_ID_SCENE_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa3b08fc8788684abb960fa3516726264)
- [BT_MESH_MODEL_ID_SCENE_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gad60472aa004a8a913aeb63ef62c45857)
- [BT_MESH_MODEL_ID_SCHEDULER_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga82b723752e240f22b9bcc8dc3dd10eb9)
- [BT_MESH_MODEL_ID_SCHEDULER_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga3dbec5a3b82cb25a142c4bc851e3fe0e)
- [BT_MESH_MODEL_ID_SCHEDULER_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gac743b26cf7e746b16302c25e8cd56221)
- [BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga16df49e84e84d0ae4a6ab5d5f3f1b2b6)
- [BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gadb93b2ed2256a5c9c3f66237841b1bf5)
- [BT_MESH_MODEL_ID_LIGHT_LIGHTNESS_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga960055723dec7b3b366efa7c49cafc2e)
- [BT_MESH_MODEL_ID_LIGHT_CTL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa9a211341c5b3283b9b0e0842adef053)
- [BT_MESH_MODEL_ID_LIGHT_CTL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga28ac69b2dbeec70bae4bd3c0381e9e93)
- [BT_MESH_MODEL_ID_LIGHT_CTL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga58fc8d99b746b0061177ac5d95341da1)
- [BT_MESH_MODEL_ID_LIGHT_CTL_TEMP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gafcb1f1ea20bb78b78a9ead4bfdbe3e47)
- [BT_MESH_MODEL_ID_LIGHT_HSL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaa0ddc753a226060d014dcd368feab17e)
- [BT_MESH_MODEL_ID_LIGHT_HSL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga574d3ba3f629bdbffc8f15db931a263a)
- [BT_MESH_MODEL_ID_LIGHT_HSL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga2d111a352322be8e33ba0cba0feb3f0c)
- [BT_MESH_MODEL_ID_LIGHT_HSL_HUE_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga865952346db9336a255c71bcb5f09774)
- [BT_MESH_MODEL_ID_LIGHT_HSL_SAT_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gae55004e70670a8711e18e9c9b3428720)
- [BT_MESH_MODEL_ID_LIGHT_XYL_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga29e1a90f166d88b6773d9b7ccf08e1c7)
- [BT_MESH_MODEL_ID_LIGHT_XYL_SETUP_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga4addae460d6b3c0a914198695b3e31ea)
- [BT_MESH_MODEL_ID_LIGHT_XYL_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga0ca4d9997e6016b5c27f42549d42a99d)
- [BT_MESH_MODEL_ID_LIGHT_LC_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga789412252034939539ba45e4bf21e3e2)
- [BT_MESH_MODEL_ID_LIGHT_LC_SETUPSRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga436358740bb64d845aa4d849d462a12e)
- [BT_MESH_MODEL_ID_LIGHT_LC_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaadd48b07e1eb53df24df40b7ea412e90)
- [BT_MESH_MODEL_ID_BLOB_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gae85d4cf7aad4e94582c24f79d6f60904)
- [BT_MESH_MODEL_ID_BLOB_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga17e2e59a1344e623fe9fec6e27b7f22e)
- [BT_MESH_MODEL_ID_DFU_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga0215c2c8cd16ab6536ea243864f9604e)
- [BT_MESH_MODEL_ID_DFU_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf477a37238ec577000a646af40862ee1)
- [BT_MESH_MODEL_ID_DFD_SRV](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#gaf4309dea32d05274f8f3a6ea45faba38)
- [BT_MESH_MODEL_ID_DFD_CLI](../api_cap_mqtt_topic_reference/P001_蓝牙 Mesh 分配编号（Bluetooth Mesh Assigned Numbers）.md#ga87d3b5cc207dc3b51e85c9594bb98cad)
- [BT_COMP_ID_LF](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6bbf21c05f24d2c2c710be9bcf05af5f)
- [BT_COD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa8793a9bc39bf833124c8c961e441a43)
- [BT_COD_VALID](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf2c925e431eec42930101a72b00a7283)
- [BT_COD_MAJOR_SERVICE_CLASSES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab598bdad77874748f74187aa32049ea6)
- [BT_COD_MAJOR_DEVICE_CLASS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga129895b48ad9071017a2e97335ec6d2b)
- [BT_COD_MINOR_DEVICE_CLASS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadcf892b98d0924ea8a78d4b8b588bddb)
- [BT_COD_MAJOR_SVC_CLASS_LIMITED_DISCOVER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga01883ae9792f486644dc96dd0559c72d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [BT_COD_MAJOR_SVC_CLASS_LE_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga031275c4187717b7556c4f0a7e16126a)
- [BT_COD_MAJOR_SVC_CLASS_RESERVED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga18cbe8ede63ed6c3396aabf01c97c672)
- [BT_COD_MAJOR_SVC_CLASS_POSITIONING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9fa4505b17dc53c22c9ac3fde9743e29)
- [BT_COD_MAJOR_SVC_CLASS_NETWORKING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga262412d5459d96d7f64a3d13db4906d2)
- [BT_COD_MAJOR_SVC_CLASS_RENDERING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6f959f962a9054102b4bbfe5b7248dd5)
- [BT_COD_MAJOR_SVC_CLASS_CAPTURING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga35cd970ddcba07d98e9e42863ee155f9)
- [BT_COD_MAJOR_SVC_CLASS_OBJECT_TRANSFER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga17cf278f25d45040991ef2d60dafb456)
- [BT_COD_MAJOR_SVC_CLASS_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2c70ab983a099e74a89aaaff02c086d0)
- [BT_COD_MAJOR_SVC_CLASS_TELEPHONY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2bca689e747d06869b3e86dbe7e10253)
- [BT_COD_MAJOR_SVC_CLASS_INFORMATION](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafb44e9944c2f84d45d448975c1ab0300)
- [BT_COD_MAJOR_DEVICE_CLASS_MISCELLANEOUS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9e57c7be37bc489c6ec4e35bf26e5718)
- [BT_COD_MAJOR_DEVICE_CLASS_COMPUTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga41f24363507a81975e1a1de8068bcd86)
- [BT_COD_MAJOR_DEVICE_CLASS_PHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf4e20997428ae008b48f1eee3f150633)
- [BT_COD_MAJOR_DEVICE_CLASS_LAN_NETWORK](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga341edcc0340d6d2d5ba3c76beeab1c93)
- [BT_COD_MAJOR_DEVICE_CLASS_AUDIO_VIDEO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga88281290c9641477d5e19b321f489e85)
- [BT_COD_MAJOR_DEVICE_CLASS_PERIPHERAL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga71cb552a1ba251492456a3862a70321b)
- [BT_COD_MAJOR_DEVICE_CLASS_IMAGING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gabd6b43f20dba80d46238567f8026a405)
- [BT_COD_MAJOR_DEVICE_CLASS_WEARABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga832d46c3654018a272f167e8d2f028c2)
- [BT_COD_MAJOR_DEVICE_CLASS_TOY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6af01f93fadb4ded2c0e7d74acdfa9a2)
- [BT_COD_MAJOR_DEVICE_CLASS_HEALTH](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7493589ba4918239c7714b12f4044c48)
- [BT_COD_MAJOR_DEVICE_CLASS_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga81690fb90860176fc17fed8625fed486)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga47d7e27a9da20b27c0483ab50db3590d)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_DESKTOP_WORKSTATION](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae1a285e3787132a97edf7adb53963880)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_SERVER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6d009b3670bfa0de1ed30c2ec87f8918)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_LAPTOP](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga60f70b01f651baab797b79ee5c7b94aa)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_HANDHELD_PC_PDA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad8af957eeafefca10f2538b2e09c7bd3)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_PALM_SIZED_PC_PDA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab5eb08bfa138cbfd55ffa2774a38fd9f)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_WEARABLE_COMPUTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaec2dc76edfa8a7edc6ce990be1658e54)
- [BT_COD_MINOR_DEVICE_CLASS_COMPUTER_TABLET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga0a98088245313a02c7dfbfdb39784632)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga86dd6474cad2c148c4bf2273707f3bca)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_CELLULAR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf3796e468def379157c2cf02a356b578)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_CORDLESS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gacce21d82143f430ff2bac1608b42b7e1)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_SMARTPHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad74d69e9ec7a82b128df0a6ad33bfc65)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_WIRED_MODEM](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga708f325406d16fbcb96f0a311ad6f12f)
- [BT_COD_MINOR_DEVICE_CLASS_PHONE_COMMON_ISDN_ACCESS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad711cb8a9d53d428f4aef9da0605c27e)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_FULLY_AVAILABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gacf4f30af8af17254d8557c2102e82930)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_1_17_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa48c789f29f33b7f129bbd593ab336fe)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_17_33_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab19bf6c95fbe0d3aa4923323b67c2f0c)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_33_50_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga17e2dd35fb4fd37f45757515a03df565)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_50_67_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaecb741bfc498bacfbd4c9059b3551e2f)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_67_83_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf296fcfd14235a0762a4565ff265e6be)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_83_99_UTILIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7a740756ba4dbc8770f4cdf5af2d1fa5)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_SERVICE_NO_SERVICE_AVAILABLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafb3f26abffdd158cfd117aefa06a31bb)
- [BT_COD_MINOR_DEVICE_CLASS_LAN_NETWORK_DEVICE_TYPE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab4af4c15266ce0f24f2f61d0578f346a)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga245357d925ffde5ce1d7d038bd661097)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_WEARABLE_HEADSET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaa79054d26b530834da97412ffc6a6d76)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HANDSFREE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaea20dcaaf0dcf2914b1ede0e657ad233)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_MICROPHONE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6c71bd324c442918d05b2ba176549f78)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_LOUDSPEAKER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga419c36342136f5ea827d2889ed666d4c)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HEADPHONES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6adf41d4cadabdca21bb1191ae0951f5)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_PORTABLE_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gac50804ea808e6e83686ad973d187bf9d)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAR_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8f60c01b2da107da93e8b873b03be337)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_SETTOP_BOX](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga3a7182ce71c7ae49330475c0093e7665)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_HIFI_AUDIO](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7ec413fa38b2e0ddcdb0cacfb9565d2a)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VCR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gafa6100bcc07e04e7177b34336a523c6a)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CAMERA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4ee160425ba1d2fa7f7ab9f360eb51ea)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_CAMCORDER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9cb9ddf5ac2d9e132b1504bb35fba5e7)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7bb6a3801475a076153529859d607254)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_DISPLAY_LOUDSPEAKER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5a20841438980c2fcf408974782c9f6e)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_VIDEO_CONFERENCING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga07f3ddf991a1de0ef1a5e4bc80f87ae9)
- [BT_COD_MINOR_DEVICE_CLASS_AUDIO_VIDEO_GAMING_TOY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga67798be9a45da9d23993851dc47b8015)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_NO_KEYBOARD_NO_POINTING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4b48d9b5ef8fdddd11f1cb528e826d79)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_KEYBOARD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gab648e64338834e0f986415603a7ee01a)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_POINTING_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga71c43b86fa8d01d45d11bea0bb56ee63)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_INPUT_DEVICE_TYPE_COMBO_KEYBOARD_POINTING](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4c26cacb0efe86dd586cacb48f7f9798)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadd57844cdd2d6ff59ea8371b64c0786a)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_JOYSTICK](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae7ceeea12447c03b901704165f815d2a)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_GAMEPAD](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaae4e0e78d28b915f7be42640aab41802)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_REMOTE_CONTROL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga55dc4b9ce33c7254ade2b32124bd5a52)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_SENSING_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6115e1fc2619c95bcf7a50e657347c8b)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITIZER_TABLET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8b21b9c98bb8ec187bb7be661c875048)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_CARD_READER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8b23f0432923353c1425244780c2cd4a)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_DIGITAL_PEN](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga7a8bec17a83efabcf83a3a0848fbd286)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_SCANNER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga3cff5d97f27e3725217f332dbd1e15ef)
- [BT_COD_MINOR_DEVICE_CLASS_PERIPHERAL_DEVICE_TYPE_HANDHELD_GESTURAL_INPUT](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2e603791c7467731fcd8e5ef521405fc)
- [BT_COD_MINOR_DEVICE_CLASS_IMAGING_DISPLAY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaeb931c305948fa843853f9f418c71d45)
- [BT_COD_MINOR_DEVICE_CLASS_IMAGING_CAMERA](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga238b06f556138d4bab338ff1375a1021)
- [BT_COD_MINOR_DEVICE_CLASS_IMAGING_SCANNER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6eb468819358a83906f40f2f64c344ae)
- [BT_COD_MINOR_DEVICE_CLASS_IMAGING_PRINTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf6a4be11446739a2aede1adf4d4fda77)
- [BT_COD_MINOR_DEVICE_CLASS_IMAGING_UNCATEGORIZED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5010b99a3111775447ac89f169d824af)
- [BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HEADSET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae879842e986be1f78b1a6afdd06f267e)
- [BT_COD_MINOR_DEVICE_CLASS_WEARABLE_PAGER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga2c68dc5a8fe4252bc2c743f05f9d4e96)
- [BT_COD_MINOR_DEVICE_CLASS_WEARABLE_JACKET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga9a7d4d0b3645f38a9888beb2ec994fe1)
- [BT_COD_MINOR_DEVICE_CLASS_WEARABLE_HELMET](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga091efe28aab4b90f3552d56704b2a886)
- [BT_COD_MINOR_DEVICE_CLASS_WEARABLE_GLASSES](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaea4e865414b40d9b370951a328dc0c36)
- [BT_COD_MINOR_DEVICE_CLASS_TOY_ROBOT](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf527b4a6353fc0e110033f1661342a80)
- [BT_COD_MINOR_DEVICE_CLASS_TOY_VEHICLE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga236dedbc75b174d221173080e734227e)
- [BT_COD_MINOR_DEVICE_CLASS_TOY_DOLL](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaf22179ae786663d350c7dfa9a25671b0)
- [BT_COD_MINOR_DEVICE_CLASS_TOY_CONTROLLER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gae51ab020f0a58a7468e79b33cf5888d2)
- [BT_COD_MINOR_DEVICE_CLASS_TOY_GAME](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4305ed742e35f7d21d97d6ca8a228776)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_UNDEFINED](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga98a4f1577322dd14790bda9ce8b28661)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_BLOOD_PRESSURE_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gadc1ba5de00271e2663dc52770acbf1f1)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_THERMOMETER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga60998708af979e1c02d8a0d6373500c8)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_WEIGHING_SCALE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga8c6cb016bdd1a5f50258c671f7528f8e)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_GLUCOSE_METER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5c9e6a84ff76bfc8c12750e9b133861a)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_PULSE_OXIMETER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gabe9f5e78c7321d8a2ff1752fe41d124d)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEART_PULSE_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga94863d500f1a576eb3d818209196d12e)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_HEALTH_DATA_DISPLAY](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad6577d566fd17b126611583b4379ad01)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_STEP_COUNTER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga6e50e1316332ba4e5da2fd81c6e65ef7)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_BODY_COMPOSITION_ANALYZER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gad34ed19a24a0b2a300b8e31c5a7ce798)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_PEAK_FLOW_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga746b3b863fb6250cd990099b014f063f)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_MEDICATION_MONITOR](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga4b376213b25611ff4bcf8cb7c7483a3a)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_KNEE_PROSTHESIS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#gaabd014dab3f24d38b8aabda2ae7e5ff4)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_ANKLE_PROSTHESIS](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga25315720692627e093a25df80d5b487d)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_GENERIC_HEALTH_MANAGER](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga308d6b8f3ed8cefccbca002ede932218)
- [BT_COD_MINOR_DEVICE_CLASS_HEALTH_PERSONAL_MOBILITY_DEVICE](../api_socket_lora_topic_reference/P003_分配编号（Assigned Numbers）.md#ga5fd6e3a6703d961259bd563ca6379c9a)
- [bt_bearer_tech](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga4bf3f820b493361a9a3b393d0282420f)
- [BT_BEARER_TECH_3G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa62dfe9fe5ac51927efef815b9ce6874e)
- [BT_BEARER_TECH_4G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa231fe012027b8d279e325231d804ed29)
- [BT_BEARER_TECH_LTE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa1bd25e0325ebefc57bdac0968e84fd64)
- [BT_BEARER_TECH_WIFI](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fab74491db769e0ab918809ab244e2ad1c)
- [BT_BEARER_TECH_5G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420faf6494f280fa28f202ce28bb7bc66ee24)
- [BT_BEARER_TECH_GSM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fac6789c1a3127b92c1d9c6a5ee6f02c8a)
- [BT_BEARER_TECH_CDMA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fa1ab62f67902936349103d33f1475a328)
- [BT_BEARER_TECH_2G](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420face445f78f84de0ef7c6d3ef23e3172b8)
- [BT_BEARER_TECH_WCDMA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga4bf3f820b493361a9a3b393d0282420fac6fad482035f2eab235dac4dffe77baa)
- [bt_audio_codec_cap_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaf58823a56eb36cfd22e582ab1ea3d015)
- [BT_AUDIO_CODEC_CAP_TYPE_FREQ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015af68f3f5665446de9b71c2f70e7aa762b)
- [BT_AUDIO_CODEC_CAP_TYPE_DURATION](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015a4a90a37cd6d8ca9d1ed984e4a122d510)
- [BT_AUDIO_CODEC_CAP_TYPE_CHAN_COUNT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015a0cd3a3d31febc9e30137e9e21d4f7191)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_LEN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015ad074bed5f79946e2388584336d30cf46)
- [BT_AUDIO_CODEC_CAP_TYPE_FRAME_COUNT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf58823a56eb36cfd22e582ab1ea3d015acba980896f080ac2ba81d1b66305bb41)
- [bt_audio_codec_cap_freq](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaafc1106d5d305874ee2f540c850ff5b4)
- [BT_AUDIO_CODEC_CAP_FREQ_8KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a3d821d03771805107707f47dcdb71f83)
- [BT_AUDIO_CODEC_CAP_FREQ_11KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a562c38a59cded025183a0f95d4a63c81)
- [BT_AUDIO_CODEC_CAP_FREQ_16KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4acfef6825ac865b1e590e7959a9270361)
- [BT_AUDIO_CODEC_CAP_FREQ_22KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ad7440157cf8864dfc5fd854482f3a982)
- [BT_AUDIO_CODEC_CAP_FREQ_24KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4acf9ff8842d72d56d27eae692e4c4b956)
- [BT_AUDIO_CODEC_CAP_FREQ_32KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a822ff105ab495c126c21d73bd90cbd9c)
- [BT_AUDIO_CODEC_CAP_FREQ_44KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ad28396f4b5a71d7c196e1a27bd17f8c3)
- [BT_AUDIO_CODEC_CAP_FREQ_48KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a91ec17ee96b8e56e31ab545e5e8abe91)
- [BT_AUDIO_CODEC_CAP_FREQ_88KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a25cc72bd630446f5154c54402058a211)
- [BT_AUDIO_CODEC_CAP_FREQ_96KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ae802fea402f207238613275917846663)
- [BT_AUDIO_CODEC_CAP_FREQ_176KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a031d159eadf7ea1ba6b00b03bef26d2b)
- [BT_AUDIO_CODEC_CAP_FREQ_192KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4a0de8d0351153650c1b48934053e18890)
- [BT_AUDIO_CODEC_CAP_FREQ_384KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4ae5ddc4504b7077e90be56f34ad8647c2)
- [BT_AUDIO_CODEC_CAP_FREQ_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaafc1106d5d305874ee2f540c850ff5b4adaaa42a6bb0c01d3819c604b6d5bbf02)
- [bt_audio_codec_cap_frame_dur](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gaf37e8e19f956afb3c3a413cbaa1a21f5)
- [BT_AUDIO_CODEC_CAP_DURATION_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a340878058d0beabeade33e0f3893d441)
- [BT_AUDIO_CODEC_CAP_DURATION_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5afd423ac4270ff0df8ca6df7f5e4c799b)
- [BT_AUDIO_CODEC_CAP_DURATION_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a81d28ce43d69d4625e9a73b37c70347a)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a7ab1c63639cf93fdf2c2dfdf43424e91)
- [BT_AUDIO_CODEC_CAP_DURATION_PREFER_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggaf37e8e19f956afb3c3a413cbaa1a21f5a9744473b3a29074c24cf0bbff35a5d8e)
- [bt_audio_codec_cap_chan_count](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gae695b5d17359967703f2509db1671fa5)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_1](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a1558716b36042597515df18ff277f8bc)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_2](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a13b236d93eb9c7516fdcf527313e16cd)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_3](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a17da27ec39a79c341c82549df891cb39)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_4](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a0fdfa6bf69b104f04d22e4f968969ac2)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5ad08bc2ea0347a1ee8fd411a023b7ca51)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_6](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5af9f9dd0cac39793793e5c8c5e50b11b8)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_7](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a86ef227772c7751b4ae75529e2a57b82)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_8](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5a50afa60bdd53172fab7a376ce374d943)
- [BT_AUDIO_CODEC_CAP_CHAN_COUNT_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggae695b5d17359967703f2509db1671fa5aaf6f7179310c64b93b300ecfc29e4219)
- [bt_audio_codec_cfg_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga9230ec4d7518bd243207ba2decb1a974)
- [BT_AUDIO_CODEC_CFG_FREQ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a49849b389d553535ea222c9ae63bccc3)
- [BT_AUDIO_CODEC_CFG_DURATION](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a8e2fae97b1565b0fa0ff988a47928223)
- [BT_AUDIO_CODEC_CFG_CHAN_ALLOC](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974ad53deb048fb0ce4d4428df4f477718b2)
- [BT_AUDIO_CODEC_CFG_FRAME_LEN](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974a85d41856175c11b1193ebdd58b83d6e2)
- [BT_AUDIO_CODEC_CFG_FRAME_BLKS_PER_SDU](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga9230ec4d7518bd243207ba2decb1a974abbc2279f5d029278d9367f08a1152aa8)
- [bt_audio_codec_cfg_freq](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga8e99fb678cc011bb8c9f6e1858bae0d7)
- [BT_AUDIO_CODEC_CFG_FREQ_8KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a7018d3fb612d4730b880ef0bb2d20b9a)
- [BT_AUDIO_CODEC_CFG_FREQ_11KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa8d8018b050a8c029b4b60c706d771f8)
- [BT_AUDIO_CODEC_CFG_FREQ_16KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7ab097ae9f9ad963fee64e61eaf2663245)
- [BT_AUDIO_CODEC_CFG_FREQ_22KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a68f8411a83f60ec4c6bb9fa65fdd7048)
- [BT_AUDIO_CODEC_CFG_FREQ_24KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a0d6d0f278628681f8ef5dc3797bf5275)
- [BT_AUDIO_CODEC_CFG_FREQ_32KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a3ce97404475ad182125ad64aba66077e)
- [BT_AUDIO_CODEC_CFG_FREQ_44KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa701e855c950fdcdd66d4dbaaf75fb84)
- [BT_AUDIO_CODEC_CFG_FREQ_48KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a2b7163ba4c486167d3e81c2aa4216f11)
- [BT_AUDIO_CODEC_CFG_FREQ_88KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aff685ebe62909eea8512b7deac0df409)
- [BT_AUDIO_CODEC_CFG_FREQ_96KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a79e7a473d3f7d6803f3b8b7843c40c60)
- [BT_AUDIO_CODEC_CFG_FREQ_176KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a85037a2eb4a64376a0a436ab43263126)
- [BT_AUDIO_CODEC_CFG_FREQ_192KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7aa85a51db272ef019e5cce5ec3982f8c7)
- [BT_AUDIO_CODEC_CFG_FREQ_384KHZ](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga8e99fb678cc011bb8c9f6e1858bae0d7a44cccbd3e7afc25f964b3c2c571d4be4)
- [bt_audio_codec_cfg_frame_dur](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga83701b5eadfcbc9b84dc0b1a85ebeb74)
- [BT_AUDIO_CODEC_CFG_DURATION_7_5](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ad2491c0ded7c7f489bdeffe024463272)
- [BT_AUDIO_CODEC_CFG_DURATION_10](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga83701b5eadfcbc9b84dc0b1a85ebeb74ab6a0dd3bbe587ff5ba110675a01514a7)
- [bt_audio_context](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gafb379ffa88388cc1397960155bbb2ab3)
- [BT_AUDIO_CONTEXT_TYPE_NONE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a890d2723c8b23127ab4a1cb8b6b1118d)
- [BT_AUDIO_CONTEXT_TYPE_UNSPECIFIED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3aad96be1265bd1be4c937c687335e33f5)
- [BT_AUDIO_CONTEXT_TYPE_CONVERSATIONAL](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a8a6262c1cf4e4591a7b92b4f8f329f9e)
- [BT_AUDIO_CONTEXT_TYPE_MEDIA](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a43d67936976a5c041027d15d66c21a5e)
- [BT_AUDIO_CONTEXT_TYPE_GAME](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a652ad83b9eb524c62933bf87a8ecb730)
- [BT_AUDIO_CONTEXT_TYPE_INSTRUCTIONAL](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a2e3af6f4ca620f91d9266257f842ddd4)
- [BT_AUDIO_CONTEXT_TYPE_VOICE_ASSISTANTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a7e208290ddc2f92ac78ff4a22b20ca7e)
- [BT_AUDIO_CONTEXT_TYPE_LIVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a42c80228bda513d5a59d4d836e73bd55)
- [BT_AUDIO_CONTEXT_TYPE_SOUND_EFFECTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a6956a9e43433e2800fd36c7022e039d9)
- [BT_AUDIO_CONTEXT_TYPE_NOTIFICATIONS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a06df6f713bb68b197be75bf821d5d377)
- [BT_AUDIO_CONTEXT_TYPE_RINGTONE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a422bb29f035583b7319456a679f880b3)
- [BT_AUDIO_CONTEXT_TYPE_ALERTS](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a915d05a728f3e083f290766a970dabb6)
- [BT_AUDIO_CONTEXT_TYPE_EMERGENCY_ALARM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggafb379ffa88388cc1397960155bbb2ab3a132abd2f9ac7be62d1306efc6bc8b7d1)
- [bt_audio_parental_rating](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga6d4aff1f93dc0b902e4b5d1355f15760)
- [BT_AUDIO_PARENTAL_RATING_NO_RATING](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aecf628bbd76651215232c8bfed04aa2c)
- [BT_AUDIO_PARENTAL_RATING_AGE_ANY](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ad6bba6a3b9537fcf913f798ab9a525f1)
- [BT_AUDIO_PARENTAL_RATING_AGE_5_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a8a8476abac3a569bd470a5237642c526)
- [BT_AUDIO_PARENTAL_RATING_AGE_6_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760accb959ba21c1238c70c594b5cdc3ebdc)
- [BT_AUDIO_PARENTAL_RATING_AGE_7_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a69508e569059bde1fed1b3fb3db1547a)
- [BT_AUDIO_PARENTAL_RATING_AGE_8_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a9ed111f80d0671bb8b4e0a304ff0b0e4)
- [BT_AUDIO_PARENTAL_RATING_AGE_9_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aaabe26ebaa4b84684005440176ad86dd)
- [BT_AUDIO_PARENTAL_RATING_AGE_10_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a4210d67d4506f8b9defb5fae32ae30d2)
- [BT_AUDIO_PARENTAL_RATING_AGE_11_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac402ee4c06b92f0cc36774cf409cbbd0)
- [BT_AUDIO_PARENTAL_RATING_AGE_12_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760ac68caf6719391afbef79e0c579dc96e7)
- [BT_AUDIO_PARENTAL_RATING_AGE_13_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aa680247699538d256111e18af1a2d15d)
- [BT_AUDIO_PARENTAL_RATING_AGE_14_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760aef216d59983eccb86e90c493b8c17d86)
- [BT_AUDIO_PARENTAL_RATING_AGE_15_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a3fe7bc3216a458ec3e5c6e177f43c077)
- [BT_AUDIO_PARENTAL_RATING_AGE_16_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a779c5dd14e5f88e8e6bb247dc66d9c92)
- [BT_AUDIO_PARENTAL_RATING_AGE_17_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a7d0794fe6796f19ff7e58819728751ff)
- [BT_AUDIO_PARENTAL_RATING_AGE_18_OR_ABOVE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga6d4aff1f93dc0b902e4b5d1355f15760a22167e0c033c176f592a447b14c30071)
- [bt_audio_active_state](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga16d403ec4db7be997682331ad365ff5f)
- [BT_AUDIO_ACTIVE_STATE_DISABLED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga16d403ec4db7be997682331ad365ff5fade27604ea8fd592aa5d0958e2ccde4f3)
- [BT_AUDIO_ACTIVE_STATE_ENABLED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga16d403ec4db7be997682331ad365ff5fa6d062944e9c49001666769601ba1c940)
- [bt_audio_assisted_listening_stream](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga207fbf0fbca9b24cba02c7f1d184e7f5)
- [BT_AUDIO_ASSISTED_LISTENING_STREAM_UNSPECIFIED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga207fbf0fbca9b24cba02c7f1d184e7f5ab1714206feaa04b3be586ddb33ed5285)
- [bt_audio_metadata_type](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gab53d0dd62bceff97cf8eed7d8cf80354)
- [BT_AUDIO_METADATA_TYPE_PREF_CONTEXT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354aac28d2a0dc883affa60b7a70f678ed9a)
- [BT_AUDIO_METADATA_TYPE_STREAM_CONTEXT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a95f128b11584ee22100ae65ce751dbaa)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a02f91ea7fb6be631687d843ad7bf4ac7)
- [BT_AUDIO_METADATA_TYPE_LANG](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354af38d342d907c3903121a03bb8394efb1)
- [BT_AUDIO_METADATA_TYPE_CCID_LIST](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a37b5552e04734392dc6c6eb9e19b377b)
- [BT_AUDIO_METADATA_TYPE_PARENTAL_RATING](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a7a83f397dc5dbe6e6d60a994cccdc613)
- [BT_AUDIO_METADATA_TYPE_PROGRAM_INFO_URI](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a58971ea21b5045e56a0e1ca838358922)
- [BT_AUDIO_METADATA_TYPE_AUDIO_STATE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354af220c40d351ec5e236cd41a5944da5fc)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_IMMEDIATE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a4b9cc5b82a1dbfc3db69bb12747443f1)
- [BT_AUDIO_METADATA_TYPE_ASSISTED_LISTENING_STREAM](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a40aad5cb3574e6e4e7bc955bc12760bf)
- [BT_AUDIO_METADATA_TYPE_BROADCAST_NAME](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354ada34d453c8ce75a155c59c371a67d8a6)
- [BT_AUDIO_METADATA_TYPE_EXTENDED](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a0b5a8cd34bad81ac53c657c3cd9ddb39)
- [BT_AUDIO_METADATA_TYPE_VENDOR](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ggab53d0dd62bceff97cf8eed7d8cf80354a30fbc4a159e64174b22f195f29012286)
- [bt_audio_location](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#ga61230848c02098352320fe751332c4e8)
- [BT_AUDIO_LOCATION_MONO_AUDIO](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8f476de613cdcb2f9f677d40291aa5df)
- [BT_AUDIO_LOCATION_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac658188fa6f1b4f248a149d0bde1e41b)
- [BT_AUDIO_LOCATION_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a26d5ba460642bcf7fb2fc950082b70b3)
- [BT_AUDIO_LOCATION_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a06b34e67c9931f8b26562218cba51337)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_1](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac4c09f948266f2c9c65b3bc16da2f3f6)
- [BT_AUDIO_LOCATION_BACK_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a96906ff7918b0a3e3e7efe73a08d9896)
- [BT_AUDIO_LOCATION_BACK_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a43f5070c2b4d39c38fa7900595d9b1aa)
- [BT_AUDIO_LOCATION_FRONT_LEFT_OF_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8af02a9d46877b742e8730bbf3dd6ad22e)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_OF_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a725707ae4703a1f9b970de5b1e4e5692)
- [BT_AUDIO_LOCATION_BACK_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ae22cd1e458d8ff503741bf48262c7983)
- [BT_AUDIO_LOCATION_LOW_FREQ_EFFECTS_2](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a0c304bdd529ad66acb71001caa1b361b)
- [BT_AUDIO_LOCATION_SIDE_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ab8e52c69b894e382f0f09cc370337064)
- [BT_AUDIO_LOCATION_SIDE_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aa01ad94f71defd158d8cfe25936341cd)
- [BT_AUDIO_LOCATION_TOP_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aa093e6218e213eac5677766e01f5c1c9)
- [BT_AUDIO_LOCATION_TOP_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a60b154a216d8e029deac7305500eaf2d)
- [BT_AUDIO_LOCATION_TOP_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac32ed6f456be2fb2d9af2c7b255f3a4e)
- [BT_AUDIO_LOCATION_TOP_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a555361fafade3bfb27dc713666757a1f)
- [BT_AUDIO_LOCATION_TOP_BACK_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a07e699c28bd847de3d85645dceb2ff06)
- [BT_AUDIO_LOCATION_TOP_BACK_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8e81b80f732b0037493712b4baa21a69)
- [BT_AUDIO_LOCATION_TOP_SIDE_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ae846b2f4186b46d3690c71071c41c7d6)
- [BT_AUDIO_LOCATION_TOP_SIDE_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a1cf8dea66e42f75ca85ba55124829a59)
- [BT_AUDIO_LOCATION_TOP_BACK_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8aebae1f0f2537a806672820fb74eba5dd)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_CENTER](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ad0be8f720f03feb18a23e77f0eff6376)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_LEFT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8ac1e355baee6ca0907356d72f0d4edb29)
- [BT_AUDIO_LOCATION_BOTTOM_FRONT_RIGHT](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a33d0f7c266f21fd086386f8c29ee31e8)
- [BT_AUDIO_LOCATION_FRONT_LEFT_WIDE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8acba90183626ad85c21692b7edd87133d)
- [BT_AUDIO_LOCATION_FRONT_RIGHT_WIDE](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a8649be1d5b7e8b312fc3374039cc0a71)
- [BT_AUDIO_LOCATION_LEFT_SURROUND](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a568a581c0ad653177f5d148d04bef0b6)
- [BT_AUDIO_LOCATION_RIGHT_SURROUND](../api_bluetooth_service_control_reference/P001_通用音频分配编号（Generic Audio Assigned Numbers）.md#gga61230848c02098352320fe751332c4e8a97954db823b6c6bed660ff2717600a5e)

<a id="header-details"></a>

---

[返回大纲](大纲.md) · [下一章](P002_zephyr__drivers__i3c__ccc.h_文件参考.md)
