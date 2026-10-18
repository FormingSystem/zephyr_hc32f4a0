---
id: learning.zephyr-docs.api-imaging-input-lwm2m-reference.page-1
title: 核心规范分配编号（Core Specification Assigned Numbers）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_核心规范分配编号（Core Specification Assigned Numbers）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__assigned__numbers__core.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

核心规范分配编号（Core Specification Assigned Numbers）

<a id="details"></a>

核心规范分配编号（Core Specification Assigned Numbers）

<a id="header-member-group"></a>
<a id="member-group"></a>

## 1.1\_外观编号（Appearance Numbers）

最后修改于 2023-01-05（Last Modified）。

<a id="r_gafd1c9ca638a362a01897792e5a00a0c5"></a>

```c
#define BT_APPEARANCE_UNKNOWN 0x0000
```

相关声明：[BT_APPEARANCE_UNKNOWN](#gafd1c9ca638a362a01897792e5a00a0c5)。

通用未知设备（Generic Unknown）。

<a id="r_gae7061e78f960563af6e1b3dea71655a9"></a>

```c
#define BT_APPEARANCE_GENERIC_PHONE 0x0040
```

相关声明：[BT_APPEARANCE_GENERIC_PHONE](#gae7061e78f960563af6e1b3dea71655a9)。

通用电话（Generic Phone）。

<a id="r_ga6b74ad86efc0e9a745f2c9e64079b1cd"></a>

```c
#define BT_APPEARANCE_GENERIC_COMPUTER 0x0080
```

相关声明：[BT_APPEARANCE_GENERIC_COMPUTER](#ga6b74ad86efc0e9a745f2c9e64079b1cd)。

通用计算机（Generic Computer）。

<a id="r_ga1aa0565ca7e00e3a1aa8968e0a7f1bef"></a>

```c
#define BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION 0x0081
```

相关声明：[BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION](#ga1aa0565ca7e00e3a1aa8968e0a7f1bef)。

台式工作站（Desktop Workstation）。

<a id="r_gab71a3c3f836561ac7bd8e52f5e01c769"></a>

```c
#define BT_APPEARANCE_COMPUTER_SERVER_CLASS 0x0082
```

相关声明：[BT_APPEARANCE_COMPUTER_SERVER_CLASS](#gab71a3c3f836561ac7bd8e52f5e01c769)。

服务器级计算机（Server-class Computer）。

<a id="r_ga55ce2ad96a153ed6bdfd841276145c28"></a>

```c
#define BT_APPEARANCE_COMPUTER_LAPTOP 0x0083
```

相关声明：[BT_APPEARANCE_COMPUTER_LAPTOP](#ga55ce2ad96a153ed6bdfd841276145c28)。

笔记本电脑（Laptop）。

<a id="r_gab64312ea16f03c5998db4429b194b8b0"></a>

```c
#define BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA 0x0084
```

相关声明：[BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA](#gab64312ea16f03c5998db4429b194b8b0)。

翻盖式手持电脑／个人数字助理（Handheld PC/PDA (clamshell)）。

<a id="r_ga9340ed60911fc7c5aab7d317b6925c10"></a>

```c
#define BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA 0x0085
```

相关声明：[BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA](#ga9340ed60911fc7c5aab7d317b6925c10)。

掌上电脑／个人数字助理（Palm­size PC/PDA）。

<a id="r_ga7c6667ba4c68dec380a548ba9530c110"></a>

```c
#define BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER 0x0086
```

相关声明：[BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER](#ga7c6667ba4c68dec380a548ba9530c110)。

手表大小的可穿戴计算机（Wearable computer (watch size)）。

<a id="r_ga11bc881cb5f88956edbf2bb2fe5b358c"></a>

```c
#define BT_APPEARANCE_COMPUTER_TABLET 0x0087
```

相关声明：[BT_APPEARANCE_COMPUTER_TABLET](#ga11bc881cb5f88956edbf2bb2fe5b358c)。

平板电脑（Tablet）。

<a id="r_ga36187d2651d08c4b3e17c36565a2d3c9"></a>

```c
#define BT_APPEARANCE_COMPUTER_DOCKING_STATION 0x0088
```

相关声明：[BT_APPEARANCE_COMPUTER_DOCKING_STATION](#ga36187d2651d08c4b3e17c36565a2d3c9)。

扩展坞（Docking Station）。

<a id="r_gaa4d962ad8661c28ed48f5cf8cd75ad6e"></a>

```c
#define BT_APPEARANCE_COMPUTER_ALL_IN_ONE 0x0089
```

相关声明：[BT_APPEARANCE_COMPUTER_ALL_IN_ONE](#gaa4d962ad8661c28ed48f5cf8cd75ad6e)。

一体机（All in One）。

<a id="r_ga53e8eff26f2020b1fc89b21684e54698"></a>

```c
#define BT_APPEARANCE_COMPUTER_BLADE_SERVER 0x008A
```

相关声明：[BT_APPEARANCE_COMPUTER_BLADE_SERVER](#ga53e8eff26f2020b1fc89b21684e54698)。

刀片服务器（Blade Server）。

<a id="r_ga073dca362cabfd2a07cdc1cb787a0f58"></a>

```c
#define BT_APPEARANCE_COMPUTER_CONVERTIBLE 0x008B
```

相关声明：[BT_APPEARANCE_COMPUTER_CONVERTIBLE](#ga073dca362cabfd2a07cdc1cb787a0f58)。

可翻转电脑（Convertible）。

<a id="r_ga8f35f76cc9de4170006669d6e9e7d72a"></a>

```c
#define BT_APPEARANCE_COMPUTER_DETACHABLE 0x008C
```

相关声明：[BT_APPEARANCE_COMPUTER_DETACHABLE](#ga8f35f76cc9de4170006669d6e9e7d72a)。

可拆卸电脑（Detachable）。

<a id="r_ga6ae353795476853bc3be2196ed220aa7"></a>

```c
#define BT_APPEARANCE_COMPUTER_IOT_GATEWAY 0x008D
```

相关声明：[BT_APPEARANCE_COMPUTER_IOT_GATEWAY](#ga6ae353795476853bc3be2196ed220aa7)。

物联网网关（IoT Gateway）。

<a id="r_ga3c47c11f56eabec15e960662c64f6fcb"></a>

```c
#define BT_APPEARANCE_COMPUTER_MINI_PC 0x008E
```

相关声明：[BT_APPEARANCE_COMPUTER_MINI_PC](#ga3c47c11f56eabec15e960662c64f6fcb)。

迷你电脑（Mini PC）。

<a id="r_gabb53daf3eb4ac9ba0cbb1614056ee214"></a>

```c
#define BT_APPEARANCE_COMPUTER_STICK_PC 0x008F
```

相关声明：[BT_APPEARANCE_COMPUTER_STICK_PC](#gabb53daf3eb4ac9ba0cbb1614056ee214)。

棒式电脑（Stick PC）。

<a id="r_ga0c512fd6aa5d35e78f02176073f5f121"></a>

```c
#define BT_APPEARANCE_GENERIC_WATCH 0x00C0
```

相关声明：[BT_APPEARANCE_GENERIC_WATCH](#ga0c512fd6aa5d35e78f02176073f5f121)。

通用手表（Generic Watch）。

<a id="r_gaca9cc93d768145ec3d87b88740954b50"></a>

```c
#define BT_APPEARANCE_SPORTS_WATCH 0x00C1
```

相关声明：[BT_APPEARANCE_SPORTS_WATCH](#gaca9cc93d768145ec3d87b88740954b50)。

运动手表（Sports Watch）。

<a id="r_gaa5662d4a544b034243faa45245a9728b"></a>

```c
#define BT_APPEARANCE_SMARTWATCH 0x00C2
```

相关声明：[BT_APPEARANCE_SMARTWATCH](#gaa5662d4a544b034243faa45245a9728b)。

智能手表（Smartwatch）。

<a id="r_ga100d26d6b9e9a3af925d64c0b006c6bd"></a>

```c
#define BT_APPEARANCE_GENERIC_CLOCK 0x0100
```

相关声明：[BT_APPEARANCE_GENERIC_CLOCK](#ga100d26d6b9e9a3af925d64c0b006c6bd)。

通用时钟（Generic Clock）。

<a id="r_ga0a21cb58861a48875002af38ee82ac08"></a>

```c
#define BT_APPEARANCE_GENERIC_DISPLAY 0x0140
```

相关声明：[BT_APPEARANCE_GENERIC_DISPLAY](#ga0a21cb58861a48875002af38ee82ac08)。

通用显示器（Generic Display）。

<a id="r_ga0b47897768b27d26b8687dd2ab28703b"></a>

```c
#define BT_APPEARANCE_GENERIC_REMOTE 0x0180
```

相关声明：[BT_APPEARANCE_GENERIC_REMOTE](#ga0b47897768b27d26b8687dd2ab28703b)。

通用遥控器（Generic Remote Control）。

<a id="r_gab2b5f6385662519a2ece8fb654a6194b"></a>

```c
#define BT_APPEARANCE_GENERIC_EYEGLASSES 0x01C0
```

相关声明：[BT_APPEARANCE_GENERIC_EYEGLASSES](#gab2b5f6385662519a2ece8fb654a6194b)。

通用眼镜（Generic Eye-glasses）。

<a id="r_gaca6d810977e6da1a3174ee2b6b36662d"></a>

```c
#define BT_APPEARANCE_GENERIC_TAG 0x0200
```

相关声明：[BT_APPEARANCE_GENERIC_TAG](#gaca6d810977e6da1a3174ee2b6b36662d)。

通用标签（Generic Tag）。

<a id="r_gaf73b11c4dbf366a854b4c68e802e3c1c"></a>

```c
#define BT_APPEARANCE_GENERIC_KEYRING 0x0240
```

相关声明：[BT_APPEARANCE_GENERIC_KEYRING](#gaf73b11c4dbf366a854b4c68e802e3c1c)。

通用钥匙圈（Generic Keyring）。

<a id="r_ga17e94209c0c96b5ca039b1613de0d05e"></a>

```c
#define BT_APPEARANCE_GENERIC_MEDIA_PLAYER 0x0280
```

相关声明：[BT_APPEARANCE_GENERIC_MEDIA_PLAYER](#ga17e94209c0c96b5ca039b1613de0d05e)。

通用媒体播放器（Generic Media Player）。

<a id="r_gadca19a01611ca83e18156bb540dd96c1"></a>

```c
#define BT_APPEARANCE_GENERIC_BARCODE_SCANNER 0x02C0
```

相关声明：[BT_APPEARANCE_GENERIC_BARCODE_SCANNER](#gadca19a01611ca83e18156bb540dd96c1)。

通用条码扫描器（Generic Barcode Scanner）。

<a id="r_ga2e0fde88d83e1f4533d69c8dc472255f"></a>

```c
#define BT_APPEARANCE_GENERIC_THERMOMETER 0x0300
```

相关声明：[BT_APPEARANCE_GENERIC_THERMOMETER](#ga2e0fde88d83e1f4533d69c8dc472255f)。

通用温度计（Generic Thermometer）。

<a id="r_ga54283061a207491dcfced899c0fc3008"></a>

```c
#define BT_APPEARANCE_THERMOMETER_EAR 0x0301
```

相关声明：[BT_APPEARANCE_THERMOMETER_EAR](#ga54283061a207491dcfced899c0fc3008)。

耳温计（Ear Thermometer）。

<a id="r_gac5bdf195b81215932848151d765e84d6"></a>

```c
#define BT_APPEARANCE_GENERIC_HEART_RATE 0x0340
```

相关声明：[BT_APPEARANCE_GENERIC_HEART_RATE](#gac5bdf195b81215932848151d765e84d6)。

通用心率传感器（Generic Heart Rate Sensor）。

<a id="r_ga895f6570a09f3eee8d821eca57cdeb03"></a>

```c
#define BT_APPEARANCE_HEART_RATE_BELT 0x0341
```

相关声明：[BT_APPEARANCE_HEART_RATE_BELT](#ga895f6570a09f3eee8d821eca57cdeb03)。

心率带（Heart Rate Belt）。

<a id="r_ga3ab7a9595e00208a9e6a56dca99b56c2"></a>

```c
#define BT_APPEARANCE_GENERIC_BLOOD_PRESSURE 0x0380
```

相关声明：[BT_APPEARANCE_GENERIC_BLOOD_PRESSURE](#ga3ab7a9595e00208a9e6a56dca99b56c2)。

通用血压设备（Generic Blood Pressure）。

<a id="r_ga55c3e67d27c8fd8ae06880ccdd9259ce"></a>

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_ARM 0x0381
```

相关声明：[BT_APPEARANCE_BLOOD_PRESSURE_ARM](#ga55c3e67d27c8fd8ae06880ccdd9259ce)。

臂式血压设备（Arm Blood Pressure）。

<a id="r_ga89684ca0544a400293b663cdf0063cfa"></a>

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_WRIST 0x0382
```

相关声明：[BT_APPEARANCE_BLOOD_PRESSURE_WRIST](#ga89684ca0544a400293b663cdf0063cfa)。

腕式血压设备（Wrist Blood Pressure）。

<a id="r_gaf2050baedf0863ec37177dd2ef872d39"></a>

```c
#define BT_APPEARANCE_GENERIC_HID 0x03C0
```

相关声明：[BT_APPEARANCE_GENERIC_HID](#gaf2050baedf0863ec37177dd2ef872d39)。

通用人机接口设备（Generic Human Interface Device）。

<a id="r_gaa74af272423a80d5489ed8cf6c3ee66c"></a>

```c
#define BT_APPEARANCE_HID_KEYBOARD 0x03C1
```

相关声明：[BT_APPEARANCE_HID_KEYBOARD](#gaa74af272423a80d5489ed8cf6c3ee66c)。

键盘（Keyboard）。

<a id="r_ga3b6ba8ffe424db08583186c448e37149"></a>

```c
#define BT_APPEARANCE_HID_MOUSE 0x03C2
```

相关声明：[BT_APPEARANCE_HID_MOUSE](#ga3b6ba8ffe424db08583186c448e37149)。

鼠标（Mouse）。

<a id="r_ga2f9f15df2260a1307f5142f37437bf0c"></a>

```c
#define BT_APPEARANCE_HID_JOYSTICK 0x03C3
```

相关声明：[BT_APPEARANCE_HID_JOYSTICK](#ga2f9f15df2260a1307f5142f37437bf0c)。

操纵杆（Joystick）。

<a id="r_ga770336524e74d106cb18354f9dbfad76"></a>

```c
#define BT_APPEARANCE_HID_GAMEPAD 0x03C4
```

相关声明：[BT_APPEARANCE_HID_GAMEPAD](#ga770336524e74d106cb18354f9dbfad76)。

游戏手柄（Gamepad）。

<a id="r_gacac11dcb96ab60963a1118e171a731de"></a>

```c
#define BT_APPEARANCE_HID_DIGITIZER_TABLET 0x03C5
```

相关声明：[BT_APPEARANCE_HID_DIGITIZER_TABLET](#gacac11dcb96ab60963a1118e171a731de)。

数字化绘图板（Digitizer Tablet）。

<a id="r_gaa03c3b4d7ea8211748316146afab8bd4"></a>

```c
#define BT_APPEARANCE_HID_CARD_READER 0x03C6
```

相关声明：[BT_APPEARANCE_HID_CARD_READER](#gaa03c3b4d7ea8211748316146afab8bd4)。

读卡器（Card Reader）。

<a id="r_ga002a1d7965b23ec62c8a196f4e5452d9"></a>

```c
#define BT_APPEARANCE_HID_DIGITAL_PEN 0x03C7
```

相关声明：[BT_APPEARANCE_HID_DIGITAL_PEN](#ga002a1d7965b23ec62c8a196f4e5452d9)。

数字笔（Digital Pen）。

<a id="r_gaf88f83afd454fe88dd7146e10ef6d35e"></a>

```c
#define BT_APPEARANCE_HID_BARCODE_SCANNER 0x03C8
```

相关声明：[BT_APPEARANCE_HID_BARCODE_SCANNER](#gaf88f83afd454fe88dd7146e10ef6d35e)。

条码扫描器（Barcode Scanner）。

<a id="r_gaee207f9434bce7d0f7e096bf3b37a01c"></a>

```c
#define BT_APPEARANCE_HID_TOUCHPAD 0x03C9
```

相关声明：[BT_APPEARANCE_HID_TOUCHPAD](#gaee207f9434bce7d0f7e096bf3b37a01c)。

触摸板（Touchpad）。

<a id="r_gae415dd9e8d620dfd1981719f4ed2d796"></a>

```c
#define BT_APPEARANCE_HID_PRESENTATION_REMOTE 0x03CA
```

相关声明：[BT_APPEARANCE_HID_PRESENTATION_REMOTE](#gae415dd9e8d620dfd1981719f4ed2d796)。

演示遥控器（Presentation Remote）。

<a id="r_ga209645f7445873beb50c388cc82aff2a"></a>

```c
#define BT_APPEARANCE_GENERIC_GLUCOSE 0x0400
```

相关声明：[BT_APPEARANCE_GENERIC_GLUCOSE](#ga209645f7445873beb50c388cc82aff2a)。

通用血糖仪（Generic Glucose Meter）。

<a id="r_ga9cf19d97db0c4c5b8473b72809b51d42"></a>

```c
#define BT_APPEARANCE_GENERIC_WALKING 0x0440
```

相关声明：[BT_APPEARANCE_GENERIC_WALKING](#ga9cf19d97db0c4c5b8473b72809b51d42)。

通用跑步／步行传感器（Generic Running Walking Sensor）。

<a id="r_gad748f5dc2e0622353d6159c3a3e4241b"></a>

```c
#define BT_APPEARANCE_WALKING_IN_SHOE 0x0441
```

相关声明：[BT_APPEARANCE_WALKING_IN_SHOE](#gad748f5dc2e0622353d6159c3a3e4241b)。

鞋内跑步／步行传感器（In-Shoe Running Walking Sensor）。

<a id="r_ga0a4541459ba8b41a3938c5b8d35b1c8c"></a>

```c
#define BT_APPEARANCE_WALKING_ON_SHOE 0x0442
```

相关声明：[BT_APPEARANCE_WALKING_ON_SHOE](#ga0a4541459ba8b41a3938c5b8d35b1c8c)。

鞋面跑步／步行传感器（On-Shoe Running Walking Sensor）。

<a id="r_gad211a7e2f11dc7effe3ba28e8c4f7092"></a>

```c
#define BT_APPEARANCE_WALKING_ON_HIP 0x0443
```

相关声明：[BT_APPEARANCE_WALKING_ON_HIP](#gad211a7e2f11dc7effe3ba28e8c4f7092)。

髋部佩戴式跑步／步行传感器（On-Hip Running Walking Sensor）。

<a id="r_ga7a0463b9b0df37bce80cada38b10ee54"></a>

```c
#define BT_APPEARANCE_GENERIC_CYCLING 0x0480
```

相关声明：[BT_APPEARANCE_GENERIC_CYCLING](#ga7a0463b9b0df37bce80cada38b10ee54)。

通用骑行设备（Generic Cycling）。

<a id="r_ga3e81dce23c3d005a9b48ff83c7b8f896"></a>

```c
#define BT_APPEARANCE_CYCLING_COMPUTER 0x0481
```

相关声明：[BT_APPEARANCE_CYCLING_COMPUTER](#ga3e81dce23c3d005a9b48ff83c7b8f896)。

自行车码表（Cycling Computer）。

<a id="r_ga16fb08fa70272252ab6b2d3a5aec485a"></a>

```c
#define BT_APPEARANCE_CYCLING_SPEED 0x0482
```

相关声明：[BT_APPEARANCE_CYCLING_SPEED](#ga16fb08fa70272252ab6b2d3a5aec485a)。

速度传感器（Speed Sensor）。

<a id="r_ga71dc370aad015e88fce7c3e758c647ed"></a>

```c
#define BT_APPEARANCE_CYCLING_CADENCE 0x0483
```

相关声明：[BT_APPEARANCE_CYCLING_CADENCE](#ga71dc370aad015e88fce7c3e758c647ed)。

踏频传感器（Cadence Sensor）。

<a id="r_ga02fd9566d9b932aeaa1163d312fbc4d8"></a>

```c
#define BT_APPEARANCE_CYCLING_POWER 0x0484
```

相关声明：[BT_APPEARANCE_CYCLING_POWER](#ga02fd9566d9b932aeaa1163d312fbc4d8)。

功率传感器（Power Sensor）。

<a id="r_ga48d8f2a285795785f8f51ce220d46371"></a>

```c
#define BT_APPEARANCE_CYCLING_SPEED_CADENCE 0x0485
```

相关声明：[BT_APPEARANCE_CYCLING_SPEED_CADENCE](#ga48d8f2a285795785f8f51ce220d46371)。

速度与踏频传感器（Speed and Cadence Sensor）。

<a id="r_ga5e16df5eefcae8556dfc387135e2b1b6"></a>

```c
#define BT_APPEARANCE_GENERIC_CONTROL_DEVICE 0x04C0
```

相关声明：[BT_APPEARANCE_GENERIC_CONTROL_DEVICE](#ga5e16df5eefcae8556dfc387135e2b1b6)。

通用控制设备（Generic Control Device）。

<a id="r_gac53247d00e3da69595274e0b94fa670f"></a>

```c
#define BT_APPEARANCE_CONTROL_SWITCH 0x04C1
```

相关声明：[BT_APPEARANCE_CONTROL_SWITCH](#gac53247d00e3da69595274e0b94fa670f)。

开关（Switch）。

<a id="r_gad30c40df58e160128893e545a11ab44c"></a>

```c
#define BT_APPEARANCE_CONTROL_MULTI_SWITCH 0x04C2
```

相关声明：[BT_APPEARANCE_CONTROL_MULTI_SWITCH](#gad30c40df58e160128893e545a11ab44c)。

多联开关（Multi-switch）。

<a id="r_ga52dfd2858663b7ab624f0c4b08cee7dc"></a>

```c
#define BT_APPEARANCE_CONTROL_BUTTON 0x04C3
```

相关声明：[BT_APPEARANCE_CONTROL_BUTTON](#ga52dfd2858663b7ab624f0c4b08cee7dc)。

按钮（Button）。

<a id="r_gaa849d890c000defcaf29893296c86cc5"></a>

```c
#define BT_APPEARANCE_CONTROL_SLIDER 0x04C4
```

相关声明：[BT_APPEARANCE_CONTROL_SLIDER](#gaa849d890c000defcaf29893296c86cc5)。

滑块（Slider）。

<a id="r_ga946b6a8bb49bf0b5cd3ded93ee8dfe89"></a>

```c
#define BT_APPEARANCE_CONTROL_ROTARY_SWITCH 0x04C5
```

相关声明：[BT_APPEARANCE_CONTROL_ROTARY_SWITCH](#ga946b6a8bb49bf0b5cd3ded93ee8dfe89)。

旋转开关（Rotary Switch）。

<a id="r_ga4d5763288557e7b7f6da0f3e9831171d"></a>

```c
#define BT_APPEARANCE_CONTROL_TOUCH_PANEL 0x04C6
```

相关声明：[BT_APPEARANCE_CONTROL_TOUCH_PANEL](#ga4d5763288557e7b7f6da0f3e9831171d)。

触摸面板（Touch Panel）。

<a id="r_ga979ca0f4febeaa55daec07e2b3b0179e"></a>

```c
#define BT_APPEARANCE_CONTROL_SINGLE_SWITCH 0x04C7
```

相关声明：[BT_APPEARANCE_CONTROL_SINGLE_SWITCH](#ga979ca0f4febeaa55daec07e2b3b0179e)。

单联开关（Single Switch）。

<a id="r_gac1c80dbb8aaa327b6125bf632692c3be"></a>

```c
#define BT_APPEARANCE_CONTROL_DOUBLE_SWITCH 0x04C8
```

相关声明：[BT_APPEARANCE_CONTROL_DOUBLE_SWITCH](#gac1c80dbb8aaa327b6125bf632692c3be)。

双联开关（Double Switch）。

<a id="r_gaa532fd1bd67c2c5b72822704a62df143"></a>

```c
#define BT_APPEARANCE_CONTROL_TRIPLE_SWITCH 0x04C9
```

相关声明：[BT_APPEARANCE_CONTROL_TRIPLE_SWITCH](#gaa532fd1bd67c2c5b72822704a62df143)。

三联开关（Triple Switch）。

<a id="r_gaea669671a53b3df5b1aa4c43e5bde9b9"></a>

```c
#define BT_APPEARANCE_CONTROL_BATTERY_SWITCH 0x04CA
```

相关声明：[BT_APPEARANCE_CONTROL_BATTERY_SWITCH](#gaea669671a53b3df5b1aa4c43e5bde9b9)。

电池供电开关（Battery Switch）。

<a id="r_gadec2907a822e302d5027f162ef9ce4b6"></a>

```c
#define BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH 0x04CB
```

相关声明：[BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH](#gadec2907a822e302d5027f162ef9ce4b6)。

能量采集开关（Energy Harvesting Switch）。

<a id="r_ga9bb358864e1388cc00502b5586ec581f"></a>

```c
#define BT_APPEARANCE_CONTROL_PUSH_BUTTON 0x04CC
```

相关声明：[BT_APPEARANCE_CONTROL_PUSH_BUTTON](#ga9bb358864e1388cc00502b5586ec581f)。

按压按钮（Push Button）。

<a id="r_gac4727ec720344ece687256ac517800e7"></a>

```c
#define BT_APPEARANCE_GENERIC_NETWORK_DEVICE 0x0500
```

相关声明：[BT_APPEARANCE_GENERIC_NETWORK_DEVICE](#gac4727ec720344ece687256ac517800e7)。

通用网络设备（Generic Network Device）。

<a id="r_ga265ba959769d56f42ff621a20e193aba"></a>

```c
#define BT_APPEARANCE_NETWORK_ACCESS_POINT 0x0501
```

相关声明：[BT_APPEARANCE_NETWORK_ACCESS_POINT](#ga265ba959769d56f42ff621a20e193aba)。

接入点（Access Point）。

<a id="r_gadcc3d795579a731ae03ade14d5193408"></a>

```c
#define BT_APPEARANCE_NETWORK_MESH_DEVICE 0x0502
```

相关声明：[BT_APPEARANCE_NETWORK_MESH_DEVICE](#gadcc3d795579a731ae03ade14d5193408)。

网状网络设备（Mesh Device）。

<a id="r_gad4c5f5840a8caba73d55b0138e506bd0"></a>

```c
#define BT_APPEARANCE_NETWORK_MESH_PROXY 0x0503
```

相关声明：[BT_APPEARANCE_NETWORK_MESH_PROXY](#gad4c5f5840a8caba73d55b0138e506bd0)。

网状网络代理（Mesh Network Proxy）。

<a id="r_gab3241fe012482e716c3f18e2962ca15d"></a>

```c
#define BT_APPEARANCE_GENERIC_SENSOR 0x0540
```

相关声明：[BT_APPEARANCE_GENERIC_SENSOR](#gab3241fe012482e716c3f18e2962ca15d)。

通用传感器（Generic Sensor）。

<a id="r_gab49b84183136e9b65ba2e1f5490a79ed"></a>

```c
#define BT_APPEARANCE_SENSOR_MOTION 0x0541
```

相关声明：[BT_APPEARANCE_SENSOR_MOTION](#gab49b84183136e9b65ba2e1f5490a79ed)。

运动传感器（Motion Sensor）。

<a id="r_gaacb0779499ad4aaa83f0b6303460caf8"></a>

```c
#define BT_APPEARANCE_SENSOR_AIR_QUALITY 0x0542
```

相关声明：[BT_APPEARANCE_SENSOR_AIR_QUALITY](#gaacb0779499ad4aaa83f0b6303460caf8)。

空气质量传感器（Air quality Sensor）。

<a id="r_ga5e072a902bf145dc2b00dbd1c8a64b52"></a>

```c
#define BT_APPEARANCE_SENSOR_TEMPERATURE 0x0543
```

相关声明：[BT_APPEARANCE_SENSOR_TEMPERATURE](#ga5e072a902bf145dc2b00dbd1c8a64b52)。

温度传感器（Temperature Sensor）。

<a id="r_ga2deff206602e1e0784af9456ef8abd5b"></a>

```c
#define BT_APPEARANCE_SENSOR_HUMIDITY 0x0544
```

相关声明：[BT_APPEARANCE_SENSOR_HUMIDITY](#ga2deff206602e1e0784af9456ef8abd5b)。

湿度传感器（Humidity Sensor）。

<a id="r_ga2cbac5e931080f1f5cb3c9bb4c73e9d8"></a>

```c
#define BT_APPEARANCE_SENSOR_LEAK 0x0545
```

相关声明：[BT_APPEARANCE_SENSOR_LEAK](#ga2cbac5e931080f1f5cb3c9bb4c73e9d8)。

泄漏传感器（Leak Sensor）。

<a id="r_gaeedc0612f8ca171aec061cf02ee907e4"></a>

```c
#define BT_APPEARANCE_SENSOR_SMOKE 0x0546
```

相关声明：[BT_APPEARANCE_SENSOR_SMOKE](#gaeedc0612f8ca171aec061cf02ee907e4)。

烟雾传感器（Smoke Sensor）。

<a id="r_ga8e8b7834c82c42a0076300aca20c2d35"></a>

```c
#define BT_APPEARANCE_SENSOR_OCCUPANCY 0x0547
```

相关声明：[BT_APPEARANCE_SENSOR_OCCUPANCY](#ga8e8b7834c82c42a0076300aca20c2d35)。

占用传感器（Occupancy Sensor）。

<a id="r_gac71e281cf1b8d1b6535623ec34c7d63f"></a>

```c
#define BT_APPEARANCE_SENSOR_CONTACT 0x0548
```

相关声明：[BT_APPEARANCE_SENSOR_CONTACT](#gac71e281cf1b8d1b6535623ec34c7d63f)。

接触传感器（Contact Sensor）。

<a id="r_ga0e60b365f871c17c0015ffcf8bc1646e"></a>

```c
#define BT_APPEARANCE_SENSOR_CARBON_MONOXIDE 0x0549
```

相关声明：[BT_APPEARANCE_SENSOR_CARBON_MONOXIDE](#ga0e60b365f871c17c0015ffcf8bc1646e)。

一氧化碳传感器（Carbon Monoxide Sensor）。

<a id="r_ga34ed8c9aefe34d5030209f073c9ecd24"></a>

```c
#define BT_APPEARANCE_SENSOR_CARBON_DIOXIDE 0x054A
```

相关声明：[BT_APPEARANCE_SENSOR_CARBON_DIOXIDE](#ga34ed8c9aefe34d5030209f073c9ecd24)。

二氧化碳传感器（Carbon Dioxide Sensor）。

<a id="r_ga622508f9b051ed0320700b01967f6446"></a>

```c
#define BT_APPEARANCE_SENSOR_AMBIENT_LIGHT 0x054B
```

相关声明：[BT_APPEARANCE_SENSOR_AMBIENT_LIGHT](#ga622508f9b051ed0320700b01967f6446)。

环境光传感器（Ambient Light Sensor）。

<a id="r_gaca0cfcd560fa4133c0bc62a61d2874c7"></a>

```c
#define BT_APPEARANCE_SENSOR_ENERGY 0x054C
```

相关声明：[BT_APPEARANCE_SENSOR_ENERGY](#gaca0cfcd560fa4133c0bc62a61d2874c7)。

能量传感器（Energy Sensor）。

<a id="r_ga8106142ddb6445e7462137e032e50854"></a>

```c
#define BT_APPEARANCE_SENSOR_COLOR_LIGHT 0x054D
```

相关声明：[BT_APPEARANCE_SENSOR_COLOR_LIGHT](#ga8106142ddb6445e7462137e032e50854)。

彩色光传感器（Color Light Sensor）。

<a id="r_ga380da83e3a69de3fd5091cdc89f7fcbc"></a>

```c
#define BT_APPEARANCE_SENSOR_RAIN 0x054E
```

相关声明：[BT_APPEARANCE_SENSOR_RAIN](#ga380da83e3a69de3fd5091cdc89f7fcbc)。

雨量传感器（Rain Sensor）。

<a id="r_ga425115e6c251a9c493c98d79f659077d"></a>

```c
#define BT_APPEARANCE_SENSOR_FIRE 0x054F
```

相关声明：[BT_APPEARANCE_SENSOR_FIRE](#ga425115e6c251a9c493c98d79f659077d)。

火灾传感器（Fire Sensor）。

<a id="r_gaa710c0666d8b5bf1e1230672cbbf55fa"></a>

```c
#define BT_APPEARANCE_SENSOR_WIND 0x0550
```

相关声明：[BT_APPEARANCE_SENSOR_WIND](#gaa710c0666d8b5bf1e1230672cbbf55fa)。

风传感器（Wind Sensor）。

<a id="r_ga6d3447e24d5d75051b81998fd9ad8bfe"></a>

```c
#define BT_APPEARANCE_SENSOR_PROXIMITY 0x0551
```

相关声明：[BT_APPEARANCE_SENSOR_PROXIMITY](#ga6d3447e24d5d75051b81998fd9ad8bfe)。

接近传感器（Proximity Sensor）。

<a id="r_gaeec9666dbdb31e9302a25aaa536f3180"></a>

```c
#define BT_APPEARANCE_SENSOR_MULTI 0x0552
```

相关声明：[BT_APPEARANCE_SENSOR_MULTI](#gaeec9666dbdb31e9302a25aaa536f3180)。

多传感器（Multi-Sensor）。

<a id="r_gaf9a9c0191ec175d14061058cf3da163c"></a>

```c
#define BT_APPEARANCE_SENSOR_FLUSH_MOUNTED 0x0553
```

相关声明：[BT_APPEARANCE_SENSOR_FLUSH_MOUNTED](#gaf9a9c0191ec175d14061058cf3da163c)。

嵌入安装式传感器（Flush Mounted Sensor）。

<a id="r_gadfb6808db5a7060316b724c24c8ceaf8"></a>

```c
#define BT_APPEARANCE_SENSOR_CEILING_MOUNTED 0x0554
```

相关声明：[BT_APPEARANCE_SENSOR_CEILING_MOUNTED](#gadfb6808db5a7060316b724c24c8ceaf8)。

吸顶安装式传感器（Ceiling Mounted Sensor）。

<a id="r_gae564900f0517d393ceffcca8d27f6e45"></a>

```c
#define BT_APPEARANCE_SENSOR_WALL_MOUNTED 0x0555
```

相关声明：[BT_APPEARANCE_SENSOR_WALL_MOUNTED](#gae564900f0517d393ceffcca8d27f6e45)。

壁挂安装式传感器（Wall Mounted Sensor）。

<a id="r_ga90237753920702380321e9f858344741"></a>

```c
#define BT_APPEARANCE_MULTISENSOR 0x0556
```

相关声明：[BT_APPEARANCE_MULTISENSOR](#ga90237753920702380321e9f858344741)。

多传感器（Multisensor）。

<a id="r_ga7238d3a45f9e62f0189db9d7eeac4d15"></a>

```c
#define BT_APPEARANCE_SENSOR_ENERGY_METER 0x0557
```

相关声明：[BT_APPEARANCE_SENSOR_ENERGY_METER](#ga7238d3a45f9e62f0189db9d7eeac4d15)。

能量计（Energy Meter）。

<a id="r_gaae8f95ef639cb7d5e97063eed710a07d"></a>

```c
#define BT_APPEARANCE_SENSOR_FLAME_DETECTOR 0x0558
```

相关声明：[BT_APPEARANCE_SENSOR_FLAME_DETECTOR](#gaae8f95ef639cb7d5e97063eed710a07d)。

火焰探测器（Flame Detector）。

<a id="r_ga4d0877a3cd9b7efebbaa5fd8a988a2a3"></a>

```c
#define BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE 0x0559
```

相关声明：[BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE](#ga4d0877a3cd9b7efebbaa5fd8a988a2a3)。

车辆胎压传感器（Vehicle Tire Pressure Sensor）。

<a id="r_gae01be867f730c06b59fcb03289ae66d7"></a>

```c
#define BT_APPEARANCE_GENERIC_LIGHT_FIXTURES 0x0580
```

相关声明：[BT_APPEARANCE_GENERIC_LIGHT_FIXTURES](#gae01be867f730c06b59fcb03289ae66d7)。

通用照明灯具（Generic Light Fixtures）。

<a id="r_gae1b2b535754f9cdc24c4a6cee63ef5cb"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_WALL 0x0581
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_WALL](#gae1b2b535754f9cdc24c4a6cee63ef5cb)。

壁灯（Wall Light）。

<a id="r_ga2d77fb5f5ed9a43771186ecc5693da8f"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CEILING 0x0582
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CEILING](#ga2d77fb5f5ed9a43771186ecc5693da8f)。

吸顶灯（Ceiling Light）。

<a id="r_ga57bb461b0ddd045d21d7fbd3843fbabb"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOR 0x0583
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_FLOOR](#ga57bb461b0ddd045d21d7fbd3843fbabb)。

落地灯（Floor Light）。

<a id="r_gadc48840b6590a89593a5d17fbdb1e9e9"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CABINET 0x0584
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CABINET](#gadc48840b6590a89593a5d17fbdb1e9e9)。

橱柜灯（Cabinet Light）。

<a id="r_ga2f37bf95ea6057b999bbf2cf94016e5d"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DESK 0x0585
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_DESK](#ga2f37bf95ea6057b999bbf2cf94016e5d)。

桌灯（Desk Light）。

<a id="r_gaa57b538ecad380ad77354e0cd9576e5b"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_TROFFER 0x0586
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_TROFFER](#gaa57b538ecad380ad77354e0cd9576e5b)。

嵌入式格栅灯（Troffer Light）。

<a id="r_ga336147b54406237e25d8cf9ed152928b"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PENDANT 0x0587
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_PENDANT](#ga336147b54406237e25d8cf9ed152928b)。

吊灯（Pendant Light）。

<a id="r_ga583b7432ba6ac4cc078d3a069e3a54e1"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND 0x0588
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND](#ga583b7432ba6ac4cc078d3a069e3a54e1)。

地埋灯（In-ground Light）。

<a id="r_gab41f8b6f1ff0f624bb6666ef2ac6dab3"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOD 0x0589
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_FLOOD](#gab41f8b6f1ff0f624bb6666ef2ac6dab3)。

泛光灯（Flood Light）。

<a id="r_ga83f50305a23250e5e2cef5004762e122"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER 0x058A
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER](#ga83f50305a23250e5e2cef5004762e122)。

水下灯（Underwater Light）。

<a id="r_ga20a7b241f292475d70626a38d983886c"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH 0x058B
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH](#ga20a7b241f292475d70626a38d983886c)。

带灯柱桩（Bollard with Light）。

<a id="r_ga7c5811bd50d9f78e67e3e56faa432aae"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY 0x058C
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY](#ga7c5811bd50d9f78e67e3e56faa432aae)。

步道灯（Pathway Light）。

<a id="r_ga348e64ffe0f3d6301dd8c911f70ead68"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_GARDEN 0x058D
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_GARDEN](#ga348e64ffe0f3d6301dd8c911f70ead68)。

庭院灯（Garden Light）。

<a id="r_ga0da0cbeebd2b20bf28dfc06def016068"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP 0x058E
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP](#ga0da0cbeebd2b20bf28dfc06def016068)。

杆顶灯（Pole-top Light）。

<a id="r_ga58e1989c99b5a223a318a716d62f6e2b"></a>

```c
#define BT_APPEARANCE_SPOT_LIGHT 0x058F
```

相关声明：[BT_APPEARANCE_SPOT_LIGHT](#ga58e1989c99b5a223a318a716d62f6e2b)。

聚光灯（Spotlight）。

<a id="r_ga5388daf123e629d6f7a0b9af13fbc366"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LINEAR 0x0590
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_LINEAR](#ga5388daf123e629d6f7a0b9af13fbc366)。

线性灯（Linear Light）。

<a id="r_gac938fb03553d2d3c27b50af2a9a1ac48"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_STREET 0x0591
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_STREET](#gac938fb03553d2d3c27b50af2a9a1ac48)。

路灯（Street Light）。

<a id="r_ga1bf2889f7a8a7ae363bc1d4355ee8d65"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_SHELVES 0x0592
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_SHELVES](#ga1bf2889f7a8a7ae363bc1d4355ee8d65)。

货架灯（Shelves Light）。

<a id="r_ga8f98c2d32664a6e03ebc2a43ae1eb52a"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BAY 0x0593
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BAY](#ga8f98c2d32664a6e03ebc2a43ae1eb52a)。

工矿灯（Bay Light）。

<a id="r_ga3f687f994ffff2ce70b81a992195d210"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT 0x0594
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT](#ga3f687f994ffff2ce70b81a992195d210)。

紧急出口灯（Emergency Exit Light）。

<a id="r_ga35a90a4e3bfef7b0cfec0d5fa7b36c4a"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER 0x0595
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER](#ga35a90a4e3bfef7b0cfec0d5fa7b36c4a)。

照明控制器（Light Controller）。

<a id="r_gac2b6de99b4e87f7c40063ba844c75ead"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DRIVER 0x0596
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_DRIVER](#gac2b6de99b4e87f7c40063ba844c75ead)。

灯具驱动器（Light Driver）。

<a id="r_ga8325830f2c977dc238a9ca1b9837803e"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BULB 0x0597
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_BULB](#ga8325830f2c977dc238a9ca1b9837803e)。

灯泡（Bulb）。

<a id="r_gafc924bbc1b6aff0130c2be3d5fe59e33"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY 0x0598
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY](#gafc924bbc1b6aff0130c2be3d5fe59e33)。

低棚灯（Low-bay Light）。

<a id="r_ga738e87008c6a64450bb7ec22dbcdd113"></a>

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY 0x0599
```

相关声明：[BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY](#ga738e87008c6a64450bb7ec22dbcdd113)。

高棚灯（High-bay Light）。

<a id="r_ga82cc89321c4f4ffbf3ef25eff624943c"></a>

```c
#define BT_APPEARANCE_GENERIC_FAN 0x05C0
```

相关声明：[BT_APPEARANCE_GENERIC_FAN](#ga82cc89321c4f4ffbf3ef25eff624943c)。

通用风扇（Generic Fan）。

<a id="r_ga8cd83cd08846ac276cc65f31333ee62e"></a>

```c
#define BT_APPEARANCE_FAN_CEILING 0x05C1
```

相关声明：[BT_APPEARANCE_FAN_CEILING](#ga8cd83cd08846ac276cc65f31333ee62e)。

吊扇（Ceiling Fan）。

<a id="r_ga32dd73ffa211d632617018aa510b89c4"></a>

```c
#define BT_APPEARANCE_FAN_AXIAL 0x05C2
```

相关声明：[BT_APPEARANCE_FAN_AXIAL](#ga32dd73ffa211d632617018aa510b89c4)。

轴流风扇（Axial Fan）。

<a id="r_ga1e842c97b90678908f4d18c86c1227c2"></a>

```c
#define BT_APPEARANCE_FAN_EXHAUST 0x05C3
```

相关声明：[BT_APPEARANCE_FAN_EXHAUST](#ga1e842c97b90678908f4d18c86c1227c2)。

排气扇（Exhaust Fan）。

<a id="r_ga2e54f8de862435f2dbd7f56b98615c84"></a>

```c
#define BT_APPEARANCE_FAN_PEDESTAL 0x05C4
```

相关声明：[BT_APPEARANCE_FAN_PEDESTAL](#ga2e54f8de862435f2dbd7f56b98615c84)。

落地风扇（Pedestal Fan）。

<a id="r_gaa9e17b8b5e06d2fb365bf152e0cbef5d"></a>

```c
#define BT_APPEARANCE_FAN_DESK 0x05C5
```

相关声明：[BT_APPEARANCE_FAN_DESK](#gaa9e17b8b5e06d2fb365bf152e0cbef5d)。

桌面风扇（Desk Fan）。

<a id="r_ga498be79799cb778c9df6629411fe32ad"></a>

```c
#define BT_APPEARANCE_FAN_WALL 0x05C6
```

相关声明：[BT_APPEARANCE_FAN_WALL](#ga498be79799cb778c9df6629411fe32ad)。

壁扇（Wall Fan）。

<a id="r_gaf1f01946f6acadcaf719d3d7cc06e55f"></a>

```c
#define BT_APPEARANCE_GENERIC_HVAC 0x0600
```

相关声明：[BT_APPEARANCE_GENERIC_HVAC](#gaf1f01946f6acadcaf719d3d7cc06e55f)。

通用暖通空调设备（Generic HVAC）。

<a id="r_ga33055b50c10bfc713b18823fca525488"></a>

```c
#define BT_APPEARANCE_HVAC_THERMOSTAT 0x0601
```

相关声明：[BT_APPEARANCE_HVAC_THERMOSTAT](#ga33055b50c10bfc713b18823fca525488)。

恒温器（Thermostat）。

<a id="r_gaf55f3f3f07cc78509e7fe19cea6cea4e"></a>

```c
#define BT_APPEARANCE_HVAC_HUMIDIFIER 0x0602
```

相关声明：[BT_APPEARANCE_HVAC_HUMIDIFIER](#gaf55f3f3f07cc78509e7fe19cea6cea4e)。

加湿器（Humidifier）。

<a id="r_gaa3b96e44638048b8891a2dece29f4b3f"></a>

```c
#define BT_APPEARANCE_HVAC_DEHUMIDIFIER 0x0603
```

相关声明：[BT_APPEARANCE_HVAC_DEHUMIDIFIER](#gaa3b96e44638048b8891a2dece29f4b3f)。

除湿机（De-humidifier）。

<a id="r_gacef9145f435d10cbf5a775b9a2c9b756"></a>

```c
#define BT_APPEARANCE_HVAC_HEATER 0x0604
```

相关声明：[BT_APPEARANCE_HVAC_HEATER](#gacef9145f435d10cbf5a775b9a2c9b756)。

加热器（Heater）。

<a id="r_gad90f108f3d33d68e27ac545cdb520f18"></a>

```c
#define BT_APPEARANCE_HVAC_RADIATOR 0x0605
```

相关声明：[BT_APPEARANCE_HVAC_RADIATOR](#gad90f108f3d33d68e27ac545cdb520f18)。

散热暖气片（Radiator）。

<a id="r_gacc28a1bc1a809c574019455de4ac9d0b"></a>

```c
#define BT_APPEARANCE_HVAC_BOILER 0x0606
```

相关声明：[BT_APPEARANCE_HVAC_BOILER](#gacc28a1bc1a809c574019455de4ac9d0b)。

锅炉（Boiler）。

<a id="r_gaead4ebeabb8855111ab9080aca4e035a"></a>

```c
#define BT_APPEARANCE_HVAC_HEAT_PUMP 0x0607
```

相关声明：[BT_APPEARANCE_HVAC_HEAT_PUMP](#gaead4ebeabb8855111ab9080aca4e035a)。

热泵（Heat Pump）。

<a id="r_ga50c5df52d8471fc8e1dc65e31079566d"></a>

```c
#define BT_APPEARANCE_HVAC_INFRARED_HEATER 0x0608
```

相关声明：[BT_APPEARANCE_HVAC_INFRARED_HEATER](#ga50c5df52d8471fc8e1dc65e31079566d)。

红外加热器（Infrared Heater）。

<a id="r_gad43d27ff96a7fba1ed7d5e20ebd472d9"></a>

```c
#define BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER 0x0609
```

相关声明：[BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER](#gad43d27ff96a7fba1ed7d5e20ebd472d9)。

辐射板式加热器（Radiant Panel Heater）。

<a id="r_ga2a044c3369ed48d216707f6e6a541a23"></a>

```c
#define BT_APPEARANCE_HVAC_FAN_HEATER 0x060A
```

相关声明：[BT_APPEARANCE_HVAC_FAN_HEATER](#ga2a044c3369ed48d216707f6e6a541a23)。

暖风机（Fan Heater）。

<a id="r_ga182ade4b2c8f4705ba132248e504bb95"></a>

```c
#define BT_APPEARANCE_HVAC_AIR_CURTAIN 0x060B
```

相关声明：[BT_APPEARANCE_HVAC_AIR_CURTAIN](#ga182ade4b2c8f4705ba132248e504bb95)。

空气幕（Air Curtain）。

<a id="r_gaa13ae6496d47df2be0a0692a28806007"></a>

```c
#define BT_APPEARANCE_GENERIC_AIR_CONDITIONING 0x0640
```

相关声明：[BT_APPEARANCE_GENERIC_AIR_CONDITIONING](#gaa13ae6496d47df2be0a0692a28806007)。

通用空调设备（Generic Air Conditioning）。

<a id="r_ga0b552243744bc598467421555e935cd0"></a>

```c
#define BT_APPEARANCE_GENERIC_HUMIDIFIER 0x0680
```

相关声明：[BT_APPEARANCE_GENERIC_HUMIDIFIER](#ga0b552243744bc598467421555e935cd0)。

通用加湿器（Generic Humidifier）。

<a id="r_ga8ea92ea92ca4e2bad4e5e2baba1271dd"></a>

```c
#define BT_APPEARANCE_GENERIC_HEATING 0x06C0
```

相关声明：[BT_APPEARANCE_GENERIC_HEATING](#ga8ea92ea92ca4e2bad4e5e2baba1271dd)。

通用供暖设备（Generic Heating）。

<a id="r_ga05b0b91c74aed5bc73a92f336bdae33a"></a>

```c
#define BT_APPEARANCE_HEATING_RADIATOR 0x06C1
```

相关声明：[BT_APPEARANCE_HEATING_RADIATOR](#ga05b0b91c74aed5bc73a92f336bdae33a)。

散热暖气片（Radiator）。

<a id="r_gac1abc9ae0b8ede2197720ea9e67b692e"></a>

```c
#define BT_APPEARANCE_HEATING_BOILER 0x06C2
```

相关声明：[BT_APPEARANCE_HEATING_BOILER](#gac1abc9ae0b8ede2197720ea9e67b692e)。

锅炉（Boiler）。

<a id="r_ga99537968fdc7e680d922ca309fba7678"></a>

```c
#define BT_APPEARANCE_HEATING_HEAT_PUMP 0x06C3
```

相关声明：[BT_APPEARANCE_HEATING_HEAT_PUMP](#ga99537968fdc7e680d922ca309fba7678)。

热泵（Heat Pump）。

<a id="r_ga8e40496a351c7ec5ea836805925f1e13"></a>

```c
#define BT_APPEARANCE_HEATING_INFRARED_HEATER 0x06C4
```

相关声明：[BT_APPEARANCE_HEATING_INFRARED_HEATER](#ga8e40496a351c7ec5ea836805925f1e13)。

红外加热器（Infrared Heater）。

<a id="r_ga46fe051c7e50492dba5ae824e154cf69"></a>

```c
#define BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER 0x06C5
```

相关声明：[BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER](#ga46fe051c7e50492dba5ae824e154cf69)。

辐射板式加热器（Radiant Panel Heater）。

<a id="r_ga995ca18db114ea062df0d76c9e241937"></a>

```c
#define BT_APPEARANCE_HEATING_FAN_HEATER 0x06C6
```

相关声明：[BT_APPEARANCE_HEATING_FAN_HEATER](#ga995ca18db114ea062df0d76c9e241937)。

暖风机（Fan Heater）。

<a id="r_gac74bc8e109f5d9b4c0988ee6378ed471"></a>

```c
#define BT_APPEARANCE_HEATING_AIR_CURTAIN 0x06C7
```

相关声明：[BT_APPEARANCE_HEATING_AIR_CURTAIN](#gac74bc8e109f5d9b4c0988ee6378ed471)。

空气幕（Air Curtain）。

<a id="r_gac856a99a5db04dc20229a6e60a18d310"></a>

```c
#define BT_APPEARANCE_GENERIC_ACCESS_CONTROL 0x0700
```

相关声明：[BT_APPEARANCE_GENERIC_ACCESS_CONTROL](#gac856a99a5db04dc20229a6e60a18d310)。

通用门禁控制设备（Generic Access Control）。

<a id="r_ga8e21f7df9d789b7c3aa6f7dab500df8c"></a>

```c
#define BT_APPEARANCE_CONTROL_ACCESS_DOOR 0x0701
```

相关声明：[BT_APPEARANCE_CONTROL_ACCESS_DOOR](#ga8e21f7df9d789b7c3aa6f7dab500df8c)。

出入门（Access Door）。

<a id="r_ga39134568b56c1d33e6567c893eb441f1"></a>

```c
#define BT_APPEARANCE_CONTROL_GARAGE_DOOR 0x0702
```

相关声明：[BT_APPEARANCE_CONTROL_GARAGE_DOOR](#ga39134568b56c1d33e6567c893eb441f1)。

车库门（Garage Door）。

<a id="r_ga2b6c7987ee4040216a385e665ff92321"></a>

```c
#define BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR 0x0703
```

相关声明：[BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR](#ga2b6c7987ee4040216a385e665ff92321)。

紧急出口门（Emergency Exit Door）。

<a id="r_gac2f588b6202e9d6140ec682cfe45f65d"></a>

```c
#define BT_APPEARANCE_CONTROL_ACCESS_LOCK 0x0704
```

相关声明：[BT_APPEARANCE_CONTROL_ACCESS_LOCK](#gac2f588b6202e9d6140ec682cfe45f65d)。

门禁锁（Access Lock）。

<a id="r_ga321d63ead349c0a83ef289bd2e4efb33"></a>

```c
#define BT_APPEARANCE_CONTROL_ELEVATOR 0x0705
```

相关声明：[BT_APPEARANCE_CONTROL_ELEVATOR](#ga321d63ead349c0a83ef289bd2e4efb33)。

电梯（Elevator）。

<a id="r_gaedc6415432862889e7f002fc9ef46b74"></a>

```c
#define BT_APPEARANCE_CONTROL_WINDOW 0x0706
```

相关声明：[BT_APPEARANCE_CONTROL_WINDOW](#gaedc6415432862889e7f002fc9ef46b74)。

窗户（Window）。

<a id="r_gab2a476a90f20576c0a1784fdc1e5e633"></a>

```c
#define BT_APPEARANCE_CONTROL_ENTRANCE_GATE 0x0707
```

相关声明：[BT_APPEARANCE_CONTROL_ENTRANCE_GATE](#gab2a476a90f20576c0a1784fdc1e5e633)。

入口大门（Entrance Gate）。

<a id="r_ga29d07ce1101740b5f6f980660e405278"></a>

```c
#define BT_APPEARANCE_CONTROL_DOOR_LOCK 0x0708
```

相关声明：[BT_APPEARANCE_CONTROL_DOOR_LOCK](#ga29d07ce1101740b5f6f980660e405278)。

门锁（Door Lock）。

<a id="r_ga824236ba19c7f54d06b9abcd7df8c767"></a>

```c
#define BT_APPEARANCE_CONTROL_LOCKER 0x0709
```

相关声明：[BT_APPEARANCE_CONTROL_LOCKER](#ga824236ba19c7f54d06b9abcd7df8c767)。

储物柜（Locker）。

<a id="r_ga414b202e93d1db533853093d66603720"></a>

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE 0x0740
```

相关声明：[BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE](#ga414b202e93d1db533853093d66603720)。

通用电动设备（Generic Motorized Device）。

<a id="r_ga376ef909868a5c273b71d1c372755707"></a>

```c
#define BT_APPEARANCE_MOTORIZED_GATE 0x0741
```

相关声明：[BT_APPEARANCE_MOTORIZED_GATE](#ga376ef909868a5c273b71d1c372755707)。

电动大门（Motorized Gate）。

<a id="r_ga338de5523abf3fd81e913f3cdb4a31b6"></a>

```c
#define BT_APPEARANCE_MOTORIZED_AWNING 0x0742
```

相关声明：[BT_APPEARANCE_MOTORIZED_AWNING](#ga338de5523abf3fd81e913f3cdb4a31b6)。

遮阳篷（Awning）。

<a id="r_gaaa39c48ed2d6edd5650743b82154462b"></a>

```c
#define BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES 0x0743
```

相关声明：[BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES](#gaaa39c48ed2d6edd5650743b82154462b)。

百叶帘或遮阳帘（Blinds or Shades）。

<a id="r_ga53f6a4df5ccc2117525952be2e174ddc"></a>

```c
#define BT_APPEARANCE_MOTORIZED_CURTAINS 0x0744
```

相关声明：[BT_APPEARANCE_MOTORIZED_CURTAINS](#ga53f6a4df5ccc2117525952be2e174ddc)。

窗帘（Curtains）。

<a id="r_ga5f32cab5c7a155fffbe0c33cadfef31a"></a>

```c
#define BT_APPEARANCE_MOTORIZED_SCREEN 0x0745
```

相关声明：[BT_APPEARANCE_MOTORIZED_SCREEN](#ga5f32cab5c7a155fffbe0c33cadfef31a)。

屏障（Screen）。

<a id="r_gadae82e45d9aafd34cafd3f0e793b1b24"></a>

```c
#define BT_APPEARANCE_GENERIC_POWER_DEVICE 0x0780
```

相关声明：[BT_APPEARANCE_GENERIC_POWER_DEVICE](#gadae82e45d9aafd34cafd3f0e793b1b24)。

通用电源设备（Generic Power Device）。

<a id="r_gad9efd19e2c95525a3972c8b0f0417449"></a>

```c
#define BT_APPEARANCE_POWER_OUTLET 0x0781
```

相关声明：[BT_APPEARANCE_POWER_OUTLET](#gad9efd19e2c95525a3972c8b0f0417449)。

电源插座（Power Outlet）。

<a id="r_ga2c5bd38d4eeb1aad2d29b004390a6d18"></a>

```c
#define BT_APPEARANCE_POWER_STRIP 0x0782
```

相关声明：[BT_APPEARANCE_POWER_STRIP](#ga2c5bd38d4eeb1aad2d29b004390a6d18)。

电源插排（Power Strip）。

<a id="r_ga0d9aadc19f5f5f484769b225164866e4"></a>

```c
#define BT_APPEARANCE_POWER_PLUG 0x0783
```

相关声明：[BT_APPEARANCE_POWER_PLUG](#ga0d9aadc19f5f5f484769b225164866e4)。

插头（Plug）。

<a id="r_ga07acce808c9cf2b5e84aacd65e8f256d"></a>

```c
#define BT_APPEARANCE_POWER_SUPPLY 0x0784
```

相关声明：[BT_APPEARANCE_POWER_SUPPLY](#ga07acce808c9cf2b5e84aacd65e8f256d)。

电源（Power Supply）。

<a id="r_ga31842298741c822dcebba942453975c6"></a>

```c
#define BT_APPEARANCE_POWER_LED_DRIVER 0x0785
```

相关声明：[BT_APPEARANCE_POWER_LED_DRIVER](#ga31842298741c822dcebba942453975c6)。

LED 驱动器（LED Driver）。

<a id="r_ga7de26016aa039e3e72ddd61653e1c1d8"></a>

```c
#define BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR 0x0786
```

相关声明：[BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR](#ga7de26016aa039e3e72ddd61653e1c1d8)。

荧光灯控制装置（Fluorescent Lamp Gear）。

<a id="r_ga6396b1d813c9764bdfe92c4f2ba961b1"></a>

```c
#define BT_APPEARANCE_POWER_HID_LAMP_GEAR 0x0787
```

相关声明：[BT_APPEARANCE_POWER_HID_LAMP_GEAR](#ga6396b1d813c9764bdfe92c4f2ba961b1)。

高强度气体放电灯控制装置（HID Lamp Gear）。

<a id="r_ga5d6b28b9660d2357e2af2bf0ceab9c18"></a>

```c
#define BT_APPEARANCE_POWER_CHARGE_CASE 0x0788
```

相关声明：[BT_APPEARANCE_POWER_CHARGE_CASE](#ga5d6b28b9660d2357e2af2bf0ceab9c18)。

充电盒（Charge Case）。

<a id="r_gab6a5ac3941a5707f052126810a7f22e0"></a>

```c
#define BT_APPEARANCE_POWER_POWER_BANK 0x0789
```

相关声明：[BT_APPEARANCE_POWER_POWER_BANK](#gab6a5ac3941a5707f052126810a7f22e0)。

移动电源（Power Bank）。

<a id="r_gacb3340c5193588eea2d42fe1bef443d0"></a>

```c
#define BT_APPEARANCE_GENERIC_LIGHT_SOURCE 0x07C0
```

相关声明：[BT_APPEARANCE_GENERIC_LIGHT_SOURCE](#gacb3340c5193588eea2d42fe1bef443d0)。

通用光源（Generic Light Source）。

<a id="r_gafed8531ffde21d0ad6e8d477d64496f0"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB 0x07C1
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB](#gafed8531ffde21d0ad6e8d477d64496f0)。

白炽灯泡（Incandescent Light Bulb）。

<a id="r_ga66bf91b8a25ac88a0fd6ab9456201de1"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP 0x07C2
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP](#ga66bf91b8a25ac88a0fd6ab9456201de1)。

LED 灯（LED Lamp）。

<a id="r_ga1babd2989112bafb5819235fe5b6c556"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP 0x07C3
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP](#ga1babd2989112bafb5819235fe5b6c556)。

高强度气体放电灯（HID Lamp）。

<a id="r_ga39957a77aa54255ab3a06441e422e7e3"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP 0x07C4
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP](#ga39957a77aa54255ab3a06441e422e7e3)。

荧光灯（Fluorescent Lamp）。

<a id="r_ga242d324cf5cf33e4edd5cf33e8c3c89b"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY 0x07C5
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY](#ga242d324cf5cf33e4edd5cf33e8c3c89b)。

LED 阵列（LED Array）。

<a id="r_ga8449006920ed1fdd562c702ee2e16a21"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY 0x07C6
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY](#ga8449006920ed1fdd562c702ee2e16a21)。

多色 LED 阵列（Multi-Color LED Array）。

<a id="r_gaf47bce54f4ae1915cd64c3c2d254e353"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN 0x07C7
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN](#gaf47bce54f4ae1915cd64c3c2d254e353)。

低压卤素灯（Low voltage halogen）。

<a id="r_gaed4400a94dae4f536a456cc55eb6f6d5"></a>

```c
#define BT_APPEARANCE_LIGHT_SOURCE_OLED 0x07C8
```

相关声明：[BT_APPEARANCE_LIGHT_SOURCE_OLED](#gaed4400a94dae4f536a456cc55eb6f6d5)。

有机发光二极管（Organic light emitting diode）。

<a id="r_ga1e70d961fca2719243c866464132684c"></a>

```c
#define BT_APPEARANCE_GENERIC_WINDOW_COVERING 0x0800
```

相关声明：[BT_APPEARANCE_GENERIC_WINDOW_COVERING](#ga1e70d961fca2719243c866464132684c)。

通用窗户遮蔽物（Generic Window Covering）。

<a id="r_ga37614ae63c8287bc4bd0c9a5bf00502e"></a>

```c
#define BT_APPEARANCE_WINDOW_SHADES 0x0801
```

相关声明：[BT_APPEARANCE_WINDOW_SHADES](#ga37614ae63c8287bc4bd0c9a5bf00502e)。

遮阳窗帘（Window Shades）。

<a id="r_ga717efaeab0329ded066567761b9983a7"></a>

```c
#define BT_APPEARANCE_WINDOW_BLINDS 0x0802
```

相关声明：[BT_APPEARANCE_WINDOW_BLINDS](#ga717efaeab0329ded066567761b9983a7)。

百叶窗帘（Window Blinds）。

<a id="r_ga9945bb52a9ee3268efda7d5e05421e12"></a>

```c
#define BT_APPEARANCE_WINDOW_AWNING 0x0803
```

相关声明：[BT_APPEARANCE_WINDOW_AWNING](#ga9945bb52a9ee3268efda7d5e05421e12)。

窗户遮阳篷（Window Awning）。

<a id="r_ga20352e58e6cec63efbb6beaa75c0e330"></a>

```c
#define BT_APPEARANCE_WINDOW_CURTAIN 0x0804
```

相关声明：[BT_APPEARANCE_WINDOW_CURTAIN](#ga20352e58e6cec63efbb6beaa75c0e330)。

窗帘（Window Curtain）。

<a id="r_ga7ead13b128fbc50be3f5c101fb1383cb"></a>

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER 0x0805
```

相关声明：[BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER](#ga7ead13b128fbc50be3f5c101fb1383cb)。

外置百叶窗（Exterior Shutter）。

<a id="r_ga0a0b87095177af0560a540e545c97f42"></a>

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN 0x0806
```

相关声明：[BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN](#ga0a0b87095177af0560a540e545c97f42)。

外置遮阳屏（Exterior Screen）。

<a id="r_ga32bb0f06096ce5259676a31342b9f0d9"></a>

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SINK 0x0840
```

相关声明：[BT_APPEARANCE_GENERIC_AUDIO_SINK](#ga32bb0f06096ce5259676a31342b9f0d9)。

通用音频接收端（Generic Audio Sink）。

<a id="r_gabcb109c4660a177494329faf353406f4"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER 0x0841
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER](#gabcb109c4660a177494329faf353406f4)。

独立扬声器（Standalone Speaker）。

<a id="r_ga93e3a858b2efabea72a8855a28ad21c2"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_SOUNDBAR 0x0842
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_SOUNDBAR](#ga93e3a858b2efabea72a8855a28ad21c2)。

条形音箱（Soundbar）。

<a id="r_ga666aed968e9a0f9566edcc1bcba0bfbd"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER 0x0843
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER](#ga666aed968e9a0f9566edcc1bcba0bfbd)。

书架式音箱（Bookshelf Speaker）。

<a id="r_ga6b3ddddf1de7d95a15aa6194ddc656ee"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER 0x0844
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER](#ga6b3ddddf1de7d95a15aa6194ddc656ee)。

支架式音箱（Standmounted Speaker）。

<a id="r_gadd82602d251aa555a06123ef0388d1b1"></a>

```c
#define BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE 0x0845
```

相关声明：[BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE](#gadd82602d251aa555a06123ef0388d1b1)。

免提电话（Speakerphone）。

<a id="r_gac85b90f2585044d0efa61191dba3c596"></a>

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SOURCE 0x0880
```

相关声明：[BT_APPEARANCE_GENERIC_AUDIO_SOURCE](#gac85b90f2585044d0efa61191dba3c596)。

通用音频源（Generic Audio Source）。

<a id="r_ga6dd1354de34ed79702d9d7878d859fcb"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE 0x0881
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE](#ga6dd1354de34ed79702d9d7878d859fcb)。

麦克风（Microphone）。

<a id="r_gaa8d5a95cb181e27efb2409d5dce3da57"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_ALARM 0x0882
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_ALARM](#gaa8d5a95cb181e27efb2409d5dce3da57)。

警报器（Alarm）。

<a id="r_ga748b4fa86145f3950069ed44cde8cacb"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BELL 0x0883
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BELL](#ga748b4fa86145f3950069ed44cde8cacb)。

铃（Bell）。

<a id="r_ga3415afbd526b29b5bbafc1ac889bd371"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_HORN 0x0884
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_HORN](#ga3415afbd526b29b5bbafc1ac889bd371)。

号角（Horn）。

<a id="r_ga35ecc1a1051379010123582c82e9b31c"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE 0x0885
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE](#ga35ecc1a1051379010123582c82e9b31c)。

广播设备（Broadcasting Device）。

<a id="r_ga48fc37d769211cba1e6121e670b02e25"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK 0x0886
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK](#ga48fc37d769211cba1e6121e670b02e25)。

服务台（Service Desk）。

<a id="r_ga6ad3ee00ed05c8a7ed182df5c82a5af4"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_KIOSK 0x0887
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_KIOSK](#ga6ad3ee00ed05c8a7ed182df5c82a5af4)。

自助服务终端（Kiosk）。

<a id="r_gaad0fe38e5246c55cc562729448b9f390"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM 0x0888
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM](#gaad0fe38e5246c55cc562729448b9f390)。

广播室（Broadcasting Room）。

<a id="r_gac8ab0549f83c9d6b68dc4dd75cfe7b1e"></a>

```c
#define BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM 0x0889
```

相关声明：[BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM](#gac8ab0549f83c9d6b68dc4dd75cfe7b1e)。

礼堂（Auditorium）。

<a id="r_ga49328394fd7505da9476d4d62ae60c03"></a>

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE 0x08C0
```

相关声明：[BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE](#ga49328394fd7505da9476d4d62ae60c03)。

通用机动车辆（Generic Motorized Vehicle）。

<a id="r_ga6257291ed3e6d09ce6197e2081b36d04"></a>

```c
#define BT_APPEARANCE_VEHICLE_CAR 0x08C1
```

相关声明：[BT_APPEARANCE_VEHICLE_CAR](#ga6257291ed3e6d09ce6197e2081b36d04)。

汽车（Car）。

<a id="r_ga31ff643e1efccffd9ba73c793f63837c"></a>

```c
#define BT_APPEARANCE_VEHICLE_LARGE_GOODS 0x08C2
```

相关声明：[BT_APPEARANCE_VEHICLE_LARGE_GOODS](#ga31ff643e1efccffd9ba73c793f63837c)。

大型货运车辆（Large Goods Vehicle）。

<a id="r_ga68ade931a12e5d9e9863decad3d8de9e"></a>

```c
#define BT_APPEARANCE_VEHICLE_TWO_WHEELED 0x08C3
```

相关声明：[BT_APPEARANCE_VEHICLE_TWO_WHEELED](#ga68ade931a12e5d9e9863decad3d8de9e)。

两轮车辆（2-Wheeled Vehicle）。

<a id="r_gaa71eaa4fd0eef66a794475cb44aaf397"></a>

```c
#define BT_APPEARANCE_VEHICLE_MOTORBIKE 0x08C4
```

相关声明：[BT_APPEARANCE_VEHICLE_MOTORBIKE](#gaa71eaa4fd0eef66a794475cb44aaf397)。

摩托车（Motorbike）。

<a id="r_gae082982b90d94404b69c57987d8a2c5a"></a>

```c
#define BT_APPEARANCE_VEHICLE_SCOOTER 0x08C5
```

相关声明：[BT_APPEARANCE_VEHICLE_SCOOTER](#gae082982b90d94404b69c57987d8a2c5a)。

踏板车（Scooter）。

<a id="r_ga18b0231dbd97d8871f685774f9e1b4e1"></a>

```c
#define BT_APPEARANCE_VEHICLE_MOPED 0x08C6
```

相关声明：[BT_APPEARANCE_VEHICLE_MOPED](#ga18b0231dbd97d8871f685774f9e1b4e1)。

轻便摩托车（Moped）。

<a id="r_ga8159dfd6933a2a5fdb2c72da9623bc2e"></a>

```c
#define BT_APPEARANCE_VEHICLE_THREE_WHEELED 0x08C7
```

相关声明：[BT_APPEARANCE_VEHICLE_THREE_WHEELED](#ga8159dfd6933a2a5fdb2c72da9623bc2e)。

三轮车辆（3-Wheeled Vehicle）。

<a id="r_gac22a0476760c42eb8f00b36b74361c5e"></a>

```c
#define BT_APPEARANCE_VEHICLE_LIGHT 0x08C8
```

相关声明：[BT_APPEARANCE_VEHICLE_LIGHT](#gac22a0476760c42eb8f00b36b74361c5e)。

轻型车辆（Light Vehicle）。

<a id="r_ga03e3660bdc2e439126f2f8df8ea335ee"></a>

```c
#define BT_APPEARANCE_VEHICLE_QUAD_BIKE 0x08C9
```

相关声明：[BT_APPEARANCE_VEHICLE_QUAD_BIKE](#ga03e3660bdc2e439126f2f8df8ea335ee)。

四轮摩托车（Quad Bike）。

<a id="r_ga0cf473bbf07d4576ab9f0116ca48f161"></a>

```c
#define BT_APPEARANCE_VEHICLE_MINIBUS 0x08CA
```

相关声明：[BT_APPEARANCE_VEHICLE_MINIBUS](#ga0cf473bbf07d4576ab9f0116ca48f161)。

小型客车（Minibus）。

<a id="r_ga0da02a18987c653a3232c28a3e4908f7"></a>

```c
#define BT_APPEARANCE_VEHICLE_BUS 0x08CB
```

相关声明：[BT_APPEARANCE_VEHICLE_BUS](#ga0da02a18987c653a3232c28a3e4908f7)。

公共汽车（Bus）。

<a id="r_gabde7af9f7c25d56f5fb9643398273526"></a>

```c
#define BT_APPEARANCE_VEHICLE_TROLLEY 0x08CC
```

相关声明：[BT_APPEARANCE_VEHICLE_TROLLEY](#gabde7af9f7c25d56f5fb9643398273526)。

电车（Trolley）。

<a id="r_gaa149e56e4b4a1b6dde821fbdac3d9c32"></a>

```c
#define BT_APPEARANCE_VEHICLE_AGRICULTURAL 0x08CD
```

相关声明：[BT_APPEARANCE_VEHICLE_AGRICULTURAL](#gaa149e56e4b4a1b6dde821fbdac3d9c32)。

农业车辆（Agricultural Vehicle）。

<a id="r_gafcb3909bf61bb130f8c0a217e69477b8"></a>

```c
#define BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN 0x08CE
```

相关声明：[BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN](#gafcb3909bf61bb130f8c0a217e69477b8)。

露营车／拖挂式旅居车（Camper/Caravan）。

<a id="r_ga9366a994d42c88490313380d419b2a8e"></a>

```c
#define BT_APPEARANCE_VEHICLE_RECREATIONAL 0x08CF
```

相关声明：[BT_APPEARANCE_VEHICLE_RECREATIONAL](#ga9366a994d42c88490313380d419b2a8e)。

休闲车辆／自行式房车（Recreational Vehicle/Motor Home）。

<a id="r_gac08b31ff9b618b19e4c1b43ae2056b5f"></a>

```c
#define BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE 0x0900
```

相关声明：[BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE](#gac08b31ff9b618b19e4c1b43ae2056b5f)。

通用家用电器（Generic Domestic Appliance）。

<a id="r_gad02c3dc8fa1321b14ee70264a36c4950"></a>

```c
#define BT_APPEARANCE_APPLIANCE_REFRIGERATOR 0x0901
```

相关声明：[BT_APPEARANCE_APPLIANCE_REFRIGERATOR](#gad02c3dc8fa1321b14ee70264a36c4950)。

冰箱（Refrigerator）。

<a id="r_ga6ec2458a171142a5e22ec339d23a5a0c"></a>

```c
#define BT_APPEARANCE_APPLIANCE_FREEZER 0x0902
```

相关声明：[BT_APPEARANCE_APPLIANCE_FREEZER](#ga6ec2458a171142a5e22ec339d23a5a0c)。

冷冻柜（Freezer）。

<a id="r_ga7a48c5a07e677167ae10412ed2c1040b"></a>

```c
#define BT_APPEARANCE_APPLIANCE_OVEN 0x0903
```

相关声明：[BT_APPEARANCE_APPLIANCE_OVEN](#ga7a48c5a07e677167ae10412ed2c1040b)。

烤箱（Oven）。

<a id="r_gabaac12b866cd29547165331333e8be3d"></a>

```c
#define BT_APPEARANCE_APPLIANCE_MICROWAVE 0x0904
```

相关声明：[BT_APPEARANCE_APPLIANCE_MICROWAVE](#gabaac12b866cd29547165331333e8be3d)。

微波炉（Microwave）。

<a id="r_ga5b0d9632cb2ed4afd856f05a1e857394"></a>

```c
#define BT_APPEARANCE_APPLIANCE_TOASTER 0x0905
```

相关声明：[BT_APPEARANCE_APPLIANCE_TOASTER](#ga5b0d9632cb2ed4afd856f05a1e857394)。

烤面包机（Toaster）。

<a id="r_ga1febcada2c95105648831094a4de6a8d"></a>

```c
#define BT_APPEARANCE_APPLIANCE_WASHING_MACHINE 0x0906
```

相关声明：[BT_APPEARANCE_APPLIANCE_WASHING_MACHINE](#ga1febcada2c95105648831094a4de6a8d)。

洗衣机（Washing Machine）。

<a id="r_gaac26996e0de10b16e24900a08c1098f5"></a>

```c
#define BT_APPEARANCE_APPLIANCE_DRYER 0x0907
```

相关声明：[BT_APPEARANCE_APPLIANCE_DRYER](#gaac26996e0de10b16e24900a08c1098f5)。

烘干机（Dryer）。

<a id="r_gac601c74c6132decf13527bdacbc5a08b"></a>

```c
#define BT_APPEARANCE_APPLIANCE_COFFEE_MAKER 0x0908
```

相关声明：[BT_APPEARANCE_APPLIANCE_COFFEE_MAKER](#gac601c74c6132decf13527bdacbc5a08b)。

咖啡机（Coffee maker）。

<a id="r_gaeb66941a8e8b38ed0ea47305da157e24"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_IRON 0x0909
```

相关声明：[BT_APPEARANCE_APPLIANCE_CLOTHES_IRON](#gaeb66941a8e8b38ed0ea47305da157e24)。

电熨斗（Clothes iron）。

<a id="r_ga6a9885e9a2133c0732d056ecd63313ad"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CURLING_IRON 0x090A
```

相关声明：[BT_APPEARANCE_APPLIANCE_CURLING_IRON](#ga6a9885e9a2133c0732d056ecd63313ad)。

卷发棒（Curling iron）。

<a id="r_ga15be0164f5883558fb61c9cb9679b78f"></a>

```c
#define BT_APPEARANCE_APPLIANCE_HAIR_DRYER 0x090B
```

相关声明：[BT_APPEARANCE_APPLIANCE_HAIR_DRYER](#ga15be0164f5883558fb61c9cb9679b78f)。

吹风机（Hair dryer）。

<a id="r_ga46d5f18bb8c764c43af97fddcec4a1ec"></a>

```c
#define BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER 0x090C
```

相关声明：[BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER](#ga46d5f18bb8c764c43af97fddcec4a1ec)。

吸尘器（Vacuum cleaner）。

<a id="r_ga423e85d0816a4bd0205f4d8188e6c406"></a>

```c
#define BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER 0x090D
```

相关声明：[BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER](#ga423e85d0816a4bd0205f4d8188e6c406)。

扫地机器人（Robotic vacuum cleaner）。

<a id="r_ga78511e0ef7d509deeba65352e7f81ad8"></a>

```c
#define BT_APPEARANCE_APPLIANCE_RICE_COOKER 0x090E
```

相关声明：[BT_APPEARANCE_APPLIANCE_RICE_COOKER](#ga78511e0ef7d509deeba65352e7f81ad8)。

电饭煲（Rice cooker）。

<a id="r_ga0292c6123b655964311d0e6027b5af20"></a>

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER 0x090F
```

相关声明：[BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER](#ga0292c6123b655964311d0e6027b5af20)。

挂烫机（Clothes steamer）。

<a id="r_gabad761094a16873dcebbc6238825d84b"></a>

```c
#define BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE 0x0940
```

相关声明：[BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE](#gabad761094a16873dcebbc6238825d84b)。

通用可穿戴音频设备（Generic Wearable Audio Device）。

<a id="r_gab480735e2ba8db23d2668ea3a2137214"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD 0x0941
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD](#gab480735e2ba8db23d2668ea3a2137214)。

耳塞式耳机（Earbud）。

<a id="r_ga8bd98ba3a4c1cbf8dbf8235d9ad0f943"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET 0x0942
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET](#ga8bd98ba3a4c1cbf8dbf8235d9ad0f943)。

带麦克风耳机（Headset）。

<a id="r_gae420044380309abba1b9570d26735315"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES 0x0943
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES](#gae420044380309abba1b9570d26735315)。

头戴式耳机（Headphones）。

<a id="r_ga59ea8ff5efec7a19bce8440e7ae78a1e"></a>

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND 0x0944
```

相关声明：[BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND](#ga59ea8ff5efec7a19bce8440e7ae78a1e)。

颈挂式耳机（Neck Band）。

<a id="r_ga24c9bcf9646ec5049abf310b31ab355e"></a>

```c
#define BT_APPEARANCE_GENERIC_AIRCRAFT 0x0980
```

相关声明：[BT_APPEARANCE_GENERIC_AIRCRAFT](#ga24c9bcf9646ec5049abf310b31ab355e)。

通用航空器（Generic Aircraft）。

<a id="r_ga6f1d2fb56f53ac5317b024d7487b8742"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_LIGHT 0x0981
```

相关声明：[BT_APPEARANCE_AIRCRAFT_LIGHT](#ga6f1d2fb56f53ac5317b024d7487b8742)。

轻型飞机（Light Aircraft）。

<a id="r_gad2d0b1c4b710e50127049ec4cd299396"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_MICROLIGHT 0x0982
```

相关声明：[BT_APPEARANCE_AIRCRAFT_MICROLIGHT](#gad2d0b1c4b710e50127049ec4cd299396)。

超轻型飞机（Microlight）。

<a id="r_ga6f827322066333fe926f0912099e6903"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_PARAGLIDER 0x0983
```

相关声明：[BT_APPEARANCE_AIRCRAFT_PARAGLIDER](#ga6f827322066333fe926f0912099e6903)。

滑翔伞（Paraglider）。

<a id="r_gae7be5c3bf9ad97e34d6c62bb791c39c0"></a>

```c
#define BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER 0x0984
```

相关声明：[BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER](#gae7be5c3bf9ad97e34d6c62bb791c39c0)。

大型客机（Large Passenger Aircraft）。

<a id="r_gadb3b07d6c3d3f679b15069fdd8d4e1ee"></a>

```c
#define BT_APPEARANCE_GENERIC_AV_EQUIPMENT 0x09C0
```

相关声明：[BT_APPEARANCE_GENERIC_AV_EQUIPMENT](#gadb3b07d6c3d3f679b15069fdd8d4e1ee)。

通用音视频设备（Generic AV Equipment）。

<a id="r_ga7294c7b26ac8da3b9800c91ec824ad22"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER 0x09C1
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER](#ga7294c7b26ac8da3b9800c91ec824ad22)。

放大器（Amplifier）。

<a id="r_gac826e2e5326d1aa5fdd7ebf55fe395e6"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RECEIVER 0x09C2
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_RECEIVER](#gac826e2e5326d1aa5fdd7ebf55fe395e6)。

接收机（Receiver）。

<a id="r_gad60d1a387a1c62218baa3044e5acc3db"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RADIO 0x09C3
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_RADIO](#gad60d1a387a1c62218baa3044e5acc3db)。

收音机（Radio）。

<a id="r_ga7ccf41932861fa5f33d12060a12d5aa7"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TUNER 0x09C4
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_TUNER](#ga7ccf41932861fa5f33d12060a12d5aa7)。

调谐器（Tuner）。

<a id="r_ga69417cb3e9c434e751483328d6134cdf"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE 0x09C5
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE](#ga69417cb3e9c434e751483328d6134cdf)。

唱盘（Turntable）。

<a id="r_ga6c9ad45a9b22a94ae0cce16bfe749a33"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER 0x09C6
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER](#ga6c9ad45a9b22a94ae0cce16bfe749a33)。

CD 播放器（CD Player）。

<a id="r_ga02681af8d755c701d9caef3f89a5c35a"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER 0x09C7
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER](#ga02681af8d755c701d9caef3f89a5c35a)。

DVD 播放器（DVD Player）。

<a id="r_ga1394bc80927fb8db4eef1786111c65c7"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER 0x09C8
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER](#ga1394bc80927fb8db4eef1786111c65c7)。

蓝光播放器（Bluray Player）。

<a id="r_gaa01c862bff9aaaad09ed925da60fcb25"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER 0x09C9
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER](#gaa01c862bff9aaaad09ed925da60fcb25)。

光盘播放器（Optical Disc Player）。

<a id="r_gad0ac86cf291b781b772fa9e85dda283a"></a>

```c
#define BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX 0x09CA
```

相关声明：[BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX](#gad0ac86cf291b781b772fa9e85dda283a)。

机顶盒（Set-Top Box）。

<a id="r_ga44b70b2f515416baf686b1e127ef4375"></a>

```c
#define BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT 0x0A00
```

相关声明：[BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT](#ga44b70b2f515416baf686b1e127ef4375)。

通用显示设备（Generic Display Equipment）。

<a id="r_ga9a6684aa8677575625e049fa0da2c26c"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION 0x0A01
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION](#ga9a6684aa8677575625e049fa0da2c26c)。

电视机（Television）。

<a id="r_gabbcb0fbbeb6423052db9d5e04410499c"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR 0x0A02
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR](#gabbcb0fbbeb6423052db9d5e04410499c)。

监视器（Monitor）。

<a id="r_gaa98f5139c99b46515746fb76e9ae7f9b"></a>

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR 0x0A03
```

相关声明：[BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR](#gaa98f5139c99b46515746fb76e9ae7f9b)。

投影仪（Projector）。

<a id="r_gadb5595a41edf5974e03649a675618b7b"></a>

```c
#define BT_APPEARANCE_GENERIC_HEARING_AID 0x0A40
```

相关声明：[BT_APPEARANCE_GENERIC_HEARING_AID](#gadb5595a41edf5974e03649a675618b7b)。

通用助听器（Generic Hearing aid）。

<a id="r_ga28cc6555937d9d5a9e8ae0079fc8a534"></a>

```c
#define BT_APPEARANCE_HEARING_AID_IN_EAR 0x0A41
```

相关声明：[BT_APPEARANCE_HEARING_AID_IN_EAR](#ga28cc6555937d9d5a9e8ae0079fc8a534)。

耳内式助听器（In-ear hearing aid）。

<a id="r_ga1fa6231e14dcfa90a5518e61f0e4e302"></a>

```c
#define BT_APPEARANCE_HEARING_AID_BEHIND_EAR 0x0A42
```

相关声明：[BT_APPEARANCE_HEARING_AID_BEHIND_EAR](#ga1fa6231e14dcfa90a5518e61f0e4e302)。

耳后式助听器（Behind-ear hearing aid）。

<a id="r_ga82ba79bd9fd04a3fbdb6d8b4e35e3877"></a>

```c
#define BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT 0x0A43
```

相关声明：[BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT](#ga82ba79bd9fd04a3fbdb6d8b4e35e3877)。

人工耳蜗（Cochlear Implant）。

<a id="r_gaca727b215a8277d921c0a3bfeccb3f14"></a>

```c
#define BT_APPEARANCE_GENERIC_GAMING 0x0A80
```

相关声明：[BT_APPEARANCE_GENERIC_GAMING](#gaca727b215a8277d921c0a3bfeccb3f14)。

通用游戏设备（Generic Gaming）。

<a id="r_ga8fbaf0fced0cce12e08c4a516351b166"></a>

```c
#define BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE 0x0A81
```

相关声明：[BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE](#ga8fbaf0fced0cce12e08c4a516351b166)。

家用电子游戏机（Home Video Game Console）。

<a id="r_ga39ad633d1795af4546bd930d0e799447"></a>

```c
#define BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE 0x0A82
```

相关声明：[BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE](#ga39ad633d1795af4546bd930d0e799447)。

便携式掌上游戏机（Portable handheld console）。

<a id="r_gabc243c7449804749704c1862db286eab"></a>

```c
#define BT_APPEARANCE_GENERIC_SIGNAGE 0x0AC0
```

相关声明：[BT_APPEARANCE_GENERIC_SIGNAGE](#gabc243c7449804749704c1862db286eab)。

通用标识设备（Generic Signage）。

<a id="r_gace31a591ef3b5f0812e4cbf417a2205a"></a>

```c
#define BT_APPEARANCE_SIGNAGE_DIGITAL 0x0AC1
```

相关声明：[BT_APPEARANCE_SIGNAGE_DIGITAL](#gace31a591ef3b5f0812e4cbf417a2205a)。

数字标牌（Digital Signage）。

<a id="r_gaa4674b06751edf98fa88ede568a68ad4"></a>

```c
#define BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL 0x0AC2
```

相关声明：[BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL](#gaa4674b06751edf98fa88ede568a68ad4)。

电子标签（Electronic Label）。

<a id="r_ga93ee753bf3b8819239041c065eaf024f"></a>

```c
#define BT_APPEARANCE_GENERIC_PULSE_OXIMETER 0x0C40
```

相关声明：[BT_APPEARANCE_GENERIC_PULSE_OXIMETER](#ga93ee753bf3b8819239041c065eaf024f)。

通用脉搏血氧仪（Generic Pulse Oximeter）。

<a id="r_ga8a298130c73299b6079dae3065954c0c"></a>

```c
#define BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP 0x0C41
```

相关声明：[BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP](#ga8a298130c73299b6079dae3065954c0c)。

指夹式脉搏血氧仪（Fingertip Pulse Oximeter）。

<a id="r_gaebcadd5c37e6d87903e2cb97e03aeb7d"></a>

```c
#define BT_APPEARANCE_PULSE_OXIMETER_WRIST 0x0C42
```

相关声明：[BT_APPEARANCE_PULSE_OXIMETER_WRIST](#gaebcadd5c37e6d87903e2cb97e03aeb7d)。

腕戴式脉搏血氧仪（Wrist Worn Pulse Oximeter）。

<a id="r_ga1aec23cd4f531a57260c7c8faf9caf40"></a>

```c
#define BT_APPEARANCE_GENERIC_WEIGHT_SCALE 0x0C80
```

相关声明：[BT_APPEARANCE_GENERIC_WEIGHT_SCALE](#ga1aec23cd4f531a57260c7c8faf9caf40)。

通用体重秤（Generic Weight Scale）。

<a id="r_ga7387d717c77b38374e981991278aeb1c"></a>

```c
#define BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE 0x0CC0
```

相关声明：[BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE](#ga7387d717c77b38374e981991278aeb1c)。

通用个人助行设备（Generic Personal Mobility Device）。

<a id="r_ga7966ec64cafe708fe94a7c323fbe3713"></a>

```c
#define BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR 0x0CC1
```

相关声明：[BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR](#ga7966ec64cafe708fe94a7c323fbe3713)。

电动轮椅（Powered Wheelchair）。

<a id="r_ga21f21a73f355ffaa408376ca4fc802a8"></a>

```c
#define BT_APPEARANCE_MOBILITY_SCOOTER 0x0CC2
```

相关声明：[BT_APPEARANCE_MOBILITY_SCOOTER](#ga21f21a73f355ffaa408376ca4fc802a8)。

助行代步车（Mobility Scooter）。

<a id="r_gab77dd4cfe254df84cbe0b8d45247e198"></a>

```c
#define BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR 0x0D00
```

相关声明：[BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR](#gab77dd4cfe254df84cbe0b8d45247e198)。

连续血糖监测仪（Continuous Glucose Monitor）。

<a id="r_ga481169a27fab19628f81a68af31d543c"></a>

```c
#define BT_APPEARANCE_GENERIC_INSULIN_PUMP 0x0D40
```

相关声明：[BT_APPEARANCE_GENERIC_INSULIN_PUMP](#ga481169a27fab19628f81a68af31d543c)。

通用胰岛素泵（Generic Insulin Pump）。

<a id="r_ga63512439364307259010bededf7bfd8b"></a>

```c
#define BT_APPEARANCE_INSULIN_PUMP_DURABLE 0x0D41
```

相关声明：[BT_APPEARANCE_INSULIN_PUMP_DURABLE](#ga63512439364307259010bededf7bfd8b)。

耐用型胰岛素泵（Insulin Pump, durable pump）。

<a id="r_ga0979695247b96321e5a8b6869d09227a"></a>

```c
#define BT_APPEARANCE_INSULIN_PUMP_PATCH 0x0D44
```

相关声明：[BT_APPEARANCE_INSULIN_PUMP_PATCH](#ga0979695247b96321e5a8b6869d09227a)。

贴片式胰岛素泵（Insulin Pump, patch pump）。

<a id="r_ga1562514d0182e8862edad570b7a346e6"></a>

```c
#define BT_APPEARANCE_INSULIN_PEN 0x0D48
```

相关声明：[BT_APPEARANCE_INSULIN_PEN](#ga1562514d0182e8862edad570b7a346e6)。

胰岛素笔（Insulin Pen）。

<a id="r_ga08453eebe2ae8f53deddaa64a029c2b5"></a>

```c
#define BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY 0x0D80
```

相关声明：[BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY](#ga08453eebe2ae8f53deddaa64a029c2b5)。

通用药物输送设备（Generic Medication Delivery）。

<a id="r_ga1332c44cc3371fa9006993d03ba4ae12"></a>

```c
#define BT_APPEARANCE_GENERIC_SPIROMETER 0x0DC0
```

相关声明：[BT_APPEARANCE_GENERIC_SPIROMETER](#ga1332c44cc3371fa9006993d03ba4ae12)。

通用肺量计（Generic Spirometer）。

<a id="r_ga42b9d596efb757b209f080a8c33f3723"></a>

```c
#define BT_APPEARANCE_SPIROMETER_HANDHELD 0x0DC1
```

相关声明：[BT_APPEARANCE_SPIROMETER_HANDHELD](#ga42b9d596efb757b209f080a8c33f3723)。

手持式肺量计（Handheld Spirometer）。

<a id="r_ga0d39ca2892bd96013b8c82111eecc1cb"></a>

```c
#define BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS 0x1440
```

相关声明：[BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS](#ga0d39ca2892bd96013b8c82111eecc1cb)。

通用户外运动设备（Generic Outdoor Sports Activity）。

<a id="r_ga30c97d6f5bff1a4a67e4f59eb4d49d2d"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION 0x1441
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION](#ga30c97d6f5bff1a4a67e4f59eb4d49d2d)。

位置显示器（Location Display）。

<a id="r_ga52b6c51c9afcbbba12d9d3cae824f4a7"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV 0x1442
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV](#ga52b6c51c9afcbbba12d9d3cae824f4a7)。

位置与导航显示器（Location and Navigation Display）。

<a id="r_gadf053353789183d1b1c3ca13ad98559f"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD 0x1443
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD](#gadf053353789183d1b1c3ca13ad98559f)。

定位模块（Location Pod）。

<a id="r_ga8fbc7782099e724febb712ee108e8cba"></a>

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV 0x1444
```

相关声明：[BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV](#ga8fbc7782099e724febb712ee108e8cba)。

定位与导航模块（Location and Navigation Pod）。

## 1.2\_通用数据类型（Common Data Types）

<a id="r_ga396b92d418fcb8263895e420b9df3df2"></a>

```c
#define BT_DATA_FLAGS 0x01
```

相关声明：[BT_DATA_FLAGS](#ga396b92d418fcb8263895e420b9df3df2)。

广播数据标志（AD flags）。

<a id="r_ga6c725bd3d31c159a4d046561dbca38ba"></a>

```c
#define BT_DATA_UUID16_SOME 0x02
```

相关声明：[`BT_DATA_UUID16_SOME`：部分 16 位 UUID（Some 16-bit UUIDs）。](#ga6c725bd3d31c159a4d046561dbca38ba)。

16 位 UUID 列表，尚有更多条目（16-bit UUID, more available）。

<a id="r_ga0d55063b9ad321b5c530a0012337df8a"></a>

```c
#define BT_DATA_UUID16_ALL 0x03
```

相关声明：[BT_DATA_UUID16_ALL](#ga0d55063b9ad321b5c530a0012337df8a)。

16 位 UUID 列表，已全部列出（16-bit UUID, all listed）。

<a id="r_ga2486a6748490ba57e442ca15223482ef"></a>

```c
#define BT_DATA_UUID32_SOME 0x04
```

相关声明：[`BT_DATA_UUID32_SOME`：部分 32 位 UUID（Some 32-bit UUIDs）。](#ga2486a6748490ba57e442ca15223482ef)。

32 位 UUID 列表，尚有更多条目（32-bit UUID, more available）。

<a id="r_gaaf825c3e4686e572a35ddd46ee6fe2e8"></a>

```c
#define BT_DATA_UUID32_ALL 0x05
```

相关声明：[BT_DATA_UUID32_ALL](#gaaf825c3e4686e572a35ddd46ee6fe2e8)。

32 位 UUID 列表，已全部列出（32-bit UUID, all listed）。

<a id="r_ga5c4f7fc1b93c611e95f735330fba243b"></a>

```c
#define BT_DATA_UUID128_SOME 0x06
```

相关声明：[`BT_DATA_UUID128_SOME`：部分 128 位 UUID（Some 128-bit UUIDs）。](#ga5c4f7fc1b93c611e95f735330fba243b)。

128 位 UUID 列表，尚有更多条目（128-bit UUID, more available）。

<a id="r_gaafcade3dbbcb4005f4590e994f91884b"></a>

```c
#define BT_DATA_UUID128_ALL 0x07
```

相关声明：[BT_DATA_UUID128_ALL](#gaafcade3dbbcb4005f4590e994f91884b)。

128 位 UUID 列表，已全部列出（128-bit UUID, all listed）。

<a id="r_gafc509b33a8d2dd9124f6893eadbe1662"></a>

```c
#define BT_DATA_NAME_SHORTENED 0x08
```

相关声明：[`BT_DATA_NAME_SHORTENED`：缩短名称（Shortened Name）。](#gafc509b33a8d2dd9124f6893eadbe1662)。

缩短名称（Shortened name）。

<a id="r_gab94a7c5689d296acf47f976538056ab5"></a>

```c
#define BT_DATA_NAME_COMPLETE 0x09
```

相关声明：[BT_DATA_NAME_COMPLETE](#gab94a7c5689d296acf47f976538056ab5)。

完整名称（Complete name）。

<a id="r_ga4988c17578c4cf76fcdd9d44e1c931b0"></a>

```c
#define BT_DATA_TX_POWER 0x0a
```

相关声明：[BT_DATA_TX_POWER](#ga4988c17578c4cf76fcdd9d44e1c931b0)。

发射功率（Tx Power）。

<a id="r_ga152c3028a2befcc4caf40aa6590c80b7"></a>

```c
#define BT_DATA_DEVICE_CLASS 0x0d
```

相关声明：[BT_DATA_DEVICE_CLASS](#ga152c3028a2befcc4caf40aa6590c80b7)。

设备类别（Class of Device）。

<a id="r_ga053c8bb0aedd01b3dd3f6154f4b49999"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_HASH_C192 0x0e
```

相关声明：[BT_DATA_SIMPLE_PAIRING_HASH_C192](#ga053c8bb0aedd01b3dd3f6154f4b49999)。

简单配对哈希 C-192（Simple Pairing Hash C-192）。

<a id="r_ga280f1f96c5204960fe034c9ddaf194ec"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_RAND_C192 0x0f
```

相关声明：[BT_DATA_SIMPLE_PAIRING_RAND_C192](#ga280f1f96c5204960fe034c9ddaf194ec)。

简单配对随机数 R-192（Simple Pairing Randomizer R-192）。

<a id="r_gac9402c597e5b4497f4bcd22d5177cc23"></a>

```c
#define BT_DATA_DEVICE_ID 0x10
```

相关声明：[BT_DATA_DEVICE_ID](#gac9402c597e5b4497f4bcd22d5177cc23)。

设备 ID 配置文件（Device ID (Profile)）。

<a id="r_ga5014acb2fe8e76b855b55bf98abe6d05"></a>

```c
#define BT_DATA_SM_TK_VALUE 0x10
```

相关声明：[BT_DATA_SM_TK_VALUE](#ga5014acb2fe8e76b855b55bf98abe6d05)。

安全管理器临时密钥值（Security Manager TK Value）。

<a id="r_gaa12c742d1c955036aa3f55e84df69890"></a>

```c
#define BT_DATA_SM_OOB_FLAGS 0x11
```

相关声明：[BT_DATA_SM_OOB_FLAGS](#gaa12c742d1c955036aa3f55e84df69890)。

安全管理器带外标志（Security Manager OOB Flags）。

<a id="r_gabcf872eafc60c21287f6be63174dc7c8"></a>

```c
#define BT_DATA_PERIPHERAL_INT_RANGE 0x12
```

相关声明：[BT_DATA_PERIPHERAL_INT_RANGE](#gabcf872eafc60c21287f6be63174dc7c8)。

外设连接间隔范围（Peripheral Connection Interval Range）。

<a id="r_ga2ad4d2ec2ff29c0aad5159de12d3f741"></a>

```c
#define BT_DATA_SOLICIT16 0x14
```

相关声明：[BT_DATA_SOLICIT16](#ga2ad4d2ec2ff29c0aad5159de12d3f741)。

服务征询 UUID，16 位（Solicit UUIDs, 16-bit）。

<a id="r_ga217df3f70846e86fa09e5605d5acd291"></a>

```c
#define BT_DATA_SOLICIT128 0x15
```

相关声明：[BT_DATA_SOLICIT128](#ga217df3f70846e86fa09e5605d5acd291)。

服务征询 UUID，128 位（Solicit UUIDs, 128-bit）。

<a id="r_ga76990dda919688b369decaf9d3606b32"></a>

```c
#define BT_DATA_SVC_DATA16 0x16
```

相关声明：[BT_DATA_SVC_DATA16](#ga76990dda919688b369decaf9d3606b32)。

服务数据，16 位 UUID（Service data, 16-bit UUID）。

<a id="r_gacb867f0436d38c5c80e3426ca6247a46"></a>

```c
#define BT_DATA_PUB_TARGET_ADDR 0x17
```

相关声明：[BT_DATA_PUB_TARGET_ADDR](#gacb867f0436d38c5c80e3426ca6247a46)。

公共目标地址（Public Target Address）。

<a id="r_ga3d9097d8f53213ccafc152c51ad6fdbd"></a>

```c
#define BT_DATA_RAND_TARGET_ADDR 0x18
```

相关声明：[BT_DATA_RAND_TARGET_ADDR](#ga3d9097d8f53213ccafc152c51ad6fdbd)。

随机目标地址（Random Target Address）。

<a id="r_ga67fc721da05758b7d7a36aecaa035fac"></a>

```c
#define BT_DATA_GAP_APPEARANCE 0x19
```

相关声明：[BT_DATA_GAP_APPEARANCE](#ga67fc721da05758b7d7a36aecaa035fac)。

通用访问配置文件外观值（GAP appearance）。

<a id="r_ga6fd8c0f32bbcb97aaafee51fda0b601e"></a>

```c
#define BT_DATA_ADV_INT 0x1a
```

相关声明：[BT_DATA_ADV_INT](#ga6fd8c0f32bbcb97aaafee51fda0b601e)。

广播间隔（Advertising Interval）。

<a id="r_gad9e8a273239fa160a6b2797ef5563a94"></a>

```c
#define BT_DATA_LE_BT_DEVICE_ADDRESS 0x1b
```

相关声明：[BT_DATA_LE_BT_DEVICE_ADDRESS](#gad9e8a273239fa160a6b2797ef5563a94)。

低功耗蓝牙设备地址（LE Bluetooth Device Address）。

<a id="r_ga255c7cb16eb24b95fa0f531fc4574273"></a>

```c
#define BT_DATA_LE_ROLE 0x1c
```

相关声明：[BT_DATA_LE_ROLE](#ga255c7cb16eb24b95fa0f531fc4574273)。

低功耗蓝牙角色（LE Role）。

<a id="r_ga324f91521eacd1e9d579c9d52d02eb06"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_HASH 0x1d
```

相关声明：[BT_DATA_SIMPLE_PAIRING_HASH](#ga324f91521eacd1e9d579c9d52d02eb06)。

简单配对哈希 C256（Simple Pairing Hash C256）。

<a id="r_gad7e7dd2d3a972e53f9e5e80627bd07e6"></a>

```c
#define BT_DATA_SIMPLE_PAIRING_RAND 0x1e
```

相关声明：[BT_DATA_SIMPLE_PAIRING_RAND](#gad7e7dd2d3a972e53f9e5e80627bd07e6)。

简单配对随机数 R256（Simple Pairing Randomizer R256）。

<a id="r_ga76e7e8971ed841b87fda08793a00b14f"></a>

```c
#define BT_DATA_SOLICIT32 0x1f
```

相关声明：[BT_DATA_SOLICIT32](#ga76e7e8971ed841b87fda08793a00b14f)。

服务征询 UUID，32 位（Solicit UUIDs, 32-bit）。

<a id="r_ga7d411a723ff2f038c3b7a1e09c88cb3d"></a>

```c
#define BT_DATA_SVC_DATA32 0x20
```

相关声明：[BT_DATA_SVC_DATA32](#ga7d411a723ff2f038c3b7a1e09c88cb3d)。

服务数据，32 位 UUID（Service data, 32-bit UUID）。

<a id="r_gaa53847910515d9488b490f17a4fdf0d1"></a>

```c
#define BT_DATA_SVC_DATA128 0x21
```

相关声明：[BT_DATA_SVC_DATA128](#gaa53847910515d9488b490f17a4fdf0d1)。

服务数据，128 位 UUID（Service data, 128-bit UUID）。

<a id="r_ga883dda02c157f0de8157b1c5f66aafd0"></a>

```c
#define BT_DATA_LE_SC_CONFIRM_VALUE 0x22
```

相关声明：[BT_DATA_LE_SC_CONFIRM_VALUE](#ga883dda02c157f0de8157b1c5f66aafd0)。

低功耗安全连接确认值（LE SC Confirmation Value）。

<a id="r_gacbc31c67684e3c68481501cf89f9ec68"></a>

```c
#define BT_DATA_LE_SC_RANDOM_VALUE 0x23
```

相关声明：[BT_DATA_LE_SC_RANDOM_VALUE](#gacbc31c67684e3c68481501cf89f9ec68)。

低功耗安全连接随机值（LE SC Random Value）。

<a id="r_ga3c6a5903cc4a46aaf0b30a0de0179403"></a>

```c
#define BT_DATA_URI 0x24
```

相关声明：[BT_DATA_URI](#ga3c6a5903cc4a46aaf0b30a0de0179403)。

统一资源标识符（URI）。

<a id="r_ga0f29f9d8f5a336af430f0a603e87e995"></a>

```c
#define BT_DATA_INDOOR_POS 0x25
```

相关声明：[BT_DATA_INDOOR_POS](#ga0f29f9d8f5a336af430f0a603e87e995)。

室内定位（Indoor Positioning）。

<a id="r_ga8e9ccc669ee545152b2d9b3120692d55"></a>

```c
#define BT_DATA_TRANS_DISCOVER_DATA 0x26
```

相关声明：[BT_DATA_TRANS_DISCOVER_DATA](#ga8e9ccc669ee545152b2d9b3120692d55)。

传输发现数据（Transport Discovery Data）。

<a id="r_ga207bc1e5405a4fd3f39863a2cb304ebc"></a>

```c
#define BT_DATA_LE_SUPPORTED_FEATURES 0x27
```

相关声明：[BT_DATA_LE_SUPPORTED_FEATURES](#ga207bc1e5405a4fd3f39863a2cb304ebc)。

低功耗蓝牙支持的特性（LE Supported Features）。

<a id="r_gae3eb96c0f127b6417d7cad288faaaceb"></a>

```c
#define BT_DATA_CHANNEL_MAP_UPDATE_IND 0x28
```

相关声明：[BT_DATA_CHANNEL_MAP_UPDATE_IND](#gae3eb96c0f127b6417d7cad288faaaceb)。

信道映射更新指示（Channel Map Update Indication）。

<a id="r_gafc5984d58b0b54ee824dd83bc78dfbe9"></a>

```c
#define BT_DATA_MESH_PROV 0x29
```

相关声明：[BT_DATA_MESH_PROV](#gafc5984d58b0b54ee824dd83bc78dfbe9)。

网状网络配置协议数据单元（Mesh Provisioning PDU）。

<a id="r_gac351c67ab58520b796fa713602d9f602"></a>

```c
#define BT_DATA_MESH_MESSAGE 0x2a
```

相关声明：[BT_DATA_MESH_MESSAGE](#gac351c67ab58520b796fa713602d9f602)。

网状网络协议数据单元（Mesh Networking PDU）。

<a id="r_ga59cc479be1f6c61a4a47aa6f479fe67a"></a>

```c
#define BT_DATA_MESH_BEACON 0x2b
```

相关声明：[BT_DATA_MESH_BEACON](#ga59cc479be1f6c61a4a47aa6f479fe67a)。

网状网络信标（Mesh Beacon）。

<a id="r_ga16feb94cd09c04d020450f61646f5486"></a>

```c
#define BT_DATA_BIG_INFO 0x2c
```

相关声明：[BT_DATA_BIG_INFO](#ga16feb94cd09c04d020450f61646f5486)。

广播等时组信息（BIGInfo）。

<a id="r_ga72d2e55819db593a6db77579ebfe1e9d"></a>

```c
#define BT_DATA_BROADCAST_CODE 0x2d
```

相关声明：[BT_DATA_BROADCAST_CODE](#ga72d2e55819db593a6db77579ebfe1e9d)。

广播码（Broadcast Code）。

<a id="r_ga122da4184d606ae140f8a311aaebeedd"></a>

```c
#define BT_DATA_CSIS_RSI 0x2e
```

相关声明：[BT_DATA_CSIS_RSI](#ga122da4184d606ae140f8a311aaebeedd)。

协调集识别服务随机集 ID 类型（CSIS Random Set ID type）。

<a id="r_gad4ac2e0de80dddcacc4ca6d25765eebd"></a>

```c
#define BT_DATA_ADV_INT_LONG 0x2f
```

相关声明：[BT_DATA_ADV_INT_LONG](#gad4ac2e0de80dddcacc4ca6d25765eebd)。

长广播间隔（Advertising Interval long）。

<a id="r_ga7d781791bc85fe3c7ea839ff617ee6e7"></a>

```c
#define BT_DATA_BROADCAST_NAME 0x30
```

相关声明：[BT_DATA_BROADCAST_NAME](#ga7d781791bc85fe3c7ea839ff617ee6e7)。

广播名称（Broadcast Name）。

<a id="r_ga41d5c898144e89b6035f92ff506f38a3"></a>

```c
#define BT_DATA_ENCRYPTED_AD_DATA 0x31
```

相关声明：[BT_DATA_ENCRYPTED_AD_DATA](#ga41d5c898144e89b6035f92ff506f38a3)。

加密广播数据（Encrypted Advertising Data）。

<a id="r_ga14a8b1cf9d6c1c9749443a012731d39c"></a>

```c
#define BT_DATA_PAWR_TIMING_INFO 0x32
```

相关声明：[BT_DATA_PAWR_TIMING_INFO](#ga14a8b1cf9d6c1c9749443a012731d39c)。

周期广播响应时序信息（Periodic Advertising Response Timing Info）。

<a id="r_ga90c7a1175148f3a56b04dc0b29525a4d"></a>

```c
#define BT_DATA_ESL 0x34
```

相关声明：[BT_DATA_ESL](#ga90c7a1175148f3a56b04dc0b29525a4d)。

电子货架标签配置文件（Electronic Shelf Label Profile）。

<a id="r_gaecab0c77f9f912c16c264e7eaf2e4707"></a>

```c
#define BT_DATA_3D_INFO 0x3D
```

相关声明：[BT_DATA_3D_INFO](#gaecab0c77f9f912c16c264e7eaf2e4707)。

三维信息数据（3D Information Data）。

<a id="r_ga63b846807bff632b1cdd49b1e46e63b4"></a>

```c
#define BT_DATA_MANUFACTURER_DATA 0xff
```

相关声明：[BT_DATA_MANUFACTURER_DATA](#ga63b846807bff632b1cdd49b1e46e63b4)。

厂商专用数据（Manufacturer Specific Data）。

## 1.3\_标志数据类型的取值（Flags data type values）

<a id="r_ga36191ee000a2098fd679c398b31e0906"></a>

```c
#define BT_LE_AD_LIMITED 0x01
```

相关声明：[BT_LE_AD_LIMITED](#ga36191ee000a2098fd679c398b31e0906)。

有限可发现模式（Limited Discoverable）。

<a id="r_ga13d9b4a24e2a8b58402bfb21f8b782c8"></a>

```c
#define BT_LE_AD_GENERAL 0x02
```

相关声明：[BT_LE_AD_GENERAL](#ga13d9b4a24e2a8b58402bfb21f8b782c8)。

通用可发现模式（General Discoverable）。

<a id="r_gabf5725f481cb73cbd974f3653c904bc9"></a>

```c
#define BT_LE_AD_NO_BREDR 0x04
```

相关声明：[BT_LE_AD_NO_BREDR](#gabf5725f481cb73cbd974f3653c904bc9)。

不支持基本速率／增强数据率（BR/EDR not supported）。

## 1.4\_详细说明（Detailed Documentation）

<a id="gae7be5c3bf9ad97e34d6c62bb791c39c0"></a>

### `BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER`

```c
#define BT_APPEARANCE_AIRCRAFT_LARGE_PASSENGER 0x0984
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

大型客机（Large Passenger Aircraft）。

<a id="ga6f1d2fb56f53ac5317b024d7487b8742"></a>

### `BT_APPEARANCE_AIRCRAFT_LIGHT`

```c
#define BT_APPEARANCE_AIRCRAFT_LIGHT 0x0981
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

轻型飞机（Light Aircraft）。

<a id="gad2d0b1c4b710e50127049ec4cd299396"></a>

### `BT_APPEARANCE_AIRCRAFT_MICROLIGHT`

```c
#define BT_APPEARANCE_AIRCRAFT_MICROLIGHT 0x0982
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

超轻型飞机（Microlight）。

<a id="ga6f827322066333fe926f0912099e6903"></a>

### `BT_APPEARANCE_AIRCRAFT_PARAGLIDER`

```c
#define BT_APPEARANCE_AIRCRAFT_PARAGLIDER 0x0983
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

滑翔伞（Paraglider）。

<a id="gaeb66941a8e8b38ed0ea47305da157e24"></a>

### `BT_APPEARANCE_APPLIANCE_CLOTHES_IRON`

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_IRON 0x0909
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电熨斗（Clothes iron）。

<a id="ga0292c6123b655964311d0e6027b5af20"></a>

### `BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER`

```c
#define BT_APPEARANCE_APPLIANCE_CLOTHES_STEAMER 0x090F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

挂烫机（Clothes steamer）。

<a id="gac601c74c6132decf13527bdacbc5a08b"></a>

### `BT_APPEARANCE_APPLIANCE_COFFEE_MAKER`

```c
#define BT_APPEARANCE_APPLIANCE_COFFEE_MAKER 0x0908
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

咖啡机（Coffee maker）。

<a id="ga6a9885e9a2133c0732d056ecd63313ad"></a>

### `BT_APPEARANCE_APPLIANCE_CURLING_IRON`

```c
#define BT_APPEARANCE_APPLIANCE_CURLING_IRON 0x090A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

卷发棒（Curling iron）。

<a id="gaac26996e0de10b16e24900a08c1098f5"></a>

### `BT_APPEARANCE_APPLIANCE_DRYER`

```c
#define BT_APPEARANCE_APPLIANCE_DRYER 0x0907
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

烘干机（Dryer）。

<a id="ga6ec2458a171142a5e22ec339d23a5a0c"></a>

### `BT_APPEARANCE_APPLIANCE_FREEZER`

```c
#define BT_APPEARANCE_APPLIANCE_FREEZER 0x0902
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

冷冻柜（Freezer）。

<a id="ga15be0164f5883558fb61c9cb9679b78f"></a>

### `BT_APPEARANCE_APPLIANCE_HAIR_DRYER`

```c
#define BT_APPEARANCE_APPLIANCE_HAIR_DRYER 0x090B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吹风机（Hair dryer）。

<a id="gabaac12b866cd29547165331333e8be3d"></a>

### `BT_APPEARANCE_APPLIANCE_MICROWAVE`

```c
#define BT_APPEARANCE_APPLIANCE_MICROWAVE 0x0904
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

微波炉（Microwave）。

<a id="ga7a48c5a07e677167ae10412ed2c1040b"></a>

### `BT_APPEARANCE_APPLIANCE_OVEN`

```c
#define BT_APPEARANCE_APPLIANCE_OVEN 0x0903
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

烤箱（Oven）。

<a id="gad02c3dc8fa1321b14ee70264a36c4950"></a>

### `BT_APPEARANCE_APPLIANCE_REFRIGERATOR`

```c
#define BT_APPEARANCE_APPLIANCE_REFRIGERATOR 0x0901
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

冰箱（Refrigerator）。

<a id="ga78511e0ef7d509deeba65352e7f81ad8"></a>

### `BT_APPEARANCE_APPLIANCE_RICE_COOKER`

```c
#define BT_APPEARANCE_APPLIANCE_RICE_COOKER 0x090E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电饭煲（Rice cooker）。

<a id="ga423e85d0816a4bd0205f4d8188e6c406"></a>

### `BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER`

```c
#define BT_APPEARANCE_APPLIANCE_ROBOTIC_VACUUM_CLEANER 0x090D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

扫地机器人（Robotic vacuum cleaner）。

<a id="ga5b0d9632cb2ed4afd856f05a1e857394"></a>

### `BT_APPEARANCE_APPLIANCE_TOASTER`

```c
#define BT_APPEARANCE_APPLIANCE_TOASTER 0x0905
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

烤面包机（Toaster）。

<a id="ga46d5f18bb8c764c43af97fddcec4a1ec"></a>

### `BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER`

```c
#define BT_APPEARANCE_APPLIANCE_VACUUM_CLEANER 0x090C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吸尘器（Vacuum cleaner）。

<a id="ga1febcada2c95105648831094a4de6a8d"></a>

### `BT_APPEARANCE_APPLIANCE_WASHING_MACHINE`

```c
#define BT_APPEARANCE_APPLIANCE_WASHING_MACHINE 0x0906
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

洗衣机（Washing Machine）。

<a id="ga666aed968e9a0f9566edcc1bcba0bfbd"></a>

### `BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER`

```c
#define BT_APPEARANCE_AUDIO_SINK_BOOKSHELF_SPEAKER 0x0843
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

书架式音箱（Bookshelf Speaker）。

<a id="ga93e3a858b2efabea72a8855a28ad21c2"></a>

### `BT_APPEARANCE_AUDIO_SINK_SOUNDBAR`

```c
#define BT_APPEARANCE_AUDIO_SINK_SOUNDBAR 0x0842
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

条形音箱（Soundbar）。

<a id="gadd82602d251aa555a06123ef0388d1b1"></a>

### `BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE`

```c
#define BT_APPEARANCE_AUDIO_SINK_SPEAKERPHONE 0x0845
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

免提电话（Speakerphone）。

<a id="gabcb109c4660a177494329faf353406f4"></a>

### `BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER`

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDALONE_SPEAKER 0x0841
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

独立扬声器（Standalone Speaker）。

<a id="ga6b3ddddf1de7d95a15aa6194ddc656ee"></a>

### `BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER`

```c
#define BT_APPEARANCE_AUDIO_SINK_STANDMOUNTED_SPEAKER 0x0844
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

支架式音箱（Standmounted Speaker）。

<a id="gaa8d5a95cb181e27efb2409d5dce3da57"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_ALARM`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_ALARM 0x0882
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

警报器（Alarm）。

<a id="gac8ab0549f83c9d6b68dc4dd75cfe7b1e"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_AUDITORIUM 0x0889
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

礼堂（Auditorium）。

<a id="ga748b4fa86145f3950069ed44cde8cacb"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_BELL`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BELL 0x0883
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

铃（Bell）。

<a id="ga35ecc1a1051379010123582c82e9b31c"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_DEVICE 0x0885
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播设备（Broadcasting Device）。

<a id="gaad0fe38e5246c55cc562729448b9f390"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_BROADCASTING_ROOM 0x0888
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播室（Broadcasting Room）。

<a id="ga3415afbd526b29b5bbafc1ac889bd371"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_HORN`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_HORN 0x0884
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

号角（Horn）。

<a id="ga6ad3ee00ed05c8a7ed182df5c82a5af4"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_KIOSK`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_KIOSK 0x0887
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

自助服务终端（Kiosk）。

<a id="ga6dd1354de34ed79702d9d7878d859fcb"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_MICROPHONE 0x0881
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

麦克风（Microphone）。

<a id="ga48fc37d769211cba1e6121e670b02e25"></a>

### `BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK`

```c
#define BT_APPEARANCE_AUDIO_SOURCE_SERVICE_DESK 0x0886
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务台（Service Desk）。

<a id="ga7294c7b26ac8da3b9800c91ec824ad22"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_AMPLIFIER 0x09C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

放大器（Amplifier）。

<a id="ga1394bc80927fb8db4eef1786111c65c7"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_BLURAY_PLAYER 0x09C8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

蓝光播放器（Bluray Player）。

<a id="ga6c9ad45a9b22a94ae0cce16bfe749a33"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_CD_PLAYER 0x09C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

CD 播放器（CD Player）。

<a id="ga02681af8d755c701d9caef3f89a5c35a"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_DVD_PLAYER 0x09C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

DVD 播放器（DVD Player）。

<a id="gaa01c862bff9aaaad09ed925da60fcb25"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_OPTICAL_DISC_PLAYER 0x09C9
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

光盘播放器（Optical Disc Player）。

<a id="gad60d1a387a1c62218baa3044e5acc3db"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_RADIO`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RADIO 0x09C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

收音机（Radio）。

<a id="gac826e2e5326d1aa5fdd7ebf55fe395e6"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_RECEIVER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_RECEIVER 0x09C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

接收机（Receiver）。

<a id="gad0ac86cf291b781b772fa9e85dda283a"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_SET_TOP_BOX 0x09CA
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

机顶盒（Set-Top Box）。

<a id="ga7ccf41932861fa5f33d12060a12d5aa7"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_TUNER`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TUNER 0x09C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

调谐器（Tuner）。

<a id="ga69417cb3e9c434e751483328d6134cdf"></a>

### `BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE`

```c
#define BT_APPEARANCE_AV_EQUIPMENT_TURNTABLE 0x09C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

唱盘（Turntable）。

<a id="ga55c3e67d27c8fd8ae06880ccdd9259ce"></a>

### `BT_APPEARANCE_BLOOD_PRESSURE_ARM`

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_ARM 0x0381
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

臂式血压设备（Arm Blood Pressure）。

<a id="ga89684ca0544a400293b663cdf0063cfa"></a>

### `BT_APPEARANCE_BLOOD_PRESSURE_WRIST`

```c
#define BT_APPEARANCE_BLOOD_PRESSURE_WRIST 0x0382
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

腕式血压设备（Wrist Blood Pressure）。

<a id="gaa4d962ad8661c28ed48f5cf8cd75ad6e"></a>

### `BT_APPEARANCE_COMPUTER_ALL_IN_ONE`

```c
#define BT_APPEARANCE_COMPUTER_ALL_IN_ONE 0x0089
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

一体机（All in One）。

<a id="ga53e8eff26f2020b1fc89b21684e54698"></a>

### `BT_APPEARANCE_COMPUTER_BLADE_SERVER`

```c
#define BT_APPEARANCE_COMPUTER_BLADE_SERVER 0x008A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

刀片服务器（Blade Server）。

<a id="ga073dca362cabfd2a07cdc1cb787a0f58"></a>

### `BT_APPEARANCE_COMPUTER_CONVERTIBLE`

```c
#define BT_APPEARANCE_COMPUTER_CONVERTIBLE 0x008B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可翻转电脑（Convertible）。

<a id="ga1aa0565ca7e00e3a1aa8968e0a7f1bef"></a>

### `BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION`

```c
#define BT_APPEARANCE_COMPUTER_DESKTOP_WORKSTATION 0x0081
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

台式工作站（Desktop Workstation）。

<a id="ga8f35f76cc9de4170006669d6e9e7d72a"></a>

### `BT_APPEARANCE_COMPUTER_DETACHABLE`

```c
#define BT_APPEARANCE_COMPUTER_DETACHABLE 0x008C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

可拆卸电脑（Detachable）。

<a id="ga36187d2651d08c4b3e17c36565a2d3c9"></a>

### `BT_APPEARANCE_COMPUTER_DOCKING_STATION`

```c
#define BT_APPEARANCE_COMPUTER_DOCKING_STATION 0x0088
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

扩展坞（Docking Station）。

<a id="gab64312ea16f03c5998db4429b194b8b0"></a>

### `BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA`

```c
#define BT_APPEARANCE_COMPUTER_HANDHELD_PCPDA 0x0084
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

翻盖式手持电脑／个人数字助理（Handheld PC/PDA (clamshell)）。

<a id="ga6ae353795476853bc3be2196ed220aa7"></a>

### `BT_APPEARANCE_COMPUTER_IOT_GATEWAY`

```c
#define BT_APPEARANCE_COMPUTER_IOT_GATEWAY 0x008D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

物联网网关（IoT Gateway）。

<a id="ga55ce2ad96a153ed6bdfd841276145c28"></a>

### `BT_APPEARANCE_COMPUTER_LAPTOP`

```c
#define BT_APPEARANCE_COMPUTER_LAPTOP 0x0083
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

笔记本电脑（Laptop）。

<a id="ga3c47c11f56eabec15e960662c64f6fcb"></a>

### `BT_APPEARANCE_COMPUTER_MINI_PC`

```c
#define BT_APPEARANCE_COMPUTER_MINI_PC 0x008E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

迷你电脑（Mini PC）。

<a id="ga9340ed60911fc7c5aab7d317b6925c10"></a>

### `BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA`

```c
#define BT_APPEARANCE_COMPUTER_PALMSIZE_PCPDA 0x0085
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

掌上电脑／个人数字助理（Palm­size PC/PDA）。

<a id="gab71a3c3f836561ac7bd8e52f5e01c769"></a>

### `BT_APPEARANCE_COMPUTER_SERVER_CLASS`

```c
#define BT_APPEARANCE_COMPUTER_SERVER_CLASS 0x0082
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务器级计算机（Server-class Computer）。

<a id="gabb53daf3eb4ac9ba0cbb1614056ee214"></a>

### `BT_APPEARANCE_COMPUTER_STICK_PC`

```c
#define BT_APPEARANCE_COMPUTER_STICK_PC 0x008F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

棒式电脑（Stick PC）。

<a id="ga11bc881cb5f88956edbf2bb2fe5b358c"></a>

### `BT_APPEARANCE_COMPUTER_TABLET`

```c
#define BT_APPEARANCE_COMPUTER_TABLET 0x0087
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

平板电脑（Tablet）。

<a id="ga7c6667ba4c68dec380a548ba9530c110"></a>

### `BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER`

```c
#define BT_APPEARANCE_COMPUTER_WEARABLE_COMPUTER 0x0086
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

手表大小的可穿戴计算机（Wearable computer (watch size)）。

<a id="gab77dd4cfe254df84cbe0b8d45247e198"></a>

### `BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR`

```c
#define BT_APPEARANCE_CONTINUOUS_GLUCOSE_MONITOR 0x0D00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

连续血糖监测仪（Continuous Glucose Monitor）。

<a id="ga8e21f7df9d789b7c3aa6f7dab500df8c"></a>

### `BT_APPEARANCE_CONTROL_ACCESS_DOOR`

```c
#define BT_APPEARANCE_CONTROL_ACCESS_DOOR 0x0701
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

出入门（Access Door）。

<a id="gac2f588b6202e9d6140ec682cfe45f65d"></a>

### `BT_APPEARANCE_CONTROL_ACCESS_LOCK`

```c
#define BT_APPEARANCE_CONTROL_ACCESS_LOCK 0x0704
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

门禁锁（Access Lock）。

<a id="gaea669671a53b3df5b1aa4c43e5bde9b9"></a>

### `BT_APPEARANCE_CONTROL_BATTERY_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_BATTERY_SWITCH 0x04CA
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电池供电开关（Battery Switch）。

<a id="ga52dfd2858663b7ab624f0c4b08cee7dc"></a>

### `BT_APPEARANCE_CONTROL_BUTTON`

```c
#define BT_APPEARANCE_CONTROL_BUTTON 0x04C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

按钮（Button）。

<a id="ga29d07ce1101740b5f6f980660e405278"></a>

### `BT_APPEARANCE_CONTROL_DOOR_LOCK`

```c
#define BT_APPEARANCE_CONTROL_DOOR_LOCK 0x0708
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

门锁（Door Lock）。

<a id="gac1c80dbb8aaa327b6125bf632692c3be"></a>

### `BT_APPEARANCE_CONTROL_DOUBLE_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_DOUBLE_SWITCH 0x04C8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

双联开关（Double Switch）。

<a id="ga321d63ead349c0a83ef289bd2e4efb33"></a>

### `BT_APPEARANCE_CONTROL_ELEVATOR`

```c
#define BT_APPEARANCE_CONTROL_ELEVATOR 0x0705
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电梯（Elevator）。

<a id="ga2b6c7987ee4040216a385e665ff92321"></a>

### `BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR`

```c
#define BT_APPEARANCE_CONTROL_EMERGENCY_EXIT_DOOR 0x0703
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

紧急出口门（Emergency Exit Door）。

<a id="gadec2907a822e302d5027f162ef9ce4b6"></a>

### `BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_ENERGY_HARVESTING_SWITCH 0x04CB
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

能量采集开关（Energy Harvesting Switch）。

<a id="gab2a476a90f20576c0a1784fdc1e5e633"></a>

### `BT_APPEARANCE_CONTROL_ENTRANCE_GATE`

```c
#define BT_APPEARANCE_CONTROL_ENTRANCE_GATE 0x0707
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

入口大门（Entrance Gate）。

<a id="ga39134568b56c1d33e6567c893eb441f1"></a>

### `BT_APPEARANCE_CONTROL_GARAGE_DOOR`

```c
#define BT_APPEARANCE_CONTROL_GARAGE_DOOR 0x0702
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

车库门（Garage Door）。

<a id="ga824236ba19c7f54d06b9abcd7df8c767"></a>

### `BT_APPEARANCE_CONTROL_LOCKER`

```c
#define BT_APPEARANCE_CONTROL_LOCKER 0x0709
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

储物柜（Locker）。

<a id="gad30c40df58e160128893e545a11ab44c"></a>

### `BT_APPEARANCE_CONTROL_MULTI_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_MULTI_SWITCH 0x04C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

多联开关（Multi-switch）。

<a id="ga9bb358864e1388cc00502b5586ec581f"></a>

### `BT_APPEARANCE_CONTROL_PUSH_BUTTON`

```c
#define BT_APPEARANCE_CONTROL_PUSH_BUTTON 0x04CC
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

按压按钮（Push Button）。

<a id="ga946b6a8bb49bf0b5cd3ded93ee8dfe89"></a>

### `BT_APPEARANCE_CONTROL_ROTARY_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_ROTARY_SWITCH 0x04C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

旋转开关（Rotary Switch）。

<a id="ga979ca0f4febeaa55daec07e2b3b0179e"></a>

### `BT_APPEARANCE_CONTROL_SINGLE_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_SINGLE_SWITCH 0x04C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

单联开关（Single Switch）。

<a id="gaa849d890c000defcaf29893296c86cc5"></a>

### `BT_APPEARANCE_CONTROL_SLIDER`

```c
#define BT_APPEARANCE_CONTROL_SLIDER 0x04C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

滑块（Slider）。

<a id="gac53247d00e3da69595274e0b94fa670f"></a>

### `BT_APPEARANCE_CONTROL_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_SWITCH 0x04C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

开关（Switch）。

<a id="ga4d5763288557e7b7f6da0f3e9831171d"></a>

### `BT_APPEARANCE_CONTROL_TOUCH_PANEL`

```c
#define BT_APPEARANCE_CONTROL_TOUCH_PANEL 0x04C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

触摸面板（Touch Panel）。

<a id="gaa532fd1bd67c2c5b72822704a62df143"></a>

### `BT_APPEARANCE_CONTROL_TRIPLE_SWITCH`

```c
#define BT_APPEARANCE_CONTROL_TRIPLE_SWITCH 0x04C9
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

三联开关（Triple Switch）。

<a id="gaedc6415432862889e7f002fc9ef46b74"></a>

### `BT_APPEARANCE_CONTROL_WINDOW`

```c
#define BT_APPEARANCE_CONTROL_WINDOW 0x0706
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

窗户（Window）。

<a id="ga71dc370aad015e88fce7c3e758c647ed"></a>

### `BT_APPEARANCE_CYCLING_CADENCE`

```c
#define BT_APPEARANCE_CYCLING_CADENCE 0x0483
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

踏频传感器（Cadence Sensor）。

<a id="ga3e81dce23c3d005a9b48ff83c7b8f896"></a>

### `BT_APPEARANCE_CYCLING_COMPUTER`

```c
#define BT_APPEARANCE_CYCLING_COMPUTER 0x0481
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

自行车码表（Cycling Computer）。

<a id="ga02fd9566d9b932aeaa1163d312fbc4d8"></a>

### `BT_APPEARANCE_CYCLING_POWER`

```c
#define BT_APPEARANCE_CYCLING_POWER 0x0484
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

功率传感器（Power Sensor）。

<a id="ga16fb08fa70272252ab6b2d3a5aec485a"></a>

### `BT_APPEARANCE_CYCLING_SPEED`

```c
#define BT_APPEARANCE_CYCLING_SPEED 0x0482
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

速度传感器（Speed Sensor）。

<a id="ga48d8f2a285795785f8f51ce220d46371"></a>

### `BT_APPEARANCE_CYCLING_SPEED_CADENCE`

```c
#define BT_APPEARANCE_CYCLING_SPEED_CADENCE 0x0485
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

速度与踏频传感器（Speed and Cadence Sensor）。

<a id="gabbcb0fbbeb6423052db9d5e04410499c"></a>

### `BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR`

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_MONITOR 0x0A02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

监视器（Monitor）。

<a id="gaa98f5139c99b46515746fb76e9ae7f9b"></a>

### `BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR`

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_PROJECTOR 0x0A03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

投影仪（Projector）。

<a id="ga9a6684aa8677575625e049fa0da2c26c"></a>

### `BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION`

```c
#define BT_APPEARANCE_DISPLAY_EQUIPMENT_TELEVISION 0x0A01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电视机（Television）。

<a id="ga32dd73ffa211d632617018aa510b89c4"></a>

### `BT_APPEARANCE_FAN_AXIAL`

```c
#define BT_APPEARANCE_FAN_AXIAL 0x05C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

轴流风扇（Axial Fan）。

<a id="ga8cd83cd08846ac276cc65f31333ee62e"></a>

### `BT_APPEARANCE_FAN_CEILING`

```c
#define BT_APPEARANCE_FAN_CEILING 0x05C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吊扇（Ceiling Fan）。

<a id="gaa9e17b8b5e06d2fb365bf152e0cbef5d"></a>

### `BT_APPEARANCE_FAN_DESK`

```c
#define BT_APPEARANCE_FAN_DESK 0x05C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

桌面风扇（Desk Fan）。

<a id="ga1e842c97b90678908f4d18c86c1227c2"></a>

### `BT_APPEARANCE_FAN_EXHAUST`

```c
#define BT_APPEARANCE_FAN_EXHAUST 0x05C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

排气扇（Exhaust Fan）。

<a id="ga2e54f8de862435f2dbd7f56b98615c84"></a>

### `BT_APPEARANCE_FAN_PEDESTAL`

```c
#define BT_APPEARANCE_FAN_PEDESTAL 0x05C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

落地风扇（Pedestal Fan）。

<a id="ga498be79799cb778c9df6629411fe32ad"></a>

### `BT_APPEARANCE_FAN_WALL`

```c
#define BT_APPEARANCE_FAN_WALL 0x05C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

壁扇（Wall Fan）。

<a id="gac856a99a5db04dc20229a6e60a18d310"></a>

### `BT_APPEARANCE_GENERIC_ACCESS_CONTROL`

```c
#define BT_APPEARANCE_GENERIC_ACCESS_CONTROL 0x0700
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用门禁控制设备（Generic Access Control）。

<a id="gaa13ae6496d47df2be0a0692a28806007"></a>

### `BT_APPEARANCE_GENERIC_AIR_CONDITIONING`

```c
#define BT_APPEARANCE_GENERIC_AIR_CONDITIONING 0x0640
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用空调设备（Generic Air Conditioning）。

<a id="ga24c9bcf9646ec5049abf310b31ab355e"></a>

### `BT_APPEARANCE_GENERIC_AIRCRAFT`

```c
#define BT_APPEARANCE_GENERIC_AIRCRAFT 0x0980
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用航空器（Generic Aircraft）。

<a id="ga32bb0f06096ce5259676a31342b9f0d9"></a>

### `BT_APPEARANCE_GENERIC_AUDIO_SINK`

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SINK 0x0840
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频接收端（Generic Audio Sink）。

<a id="gac85b90f2585044d0efa61191dba3c596"></a>

### `BT_APPEARANCE_GENERIC_AUDIO_SOURCE`

```c
#define BT_APPEARANCE_GENERIC_AUDIO_SOURCE 0x0880
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音频源（Generic Audio Source）。

<a id="gadb3b07d6c3d3f679b15069fdd8d4e1ee"></a>

### `BT_APPEARANCE_GENERIC_AV_EQUIPMENT`

```c
#define BT_APPEARANCE_GENERIC_AV_EQUIPMENT 0x09C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用音视频设备（Generic AV Equipment）。

<a id="gadca19a01611ca83e18156bb540dd96c1"></a>

### `BT_APPEARANCE_GENERIC_BARCODE_SCANNER`

```c
#define BT_APPEARANCE_GENERIC_BARCODE_SCANNER 0x02C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用条码扫描器（Generic Barcode Scanner）。

<a id="ga3ab7a9595e00208a9e6a56dca99b56c2"></a>

### `BT_APPEARANCE_GENERIC_BLOOD_PRESSURE`

```c
#define BT_APPEARANCE_GENERIC_BLOOD_PRESSURE 0x0380
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用血压设备（Generic Blood Pressure）。

<a id="ga100d26d6b9e9a3af925d64c0b006c6bd"></a>

### `BT_APPEARANCE_GENERIC_CLOCK`

```c
#define BT_APPEARANCE_GENERIC_CLOCK 0x0100
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用时钟（Generic Clock）。

<a id="ga6b74ad86efc0e9a745f2c9e64079b1cd"></a>

### `BT_APPEARANCE_GENERIC_COMPUTER`

```c
#define BT_APPEARANCE_GENERIC_COMPUTER 0x0080
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用计算机（Generic Computer）。

<a id="ga5e16df5eefcae8556dfc387135e2b1b6"></a>

### `BT_APPEARANCE_GENERIC_CONTROL_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_CONTROL_DEVICE 0x04C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用控制设备（Generic Control Device）。

<a id="ga7a0463b9b0df37bce80cada38b10ee54"></a>

### `BT_APPEARANCE_GENERIC_CYCLING`

```c
#define BT_APPEARANCE_GENERIC_CYCLING 0x0480
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用骑行设备（Generic Cycling）。

<a id="ga0a21cb58861a48875002af38ee82ac08"></a>

### `BT_APPEARANCE_GENERIC_DISPLAY`

```c
#define BT_APPEARANCE_GENERIC_DISPLAY 0x0140
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用显示器（Generic Display）。

<a id="ga44b70b2f515416baf686b1e127ef4375"></a>

### `BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT`

```c
#define BT_APPEARANCE_GENERIC_DISPLAY_EQUIPMENT 0x0A00
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用显示设备（Generic Display Equipment）。

<a id="gac08b31ff9b618b19e4c1b43ae2056b5f"></a>

### `BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE`

```c
#define BT_APPEARANCE_GENERIC_DOMESTIC_APPLIANCE 0x0900
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用家用电器（Generic Domestic Appliance）。

<a id="gab2b5f6385662519a2ece8fb654a6194b"></a>

### `BT_APPEARANCE_GENERIC_EYEGLASSES`

```c
#define BT_APPEARANCE_GENERIC_EYEGLASSES 0x01C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用眼镜（Generic Eye-glasses）。

<a id="ga82cc89321c4f4ffbf3ef25eff624943c"></a>

### `BT_APPEARANCE_GENERIC_FAN`

```c
#define BT_APPEARANCE_GENERIC_FAN 0x05C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用风扇（Generic Fan）。

<a id="gaca727b215a8277d921c0a3bfeccb3f14"></a>

### `BT_APPEARANCE_GENERIC_GAMING`

```c
#define BT_APPEARANCE_GENERIC_GAMING 0x0A80
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用游戏设备（Generic Gaming）。

<a id="ga209645f7445873beb50c388cc82aff2a"></a>

### `BT_APPEARANCE_GENERIC_GLUCOSE`

```c
#define BT_APPEARANCE_GENERIC_GLUCOSE 0x0400
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用血糖仪（Generic Glucose Meter）。

<a id="gadb5595a41edf5974e03649a675618b7b"></a>

### `BT_APPEARANCE_GENERIC_HEARING_AID`

```c
#define BT_APPEARANCE_GENERIC_HEARING_AID 0x0A40
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用助听器（Generic Hearing aid）。

<a id="gac5bdf195b81215932848151d765e84d6"></a>

### `BT_APPEARANCE_GENERIC_HEART_RATE`

```c
#define BT_APPEARANCE_GENERIC_HEART_RATE 0x0340
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用心率传感器（Generic Heart Rate Sensor）。

<a id="ga8ea92ea92ca4e2bad4e5e2baba1271dd"></a>

### `BT_APPEARANCE_GENERIC_HEATING`

```c
#define BT_APPEARANCE_GENERIC_HEATING 0x06C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用供暖设备（Generic Heating）。

<a id="gaf2050baedf0863ec37177dd2ef872d39"></a>

### `BT_APPEARANCE_GENERIC_HID`

```c
#define BT_APPEARANCE_GENERIC_HID 0x03C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用人机接口设备（Generic Human Interface Device）。

<a id="ga0b552243744bc598467421555e935cd0"></a>

### `BT_APPEARANCE_GENERIC_HUMIDIFIER`

```c
#define BT_APPEARANCE_GENERIC_HUMIDIFIER 0x0680
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用加湿器（Generic Humidifier）。

<a id="gaf1f01946f6acadcaf719d3d7cc06e55f"></a>

### `BT_APPEARANCE_GENERIC_HVAC`

```c
#define BT_APPEARANCE_GENERIC_HVAC 0x0600
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用暖通空调设备（Generic HVAC）。

<a id="ga481169a27fab19628f81a68af31d543c"></a>

### `BT_APPEARANCE_GENERIC_INSULIN_PUMP`

```c
#define BT_APPEARANCE_GENERIC_INSULIN_PUMP 0x0D40
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用胰岛素泵（Generic Insulin Pump）。

<a id="gaf73b11c4dbf366a854b4c68e802e3c1c"></a>

### `BT_APPEARANCE_GENERIC_KEYRING`

```c
#define BT_APPEARANCE_GENERIC_KEYRING 0x0240
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用钥匙圈（Generic Keyring）。

<a id="gae01be867f730c06b59fcb03289ae66d7"></a>

### `BT_APPEARANCE_GENERIC_LIGHT_FIXTURES`

```c
#define BT_APPEARANCE_GENERIC_LIGHT_FIXTURES 0x0580
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用照明灯具（Generic Light Fixtures）。

<a id="gacb3340c5193588eea2d42fe1bef443d0"></a>

### `BT_APPEARANCE_GENERIC_LIGHT_SOURCE`

```c
#define BT_APPEARANCE_GENERIC_LIGHT_SOURCE 0x07C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用光源（Generic Light Source）。

<a id="ga17e94209c0c96b5ca039b1613de0d05e"></a>

### `BT_APPEARANCE_GENERIC_MEDIA_PLAYER`

```c
#define BT_APPEARANCE_GENERIC_MEDIA_PLAYER 0x0280
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用媒体播放器（Generic Media Player）。

<a id="ga08453eebe2ae8f53deddaa64a029c2b5"></a>

### `BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY`

```c
#define BT_APPEARANCE_GENERIC_MEDICATION_DELIVERY 0x0D80
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用药物输送设备（Generic Medication Delivery）。

<a id="ga414b202e93d1db533853093d66603720"></a>

### `BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_DEVICE 0x0740
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电动设备（Generic Motorized Device）。

<a id="ga49328394fd7505da9476d4d62ae60c03"></a>

### `BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE`

```c
#define BT_APPEARANCE_GENERIC_MOTORIZED_VEHICLE 0x08C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用机动车辆（Generic Motorized Vehicle）。

<a id="gac4727ec720344ece687256ac517800e7"></a>

### `BT_APPEARANCE_GENERIC_NETWORK_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_NETWORK_DEVICE 0x0500
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用网络设备（Generic Network Device）。

<a id="ga0d39ca2892bd96013b8c82111eecc1cb"></a>

### `BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS`

```c
#define BT_APPEARANCE_GENERIC_OUTDOOR_SPORTS 0x1440
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用户外运动设备（Generic Outdoor Sports Activity）。

<a id="ga7387d717c77b38374e981991278aeb1c"></a>

### `BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_PERSONAL_MOBILITY_DEVICE 0x0CC0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用个人助行设备（Generic Personal Mobility Device）。

<a id="gae7061e78f960563af6e1b3dea71655a9"></a>

### `BT_APPEARANCE_GENERIC_PHONE`

```c
#define BT_APPEARANCE_GENERIC_PHONE 0x0040
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电话（Generic Phone）。

<a id="gadae82e45d9aafd34cafd3f0e793b1b24"></a>

### `BT_APPEARANCE_GENERIC_POWER_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_POWER_DEVICE 0x0780
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用电源设备（Generic Power Device）。

<a id="ga93ee753bf3b8819239041c065eaf024f"></a>

### `BT_APPEARANCE_GENERIC_PULSE_OXIMETER`

```c
#define BT_APPEARANCE_GENERIC_PULSE_OXIMETER 0x0C40
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用脉搏血氧仪（Generic Pulse Oximeter）。

<a id="ga0b47897768b27d26b8687dd2ab28703b"></a>

### `BT_APPEARANCE_GENERIC_REMOTE`

```c
#define BT_APPEARANCE_GENERIC_REMOTE 0x0180
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用遥控器（Generic Remote Control）。

<a id="gab3241fe012482e716c3f18e2962ca15d"></a>

### `BT_APPEARANCE_GENERIC_SENSOR`

```c
#define BT_APPEARANCE_GENERIC_SENSOR 0x0540
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用传感器（Generic Sensor）。

<a id="gabc243c7449804749704c1862db286eab"></a>

### `BT_APPEARANCE_GENERIC_SIGNAGE`

```c
#define BT_APPEARANCE_GENERIC_SIGNAGE 0x0AC0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用标识设备（Generic Signage）。

<a id="ga1332c44cc3371fa9006993d03ba4ae12"></a>

### `BT_APPEARANCE_GENERIC_SPIROMETER`

```c
#define BT_APPEARANCE_GENERIC_SPIROMETER 0x0DC0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用肺量计（Generic Spirometer）。

<a id="gaca6d810977e6da1a3174ee2b6b36662d"></a>

### `BT_APPEARANCE_GENERIC_TAG`

```c
#define BT_APPEARANCE_GENERIC_TAG 0x0200
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用标签（Generic Tag）。

<a id="ga2e0fde88d83e1f4533d69c8dc472255f"></a>

### `BT_APPEARANCE_GENERIC_THERMOMETER`

```c
#define BT_APPEARANCE_GENERIC_THERMOMETER 0x0300
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用温度计（Generic Thermometer）。

<a id="ga9cf19d97db0c4c5b8473b72809b51d42"></a>

### `BT_APPEARANCE_GENERIC_WALKING`

```c
#define BT_APPEARANCE_GENERIC_WALKING 0x0440
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用跑步／步行传感器（Generic Running Walking Sensor）。

<a id="ga0c512fd6aa5d35e78f02176073f5f121"></a>

### `BT_APPEARANCE_GENERIC_WATCH`

```c
#define BT_APPEARANCE_GENERIC_WATCH 0x00C0
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用手表（Generic Watch）。

<a id="gabad761094a16873dcebbc6238825d84b"></a>

### `BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE`

```c
#define BT_APPEARANCE_GENERIC_WEARABLE_AUDIO_DEVICE 0x0940
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用可穿戴音频设备（Generic Wearable Audio Device）。

<a id="ga1aec23cd4f531a57260c7c8faf9caf40"></a>

### `BT_APPEARANCE_GENERIC_WEIGHT_SCALE`

```c
#define BT_APPEARANCE_GENERIC_WEIGHT_SCALE 0x0C80
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用体重秤（Generic Weight Scale）。

<a id="ga1e70d961fca2719243c866464132684c"></a>

### `BT_APPEARANCE_GENERIC_WINDOW_COVERING`

```c
#define BT_APPEARANCE_GENERIC_WINDOW_COVERING 0x0800
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用窗户遮蔽物（Generic Window Covering）。

<a id="ga1fa6231e14dcfa90a5518e61f0e4e302"></a>

### `BT_APPEARANCE_HEARING_AID_BEHIND_EAR`

```c
#define BT_APPEARANCE_HEARING_AID_BEHIND_EAR 0x0A42
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耳后式助听器（Behind-ear hearing aid）。

<a id="ga82ba79bd9fd04a3fbdb6d8b4e35e3877"></a>

### `BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT`

```c
#define BT_APPEARANCE_HEARING_AID_COCHLEAR_IMPLANT 0x0A43
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

人工耳蜗（Cochlear Implant）。

<a id="ga28cc6555937d9d5a9e8ae0079fc8a534"></a>

### `BT_APPEARANCE_HEARING_AID_IN_EAR`

```c
#define BT_APPEARANCE_HEARING_AID_IN_EAR 0x0A41
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耳内式助听器（In-ear hearing aid）。

<a id="ga895f6570a09f3eee8d821eca57cdeb03"></a>

### `BT_APPEARANCE_HEART_RATE_BELT`

```c
#define BT_APPEARANCE_HEART_RATE_BELT 0x0341
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

心率带（Heart Rate Belt）。

<a id="gac74bc8e109f5d9b4c0988ee6378ed471"></a>

### `BT_APPEARANCE_HEATING_AIR_CURTAIN`

```c
#define BT_APPEARANCE_HEATING_AIR_CURTAIN 0x06C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

空气幕（Air Curtain）。

<a id="gac1abc9ae0b8ede2197720ea9e67b692e"></a>

### `BT_APPEARANCE_HEATING_BOILER`

```c
#define BT_APPEARANCE_HEATING_BOILER 0x06C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

锅炉（Boiler）。

<a id="ga995ca18db114ea062df0d76c9e241937"></a>

### `BT_APPEARANCE_HEATING_FAN_HEATER`

```c
#define BT_APPEARANCE_HEATING_FAN_HEATER 0x06C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

暖风机（Fan Heater）。

<a id="ga99537968fdc7e680d922ca309fba7678"></a>

### `BT_APPEARANCE_HEATING_HEAT_PUMP`

```c
#define BT_APPEARANCE_HEATING_HEAT_PUMP 0x06C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

热泵（Heat Pump）。

<a id="ga8e40496a351c7ec5ea836805925f1e13"></a>

### `BT_APPEARANCE_HEATING_INFRARED_HEATER`

```c
#define BT_APPEARANCE_HEATING_INFRARED_HEATER 0x06C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

红外加热器（Infrared Heater）。

<a id="ga46fe051c7e50492dba5ae824e154cf69"></a>

### `BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER`

```c
#define BT_APPEARANCE_HEATING_RADIANT_PANEL_HEATER 0x06C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

辐射板式加热器（Radiant Panel Heater）。

<a id="ga05b0b91c74aed5bc73a92f336bdae33a"></a>

### `BT_APPEARANCE_HEATING_RADIATOR`

```c
#define BT_APPEARANCE_HEATING_RADIATOR 0x06C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

散热暖气片（Radiator）。

<a id="gaf88f83afd454fe88dd7146e10ef6d35e"></a>

### `BT_APPEARANCE_HID_BARCODE_SCANNER`

```c
#define BT_APPEARANCE_HID_BARCODE_SCANNER 0x03C8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

条码扫描器（Barcode Scanner）。

<a id="gaa03c3b4d7ea8211748316146afab8bd4"></a>

### `BT_APPEARANCE_HID_CARD_READER`

```c
#define BT_APPEARANCE_HID_CARD_READER 0x03C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

读卡器（Card Reader）。

<a id="ga002a1d7965b23ec62c8a196f4e5452d9"></a>

### `BT_APPEARANCE_HID_DIGITAL_PEN`

```c
#define BT_APPEARANCE_HID_DIGITAL_PEN 0x03C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

数字笔（Digital Pen）。

<a id="gacac11dcb96ab60963a1118e171a731de"></a>

### `BT_APPEARANCE_HID_DIGITIZER_TABLET`

```c
#define BT_APPEARANCE_HID_DIGITIZER_TABLET 0x03C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

数字化绘图板（Digitizer Tablet）。

<a id="ga770336524e74d106cb18354f9dbfad76"></a>

### `BT_APPEARANCE_HID_GAMEPAD`

```c
#define BT_APPEARANCE_HID_GAMEPAD 0x03C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

游戏手柄（Gamepad）。

<a id="ga2f9f15df2260a1307f5142f37437bf0c"></a>

### `BT_APPEARANCE_HID_JOYSTICK`

```c
#define BT_APPEARANCE_HID_JOYSTICK 0x03C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

操纵杆（Joystick）。

<a id="gaa74af272423a80d5489ed8cf6c3ee66c"></a>

### `BT_APPEARANCE_HID_KEYBOARD`

```c
#define BT_APPEARANCE_HID_KEYBOARD 0x03C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

键盘（Keyboard）。

<a id="ga3b6ba8ffe424db08583186c448e37149"></a>

### `BT_APPEARANCE_HID_MOUSE`

```c
#define BT_APPEARANCE_HID_MOUSE 0x03C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

鼠标（Mouse）。

<a id="gae415dd9e8d620dfd1981719f4ed2d796"></a>

### `BT_APPEARANCE_HID_PRESENTATION_REMOTE`

```c
#define BT_APPEARANCE_HID_PRESENTATION_REMOTE 0x03CA
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

演示遥控器（Presentation Remote）。

<a id="gaee207f9434bce7d0f7e096bf3b37a01c"></a>

### `BT_APPEARANCE_HID_TOUCHPAD`

```c
#define BT_APPEARANCE_HID_TOUCHPAD 0x03C9
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

触摸板（Touchpad）。

<a id="ga8fbaf0fced0cce12e08c4a516351b166"></a>

### `BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE`

```c
#define BT_APPEARANCE_HOME_VIDEO_GAME_CONSOLE 0x0A81
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

家用电子游戏机（Home Video Game Console）。

<a id="ga182ade4b2c8f4705ba132248e504bb95"></a>

### `BT_APPEARANCE_HVAC_AIR_CURTAIN`

```c
#define BT_APPEARANCE_HVAC_AIR_CURTAIN 0x060B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

空气幕（Air Curtain）。

<a id="gacc28a1bc1a809c574019455de4ac9d0b"></a>

### `BT_APPEARANCE_HVAC_BOILER`

```c
#define BT_APPEARANCE_HVAC_BOILER 0x0606
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

锅炉（Boiler）。

<a id="gaa3b96e44638048b8891a2dece29f4b3f"></a>

### `BT_APPEARANCE_HVAC_DEHUMIDIFIER`

```c
#define BT_APPEARANCE_HVAC_DEHUMIDIFIER 0x0603
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

除湿机（De-humidifier）。

<a id="ga2a044c3369ed48d216707f6e6a541a23"></a>

### `BT_APPEARANCE_HVAC_FAN_HEATER`

```c
#define BT_APPEARANCE_HVAC_FAN_HEATER 0x060A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

暖风机（Fan Heater）。

<a id="gaead4ebeabb8855111ab9080aca4e035a"></a>

### `BT_APPEARANCE_HVAC_HEAT_PUMP`

```c
#define BT_APPEARANCE_HVAC_HEAT_PUMP 0x0607
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

热泵（Heat Pump）。

<a id="gacef9145f435d10cbf5a775b9a2c9b756"></a>

### `BT_APPEARANCE_HVAC_HEATER`

```c
#define BT_APPEARANCE_HVAC_HEATER 0x0604
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

加热器（Heater）。

<a id="gaf55f3f3f07cc78509e7fe19cea6cea4e"></a>

### `BT_APPEARANCE_HVAC_HUMIDIFIER`

```c
#define BT_APPEARANCE_HVAC_HUMIDIFIER 0x0602
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

加湿器（Humidifier）。

<a id="ga50c5df52d8471fc8e1dc65e31079566d"></a>

### `BT_APPEARANCE_HVAC_INFRARED_HEATER`

```c
#define BT_APPEARANCE_HVAC_INFRARED_HEATER 0x0608
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

红外加热器（Infrared Heater）。

<a id="gad43d27ff96a7fba1ed7d5e20ebd472d9"></a>

### `BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER`

```c
#define BT_APPEARANCE_HVAC_RADIANT_PANEL_HEATER 0x0609
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

辐射板式加热器（Radiant Panel Heater）。

<a id="gad90f108f3d33d68e27ac545cdb520f18"></a>

### `BT_APPEARANCE_HVAC_RADIATOR`

```c
#define BT_APPEARANCE_HVAC_RADIATOR 0x0605
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

散热暖气片（Radiator）。

<a id="ga33055b50c10bfc713b18823fca525488"></a>

### `BT_APPEARANCE_HVAC_THERMOSTAT`

```c
#define BT_APPEARANCE_HVAC_THERMOSTAT 0x0601
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

恒温器（Thermostat）。

<a id="ga1562514d0182e8862edad570b7a346e6"></a>

### `BT_APPEARANCE_INSULIN_PEN`

```c
#define BT_APPEARANCE_INSULIN_PEN 0x0D48
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

胰岛素笔（Insulin Pen）。

<a id="ga63512439364307259010bededf7bfd8b"></a>

### `BT_APPEARANCE_INSULIN_PUMP_DURABLE`

```c
#define BT_APPEARANCE_INSULIN_PUMP_DURABLE 0x0D41
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耐用型胰岛素泵（Insulin Pump, durable pump）。

<a id="ga0979695247b96321e5a8b6869d09227a"></a>

### `BT_APPEARANCE_INSULIN_PUMP_PATCH`

```c
#define BT_APPEARANCE_INSULIN_PUMP_PATCH 0x0D44
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

贴片式胰岛素泵（Insulin Pump, patch pump）。

<a id="ga8f98c2d32664a6e03ebc2a43ae1eb52a"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_BAY`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BAY 0x0593
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

工矿灯（Bay Light）。

<a id="ga20a7b241f292475d70626a38d983886c"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BOLLARD_WITH 0x058B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

带灯柱桩（Bollard with Light）。

<a id="ga8325830f2c977dc238a9ca1b9837803e"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_BULB`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_BULB 0x0597
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯泡（Bulb）。

<a id="gadc48840b6590a89593a5d17fbdb1e9e9"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_CABINET`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CABINET 0x0584
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

橱柜灯（Cabinet Light）。

<a id="ga2d77fb5f5ed9a43771186ecc5693da8f"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_CEILING`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CEILING 0x0582
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吸顶灯（Ceiling Light）。

<a id="ga35a90a4e3bfef7b0cfec0d5fa7b36c4a"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_CONTROLLER 0x0595
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

照明控制器（Light Controller）。

<a id="ga2f37bf95ea6057b999bbf2cf94016e5d"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_DESK`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DESK 0x0585
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

桌灯（Desk Light）。

<a id="gac2b6de99b4e87f7c40063ba844c75ead"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_DRIVER`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_DRIVER 0x0596
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

灯具驱动器（Light Driver）。

<a id="ga3f687f994ffff2ce70b81a992195d210"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_EMERGENCY_EXIT 0x0594
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

紧急出口灯（Emergency Exit Light）。

<a id="gab41f8b6f1ff0f624bb6666ef2ac6dab3"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_FLOOD`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOD 0x0589
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

泛光灯（Flood Light）。

<a id="ga57bb461b0ddd045d21d7fbd3843fbabb"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_FLOOR`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_FLOOR 0x0583
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

落地灯（Floor Light）。

<a id="ga348e64ffe0f3d6301dd8c911f70ead68"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_GARDEN`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_GARDEN 0x058D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

庭院灯（Garden Light）。

<a id="ga738e87008c6a64450bb7ec22dbcdd113"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_HIGH_BAY 0x0599
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

高棚灯（High-bay Light）。

<a id="ga583b7432ba6ac4cc078d3a069e3a54e1"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_IN_GROUND 0x0588
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

地埋灯（In-ground Light）。

<a id="ga5388daf123e629d6f7a0b9af13fbc366"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_LINEAR`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LINEAR 0x0590
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

线性灯（Linear Light）。

<a id="gafc924bbc1b6aff0130c2be3d5fe59e33"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_LOW_BAY 0x0598
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低棚灯（Low-bay Light）。

<a id="ga7c5811bd50d9f78e67e3e56faa432aae"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PATHWAY 0x058C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

步道灯（Pathway Light）。

<a id="ga336147b54406237e25d8cf9ed152928b"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_PENDANT`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_PENDANT 0x0587
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吊灯（Pendant Light）。

<a id="ga0da0cbeebd2b20bf28dfc06def016068"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_POLE_TOP 0x058E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

杆顶灯（Pole-top Light）。

<a id="ga1bf2889f7a8a7ae363bc1d4355ee8d65"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_SHELVES`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_SHELVES 0x0592
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

货架灯（Shelves Light）。

<a id="gac938fb03553d2d3c27b50af2a9a1ac48"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_STREET`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_STREET 0x0591
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

路灯（Street Light）。

<a id="gaa57b538ecad380ad77354e0cd9576e5b"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_TROFFER`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_TROFFER 0x0586
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

嵌入式格栅灯（Troffer Light）。

<a id="ga83f50305a23250e5e2cef5004762e122"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_UNDERWATER 0x058A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

水下灯（Underwater Light）。

<a id="gae1b2b535754f9cdc24c4a6cee63ef5cb"></a>

### `BT_APPEARANCE_LIGHT_FIXTURES_WALL`

```c
#define BT_APPEARANCE_LIGHT_FIXTURES_WALL 0x0581
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

壁灯（Wall Light）。

<a id="ga39957a77aa54255ab3a06441e422e7e3"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_FLUORESCENT_LAMP 0x07C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

荧光灯（Fluorescent Lamp）。

<a id="ga1babd2989112bafb5819235fe5b6c556"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_HID_LAMP 0x07C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

高强度气体放电灯（HID Lamp）。

<a id="gafed8531ffde21d0ad6e8d477d64496f0"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_INCANDESCENT_BULB 0x07C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

白炽灯泡（Incandescent Light Bulb）。

<a id="ga242d324cf5cf33e4edd5cf33e8c3c89b"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_ARRAY 0x07C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

LED 阵列（LED Array）。

<a id="ga66bf91b8a25ac88a0fd6ab9456201de1"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LED_LAMP 0x07C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

LED 灯（LED Lamp）。

<a id="gaf47bce54f4ae1915cd64c3c2d254e353"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_LOW_VOLTAGE_HALOGEN 0x07C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低压卤素灯（Low voltage halogen）。

<a id="ga8449006920ed1fdd562c702ee2e16a21"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_MULTICOLOR_LED_ARRAY 0x07C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

多色 LED 阵列（Multi-Color LED Array）。

<a id="gaed4400a94dae4f536a456cc55eb6f6d5"></a>

### `BT_APPEARANCE_LIGHT_SOURCE_OLED`

```c
#define BT_APPEARANCE_LIGHT_SOURCE_OLED 0x07C8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

有机发光二极管（Organic light emitting diode）。

<a id="ga7966ec64cafe708fe94a7c323fbe3713"></a>

### `BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR`

```c
#define BT_APPEARANCE_MOBILITY_POWERED_WHEELCHAIR 0x0CC1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电动轮椅（Powered Wheelchair）。

<a id="ga21f21a73f355ffaa408376ca4fc802a8"></a>

### `BT_APPEARANCE_MOBILITY_SCOOTER`

```c
#define BT_APPEARANCE_MOBILITY_SCOOTER 0x0CC2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

助行代步车（Mobility Scooter）。

<a id="ga338de5523abf3fd81e913f3cdb4a31b6"></a>

### `BT_APPEARANCE_MOTORIZED_AWNING`

```c
#define BT_APPEARANCE_MOTORIZED_AWNING 0x0742
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

遮阳篷（Awning）。

<a id="gaaa39c48ed2d6edd5650743b82154462b"></a>

### `BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES`

```c
#define BT_APPEARANCE_MOTORIZED_BLINDS_OR_SHADES 0x0743
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

百叶帘或遮阳帘（Blinds or Shades）。

<a id="ga53f6a4df5ccc2117525952be2e174ddc"></a>

### `BT_APPEARANCE_MOTORIZED_CURTAINS`

```c
#define BT_APPEARANCE_MOTORIZED_CURTAINS 0x0744
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

窗帘（Curtains）。

<a id="ga376ef909868a5c273b71d1c372755707"></a>

### `BT_APPEARANCE_MOTORIZED_GATE`

```c
#define BT_APPEARANCE_MOTORIZED_GATE 0x0741
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电动大门（Motorized Gate）。

<a id="ga5f32cab5c7a155fffbe0c33cadfef31a"></a>

### `BT_APPEARANCE_MOTORIZED_SCREEN`

```c
#define BT_APPEARANCE_MOTORIZED_SCREEN 0x0745
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

屏障（Screen）。

<a id="ga90237753920702380321e9f858344741"></a>

### `BT_APPEARANCE_MULTISENSOR`

```c
#define BT_APPEARANCE_MULTISENSOR 0x0556
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

多传感器（Multisensor）。

<a id="ga265ba959769d56f42ff621a20e193aba"></a>

### `BT_APPEARANCE_NETWORK_ACCESS_POINT`

```c
#define BT_APPEARANCE_NETWORK_ACCESS_POINT 0x0501
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

接入点（Access Point）。

<a id="gadcc3d795579a731ae03ade14d5193408"></a>

### `BT_APPEARANCE_NETWORK_MESH_DEVICE`

```c
#define BT_APPEARANCE_NETWORK_MESH_DEVICE 0x0502
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

网状网络设备（Mesh Device）。

<a id="gad4c5f5840a8caba73d55b0138e506bd0"></a>

### `BT_APPEARANCE_NETWORK_MESH_PROXY`

```c
#define BT_APPEARANCE_NETWORK_MESH_PROXY 0x0503
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

网状网络代理（Mesh Network Proxy）。

<a id="ga30c97d6f5bff1a4a67e4f59eb4d49d2d"></a>

### `BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION`

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION 0x1441
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

位置显示器（Location Display）。

<a id="ga52b6c51c9afcbbba12d9d3cae824f4a7"></a>

### `BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV`

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_AND_NAV 0x1442
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

位置与导航显示器（Location and Navigation Display）。

<a id="gadf053353789183d1b1c3ca13ad98559f"></a>

### `BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD`

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD 0x1443
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

定位模块（Location Pod）。

<a id="ga8fbc7782099e724febb712ee108e8cba"></a>

### `BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV`

```c
#define BT_APPEARANCE_OUTDOOR_SPORTS_LOCATION_POD_AND_NAV 0x1444
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

定位与导航模块（Location and Navigation Pod）。

<a id="ga39ad633d1795af4546bd930d0e799447"></a>

### `BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE`

```c
#define BT_APPEARANCE_PORTABLE_HANDHELD_CONSOLE 0x0A82
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

便携式掌上游戏机（Portable handheld console）。

<a id="ga5d6b28b9660d2357e2af2bf0ceab9c18"></a>

### `BT_APPEARANCE_POWER_CHARGE_CASE`

```c
#define BT_APPEARANCE_POWER_CHARGE_CASE 0x0788
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

充电盒（Charge Case）。

<a id="ga7de26016aa039e3e72ddd61653e1c1d8"></a>

### `BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR`

```c
#define BT_APPEARANCE_POWER_FLUORESCENT_LAMP_GEAR 0x0786
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

荧光灯控制装置（Fluorescent Lamp Gear）。

<a id="ga6396b1d813c9764bdfe92c4f2ba961b1"></a>

### `BT_APPEARANCE_POWER_HID_LAMP_GEAR`

```c
#define BT_APPEARANCE_POWER_HID_LAMP_GEAR 0x0787
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

高强度气体放电灯控制装置（HID Lamp Gear）。

<a id="ga31842298741c822dcebba942453975c6"></a>

### `BT_APPEARANCE_POWER_LED_DRIVER`

```c
#define BT_APPEARANCE_POWER_LED_DRIVER 0x0785
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

LED 驱动器（LED Driver）。

<a id="gad9efd19e2c95525a3972c8b0f0417449"></a>

### `BT_APPEARANCE_POWER_OUTLET`

```c
#define BT_APPEARANCE_POWER_OUTLET 0x0781
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电源插座（Power Outlet）。

<a id="ga0d9aadc19f5f5f484769b225164866e4"></a>

### `BT_APPEARANCE_POWER_PLUG`

```c
#define BT_APPEARANCE_POWER_PLUG 0x0783
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

插头（Plug）。

<a id="gab6a5ac3941a5707f052126810a7f22e0"></a>

### `BT_APPEARANCE_POWER_POWER_BANK`

```c
#define BT_APPEARANCE_POWER_POWER_BANK 0x0789
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

移动电源（Power Bank）。

<a id="ga2c5bd38d4eeb1aad2d29b004390a6d18"></a>

### `BT_APPEARANCE_POWER_STRIP`

```c
#define BT_APPEARANCE_POWER_STRIP 0x0782
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电源插排（Power Strip）。

<a id="ga07acce808c9cf2b5e84aacd65e8f256d"></a>

### `BT_APPEARANCE_POWER_SUPPLY`

```c
#define BT_APPEARANCE_POWER_SUPPLY 0x0784
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电源（Power Supply）。

<a id="ga8a298130c73299b6079dae3065954c0c"></a>

### `BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP`

```c
#define BT_APPEARANCE_PULSE_OXIMETER_FINGERTIP 0x0C41
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

指夹式脉搏血氧仪（Fingertip Pulse Oximeter）。

<a id="gaebcadd5c37e6d87903e2cb97e03aeb7d"></a>

### `BT_APPEARANCE_PULSE_OXIMETER_WRIST`

```c
#define BT_APPEARANCE_PULSE_OXIMETER_WRIST 0x0C42
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

腕戴式脉搏血氧仪（Wrist Worn Pulse Oximeter）。

<a id="gaacb0779499ad4aaa83f0b6303460caf8"></a>

### `BT_APPEARANCE_SENSOR_AIR_QUALITY`

```c
#define BT_APPEARANCE_SENSOR_AIR_QUALITY 0x0542
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

空气质量传感器（Air quality Sensor）。

<a id="ga622508f9b051ed0320700b01967f6446"></a>

### `BT_APPEARANCE_SENSOR_AMBIENT_LIGHT`

```c
#define BT_APPEARANCE_SENSOR_AMBIENT_LIGHT 0x054B
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

环境光传感器（Ambient Light Sensor）。

<a id="ga34ed8c9aefe34d5030209f073c9ecd24"></a>

### `BT_APPEARANCE_SENSOR_CARBON_DIOXIDE`

```c
#define BT_APPEARANCE_SENSOR_CARBON_DIOXIDE 0x054A
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

二氧化碳传感器（Carbon Dioxide Sensor）。

<a id="ga0e60b365f871c17c0015ffcf8bc1646e"></a>

### `BT_APPEARANCE_SENSOR_CARBON_MONOXIDE`

```c
#define BT_APPEARANCE_SENSOR_CARBON_MONOXIDE 0x0549
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

一氧化碳传感器（Carbon Monoxide Sensor）。

<a id="gadfb6808db5a7060316b724c24c8ceaf8"></a>

### `BT_APPEARANCE_SENSOR_CEILING_MOUNTED`

```c
#define BT_APPEARANCE_SENSOR_CEILING_MOUNTED 0x0554
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

吸顶安装式传感器（Ceiling Mounted Sensor）。

<a id="ga8106142ddb6445e7462137e032e50854"></a>

### `BT_APPEARANCE_SENSOR_COLOR_LIGHT`

```c
#define BT_APPEARANCE_SENSOR_COLOR_LIGHT 0x054D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

彩色光传感器（Color Light Sensor）。

<a id="gac71e281cf1b8d1b6535623ec34c7d63f"></a>

### `BT_APPEARANCE_SENSOR_CONTACT`

```c
#define BT_APPEARANCE_SENSOR_CONTACT 0x0548
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

接触传感器（Contact Sensor）。

<a id="gaca0cfcd560fa4133c0bc62a61d2874c7"></a>

### `BT_APPEARANCE_SENSOR_ENERGY`

```c
#define BT_APPEARANCE_SENSOR_ENERGY 0x054C
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

能量传感器（Energy Sensor）。

<a id="ga7238d3a45f9e62f0189db9d7eeac4d15"></a>

### `BT_APPEARANCE_SENSOR_ENERGY_METER`

```c
#define BT_APPEARANCE_SENSOR_ENERGY_METER 0x0557
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

能量计（Energy Meter）。

<a id="ga425115e6c251a9c493c98d79f659077d"></a>

### `BT_APPEARANCE_SENSOR_FIRE`

```c
#define BT_APPEARANCE_SENSOR_FIRE 0x054F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

火灾传感器（Fire Sensor）。

<a id="gaae8f95ef639cb7d5e97063eed710a07d"></a>

### `BT_APPEARANCE_SENSOR_FLAME_DETECTOR`

```c
#define BT_APPEARANCE_SENSOR_FLAME_DETECTOR 0x0558
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

火焰探测器（Flame Detector）。

<a id="gaf9a9c0191ec175d14061058cf3da163c"></a>

### `BT_APPEARANCE_SENSOR_FLUSH_MOUNTED`

```c
#define BT_APPEARANCE_SENSOR_FLUSH_MOUNTED 0x0553
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

嵌入安装式传感器（Flush Mounted Sensor）。

<a id="ga2deff206602e1e0784af9456ef8abd5b"></a>

### `BT_APPEARANCE_SENSOR_HUMIDITY`

```c
#define BT_APPEARANCE_SENSOR_HUMIDITY 0x0544
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

湿度传感器（Humidity Sensor）。

<a id="ga2cbac5e931080f1f5cb3c9bb4c73e9d8"></a>

### `BT_APPEARANCE_SENSOR_LEAK`

```c
#define BT_APPEARANCE_SENSOR_LEAK 0x0545
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

泄漏传感器（Leak Sensor）。

<a id="gab49b84183136e9b65ba2e1f5490a79ed"></a>

### `BT_APPEARANCE_SENSOR_MOTION`

```c
#define BT_APPEARANCE_SENSOR_MOTION 0x0541
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

运动传感器（Motion Sensor）。

<a id="gaeec9666dbdb31e9302a25aaa536f3180"></a>

### `BT_APPEARANCE_SENSOR_MULTI`

```c
#define BT_APPEARANCE_SENSOR_MULTI 0x0552
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

多传感器（Multi-Sensor）。

<a id="ga8e8b7834c82c42a0076300aca20c2d35"></a>

### `BT_APPEARANCE_SENSOR_OCCUPANCY`

```c
#define BT_APPEARANCE_SENSOR_OCCUPANCY 0x0547
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

占用传感器（Occupancy Sensor）。

<a id="ga6d3447e24d5d75051b81998fd9ad8bfe"></a>

### `BT_APPEARANCE_SENSOR_PROXIMITY`

```c
#define BT_APPEARANCE_SENSOR_PROXIMITY 0x0551
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

接近传感器（Proximity Sensor）。

<a id="ga380da83e3a69de3fd5091cdc89f7fcbc"></a>

### `BT_APPEARANCE_SENSOR_RAIN`

```c
#define BT_APPEARANCE_SENSOR_RAIN 0x054E
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

雨量传感器（Rain Sensor）。

<a id="gaeedc0612f8ca171aec061cf02ee907e4"></a>

### `BT_APPEARANCE_SENSOR_SMOKE`

```c
#define BT_APPEARANCE_SENSOR_SMOKE 0x0546
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

烟雾传感器（Smoke Sensor）。

<a id="ga5e072a902bf145dc2b00dbd1c8a64b52"></a>

### `BT_APPEARANCE_SENSOR_TEMPERATURE`

```c
#define BT_APPEARANCE_SENSOR_TEMPERATURE 0x0543
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

温度传感器（Temperature Sensor）。

<a id="ga4d0877a3cd9b7efebbaa5fd8a988a2a3"></a>

### `BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE`

```c
#define BT_APPEARANCE_SENSOR_VEHICLE_TIRE_PRESSURE 0x0559
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

车辆胎压传感器（Vehicle Tire Pressure Sensor）。

<a id="gae564900f0517d393ceffcca8d27f6e45"></a>

### `BT_APPEARANCE_SENSOR_WALL_MOUNTED`

```c
#define BT_APPEARANCE_SENSOR_WALL_MOUNTED 0x0555
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

壁挂安装式传感器（Wall Mounted Sensor）。

<a id="gaa710c0666d8b5bf1e1230672cbbf55fa"></a>

### `BT_APPEARANCE_SENSOR_WIND`

```c
#define BT_APPEARANCE_SENSOR_WIND 0x0550
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

风传感器（Wind Sensor）。

<a id="gace31a591ef3b5f0812e4cbf417a2205a"></a>

### `BT_APPEARANCE_SIGNAGE_DIGITAL`

```c
#define BT_APPEARANCE_SIGNAGE_DIGITAL 0x0AC1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

数字标牌（Digital Signage）。

<a id="gaa4674b06751edf98fa88ede568a68ad4"></a>

### `BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL`

```c
#define BT_APPEARANCE_SIGNAGE_ELECTRONIC_LABEL 0x0AC2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电子标签（Electronic Label）。

<a id="gaa5662d4a544b034243faa45245a9728b"></a>

### `BT_APPEARANCE_SMARTWATCH`

```c
#define BT_APPEARANCE_SMARTWATCH 0x00C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

智能手表（Smartwatch）。

<a id="ga42b9d596efb757b209f080a8c33f3723"></a>

### `BT_APPEARANCE_SPIROMETER_HANDHELD`

```c
#define BT_APPEARANCE_SPIROMETER_HANDHELD 0x0DC1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

手持式肺量计（Handheld Spirometer）。

<a id="gaca9cc93d768145ec3d87b88740954b50"></a>

### `BT_APPEARANCE_SPORTS_WATCH`

```c
#define BT_APPEARANCE_SPORTS_WATCH 0x00C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

运动手表（Sports Watch）。

<a id="ga58e1989c99b5a223a318a716d62f6e2b"></a>

### `BT_APPEARANCE_SPOT_LIGHT`

```c
#define BT_APPEARANCE_SPOT_LIGHT 0x058F
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

聚光灯（Spotlight）。

<a id="ga54283061a207491dcfced899c0fc3008"></a>

### `BT_APPEARANCE_THERMOMETER_EAR`

```c
#define BT_APPEARANCE_THERMOMETER_EAR 0x0301
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耳温计（Ear Thermometer）。

<a id="gafd1c9ca638a362a01897792e5a00a0c5"></a>

### `BT_APPEARANCE_UNKNOWN`

```c
#define BT_APPEARANCE_UNKNOWN 0x0000
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用未知设备（Generic Unknown）。

<a id="gaa149e56e4b4a1b6dde821fbdac3d9c32"></a>

### `BT_APPEARANCE_VEHICLE_AGRICULTURAL`

```c
#define BT_APPEARANCE_VEHICLE_AGRICULTURAL 0x08CD
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

农业车辆（Agricultural Vehicle）。

<a id="ga0da02a18987c653a3232c28a3e4908f7"></a>

### `BT_APPEARANCE_VEHICLE_BUS`

```c
#define BT_APPEARANCE_VEHICLE_BUS 0x08CB
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

公共汽车（Bus）。

<a id="gafcb3909bf61bb130f8c0a217e69477b8"></a>

### `BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN`

```c
#define BT_APPEARANCE_VEHICLE_CAMPER_OR_CARAVAN 0x08CE
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

露营车／拖挂式旅居车（Camper/Caravan）。

<a id="ga6257291ed3e6d09ce6197e2081b36d04"></a>

### `BT_APPEARANCE_VEHICLE_CAR`

```c
#define BT_APPEARANCE_VEHICLE_CAR 0x08C1
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

汽车（Car）。

<a id="ga31ff643e1efccffd9ba73c793f63837c"></a>

### `BT_APPEARANCE_VEHICLE_LARGE_GOODS`

```c
#define BT_APPEARANCE_VEHICLE_LARGE_GOODS 0x08C2
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

大型货运车辆（Large Goods Vehicle）。

<a id="gac22a0476760c42eb8f00b36b74361c5e"></a>

### `BT_APPEARANCE_VEHICLE_LIGHT`

```c
#define BT_APPEARANCE_VEHICLE_LIGHT 0x08C8
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

轻型车辆（Light Vehicle）。

<a id="ga0cf473bbf07d4576ab9f0116ca48f161"></a>

### `BT_APPEARANCE_VEHICLE_MINIBUS`

```c
#define BT_APPEARANCE_VEHICLE_MINIBUS 0x08CA
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

小型客车（Minibus）。

<a id="ga18b0231dbd97d8871f685774f9e1b4e1"></a>

### `BT_APPEARANCE_VEHICLE_MOPED`

```c
#define BT_APPEARANCE_VEHICLE_MOPED 0x08C6
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

轻便摩托车（Moped）。

<a id="gaa71eaa4fd0eef66a794475cb44aaf397"></a>

### `BT_APPEARANCE_VEHICLE_MOTORBIKE`

```c
#define BT_APPEARANCE_VEHICLE_MOTORBIKE 0x08C4
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

摩托车（Motorbike）。

<a id="ga03e3660bdc2e439126f2f8df8ea335ee"></a>

### `BT_APPEARANCE_VEHICLE_QUAD_BIKE`

```c
#define BT_APPEARANCE_VEHICLE_QUAD_BIKE 0x08C9
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

四轮摩托车（Quad Bike）。

<a id="ga9366a994d42c88490313380d419b2a8e"></a>

### `BT_APPEARANCE_VEHICLE_RECREATIONAL`

```c
#define BT_APPEARANCE_VEHICLE_RECREATIONAL 0x08CF
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

休闲车辆／自行式房车（Recreational Vehicle/Motor Home）。

<a id="gae082982b90d94404b69c57987d8a2c5a"></a>

### `BT_APPEARANCE_VEHICLE_SCOOTER`

```c
#define BT_APPEARANCE_VEHICLE_SCOOTER 0x08C5
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

踏板车（Scooter）。

<a id="ga8159dfd6933a2a5fdb2c72da9623bc2e"></a>

### `BT_APPEARANCE_VEHICLE_THREE_WHEELED`

```c
#define BT_APPEARANCE_VEHICLE_THREE_WHEELED 0x08C7
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

三轮车辆（3-Wheeled Vehicle）。

<a id="gabde7af9f7c25d56f5fb9643398273526"></a>

### `BT_APPEARANCE_VEHICLE_TROLLEY`

```c
#define BT_APPEARANCE_VEHICLE_TROLLEY 0x08CC
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电车（Trolley）。

<a id="ga68ade931a12e5d9e9863decad3d8de9e"></a>

### `BT_APPEARANCE_VEHICLE_TWO_WHEELED`

```c
#define BT_APPEARANCE_VEHICLE_TWO_WHEELED 0x08C3
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

两轮车辆（2-Wheeled Vehicle）。

<a id="gad748f5dc2e0622353d6159c3a3e4241b"></a>

### `BT_APPEARANCE_WALKING_IN_SHOE`

```c
#define BT_APPEARANCE_WALKING_IN_SHOE 0x0441
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

鞋内跑步／步行传感器（In-Shoe Running Walking Sensor）。

<a id="gad211a7e2f11dc7effe3ba28e8c4f7092"></a>

### `BT_APPEARANCE_WALKING_ON_HIP`

```c
#define BT_APPEARANCE_WALKING_ON_HIP 0x0443
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

髋部佩戴式跑步／步行传感器（On-Hip Running Walking Sensor）。

<a id="ga0a4541459ba8b41a3938c5b8d35b1c8c"></a>

### `BT_APPEARANCE_WALKING_ON_SHOE`

```c
#define BT_APPEARANCE_WALKING_ON_SHOE 0x0442
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

鞋面跑步／步行传感器（On-Shoe Running Walking Sensor）。

<a id="gab480735e2ba8db23d2668ea3a2137214"></a>

### `BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD`

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_EARBUD 0x0941
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

耳塞式耳机（Earbud）。

<a id="gae420044380309abba1b9570d26735315"></a>

### `BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES`

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADPHONES 0x0943
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

头戴式耳机（Headphones）。

<a id="ga8bd98ba3a4c1cbf8dbf8235d9ad0f943"></a>

### `BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET`

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_HEADSET 0x0942
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

带麦克风耳机（Headset）。

<a id="ga59ea8ff5efec7a19bce8440e7ae78a1e"></a>

### `BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND`

```c
#define BT_APPEARANCE_WEARABLE_AUDIO_DEVICE_NECK_BAND 0x0944
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

颈挂式耳机（Neck Band）。

<a id="ga9945bb52a9ee3268efda7d5e05421e12"></a>

### `BT_APPEARANCE_WINDOW_AWNING`

```c
#define BT_APPEARANCE_WINDOW_AWNING 0x0803
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

窗户遮阳篷（Window Awning）。

<a id="ga717efaeab0329ded066567761b9983a7"></a>

### `BT_APPEARANCE_WINDOW_BLINDS`

```c
#define BT_APPEARANCE_WINDOW_BLINDS 0x0802
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

百叶窗帘（Window Blinds）。

<a id="ga20352e58e6cec63efbb6beaa75c0e330"></a>

### `BT_APPEARANCE_WINDOW_CURTAIN`

```c
#define BT_APPEARANCE_WINDOW_CURTAIN 0x0804
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

窗帘（Window Curtain）。

<a id="ga0a0b87095177af0560a540e545c97f42"></a>

### `BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN`

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SCREEN 0x0806
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外置遮阳屏（Exterior Screen）。

<a id="ga7ead13b128fbc50be3f5c101fb1383cb"></a>

### `BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER`

```c
#define BT_APPEARANCE_WINDOW_EXTERIOR_SHUTTER 0x0805
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外置百叶窗（Exterior Shutter）。

<a id="ga37614ae63c8287bc4bd0c9a5bf00502e"></a>

### `BT_APPEARANCE_WINDOW_SHADES`

```c
#define BT_APPEARANCE_WINDOW_SHADES 0x0801
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

遮阳窗帘（Window Shades）。

<a id="gaecab0c77f9f912c16c264e7eaf2e4707"></a>

### `BT_DATA_3D_INFO`

```c
#define BT_DATA_3D_INFO 0x3D
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

三维信息数据（3D Information Data）。

<a id="ga6fd8c0f32bbcb97aaafee51fda0b601e"></a>

### `BT_DATA_ADV_INT`

```c
#define BT_DATA_ADV_INT 0x1a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播间隔（Advertising Interval）。

<a id="gad4ac2e0de80dddcacc4ca6d25765eebd"></a>

### `BT_DATA_ADV_INT_LONG`

```c
#define BT_DATA_ADV_INT_LONG 0x2f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

长广播间隔（Advertising Interval long）。

<a id="ga16feb94cd09c04d020450f61646f5486"></a>

### `BT_DATA_BIG_INFO`

```c
#define BT_DATA_BIG_INFO 0x2c
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播等时组信息（BIGInfo）。

<a id="ga72d2e55819db593a6db77579ebfe1e9d"></a>

### `BT_DATA_BROADCAST_CODE`

```c
#define BT_DATA_BROADCAST_CODE 0x2d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播码（Broadcast Code）。

<a id="ga7d781791bc85fe3c7ea839ff617ee6e7"></a>

### `BT_DATA_BROADCAST_NAME`

```c
#define BT_DATA_BROADCAST_NAME 0x30
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播名称（Broadcast Name）。

<a id="gae3eb96c0f127b6417d7cad288faaaceb"></a>

### `BT_DATA_CHANNEL_MAP_UPDATE_IND`

```c
#define BT_DATA_CHANNEL_MAP_UPDATE_IND 0x28
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

信道映射更新指示（Channel Map Update Indication）。

<a id="ga122da4184d606ae140f8a311aaebeedd"></a>

### `BT_DATA_CSIS_RSI`

```c
#define BT_DATA_CSIS_RSI 0x2e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

协调集识别服务随机集 ID 类型（CSIS Random Set ID type）。

<a id="ga152c3028a2befcc4caf40aa6590c80b7"></a>

### `BT_DATA_DEVICE_CLASS`

```c
#define BT_DATA_DEVICE_CLASS 0x0d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

设备类别（Class of Device）。

<a id="gac9402c597e5b4497f4bcd22d5177cc23"></a>

### `BT_DATA_DEVICE_ID`

```c
#define BT_DATA_DEVICE_ID 0x10
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

设备 ID 配置文件（Device ID (Profile)）。

<a id="ga41d5c898144e89b6035f92ff506f38a3"></a>

### `BT_DATA_ENCRYPTED_AD_DATA`

```c
#define BT_DATA_ENCRYPTED_AD_DATA 0x31
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

加密广播数据（Encrypted Advertising Data）。

<a id="ga90c7a1175148f3a56b04dc0b29525a4d"></a>

### `BT_DATA_ESL`

```c
#define BT_DATA_ESL 0x34
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

电子货架标签配置文件（Electronic Shelf Label Profile）。

<a id="ga396b92d418fcb8263895e420b9df3df2"></a>

### `BT_DATA_FLAGS`

```c
#define BT_DATA_FLAGS 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

广播数据标志（AD flags）。

<a id="ga67fc721da05758b7d7a36aecaa035fac"></a>

### `BT_DATA_GAP_APPEARANCE`

```c
#define BT_DATA_GAP_APPEARANCE 0x19
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用访问配置文件外观值（GAP appearance）。

<a id="ga0f29f9d8f5a336af430f0a603e87e995"></a>

### `BT_DATA_INDOOR_POS`

```c
#define BT_DATA_INDOOR_POS 0x25
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

室内定位（Indoor Positioning）。

<a id="gad9e8a273239fa160a6b2797ef5563a94"></a>

### `BT_DATA_LE_BT_DEVICE_ADDRESS`

```c
#define BT_DATA_LE_BT_DEVICE_ADDRESS 0x1b
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗蓝牙设备地址（LE Bluetooth Device Address）。

<a id="ga255c7cb16eb24b95fa0f531fc4574273"></a>

### `BT_DATA_LE_ROLE`

```c
#define BT_DATA_LE_ROLE 0x1c
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗蓝牙角色（LE Role）。

<a id="ga883dda02c157f0de8157b1c5f66aafd0"></a>

### `BT_DATA_LE_SC_CONFIRM_VALUE`

```c
#define BT_DATA_LE_SC_CONFIRM_VALUE 0x22
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗安全连接确认值（LE SC Confirmation Value）。

<a id="gacbc31c67684e3c68481501cf89f9ec68"></a>

### `BT_DATA_LE_SC_RANDOM_VALUE`

```c
#define BT_DATA_LE_SC_RANDOM_VALUE 0x23
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗安全连接随机值（LE SC Random Value）。

<a id="ga207bc1e5405a4fd3f39863a2cb304ebc"></a>

### `BT_DATA_LE_SUPPORTED_FEATURES`

```c
#define BT_DATA_LE_SUPPORTED_FEATURES 0x27
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

低功耗蓝牙支持的特性（LE Supported Features）。

<a id="ga63b846807bff632b1cdd49b1e46e63b4"></a>

### `BT_DATA_MANUFACTURER_DATA`

```c
#define BT_DATA_MANUFACTURER_DATA 0xff
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

厂商专用数据（Manufacturer Specific Data）。

<a id="ga59cc479be1f6c61a4a47aa6f479fe67a"></a>

### `BT_DATA_MESH_BEACON`

```c
#define BT_DATA_MESH_BEACON 0x2b
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

网状网络信标（Mesh Beacon）。

<a id="gac351c67ab58520b796fa713602d9f602"></a>

### `BT_DATA_MESH_MESSAGE`

```c
#define BT_DATA_MESH_MESSAGE 0x2a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

网状网络协议数据单元（Mesh Networking PDU）。

<a id="gafc5984d58b0b54ee824dd83bc78dfbe9"></a>

### `BT_DATA_MESH_PROV`

```c
#define BT_DATA_MESH_PROV 0x29
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

网状网络配置协议数据单元（Mesh Provisioning PDU）。

<a id="gab94a7c5689d296acf47f976538056ab5"></a>

### `BT_DATA_NAME_COMPLETE`

```c
#define BT_DATA_NAME_COMPLETE 0x09
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

完整名称（Complete name）。

<a id="gafc509b33a8d2dd9124f6893eadbe1662"></a>

### `BT_DATA_NAME_SHORTENED`

```c
#define BT_DATA_NAME_SHORTENED 0x08
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

缩短名称（Shortened name）。

<a id="ga14a8b1cf9d6c1c9749443a012731d39c"></a>

### `BT_DATA_PAWR_TIMING_INFO`

```c
#define BT_DATA_PAWR_TIMING_INFO 0x32
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

周期广播响应时序信息（Periodic Advertising Response Timing Info）。

<a id="gabcf872eafc60c21287f6be63174dc7c8"></a>

### `BT_DATA_PERIPHERAL_INT_RANGE`

```c
#define BT_DATA_PERIPHERAL_INT_RANGE 0x12
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

外设连接间隔范围（Peripheral Connection Interval Range）。

<a id="gacb867f0436d38c5c80e3426ca6247a46"></a>

### `BT_DATA_PUB_TARGET_ADDR`

```c
#define BT_DATA_PUB_TARGET_ADDR 0x17
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

公共目标地址（Public Target Address）。

<a id="ga3d9097d8f53213ccafc152c51ad6fdbd"></a>

### `BT_DATA_RAND_TARGET_ADDR`

```c
#define BT_DATA_RAND_TARGET_ADDR 0x18
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

随机目标地址（Random Target Address）。

<a id="ga324f91521eacd1e9d579c9d52d02eb06"></a>

### `BT_DATA_SIMPLE_PAIRING_HASH`

```c
#define BT_DATA_SIMPLE_PAIRING_HASH 0x1d
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

简单配对哈希 C256（Simple Pairing Hash C256）。

<a id="ga053c8bb0aedd01b3dd3f6154f4b49999"></a>

### `BT_DATA_SIMPLE_PAIRING_HASH_C192`

```c
#define BT_DATA_SIMPLE_PAIRING_HASH_C192 0x0e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

简单配对哈希 C-192（Simple Pairing Hash C-192）。

<a id="gad7e7dd2d3a972e53f9e5e80627bd07e6"></a>

### `BT_DATA_SIMPLE_PAIRING_RAND`

```c
#define BT_DATA_SIMPLE_PAIRING_RAND 0x1e
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

简单配对随机数 R256（Simple Pairing Randomizer R256）。

<a id="ga280f1f96c5204960fe034c9ddaf194ec"></a>

### `BT_DATA_SIMPLE_PAIRING_RAND_C192`

```c
#define BT_DATA_SIMPLE_PAIRING_RAND_C192 0x0f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

简单配对随机数 R-192（Simple Pairing Randomizer R-192）。

<a id="gaa12c742d1c955036aa3f55e84df69890"></a>

### `BT_DATA_SM_OOB_FLAGS`

```c
#define BT_DATA_SM_OOB_FLAGS 0x11
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

安全管理器带外标志（Security Manager OOB Flags）。

<a id="ga5014acb2fe8e76b855b55bf98abe6d05"></a>

### `BT_DATA_SM_TK_VALUE`

```c
#define BT_DATA_SM_TK_VALUE 0x10
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

安全管理器临时密钥值（Security Manager TK Value）。

<a id="ga217df3f70846e86fa09e5605d5acd291"></a>

### `BT_DATA_SOLICIT128`

```c
#define BT_DATA_SOLICIT128 0x15
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务征询 UUID，128 位（Solicit UUIDs, 128-bit）。

<a id="ga2ad4d2ec2ff29c0aad5159de12d3f741"></a>

### `BT_DATA_SOLICIT16`

```c
#define BT_DATA_SOLICIT16 0x14
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务征询 UUID，16 位（Solicit UUIDs, 16-bit）。

<a id="ga76e7e8971ed841b87fda08793a00b14f"></a>

### `BT_DATA_SOLICIT32`

```c
#define BT_DATA_SOLICIT32 0x1f
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务征询 UUID，32 位（Solicit UUIDs, 32-bit）。

<a id="gaa53847910515d9488b490f17a4fdf0d1"></a>

### `BT_DATA_SVC_DATA128`

```c
#define BT_DATA_SVC_DATA128 0x21
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务数据，128 位 UUID（Service data, 128-bit UUID）。

<a id="ga76990dda919688b369decaf9d3606b32"></a>

### `BT_DATA_SVC_DATA16`

```c
#define BT_DATA_SVC_DATA16 0x16
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务数据，16 位 UUID（Service data, 16-bit UUID）。

<a id="ga7d411a723ff2f038c3b7a1e09c88cb3d"></a>

### `BT_DATA_SVC_DATA32`

```c
#define BT_DATA_SVC_DATA32 0x20
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

服务数据，32 位 UUID（Service data, 32-bit UUID）。

<a id="ga8e9ccc669ee545152b2d9b3120692d55"></a>

### `BT_DATA_TRANS_DISCOVER_DATA`

```c
#define BT_DATA_TRANS_DISCOVER_DATA 0x26
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

传输发现数据（Transport Discovery Data）。

<a id="ga4988c17578c4cf76fcdd9d44e1c931b0"></a>

### `BT_DATA_TX_POWER`

```c
#define BT_DATA_TX_POWER 0x0a
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

发射功率（Tx Power）。

<a id="ga3c6a5903cc4a46aaf0b30a0de0179403"></a>

### `BT_DATA_URI`

```c
#define BT_DATA_URI 0x24
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

统一资源标识符（URI）。

<a id="gaafcade3dbbcb4005f4590e994f91884b"></a>

### `BT_DATA_UUID128_ALL`

```c
#define BT_DATA_UUID128_ALL 0x07
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

128 位 UUID 列表，已全部列出（128-bit UUID, all listed）。

<a id="ga5c4f7fc1b93c611e95f735330fba243b"></a>

### `BT_DATA_UUID128_SOME`

```c
#define BT_DATA_UUID128_SOME 0x06
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

128 位 UUID 列表，尚有更多条目（128-bit UUID, more available）。

<a id="ga0d55063b9ad321b5c530a0012337df8a"></a>

### `BT_DATA_UUID16_ALL`

```c
#define BT_DATA_UUID16_ALL 0x03
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

16 位 UUID 列表，已全部列出（16-bit UUID, all listed）。

<a id="ga6c725bd3d31c159a4d046561dbca38ba"></a>

### `BT_DATA_UUID16_SOME`

```c
#define BT_DATA_UUID16_SOME 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

16 位 UUID 列表，尚有更多条目（16-bit UUID, more available）。

<a id="gaaf825c3e4686e572a35ddd46ee6fe2e8"></a>

### `BT_DATA_UUID32_ALL`

```c
#define BT_DATA_UUID32_ALL 0x05
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

32 位 UUID 列表，已全部列出（32-bit UUID, all listed）。

<a id="ga2486a6748490ba57e442ca15223482ef"></a>

### `BT_DATA_UUID32_SOME`

```c
#define BT_DATA_UUID32_SOME 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

32 位 UUID 列表，尚有更多条目（32-bit UUID, more available）。

<a id="ga13d9b4a24e2a8b58402bfb21f8b782c8"></a>

### `BT_LE_AD_GENERAL`

```c
#define BT_LE_AD_GENERAL 0x02
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

通用可发现模式（General Discoverable）。

<a id="ga36191ee000a2098fd679c398b31e0906"></a>

### `BT_LE_AD_LIMITED`

```c
#define BT_LE_AD_LIMITED 0x01
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

有限可发现模式（Limited Discoverable）。

<a id="gabf5725f481cb73cbd974f3653c904bc9"></a>

### `BT_LE_AD_NO_BREDR`

```c
#define BT_LE_AD_NO_BREDR 0x04
```

```c
#include <zephyr/bluetooth/assigned_numbers.h>
```

不支持基本速率／增强数据率（BR/EDR not supported）。


## 1.5\_原页交叉引用（Cross References）

- [zephyr/bluetooth/assigned_numbers.h](../api_file_input_wake_protocol_reference/P001_zephyr__bluetooth__assigned_numbers.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>

---

[返回大纲](大纲.md) · [下一章](P002_基本成像配置文件（Basic Imaging Profile，BIP）.md)
