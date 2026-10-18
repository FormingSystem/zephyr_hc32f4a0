---
id: learning.zephyr-docs.hardware.dacapi-2
title: SiliconLabsVDAC设备树常量
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第821章\_SiliconLabsVDAC设备树常量

原文：[silabs-vdac_8h](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html)。读取日期：2026-10-13，`latest`。

头文件 `zephyr/dt-bindings/dac/silabs-vdac.h` 列出Silicon Labs电压数模转换器（Voltage Digital-to-Analog Converter，VDAC）的65个输出选择常量（Output Selection Constants）。原页只有宏定义，没有附加说明或包含项。[官方源码浏览](P836_SiliconLabsVDAC常量源码.md)保留原始定义；配置方式见[VDAC绑定](P774_SiliconLabs电压数模转换器绑定.md)。

下表中文为名称释义：AUX表示辅助输出（Auxiliary Output），PA／PB／PC／PD分别表示端口A／B／C／D及其引脚编号。宏存在并不等于某个具体封装上一定引出了全部引脚，实际连接仍按器件和引脚控制配置确定。

## 821.1\_辅助输出

```c
#define VDAC_OUTPUT_AUX 0x0
```

[`VDAC_OUTPUT_AUX`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a5545b0ba8e6f182690103dc00ab12122) 的编码为 `0x0`，原页没有进一步解释其路由。

## 821.2\_端口A输出

```c
#define VDAC_OUTPUT_PA0 0x10
#define VDAC_OUTPUT_PA1 0x11
#define VDAC_OUTPUT_PA2 0x12
#define VDAC_OUTPUT_PA3 0x13
#define VDAC_OUTPUT_PA4 0x14
#define VDAC_OUTPUT_PA5 0x15
#define VDAC_OUTPUT_PA6 0x16
#define VDAC_OUTPUT_PA7 0x17
#define VDAC_OUTPUT_PA8 0x18
#define VDAC_OUTPUT_PA9 0x19
#define VDAC_OUTPUT_PA10 0x1a
#define VDAC_OUTPUT_PA11 0x1b
#define VDAC_OUTPUT_PA12 0x1c
#define VDAC_OUTPUT_PA13 0x1d
#define VDAC_OUTPUT_PA14 0x1e
#define VDAC_OUTPUT_PA15 0x1f
```

| 宏 | 编码 | 引脚名称 |
| --- | --- | --- |
| [`VDAC_OUTPUT_PA0`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ac5e39445de50e8d2f5471719ca090e70) | `0x10` | 端口A的第0号引脚 `PA0` |
| [`VDAC_OUTPUT_PA1`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a6d414d82466215af74995a8bdebf2648) | `0x11` | 端口A的第1号引脚 `PA1` |
| [`VDAC_OUTPUT_PA2`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#acd15e53133eae68c420ccae1938683d1) | `0x12` | 端口A的第2号引脚 `PA2` |
| [`VDAC_OUTPUT_PA3`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a5d81c7dc9749755c75655c302a1b2a13) | `0x13` | 端口A的第3号引脚 `PA3` |
| [`VDAC_OUTPUT_PA4`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#afc76787799c948bf406e83fbe6d7e8d8) | `0x14` | 端口A的第4号引脚 `PA4` |
| [`VDAC_OUTPUT_PA5`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a9f3cba6b5b5a753774565abdb52ff155) | `0x15` | 端口A的第5号引脚 `PA5` |
| [`VDAC_OUTPUT_PA6`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a9a5bbd37224f47fd0a9bfe346ee27a70) | `0x16` | 端口A的第6号引脚 `PA6` |
| [`VDAC_OUTPUT_PA7`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ab07869f9a8745f97ad3d8e225d9d540e) | `0x17` | 端口A的第7号引脚 `PA7` |
| [`VDAC_OUTPUT_PA8`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aadaedef22803f8462e0fdec5a5bc8032) | `0x18` | 端口A的第8号引脚 `PA8` |
| [`VDAC_OUTPUT_PA9`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a3d66fdc02f761e404ad657b4c9084de1) | `0x19` | 端口A的第9号引脚 `PA9` |
| [`VDAC_OUTPUT_PA10`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aa539aedc126993482c802a069c8acdd2) | `0x1a` | 端口A的第10号引脚 `PA10` |
| [`VDAC_OUTPUT_PA11`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a32f7eb46078b1d9a23f13775295273af) | `0x1b` | 端口A的第11号引脚 `PA11` |
| [`VDAC_OUTPUT_PA12`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ac150c82becb59fd6561ac60c8458805f) | `0x1c` | 端口A的第12号引脚 `PA12` |
| [`VDAC_OUTPUT_PA13`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a156a5d3770648fb20834bfc0e5d8fc42) | `0x1d` | 端口A的第13号引脚 `PA13` |
| [`VDAC_OUTPUT_PA14`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a406f5e3d93ba8369db4dfec8df01bfa5) | `0x1e` | 端口A的第14号引脚 `PA14` |
| [`VDAC_OUTPUT_PA15`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ab5466cd0b71401b9f85b6baacd66990a) | `0x1f` | 端口A的第15号引脚 `PA15` |

## 821.3\_端口B输出

```c
#define VDAC_OUTPUT_PB0 0x20
#define VDAC_OUTPUT_PB1 0x21
#define VDAC_OUTPUT_PB2 0x22
#define VDAC_OUTPUT_PB3 0x23
#define VDAC_OUTPUT_PB4 0x24
#define VDAC_OUTPUT_PB5 0x25
#define VDAC_OUTPUT_PB6 0x26
#define VDAC_OUTPUT_PB7 0x27
#define VDAC_OUTPUT_PB8 0x28
#define VDAC_OUTPUT_PB9 0x29
#define VDAC_OUTPUT_PB10 0x2a
#define VDAC_OUTPUT_PB11 0x2b
#define VDAC_OUTPUT_PB12 0x2c
#define VDAC_OUTPUT_PB13 0x2d
#define VDAC_OUTPUT_PB14 0x2e
#define VDAC_OUTPUT_PB15 0x2f
```

| 宏 | 编码 | 引脚名称 |
| --- | --- | --- |
| [`VDAC_OUTPUT_PB0`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a309f757b8ad93a2a338a7252bfda5118) | `0x20` | 端口B的第0号引脚 `PB0` |
| [`VDAC_OUTPUT_PB1`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ad840e6900ed7c34e64f06e6ceabf7b71) | `0x21` | 端口B的第1号引脚 `PB1` |
| [`VDAC_OUTPUT_PB2`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a800c986d3963f745862c31b3953ea810) | `0x22` | 端口B的第2号引脚 `PB2` |
| [`VDAC_OUTPUT_PB3`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a071ef1641ff332c7de99a740ab73d152) | `0x23` | 端口B的第3号引脚 `PB3` |
| [`VDAC_OUTPUT_PB4`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a145e1425f3360393a491e601c8404f75) | `0x24` | 端口B的第4号引脚 `PB4` |
| [`VDAC_OUTPUT_PB5`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aa69074132590a624ef639b0a30cc5ad2) | `0x25` | 端口B的第5号引脚 `PB5` |
| [`VDAC_OUTPUT_PB6`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aed99f5cab1e4b4266f4eceb6f06c7edf) | `0x26` | 端口B的第6号引脚 `PB6` |
| [`VDAC_OUTPUT_PB7`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a210b19a08dbb3d5ec0d402aadc1ae2d3) | `0x27` | 端口B的第7号引脚 `PB7` |
| [`VDAC_OUTPUT_PB8`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a885b506b8a01dc17e34958f8e9531469) | `0x28` | 端口B的第8号引脚 `PB8` |
| [`VDAC_OUTPUT_PB9`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a9ce987ddaaa33ad84c241be09f5949d9) | `0x29` | 端口B的第9号引脚 `PB9` |
| [`VDAC_OUTPUT_PB10`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a48ba98440b2283111388c6e4d3cf02a9) | `0x2a` | 端口B的第10号引脚 `PB10` |
| [`VDAC_OUTPUT_PB11`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a78806c5582f5cec999f7820b6d3a3d6c) | `0x2b` | 端口B的第11号引脚 `PB11` |
| [`VDAC_OUTPUT_PB12`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a3c80784cf816b1b25d7377c4490d7988) | `0x2c` | 端口B的第12号引脚 `PB12` |
| [`VDAC_OUTPUT_PB13`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ae57eb93e08d951224813d696f02e2c00) | `0x2d` | 端口B的第13号引脚 `PB13` |
| [`VDAC_OUTPUT_PB14`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a44b9774e53a93457fae91f3acdc94c4b) | `0x2e` | 端口B的第14号引脚 `PB14` |
| [`VDAC_OUTPUT_PB15`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aa1b4afc2d00f44d7372dc7affd0114b8) | `0x2f` | 端口B的第15号引脚 `PB15` |

## 821.4\_端口C输出

```c
#define VDAC_OUTPUT_PC0 0x30
#define VDAC_OUTPUT_PC1 0x31
#define VDAC_OUTPUT_PC2 0x32
#define VDAC_OUTPUT_PC3 0x33
#define VDAC_OUTPUT_PC4 0x34
#define VDAC_OUTPUT_PC5 0x35
#define VDAC_OUTPUT_PC6 0x36
#define VDAC_OUTPUT_PC7 0x37
#define VDAC_OUTPUT_PC8 0x38
#define VDAC_OUTPUT_PC9 0x39
#define VDAC_OUTPUT_PC10 0x3a
#define VDAC_OUTPUT_PC11 0x3b
#define VDAC_OUTPUT_PC12 0x3c
#define VDAC_OUTPUT_PC13 0x3d
#define VDAC_OUTPUT_PC14 0x3e
#define VDAC_OUTPUT_PC15 0x3f
```

| 宏 | 编码 | 引脚名称 |
| --- | --- | --- |
| [`VDAC_OUTPUT_PC0`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a8dd45b3331718042750e4e43ce33b377) | `0x30` | 端口C的第0号引脚 `PC0` |
| [`VDAC_OUTPUT_PC1`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ae015997f75eadc11dbc20784715f9a94) | `0x31` | 端口C的第1号引脚 `PC1` |
| [`VDAC_OUTPUT_PC2`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a55e501c7812234c3b4f96ef679067ee2) | `0x32` | 端口C的第2号引脚 `PC2` |
| [`VDAC_OUTPUT_PC3`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ad60778e6a9b910079bd467556b604bd9) | `0x33` | 端口C的第3号引脚 `PC3` |
| [`VDAC_OUTPUT_PC4`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aefceda0bf57a6c6c8d4e44956ab693ad) | `0x34` | 端口C的第4号引脚 `PC4` |
| [`VDAC_OUTPUT_PC5`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a1b7e524fdcb414251c297be86b5ac5e1) | `0x35` | 端口C的第5号引脚 `PC5` |
| [`VDAC_OUTPUT_PC6`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a46b116a4f3f57352ecf390d3f3ed2709) | `0x36` | 端口C的第6号引脚 `PC6` |
| [`VDAC_OUTPUT_PC7`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#af233a1fbd5225c72f3048d0c891c9654) | `0x37` | 端口C的第7号引脚 `PC7` |
| [`VDAC_OUTPUT_PC8`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ac48cf52a237451e0ae8fa5649f5e9e59) | `0x38` | 端口C的第8号引脚 `PC8` |
| [`VDAC_OUTPUT_PC9`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ab0d2ed6db9c469a5de71b3075d5dae62) | `0x39` | 端口C的第9号引脚 `PC9` |
| [`VDAC_OUTPUT_PC10`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a69e2453538a1b5d17f5a842bbb98ca35) | `0x3a` | 端口C的第10号引脚 `PC10` |
| [`VDAC_OUTPUT_PC11`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a493464f46320be434ecec9a5d90e8322) | `0x3b` | 端口C的第11号引脚 `PC11` |
| [`VDAC_OUTPUT_PC12`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#acb7f197cd6998fb8a8678fe104d3fc54) | `0x3c` | 端口C的第12号引脚 `PC12` |
| [`VDAC_OUTPUT_PC13`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a0bb99720b013ca3dea2529894ad1b7b6) | `0x3d` | 端口C的第13号引脚 `PC13` |
| [`VDAC_OUTPUT_PC14`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ac91e186649b701ed11ebbc17da88b7c7) | `0x3e` | 端口C的第14号引脚 `PC14` |
| [`VDAC_OUTPUT_PC15`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ac2d398e97eb05080df9f1e0d493421e5) | `0x3f` | 端口C的第15号引脚 `PC15` |

## 821.5\_端口D输出

```c
#define VDAC_OUTPUT_PD0 0x40
#define VDAC_OUTPUT_PD1 0x41
#define VDAC_OUTPUT_PD2 0x42
#define VDAC_OUTPUT_PD3 0x43
#define VDAC_OUTPUT_PD4 0x44
#define VDAC_OUTPUT_PD5 0x45
#define VDAC_OUTPUT_PD6 0x46
#define VDAC_OUTPUT_PD7 0x47
#define VDAC_OUTPUT_PD8 0x48
#define VDAC_OUTPUT_PD9 0x49
#define VDAC_OUTPUT_PD10 0x4a
#define VDAC_OUTPUT_PD11 0x4b
#define VDAC_OUTPUT_PD12 0x4c
#define VDAC_OUTPUT_PD13 0x4d
#define VDAC_OUTPUT_PD14 0x4e
#define VDAC_OUTPUT_PD15 0x4f
```

| 宏 | 编码 | 引脚名称 |
| --- | --- | --- |
| [`VDAC_OUTPUT_PD0`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a33f2cc1419c7974901b77a7d24044e45) | `0x40` | 端口D的第0号引脚 `PD0` |
| [`VDAC_OUTPUT_PD1`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ab7f7ab8646edb408e245ddb448cccd90) | `0x41` | 端口D的第1号引脚 `PD1` |
| [`VDAC_OUTPUT_PD2`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a4f97276d3ebca8d5a268ae45b6cac0e3) | `0x42` | 端口D的第2号引脚 `PD2` |
| [`VDAC_OUTPUT_PD3`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aa80c304a6a7a505dc3d6674477cbf7c6) | `0x43` | 端口D的第3号引脚 `PD3` |
| [`VDAC_OUTPUT_PD4`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a495f00cd82c901d942446c24f711000c) | `0x44` | 端口D的第4号引脚 `PD4` |
| [`VDAC_OUTPUT_PD5`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a9fa6aa40e0d073f4f8819accc1bce57b) | `0x45` | 端口D的第5号引脚 `PD5` |
| [`VDAC_OUTPUT_PD6`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a804c9be322f4312ff6deab9dc5918972) | `0x46` | 端口D的第6号引脚 `PD6` |
| [`VDAC_OUTPUT_PD7`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#aad7843143e53d0dbd94edac3e5e9adb5) | `0x47` | 端口D的第7号引脚 `PD7` |
| [`VDAC_OUTPUT_PD8`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a4c4520f455bdd8fe3f50823251047b10) | `0x48` | 端口D的第8号引脚 `PD8` |
| [`VDAC_OUTPUT_PD9`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a11277a8697ac6dfec2eda805bae34862) | `0x49` | 端口D的第9号引脚 `PD9` |
| [`VDAC_OUTPUT_PD10`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a41719f821978fb1ba3d99a7dc5b20e56) | `0x4a` | 端口D的第10号引脚 `PD10` |
| [`VDAC_OUTPUT_PD11`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#ae8dfb3fee368dfd3c22cb6007d9edcab) | `0x4b` | 端口D的第11号引脚 `PD11` |
| [`VDAC_OUTPUT_PD12`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a869c32947d107c74807c08c8d9f8c5ff) | `0x4c` | 端口D的第12号引脚 `PD12` |
| [`VDAC_OUTPUT_PD13`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a54ff937f5f7a0617cf3b663a0088ff16) | `0x4d` | 端口D的第13号引脚 `PD13` |
| [`VDAC_OUTPUT_PD14`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a7943b97141bff5c3417703e33809d716) | `0x4e` | 端口D的第14号引脚 `PD14` |
| [`VDAC_OUTPUT_PD15`](https://docs.zephyrproject.org/latest/doxygen/html/silabs-vdac_8h.html#a5e9b7ba0e117211b369621b3f34d0372) | `0x4f` | 端口D的第15号引脚 `PD15` |


---

[上一章：Infineon连续时间DAC设备树常量](P820_Infineon连续时间DAC设备树常量.md) · [下一章：数模转换器接口](P822_数模转换器接口.md) · [返回大纲](大纲.md)
