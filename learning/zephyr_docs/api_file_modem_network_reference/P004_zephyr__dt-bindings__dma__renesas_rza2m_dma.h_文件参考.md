---
id: learning.zephyr-docs.api-file-modem-network-reference.page-4
title: zephyr__dt-bindings__dma__renesas_rza2m_dma.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_dt-bindings\_\_dma\_\_renesas\_rza2m\_dma.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rza2m__dma_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

RZ/A2M DMA的设备树绑定标志及请求源定义（Request-Source Definitions）。

查看此文件的源码。

<a id="details"></a>

RZ/A2M 直接存储器访问（DMA）设备树绑定（Devicetree Bindings）的标志与请求源定义。本头文件提供用于填充 Renesas RZ/A2M 片上系统（SoC）的 `dmas` 设备树属性的位字段标志（Bit-field Flags），以及预先打包的请求源（Request-source）宏 `RZA2M_DMA_RS_*`。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.1\_宏定义（Macros）

<a id="r_a391ba1663b69e478fb4c82c35b16e176"></a>

```c
#define RZA2M_DMA_RS(dmars, lvl, am, reqd)
```

相关声明：[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

将 DMARS 请求码（Request Code）及其固定的 CHCFG 标志（Flags）打包为一个槽位值（Slot Value）。

<a id="r_a2b5170fc1b55ab2fab9da061f42bc9fc"></a>

```c
#define RZA2M_DMA_MEM_2_MEM 0x0U
```

相关声明：[RZA2M_DMA_MEM_2_MEM](#a2b5170fc1b55ab2fab9da061f42bc9fc)。

内存到内存传输（Memory-to-memory Transfer），由软件触发（Software Triggered）。

<a id="r_ac521f38a9178670684798851196939bc"></a>

```c
#define RZA2M_DMA_RS_OSTM0TINT RZA2M_DMA_RS(0x023U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OSTM0TINT](#ac521f38a9178670684798851196939bc)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

OSTM0 定时器中断（OSTM0 timer interrupt）。

<a id="r_af861a0ce876f339b3e7f59ca3c83ec10"></a>

```c
#define RZA2M_DMA_RS_OSTM1TINT RZA2M_DMA_RS(0x027U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OSTM1TINT](#af861a0ce876f339b3e7f59ca3c83ec10)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

OSTM1 定时器中断（OSTM1 timer interrupt）。

<a id="r_ab914a5b323ae7fa91f6b8490cc7417f8"></a>

```c
#define RZA2M_DMA_RS_OSTM2TINT RZA2M_DMA_RS(0x02BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OSTM2TINT](#ab914a5b323ae7fa91f6b8490cc7417f8)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

OSTM2 定时器中断（OSTM2 timer interrupt）。

<a id="r_a369d818ab82c5b4b0c6502967f6757e4"></a>

```c
#define RZA2M_DMA_RS_TGIA_0 RZA2M_DMA_RS(0x043U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_0](#a369d818ab82c5b4b0c6502967f6757e4)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 0, 比较匹配／输入捕获 A（MTU channel 0, compare match/input capture A）。

<a id="r_ade2b671145723b401570432cc2c8cd54"></a>

```c
#define RZA2M_DMA_RS_TGIB_0 RZA2M_DMA_RS(0x047U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_0](#ade2b671145723b401570432cc2c8cd54)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 0, 比较匹配／输入捕获 B（MTU channel 0, compare match/input capture B）。

<a id="r_a472581fa62f8269f60e1b0db4d8b8bda"></a>

```c
#define RZA2M_DMA_RS_TGIC_0 RZA2M_DMA_RS(0x04BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_0](#a472581fa62f8269f60e1b0db4d8b8bda)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 0, 比较匹配／输入捕获 C（MTU channel 0, compare match/input capture C）。

<a id="r_ad2c236d2aaae652b3bf52a025241107d"></a>

```c
#define RZA2M_DMA_RS_TGID_0 RZA2M_DMA_RS(0x04FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_0](#ad2c236d2aaae652b3bf52a025241107d)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 0, 比较匹配／输入捕获 D（MTU channel 0, compare match/input capture D）。

<a id="r_aab6298b2f1e34f09f4b6044ac9a6f233"></a>

```c
#define RZA2M_DMA_RS_TGIA_1 RZA2M_DMA_RS(0x053U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_1](#aab6298b2f1e34f09f4b6044ac9a6f233)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 1, 比较匹配／输入捕获 A（MTU channel 1, compare match/input capture A）。

<a id="r_a23d862e8c0fce9dbfba93285ea32589d"></a>

```c
#define RZA2M_DMA_RS_TGIB_1 RZA2M_DMA_RS(0x057U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_1](#a23d862e8c0fce9dbfba93285ea32589d)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 1, 比较匹配／输入捕获 B（MTU channel 1, compare match/input capture B）。

<a id="r_a7f2fb65fdf92760fe85b8bf2193a82fc"></a>

```c
#define RZA2M_DMA_RS_TGIA_2 RZA2M_DMA_RS(0x05BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_2](#a7f2fb65fdf92760fe85b8bf2193a82fc)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 2, 比较匹配／输入捕获 A（MTU channel 2, compare match/input capture A）。

<a id="r_abc0a77e490cd9a3787a1bdafa9e5cf31"></a>

```c
#define RZA2M_DMA_RS_TGIB_2 RZA2M_DMA_RS(0x05FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_2](#abc0a77e490cd9a3787a1bdafa9e5cf31)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 2, 比较匹配／输入捕获 B（MTU channel 2, compare match/input capture B）。

<a id="r_a446a00d865413f135c105003db9dbf98"></a>

```c
#define RZA2M_DMA_RS_TGIA_3 RZA2M_DMA_RS(0x063U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_3](#a446a00d865413f135c105003db9dbf98)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 3, 比较匹配／输入捕获 A（MTU channel 3, compare match/input capture A）。

<a id="r_a2d49f329a8469a0f8730dfff9574d955"></a>

```c
#define RZA2M_DMA_RS_TGIB_3 RZA2M_DMA_RS(0x067U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_3](#a2d49f329a8469a0f8730dfff9574d955)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 3, 比较匹配／输入捕获 B（MTU channel 3, compare match/input capture B）。

<a id="r_af19bba4cecb049d8e5fcd2eab79119d5"></a>

```c
#define RZA2M_DMA_RS_TGIC_3 RZA2M_DMA_RS(0x06BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_3](#af19bba4cecb049d8e5fcd2eab79119d5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 3, 比较匹配／输入捕获 C（MTU channel 3, compare match/input capture C）。

<a id="r_a704aff4a1226e18e06023fded37142d3"></a>

```c
#define RZA2M_DMA_RS_TGID_3 RZA2M_DMA_RS(0x06FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_3](#a704aff4a1226e18e06023fded37142d3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 3, 比较匹配／输入捕获 D（MTU channel 3, compare match/input capture D）。

<a id="r_a5f6841e43bd15fdfc0816301871fdbda"></a>

```c
#define RZA2M_DMA_RS_TGIA_4 RZA2M_DMA_RS(0x073U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_4](#a5f6841e43bd15fdfc0816301871fdbda)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 4, 比较匹配／输入捕获 A（MTU channel 4, compare match/input capture A）。

<a id="r_aa0b0855807d72c73cee5b377cd261575"></a>

```c
#define RZA2M_DMA_RS_TGIB_4 RZA2M_DMA_RS(0x077U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_4](#aa0b0855807d72c73cee5b377cd261575)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 4, 比较匹配／输入捕获 B（MTU channel 4, compare match/input capture B）。

<a id="r_a7b84b6850efbc5c8070fbc3802e43cf3"></a>

```c
#define RZA2M_DMA_RS_TGIC_4 RZA2M_DMA_RS(0x07BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_4](#a7b84b6850efbc5c8070fbc3802e43cf3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 4, 比较匹配／输入捕获 C（MTU channel 4, compare match/input capture C）。

<a id="r_ac3df895b3451bf2925606dec8ba54e2b"></a>

```c
#define RZA2M_DMA_RS_TGID_4 RZA2M_DMA_RS(0x07FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_4](#ac3df895b3451bf2925606dec8ba54e2b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 4, 比较匹配／输入捕获 D（MTU channel 4, compare match/input capture D）。

<a id="r_a1065735c9aa60cbc99903810c67cbc3b"></a>

```c
#define RZA2M_DMA_RS_TCIV_4 RZA2M_DMA_RS(0x083U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TCIV_4](#a1065735c9aa60cbc99903810c67cbc3b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 4, TCNT 的上溢／下溢中断（MTU channel 4, overflow/underflow interrupt of TCNT）。

<a id="r_a16e54abe66cd04ff09d2fb318899e7b7"></a>

```c
#define RZA2M_DMA_RS_TGIU_5 RZA2M_DMA_RS(0x087U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIU_5](#a16e54abe66cd04ff09d2fb318899e7b7)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 5, 比较匹配／输入捕获 U（MTU channel 5, compare match/input capture U）。

<a id="r_aac3735c168591e161681bcdf96f3f150"></a>

```c
#define RZA2M_DMA_RS_TGIV_5 RZA2M_DMA_RS(0x08BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIV_5](#aac3735c168591e161681bcdf96f3f150)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 5, 比较匹配／输入捕获 V（MTU channel 5, compare match/input capture V）。

<a id="r_afdebfb68206593eba15765cbf7e96405"></a>

```c
#define RZA2M_DMA_RS_TGIW_5 RZA2M_DMA_RS(0x08FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIW_5](#afdebfb68206593eba15765cbf7e96405)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 5, 比较匹配／输入捕获 W（MTU channel 5, compare match/input capture W）。

<a id="r_a1197065cbf95f829932cc150ce27bd91"></a>

```c
#define RZA2M_DMA_RS_TGIA_6 RZA2M_DMA_RS(0x093U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_6](#a1197065cbf95f829932cc150ce27bd91)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 6, 比较匹配／输入捕获 A（MTU channel 6, compare match/input capture A）。

<a id="r_af124980bc5bb74c5ad625c2443392b6b"></a>

```c
#define RZA2M_DMA_RS_TGIB_6 RZA2M_DMA_RS(0x097U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_6](#af124980bc5bb74c5ad625c2443392b6b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 6, 比较匹配／输入捕获 B（MTU channel 6, compare match/input capture B）。

<a id="r_a992961b8a4aceca82925e7a0474c0225"></a>

```c
#define RZA2M_DMA_RS_TGIC_6 RZA2M_DMA_RS(0x09BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_6](#a992961b8a4aceca82925e7a0474c0225)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 6, 比较匹配／输入捕获 C（MTU channel 6, compare match/input capture C）。

<a id="r_ab365586d7aa2fb4e8a761d1b102c528b"></a>

```c
#define RZA2M_DMA_RS_TGID_6 RZA2M_DMA_RS(0x09FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_6](#ab365586d7aa2fb4e8a761d1b102c528b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 6, 比较匹配／输入捕获 D（MTU channel 6, compare match/input capture D）。

<a id="r_a123b96db8690952648c20ff32acc49de"></a>

```c
#define RZA2M_DMA_RS_TGIA_7 RZA2M_DMA_RS(0x0A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_7](#a123b96db8690952648c20ff32acc49de)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 7, 比较匹配／输入捕获 A（MTU channel 7, compare match/input capture A）。

<a id="r_a2fd591c9dfd12921cad0097d84034a67"></a>

```c
#define RZA2M_DMA_RS_TGIB_7 RZA2M_DMA_RS(0x0A7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_7](#a2fd591c9dfd12921cad0097d84034a67)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 7, 比较匹配／输入捕获 B（MTU channel 7, compare match/input capture B）。

<a id="r_a35c6aa421d48382b1f7b0c1496e0cd3b"></a>

```c
#define RZA2M_DMA_RS_TGIC_7 RZA2M_DMA_RS(0x0ABU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_7](#a35c6aa421d48382b1f7b0c1496e0cd3b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 7, 比较匹配／输入捕获 C（MTU channel 7, compare match/input capture C）。

<a id="r_ac681f555edcefcda45c5fa2e708e6173"></a>

```c
#define RZA2M_DMA_RS_TGID_7 RZA2M_DMA_RS(0x0AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_7](#ac681f555edcefcda45c5fa2e708e6173)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 7, 比较匹配／输入捕获 D（MTU channel 7, compare match/input capture D）。

<a id="r_a00b1a6cfd73d0194435432ce1fda422f"></a>

```c
#define RZA2M_DMA_RS_TCIV_7 RZA2M_DMA_RS(0x0B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TCIV_7](#a00b1a6cfd73d0194435432ce1fda422f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 7, TCNT 的上溢／下溢中断（MTU channel 7, overflow/underflow interrupt of TCNT）。

<a id="r_aaa1f3a728a201692557773551a3a9cdf"></a>

```c
#define RZA2M_DMA_RS_TGIA_8 RZA2M_DMA_RS(0x0B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIA_8](#aaa1f3a728a201692557773551a3a9cdf)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 8, 比较匹配／输入捕获 A（MTU channel 8, compare match/input capture A）。

<a id="r_a24a3472223b1f6dba3f79b4bb30f174e"></a>

```c
#define RZA2M_DMA_RS_TGIB_8 RZA2M_DMA_RS(0x0BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIB_8](#a24a3472223b1f6dba3f79b4bb30f174e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 8, 比较匹配／输入捕获 B（MTU channel 8, compare match/input capture B）。

<a id="r_af7a6dfcf39dbaa9249f887c8e82acc00"></a>

```c
#define RZA2M_DMA_RS_TGIC_8 RZA2M_DMA_RS(0x0BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGIC_8](#af7a6dfcf39dbaa9249f887c8e82acc00)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 8, 比较匹配／输入捕获 C（MTU channel 8, compare match/input capture C）。

<a id="r_a7a44df400aa8769568192be0d9fa6f18"></a>

```c
#define RZA2M_DMA_RS_TGID_8 RZA2M_DMA_RS(0x0C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_TGID_8](#a7a44df400aa8769568192be0d9fa6f18)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

MTU 通道 8, 比较匹配／输入捕获 D（MTU channel 8, compare match/input capture D）。

<a id="r_aef4ed46740b478c7e521e143bb3bdcb8"></a>

```c
#define RZA2M_DMA_RS_CCMPA_0 RZA2M_DMA_RS(0x0C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_0](#aef4ed46740b478c7e521e143bb3bdcb8)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配／输入捕获 A（GPT channel 0, compare match/input capture A）。

<a id="r_a689150899bb088f5194109c91369eff7"></a>

```c
#define RZA2M_DMA_RS_CCMPB_0 RZA2M_DMA_RS(0x0CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_0](#a689150899bb088f5194109c91369eff7)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配／输入捕获 B（GPT channel 0, compare match/input capture B）。

<a id="r_a4f3a8525da395c46d6d4eb44417754cd"></a>

```c
#define RZA2M_DMA_RS_CMPC_0 RZA2M_DMA_RS(0x0CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_0](#a4f3a8525da395c46d6d4eb44417754cd)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配 C（GPT channel 0, compare match C）。

<a id="r_a58be60629b2b39a2bfa57ce9e37cc076"></a>

```c
#define RZA2M_DMA_RS_CMPD_0 RZA2M_DMA_RS(0x0D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_0](#a58be60629b2b39a2bfa57ce9e37cc076)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配 D（GPT channel 0, compare match D）。

<a id="r_a4ce7f0b2e77b9284eeecc50a131f7666"></a>

```c
#define RZA2M_DMA_RS_CMPE_0 RZA2M_DMA_RS(0x0E3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_0](#a4ce7f0b2e77b9284eeecc50a131f7666)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配 E（GPT channel 0, compare match E）。

<a id="r_ae3cb688e4edbfd4f40b76a161c8bfa38"></a>

```c
#define RZA2M_DMA_RS_CMPF_0 RZA2M_DMA_RS(0x0E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_0](#ae3cb688e4edbfd4f40b76a161c8bfa38)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 比较匹配 F（GPT channel 0, compare match F）。

<a id="r_ac77fa619e6b8e4f0ad6ed834da1f61b1"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_0 RZA2M_DMA_RS(0x0EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_0](#ac77fa619e6b8e4f0ad6ed834da1f61b1)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 模数转换启动 A（GPT channel 0, A/D conversion start A）。

<a id="r_a6fb7cbeab5a0d05a2d58b59705279e2c"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_0 RZA2M_DMA_RS(0x0EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_0](#a6fb7cbeab5a0d05a2d58b59705279e2c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 模数转换启动 B（GPT channel 0, A/D conversion start B）。

<a id="r_a6ec09447832d6626096d2434782e6ab1"></a>

```c
#define RZA2M_DMA_RS_OVF_0 RZA2M_DMA_RS(0x0F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_0](#a6ec09447832d6626096d2434782e6ab1)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 上溢（GPT channel 0, overflow）。

<a id="r_a51b8da6256c92ab9bad709bf11ed4707"></a>

```c
#define RZA2M_DMA_RS_UNF_0 RZA2M_DMA_RS(0x0F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_0](#a51b8da6256c92ab9bad709bf11ed4707)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 0, 下溢（GPT channel 0, underflow）。

<a id="r_a72db7dba30d7456ad1dd81325360f04e"></a>

```c
#define RZA2M_DMA_RS_CCMPA_1 RZA2M_DMA_RS(0x0FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_1](#a72db7dba30d7456ad1dd81325360f04e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配／输入捕获 A（GPT channel 1, compare match/input capture A）。

<a id="r_a02ccc8a1e530c56b2ad92ebb6117693e"></a>

```c
#define RZA2M_DMA_RS_CCMPB_1 RZA2M_DMA_RS(0x0FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_1](#a02ccc8a1e530c56b2ad92ebb6117693e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配／输入捕获 B（GPT channel 1, compare match/input capture B）。

<a id="r_abfc0de01ac870273e400115539e398ea"></a>

```c
#define RZA2M_DMA_RS_CMPC_1 RZA2M_DMA_RS(0x103U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_1](#abfc0de01ac870273e400115539e398ea)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配 C（GPT channel 1, compare match C）。

<a id="r_a655a7efd37cb45e8d9faafcaaac85ae0"></a>

```c
#define RZA2M_DMA_RS_CMPD_1 RZA2M_DMA_RS(0x107U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_1](#a655a7efd37cb45e8d9faafcaaac85ae0)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配 D（GPT channel 1, compare match D）。

<a id="r_aae314bf45c7b5bfd44b04f9c8a460eee"></a>

```c
#define RZA2M_DMA_RS_CMPE_1 RZA2M_DMA_RS(0x117U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_1](#aae314bf45c7b5bfd44b04f9c8a460eee)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配 E（GPT channel 1, compare match E）。

<a id="r_ac8e8117447f3d4631d3b88946564932c"></a>

```c
#define RZA2M_DMA_RS_CMPF_1 RZA2M_DMA_RS(0x11BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_1](#ac8e8117447f3d4631d3b88946564932c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 比较匹配 F（GPT channel 1, compare match F）。

<a id="r_a34ccbbf7062e250a45c5da1334a696ab"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_1 RZA2M_DMA_RS(0x11FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_1](#a34ccbbf7062e250a45c5da1334a696ab)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 模数转换启动 A（GPT channel 1, A/D conversion start A）。

<a id="r_a922d8675c78b8937b539cbaeb574bc12"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_1 RZA2M_DMA_RS(0x123U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_1](#a922d8675c78b8937b539cbaeb574bc12)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 模数转换启动 B（GPT channel 1, A/D conversion start B）。

<a id="r_a2fb455da7133660be6ff171638cb9085"></a>

```c
#define RZA2M_DMA_RS_OVF_1 RZA2M_DMA_RS(0x127U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_1](#a2fb455da7133660be6ff171638cb9085)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 上溢（GPT channel 1, overflow）。

<a id="r_a461c8cacd8900dfddeb0f33569acd39b"></a>

```c
#define RZA2M_DMA_RS_UNF_1 RZA2M_DMA_RS(0x12BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_1](#a461c8cacd8900dfddeb0f33569acd39b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 1, 下溢（GPT channel 1, underflow）。

<a id="r_a0a3953d2055d7a37ecd73920c764ac19"></a>

```c
#define RZA2M_DMA_RS_CCMPA_2 RZA2M_DMA_RS(0x12FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_2](#a0a3953d2055d7a37ecd73920c764ac19)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配／输入捕获 A（GPT channel 2, compare match/input capture A）。

<a id="r_ad7bf1fa4ee518612f120b3920617ce15"></a>

```c
#define RZA2M_DMA_RS_CCMPB_2 RZA2M_DMA_RS(0x133U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_2](#ad7bf1fa4ee518612f120b3920617ce15)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配／输入捕获 B（GPT channel 2, compare match/input capture B）。

<a id="r_ac35c2d37a22b3f39ea1f5b8334442eb8"></a>

```c
#define RZA2M_DMA_RS_CMPC_2 RZA2M_DMA_RS(0x137U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_2](#ac35c2d37a22b3f39ea1f5b8334442eb8)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配 C（GPT channel 2, compare match C）。

<a id="r_a174500c43e9cdafce8a9817933d68e8f"></a>

```c
#define RZA2M_DMA_RS_CMPD_2 RZA2M_DMA_RS(0x13BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_2](#a174500c43e9cdafce8a9817933d68e8f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配 D（GPT channel 2, compare match D）。

<a id="r_a6cf8eac779bb550c3b810a07c5db6315"></a>

```c
#define RZA2M_DMA_RS_CMPE_2 RZA2M_DMA_RS(0x14BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_2](#a6cf8eac779bb550c3b810a07c5db6315)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配 E（GPT channel 2, compare match E）。

<a id="r_a96f6e7b2d20f4700d96e3e3d882a5a02"></a>

```c
#define RZA2M_DMA_RS_CMPF_2 RZA2M_DMA_RS(0x14FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_2](#a96f6e7b2d20f4700d96e3e3d882a5a02)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 比较匹配 F（GPT channel 2, compare match F）。

<a id="r_a2387bce54fc9dc6e0113b7efe0fab9e6"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_2 RZA2M_DMA_RS(0x153U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_2](#a2387bce54fc9dc6e0113b7efe0fab9e6)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 模数转换启动 A（GPT channel 2, A/D conversion start A）。

<a id="r_a279053cff8f0b65cdb5e708391cbbf2f"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_2 RZA2M_DMA_RS(0x157U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_2](#a279053cff8f0b65cdb5e708391cbbf2f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 模数转换启动 B（GPT channel 2, A/D conversion start B）。

<a id="r_acc1a0c994391fbee33100ff89755c740"></a>

```c
#define RZA2M_DMA_RS_OVF_2 RZA2M_DMA_RS(0x15BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_2](#acc1a0c994391fbee33100ff89755c740)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 上溢（GPT channel 2, overflow）。

<a id="r_a4d6bab832a8c9f8040f19e3b3458ad02"></a>

```c
#define RZA2M_DMA_RS_UNF_2 RZA2M_DMA_RS(0x15FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_2](#a4d6bab832a8c9f8040f19e3b3458ad02)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 2, 下溢（GPT channel 2, underflow）。

<a id="r_a775b62673fdf2bc099f9c9744df18398"></a>

```c
#define RZA2M_DMA_RS_CCMPA_3 RZA2M_DMA_RS(0x163U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_3](#a775b62673fdf2bc099f9c9744df18398)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配／输入捕获 A（GPT channel 3, compare match/input capture A）。

<a id="r_a79fe26d9f11d9ade5c17753b6ffc0cf7"></a>

```c
#define RZA2M_DMA_RS_CCMPB_3 RZA2M_DMA_RS(0x167U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_3](#a79fe26d9f11d9ade5c17753b6ffc0cf7)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配／输入捕获 B（GPT channel 3, compare match/input capture B）。

<a id="r_a758fdf3f2b4144d47fd7220a9456dd10"></a>

```c
#define RZA2M_DMA_RS_CMPC_3 RZA2M_DMA_RS(0x16BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_3](#a758fdf3f2b4144d47fd7220a9456dd10)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配 C（GPT channel 3, compare match C）。

<a id="r_adf8e674c8020932d1224eafc49106c4b"></a>

```c
#define RZA2M_DMA_RS_CMPD_3 RZA2M_DMA_RS(0x16FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_3](#adf8e674c8020932d1224eafc49106c4b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配 D（GPT channel 3, compare match D）。

<a id="r_a8cf1831b2a4487142214f081eb51448f"></a>

```c
#define RZA2M_DMA_RS_CMPE_3 RZA2M_DMA_RS(0x17FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_3](#a8cf1831b2a4487142214f081eb51448f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配 E（GPT channel 3, compare match E）。

<a id="r_a185a72b0562aa1455e6ead1ee85cb717"></a>

```c
#define RZA2M_DMA_RS_CMPF_3 RZA2M_DMA_RS(0x183U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_3](#a185a72b0562aa1455e6ead1ee85cb717)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 比较匹配 F（GPT channel 3, compare match F）。

<a id="r_ac73970fc88a90ba691424e4a93d32cd2"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_3 RZA2M_DMA_RS(0x187U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_3](#ac73970fc88a90ba691424e4a93d32cd2)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 模数转换启动 A（GPT channel 3, A/D conversion start A）。

<a id="r_adce2b9eb22e4ce5365a425aaafb9e753"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_3 RZA2M_DMA_RS(0x18BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_3](#adce2b9eb22e4ce5365a425aaafb9e753)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 模数转换启动 B（GPT channel 3, A/D conversion start B）。

<a id="r_a9e4755f83c4a8aaec0f063f83676b666"></a>

```c
#define RZA2M_DMA_RS_OVF_3 RZA2M_DMA_RS(0x18FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_3](#a9e4755f83c4a8aaec0f063f83676b666)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 上溢（GPT channel 3, overflow）。

<a id="r_aa875e7915331b5e49542755010366aeb"></a>

```c
#define RZA2M_DMA_RS_UNF_3 RZA2M_DMA_RS(0x193U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_3](#aa875e7915331b5e49542755010366aeb)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 3, 下溢（GPT channel 3, underflow）。

<a id="r_a930919806c768a6448f52a89afd2c2fe"></a>

```c
#define RZA2M_DMA_RS_CCMPA_4 RZA2M_DMA_RS(0x197U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_4](#a930919806c768a6448f52a89afd2c2fe)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配／输入捕获 A（GPT channel 4, compare match/input capture A）。

<a id="r_aca2adf86cbbe2d76338f21539120262f"></a>

```c
#define RZA2M_DMA_RS_CCMPB_4 RZA2M_DMA_RS(0x19BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_4](#aca2adf86cbbe2d76338f21539120262f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配／输入捕获 B（GPT channel 4, compare match/input capture B）。

<a id="r_a7fcf9c9696beddfa33af1fd73a43983a"></a>

```c
#define RZA2M_DMA_RS_CMPC_4 RZA2M_DMA_RS(0x19FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_4](#a7fcf9c9696beddfa33af1fd73a43983a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配 C（GPT channel 4, compare match C）。

<a id="r_a767c91361a18b5e15a149d8e4972d51a"></a>

```c
#define RZA2M_DMA_RS_CMPD_4 RZA2M_DMA_RS(0x1A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_4](#a767c91361a18b5e15a149d8e4972d51a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配 D（GPT channel 4, compare match D）。

<a id="r_ab658928a62b08b9bb7a7ab55bf1d77a5"></a>

```c
#define RZA2M_DMA_RS_CMPE_4 RZA2M_DMA_RS(0x1B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_4](#ab658928a62b08b9bb7a7ab55bf1d77a5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配 E（GPT channel 4, compare match E）。

<a id="r_a03fdeb8ee3ecee0cc546da79891966ca"></a>

```c
#define RZA2M_DMA_RS_CMPF_4 RZA2M_DMA_RS(0x1B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_4](#a03fdeb8ee3ecee0cc546da79891966ca)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 比较匹配 F（GPT channel 4, compare match F）。

<a id="r_a2ddd577e6d7f2f11074b25741aef8fb2"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_4 RZA2M_DMA_RS(0x1BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_4](#a2ddd577e6d7f2f11074b25741aef8fb2)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 模数转换启动 A（GPT channel 4, A/D conversion start A）。

<a id="r_a0866d0dae655a6804a2b3aa44a68dffb"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_4 RZA2M_DMA_RS(0x1BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_4](#a0866d0dae655a6804a2b3aa44a68dffb)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 模数转换启动 B（GPT channel 4, A/D conversion start B）。

<a id="r_a7e89308b7bb3999dc92c2b1debe6f264"></a>

```c
#define RZA2M_DMA_RS_OVF_4 RZA2M_DMA_RS(0x1C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_4](#a7e89308b7bb3999dc92c2b1debe6f264)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 上溢（GPT channel 4, overflow）。

<a id="r_ad4d7c222146f01f5f12c5dc4c68c7138"></a>

```c
#define RZA2M_DMA_RS_UNF_4 RZA2M_DMA_RS(0x1C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_4](#ad4d7c222146f01f5f12c5dc4c68c7138)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 4, 下溢（GPT channel 4, underflow）。

<a id="r_a34b1033e15f1cef7bde682626a51c237"></a>

```c
#define RZA2M_DMA_RS_CCMPA_5 RZA2M_DMA_RS(0x1CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_5](#a34b1033e15f1cef7bde682626a51c237)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配／输入捕获 A（GPT channel 5, compare match/input capture A）。

<a id="r_a4d5cec13fa602cf1dd68b845c8f024d8"></a>

```c
#define RZA2M_DMA_RS_CCMPB_5 RZA2M_DMA_RS(0x1CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_5](#a4d5cec13fa602cf1dd68b845c8f024d8)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配／输入捕获 B（GPT channel 5, compare match/input capture B）。

<a id="r_a166de2e44482fd2059f3d1d9fe5c0a21"></a>

```c
#define RZA2M_DMA_RS_CMPC_5 RZA2M_DMA_RS(0x1D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_5](#a166de2e44482fd2059f3d1d9fe5c0a21)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配 C（GPT channel 5, compare match C）。

<a id="r_aa32e5e651d7741e6fbb42f40c0bf64de"></a>

```c
#define RZA2M_DMA_RS_CMPD_5 RZA2M_DMA_RS(0x1D7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_5](#aa32e5e651d7741e6fbb42f40c0bf64de)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配 D（GPT channel 5, compare match D）。

<a id="r_a25f2fbd06abce86ac6e9663cc1df1e32"></a>

```c
#define RZA2M_DMA_RS_CMPE_5 RZA2M_DMA_RS(0x1E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_5](#a25f2fbd06abce86ac6e9663cc1df1e32)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配 E（GPT channel 5, compare match E）。

<a id="r_ae2613a5c3d68bcd7beee23930386ed93"></a>

```c
#define RZA2M_DMA_RS_CMPF_5 RZA2M_DMA_RS(0x1EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_5](#ae2613a5c3d68bcd7beee23930386ed93)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 比较匹配 F（GPT channel 5, compare match F）。

<a id="r_adf40ee3c6c661dacde4a846d9a8d4663"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_5 RZA2M_DMA_RS(0x1EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_5](#adf40ee3c6c661dacde4a846d9a8d4663)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 模数转换启动 A（GPT channel 5, A/D conversion start A）。

<a id="r_ae4cbb52e364034c41b2a45ad565c74ee"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_5 RZA2M_DMA_RS(0x1F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_5](#ae4cbb52e364034c41b2a45ad565c74ee)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 模数转换启动 B（GPT channel 5, A/D conversion start B）。

<a id="r_a3a77cedf37f532e3fb254106f9a48c2f"></a>

```c
#define RZA2M_DMA_RS_OVF_5 RZA2M_DMA_RS(0x1F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_5](#a3a77cedf37f532e3fb254106f9a48c2f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 上溢（GPT channel 5, overflow）。

<a id="r_ae9662e33f5bd00f2b1dbea6eda67bacb"></a>

```c
#define RZA2M_DMA_RS_UNF_5 RZA2M_DMA_RS(0x1FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_5](#ae9662e33f5bd00f2b1dbea6eda67bacb)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 5, 下溢（GPT channel 5, underflow）。

<a id="r_ad99c4d8ff86be43feb28a59d36aafe23"></a>

```c
#define RZA2M_DMA_RS_CCMPA_6 RZA2M_DMA_RS(0x1FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_6](#ad99c4d8ff86be43feb28a59d36aafe23)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配／输入捕获 A（GPT channel 6, compare match/input capture A）。

<a id="r_a81fbfe5613b591a79a3aa1f563b597ba"></a>

```c
#define RZA2M_DMA_RS_CCMPB_6 RZA2M_DMA_RS(0x203U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_6](#a81fbfe5613b591a79a3aa1f563b597ba)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配／输入捕获 B（GPT channel 6, compare match/input capture B）。

<a id="r_aa65898905b5e64c3f886d1451d3e1a5a"></a>

```c
#define RZA2M_DMA_RS_CMPC_6 RZA2M_DMA_RS(0x207U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_6](#aa65898905b5e64c3f886d1451d3e1a5a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配 C（GPT channel 6, compare match C）。

<a id="r_aef67f43795a139ad7b9e92f691417e28"></a>

```c
#define RZA2M_DMA_RS_CMPD_6 RZA2M_DMA_RS(0x20BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_6](#aef67f43795a139ad7b9e92f691417e28)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配 D（GPT channel 6, compare match D）。

<a id="r_a32873bb00c33f466c6f93baeccc02fa7"></a>

```c
#define RZA2M_DMA_RS_CMPE_6 RZA2M_DMA_RS(0x21BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_6](#a32873bb00c33f466c6f93baeccc02fa7)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配 E（GPT channel 6, compare match E）。

<a id="r_a0f6943f30cf0c1a615f5194b8e9c10ad"></a>

```c
#define RZA2M_DMA_RS_CMPF_6 RZA2M_DMA_RS(0x21FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_6](#a0f6943f30cf0c1a615f5194b8e9c10ad)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 比较匹配 F（GPT channel 6, compare match F）。

<a id="r_aed78a351eb8cc5c082761316d469d299"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_6 RZA2M_DMA_RS(0x223U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_6](#aed78a351eb8cc5c082761316d469d299)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 模数转换启动 A（GPT channel 6, A/D conversion start A）。

<a id="r_acc19c22f0d0eb6dc5d2a5c39fd60d3e5"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_6 RZA2M_DMA_RS(0x227U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_6](#acc19c22f0d0eb6dc5d2a5c39fd60d3e5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 模数转换启动 B（GPT channel 6, A/D conversion start B）。

<a id="r_aed75e450cf1ca73e617e40e1d77a7f2e"></a>

```c
#define RZA2M_DMA_RS_OVF_6 RZA2M_DMA_RS(0x22BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_6](#aed75e450cf1ca73e617e40e1d77a7f2e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 上溢（GPT channel 6, overflow）。

<a id="r_ac10ea111ad9060f6eed4976396898e92"></a>

```c
#define RZA2M_DMA_RS_UNF_6 RZA2M_DMA_RS(0x22FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_6](#ac10ea111ad9060f6eed4976396898e92)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 6, 下溢（GPT channel 6, underflow）。

<a id="r_a56d7db661f49b13a49e169c986c990a0"></a>

```c
#define RZA2M_DMA_RS_CCMPA_7 RZA2M_DMA_RS(0x233U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPA_7](#a56d7db661f49b13a49e169c986c990a0)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配／输入捕获 A（GPT channel 7, compare match/input capture A）。

<a id="r_a96eb7929f0764a7a48b1e8511dca5d8f"></a>

```c
#define RZA2M_DMA_RS_CCMPB_7 RZA2M_DMA_RS(0x237U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CCMPB_7](#a96eb7929f0764a7a48b1e8511dca5d8f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配／输入捕获 B（GPT channel 7, compare match/input capture B）。

<a id="r_ad5ae81d3e17d8a207ab21c584e97299b"></a>

```c
#define RZA2M_DMA_RS_CMPC_7 RZA2M_DMA_RS(0x23BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPC_7](#ad5ae81d3e17d8a207ab21c584e97299b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配 C（GPT channel 7, compare match C）。

<a id="r_abbca7860c61098afc9f2f6e1bd0e0a2b"></a>

```c
#define RZA2M_DMA_RS_CMPD_7 RZA2M_DMA_RS(0x23FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPD_7](#abbca7860c61098afc9f2f6e1bd0e0a2b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配 D（GPT channel 7, compare match D）。

<a id="r_a12f540fa28f0192c11e5204bd88f5217"></a>

```c
#define RZA2M_DMA_RS_CMPE_7 RZA2M_DMA_RS(0x24FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPE_7](#a12f540fa28f0192c11e5204bd88f5217)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配 E（GPT channel 7, compare match E）。

<a id="r_abc38d3179ddaccc328b5ecebe379c4ae"></a>

```c
#define RZA2M_DMA_RS_CMPF_7 RZA2M_DMA_RS(0x253U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_CMPF_7](#abc38d3179ddaccc328b5ecebe379c4ae)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 比较匹配 F（GPT channel 7, compare match F）。

<a id="r_a54c65d5895f9683b7962e0fb065ff592"></a>

```c
#define RZA2M_DMA_RS_ADTRGA_7 RZA2M_DMA_RS(0x257U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGA_7](#a54c65d5895f9683b7962e0fb065ff592)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 模数转换启动 A（GPT channel 7, A/D conversion start A）。

<a id="r_ae40a4d166556998062efcea860adae22"></a>

```c
#define RZA2M_DMA_RS_ADTRGB_7 RZA2M_DMA_RS(0x25BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_ADTRGB_7](#ae40a4d166556998062efcea860adae22)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 模数转换启动 B（GPT channel 7, A/D conversion start B）。

<a id="r_a3bdff659a036dd2153902e8ba5d16add"></a>

```c
#define RZA2M_DMA_RS_OVF_7 RZA2M_DMA_RS(0x25FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_OVF_7](#a3bdff659a036dd2153902e8ba5d16add)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 上溢（GPT channel 7, overflow）。

<a id="r_ad3fd3d94dd8f4af97717b7da6c27fe04"></a>

```c
#define RZA2M_DMA_RS_UNF_7 RZA2M_DMA_RS(0x263U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_UNF_7](#ad3fd3d94dd8f4af97717b7da6c27fe04)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

GPT 通道 7, 下溢（GPT channel 7, underflow）。

<a id="r_adfffeffc377bfb7236ce602a064f603d"></a>

```c
#define RZA2M_DMA_RS_S12ADI_0 RZA2M_DMA_RS(0x267U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_S12ADI_0](#adfffeffc377bfb7236ce602a064f603d)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

ADC 扫描结束中断（ADC scan end interrupt）。

<a id="r_ab30dccf89ae684329c9d39bfcb8838f6"></a>

```c
#define RZA2M_DMA_RS_S12GBADI_0 RZA2M_DMA_RS(0x26BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_S12GBADI_0](#ab30dccf89ae684329c9d39bfcb8838f6)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

ADC 组 B 扫描结束中断（ADC group B scan end interrupt）。

<a id="r_abbf1a7432706059fb1786159810e6c40"></a>

```c
#define RZA2M_DMA_RS_S12GCADI_0 RZA2M_DMA_RS(0x26FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_S12GCADI_0](#abbf1a7432706059fb1786159810e6c40)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

ADC 组 C 扫描结束中断（ADC group C scan end interrupt）。

<a id="r_a424d5349b245f3b4b51c55b58a83cd73"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_0 RZA2M_DMA_RS(0x272U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_RX_0](#a424d5349b245f3b4b51c55b58a83cd73)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 0, DMA 接收（SSIF channel 0, DMA receive）。

<a id="r_a615bba9636d6b50b071467330db990db"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_0 RZA2M_DMA_RS(0x271U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_TX_0](#a615bba9636d6b50b071467330db990db)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 0, DMA 发送（SSIF channel 0, DMA transmit）。

<a id="r_aca770562cba12f664d689d578ac8e061"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_1 RZA2M_DMA_RS(0x276U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_RX_1](#aca770562cba12f664d689d578ac8e061)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 1, DMA 接收（SSIF channel 1, DMA receive）。

<a id="r_a5f9cb34b8bed3618ec82dc743d6cb66d"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_1 RZA2M_DMA_RS(0x275U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_TX_1](#a5f9cb34b8bed3618ec82dc743d6cb66d)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 1, DMA 发送（SSIF channel 1, DMA transmit）。

<a id="r_a462d83c5f1c67b839279eabb4948eed3"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_2 RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_RX_2](#a462d83c5f1c67b839279eabb4948eed3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 2, DMA 接收（SSIF channel 2, DMA receive）。

<a id="r_a4057badb9ab4c26ae07a44ff8174d6d3"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_2 RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_TX_2](#a4057badb9ab4c26ae07a44ff8174d6d3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 2, DMA 发送（SSIF channel 2, DMA transmit）。

<a id="r_a3040329c3dd6cd6cd7c763308542324a"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_3 RZA2M_DMA_RS(0x27EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_RX_3](#a3040329c3dd6cd6cd7c763308542324a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 3, DMA 接收（SSIF channel 3, DMA receive）。

<a id="r_a9caff07d4ded76f507e4290f355e1927"></a>

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_3 RZA2M_DMA_RS(0x27DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INT_SSIF_DMA_TX_3](#a9caff07d4ded76f507e4290f355e1927)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SSIF 通道 3, DMA 发送（SSIF channel 3, DMA transmit）。

<a id="r_a6354bbdb9965199e9ab9b76e00182fc4"></a>

```c
#define RZA2M_DMA_RS_SPDIFTXI RZA2M_DMA_RS(0x283U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SPDIFTXI](#a6354bbdb9965199e9ab9b76e00182fc4)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SPDIF 发送中断（SPDIF transmit interrupt）。

<a id="r_ad063e32fe7421099580d982031680efb"></a>

```c
#define RZA2M_DMA_RS_SPDIFRXI RZA2M_DMA_RS(0x287U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SPDIFRXI](#ad063e32fe7421099580d982031680efb)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SPDIF 接收中断（SPDIF receive interrupt）。

<a id="r_a512e50009a95d69d84f258691185396a"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_RI0 RZA2M_DMA_RS(0x28AU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_RI0](#a512e50009a95d69d84f258691185396a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 0, 接收中断（RIIC channel 0, receive interrupt）。

<a id="r_a748fd050ce97162bc6bf8b55dfff6202"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_TI0 RZA2M_DMA_RS(0x289U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_TI0](#a748fd050ce97162bc6bf8b55dfff6202)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 0, 发送中断（RIIC channel 0, transmit interrupt）。

<a id="r_a3ccf8181a26704505026cd6ca6e78776"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_RI1 RZA2M_DMA_RS(0x28EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_RI1](#a3ccf8181a26704505026cd6ca6e78776)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 1, 接收中断（RIIC channel 1, receive interrupt）。

<a id="r_aa8cd867c1c9b8a8c8ff7a0e933083979"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_TI1 RZA2M_DMA_RS(0x28DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_TI1](#aa8cd867c1c9b8a8c8ff7a0e933083979)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 1, 发送中断（RIIC channel 1, transmit interrupt）。

<a id="r_a1bd7dc91baca8523305a9aa7593413e9"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_RI2 RZA2M_DMA_RS(0x292U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_RI2](#a1bd7dc91baca8523305a9aa7593413e9)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 2, 接收中断（RIIC channel 2, receive interrupt）。

<a id="r_a70576d59a7cd36f8866efc457bc9846b"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_TI2 RZA2M_DMA_RS(0x291U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_TI2](#a70576d59a7cd36f8866efc457bc9846b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 2, 发送中断（RIIC channel 2, transmit interrupt）。

<a id="r_a0bf3255b1b88d156ecbea326c9e6578c"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_RI3 RZA2M_DMA_RS(0x296U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_RI3](#a0bf3255b1b88d156ecbea326c9e6578c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 3, 接收中断（RIIC channel 3, receive interrupt）。

<a id="r_a5f212e541dd402b608ced9b9091c5da4"></a>

```c
#define RZA2M_DMA_RS_INTRIIC_TI3 RZA2M_DMA_RS(0x295U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_INTRIIC_TI3](#a5f212e541dd402b608ced9b9091c5da4)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RIIC 通道 3, 发送中断（RIIC channel 3, transmit interrupt）。

<a id="r_a7dd81d3f4b4a338c336efb0fb5748abc"></a>

```c
#define RZA2M_DMA_RS_RXI0 RZA2M_DMA_RS(0x29AU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_RXI0](#a7dd81d3f4b4a338c336efb0fb5748abc)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 0, 接收中断（SCIF channel 0, receive interrupt）。

<a id="r_a496490e9393b330865cd4553a35d76bf"></a>

```c
#define RZA2M_DMA_RS_TXI0 RZA2M_DMA_RS(0x299U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TXI0](#a496490e9393b330865cd4553a35d76bf)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 0, 发送中断（SCIF channel 0, transmit interrupt）。

<a id="r_a08a2bf046ae7193f0cf82db34038ca8d"></a>

```c
#define RZA2M_DMA_RS_RXI1 RZA2M_DMA_RS(0x29EU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_RXI1](#a08a2bf046ae7193f0cf82db34038ca8d)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 1, 接收中断（SCIF channel 1, receive interrupt）。

<a id="r_a7516731e183b49a7790d0e61b0768e23"></a>

```c
#define RZA2M_DMA_RS_TXI1 RZA2M_DMA_RS(0x29DU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TXI1](#a7516731e183b49a7790d0e61b0768e23)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 1, 发送中断（SCIF channel 1, transmit interrupt）。

<a id="r_a93c5b3e0d31c22fbe710e5e42ca73ed5"></a>

```c
#define RZA2M_DMA_RS_RXI2 RZA2M_DMA_RS(0x2A2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_RXI2](#a93c5b3e0d31c22fbe710e5e42ca73ed5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 2, 接收中断（SCIF channel 2, receive interrupt）。

<a id="r_a5dd127eca1fd1c1964bd2d7f75438f2c"></a>

```c
#define RZA2M_DMA_RS_TXI2 RZA2M_DMA_RS(0x2A1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TXI2](#a5dd127eca1fd1c1964bd2d7f75438f2c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 2, 发送中断（SCIF channel 2, transmit interrupt）。

<a id="r_a73afb81051a66a6de0dc1c4665d09304"></a>

```c
#define RZA2M_DMA_RS_RXI3 RZA2M_DMA_RS(0x2A6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_RXI3](#a73afb81051a66a6de0dc1c4665d09304)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 3, 接收中断（SCIF channel 3, receive interrupt）。

<a id="r_a3f13c36be6185f9f371411e3c516a38c"></a>

```c
#define RZA2M_DMA_RS_TXI3 RZA2M_DMA_RS(0x2A5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TXI3](#a3f13c36be6185f9f371411e3c516a38c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 3, 发送中断（SCIF channel 3, transmit interrupt）。

<a id="r_ab417d142ddba4bad46a692153202d06b"></a>

```c
#define RZA2M_DMA_RS_RXI4 RZA2M_DMA_RS(0x2AAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_RXI4](#ab417d142ddba4bad46a692153202d06b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 4, 接收中断（SCIF channel 4, receive interrupt）。

<a id="r_a8762f45b557c41d228857a7deede8030"></a>

```c
#define RZA2M_DMA_RS_TXI4 RZA2M_DMA_RS(0x2A9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TXI4](#a8762f45b557c41d228857a7deede8030)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCIF 通道 4, 发送中断（SCIF channel 4, transmit interrupt）。

<a id="r_a95e9a78cd37654fb493171c5d2445789"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA0 RZA2M_DMA_RS(0x2AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA0](#a95e9a78cd37654fb493171c5d2445789)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 0（CAN, receive FIFO DMA channel 0）。

<a id="r_a8f473b6e68d0ecbb27cc85450240fcbe"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA1 RZA2M_DMA_RS(0x2B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA1](#a8f473b6e68d0ecbb27cc85450240fcbe)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 1（CAN, receive FIFO DMA channel 1）。

<a id="r_ab0c51920a47fe8379e780601df5919b3"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA2 RZA2M_DMA_RS(0x2B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA2](#ab0c51920a47fe8379e780601df5919b3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 2（CAN, receive FIFO DMA channel 2）。

<a id="r_a1d50c93288a532ef168f1b86ec8692f0"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA3 RZA2M_DMA_RS(0x2BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA3](#a1d50c93288a532ef168f1b86ec8692f0)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 3（CAN, receive FIFO DMA channel 3）。

<a id="r_ab7f1184156a68ec8d0da0b2912979f32"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA4 RZA2M_DMA_RS(0x2BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA4](#ab7f1184156a68ec8d0da0b2912979f32)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 4（CAN, receive FIFO DMA channel 4）。

<a id="r_a49d3857e13e2c80c5890edde428edb6b"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA5 RZA2M_DMA_RS(0x2C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA5](#a49d3857e13e2c80c5890edde428edb6b)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 5（CAN, receive FIFO DMA channel 5）。

<a id="r_a8b051cd40a1fd1512de65db48ea7a49e"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA6 RZA2M_DMA_RS(0x2C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA6](#a8b051cd40a1fd1512de65db48ea7a49e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 6（CAN, receive FIFO DMA channel 6）。

<a id="r_a1ab1c31d3c7e4cf6bca4412ac17aa5a4"></a>

```c
#define RZA2M_DMA_RS_RXF_DMA7 RZA2M_DMA_RS(0x2CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_RXF_DMA7](#a1ab1c31d3c7e4cf6bca4412ac17aa5a4)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 接收 FIFO DMA 通道 7（CAN, receive FIFO DMA channel 7）。

<a id="r_a3e456126b008f6ca2e49aa300ed3b8dd"></a>

```c
#define RZA2M_DMA_RS_COM_DMA0 RZA2M_DMA_RS(0x2CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_COM_DMA0](#a3e456126b008f6ca2e49aa300ed3b8dd)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 公共 FIFO DMA 通道 0（CAN, common FIFO DMA channel 0）。

<a id="r_ab620ddb2e02d5f3a9bd55d8b306e759a"></a>

```c
#define RZA2M_DMA_RS_COM_DMA1 RZA2M_DMA_RS(0x2D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_COM_DMA1](#ab620ddb2e02d5f3a9bd55d8b306e759a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

CAN, 公共 FIFO DMA 通道 1（CAN, common FIFO DMA channel 1）。

<a id="r_a72a053f7bd6e62562148a40b3b9795de"></a>

```c
#define RZA2M_DMA_RS_SPRI0 RZA2M_DMA_RS(0x2D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SPRI0](#a72a053f7bd6e62562148a40b3b9795de)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 0, 接收中断（RSPI channel 0, receive interrupt）。

<a id="r_a6231a82cb548bea0d25d6208c3f251e5"></a>

```c
#define RZA2M_DMA_RS_SPTI0 RZA2M_DMA_RS(0x2D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SPTI0](#a6231a82cb548bea0d25d6208c3f251e5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 0, 发送中断（RSPI channel 0, transmit interrupt）。

<a id="r_adb9fc9139570ff8cd6f654574abaf7b1"></a>

```c
#define RZA2M_DMA_RS_SPRI1 RZA2M_DMA_RS(0x2DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SPRI1](#adb9fc9139570ff8cd6f654574abaf7b1)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 1, 接收中断（RSPI channel 1, receive interrupt）。

<a id="r_a5668f986198059bc6ea00fff3f3a5bad"></a>

```c
#define RZA2M_DMA_RS_SPTI1 RZA2M_DMA_RS(0x2D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SPTI1](#a5668f986198059bc6ea00fff3f3a5bad)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 1, 发送中断（RSPI channel 1, transmit interrupt）。

<a id="r_a33412fcf2247e86f10ab8cb2536c9b3e"></a>

```c
#define RZA2M_DMA_RS_SPRI2 RZA2M_DMA_RS(0x2DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SPRI2](#a33412fcf2247e86f10ab8cb2536c9b3e)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 2, 接收中断（RSPI channel 2, receive interrupt）。

<a id="r_a9149fb1b1f9731366556b162dbf493f9"></a>

```c
#define RZA2M_DMA_RS_SPTI2 RZA2M_DMA_RS(0x2DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SPTI2](#a9149fb1b1f9731366556b162dbf493f9)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

RSPI 通道 2, 发送中断（RSPI channel 2, transmit interrupt）。

<a id="r_a7ecda7d5cccfd90fcda09a350f420e3a"></a>

```c
#define RZA2M_DMA_RS_SCI_RXI0 RZA2M_DMA_RS(0x2E2U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SCI_RXI0](#a7ecda7d5cccfd90fcda09a350f420e3a)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCI 通道 0, 接收中断（SCI channel 0, receive interrupt）。

<a id="r_aa8e3ecdcdcfbf107eae78dc913736ac3"></a>

```c
#define RZA2M_DMA_RS_SCI_TXI0 RZA2M_DMA_RS(0x2E1U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SCI_TXI0](#aa8e3ecdcdcfbf107eae78dc913736ac3)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCI 通道 0, 发送中断（SCI channel 0, transmit interrupt）。

<a id="r_a83a3cc69c4b548c0cae87c68495dabe8"></a>

```c
#define RZA2M_DMA_RS_SCI_RXI1 RZA2M_DMA_RS(0x2E6U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_SCI_RXI1](#a83a3cc69c4b548c0cae87c68495dabe8)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCI 通道 1, 接收中断（SCI channel 1, receive interrupt）。

<a id="r_a216e8cbeecc148f27638c1edba42f0fd"></a>

```c
#define RZA2M_DMA_RS_SCI_TXI1 RZA2M_DMA_RS(0x2E5U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_SCI_TXI1](#a216e8cbeecc148f27638c1edba42f0fd)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

SCI 通道 1, 发送中断（SCI channel 1, transmit interrupt）。

<a id="r_a5eb36dd01681895e8e93127f37226aee"></a>

```c
#define RZA2M_DMA_RS_IPLS RZA2M_DMA_RS(0x2EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

相关声明：[RZA2M_DMA_RS_IPLS](#a5eb36dd01681895e8e93127f37226aee)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

以太网 MAC 控制器（Ethernet MAC Controller）的 IPLS。

<a id="r_a5aeb8ebfcd18f53cc39ebbe8832c324f"></a>

```c
#define RZA2M_DMA_RS_TILE_0_PAFI RZA2M_DMA_RS(0x3CEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_0_PAFI](#a5aeb8ebfcd18f53cc39ebbe8832c324f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 0 可编程近满（DRP Tile 0 Programmable Almost Full）。

<a id="r_afb75f0c8cd0e4a150ab69d202f3891b0"></a>

```c
#define RZA2M_DMA_RS_TILE_0_PAEI RZA2M_DMA_RS(0x3CDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_0_PAEI](#afb75f0c8cd0e4a150ab69d202f3891b0)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 0 可编程近空（DRP Tile 0 Programmable Almost Empty）。

<a id="r_ab3dbfc391e66332a5921ec2c1fdca39f"></a>

```c
#define RZA2M_DMA_RS_TILE_1_PAFI RZA2M_DMA_RS(0x3D2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_1_PAFI](#ab3dbfc391e66332a5921ec2c1fdca39f)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 1 可编程近满（DRP Tile 1 Programmable Almost Full）。

<a id="r_aae0118afd293747ebdce414548a5b6a7"></a>

```c
#define RZA2M_DMA_RS_TILE_1_PAEI RZA2M_DMA_RS(0x3D1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_1_PAEI](#aae0118afd293747ebdce414548a5b6a7)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 1 可编程近空（DRP Tile 1 Programmable Almost Empty）。

<a id="r_ae4003c09956059f2afa1086f84e162eb"></a>

```c
#define RZA2M_DMA_RS_TILE_2_PAFI RZA2M_DMA_RS(0x3D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_2_PAFI](#ae4003c09956059f2afa1086f84e162eb)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 2 可编程近满（DRP Tile 2 Programmable Almost Full）。

<a id="r_acdeb33533030248bb7fcd8afe1c72f09"></a>

```c
#define RZA2M_DMA_RS_TILE_2_PAEI RZA2M_DMA_RS(0x3D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_2_PAEI](#acdeb33533030248bb7fcd8afe1c72f09)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 2 可编程近空（DRP Tile 2 Programmable Almost Empty）。

<a id="r_af2da1374c122258426a74758bfa4866c"></a>

```c
#define RZA2M_DMA_RS_TILE_3_PAFI RZA2M_DMA_RS(0x3DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_3_PAFI](#af2da1374c122258426a74758bfa4866c)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 3 可编程近满（DRP Tile 3 Programmable Almost Full）。

<a id="r_a4b4da99cb156f9c2521373b10b9d0318"></a>

```c
#define RZA2M_DMA_RS_TILE_3_PAEI RZA2M_DMA_RS(0x3D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_3_PAEI](#a4b4da99cb156f9c2521373b10b9d0318)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 3 可编程近空（DRP Tile 3 Programmable Almost Empty）。

<a id="r_a1e8d4ec416151d4dd59e1e5fb80900c5"></a>

```c
#define RZA2M_DMA_RS_TILE_4_PAFI RZA2M_DMA_RS(0x3DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_4_PAFI](#a1e8d4ec416151d4dd59e1e5fb80900c5)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 4 可编程近满（DRP Tile 4 Programmable Almost Full）。

<a id="r_ace299eb47bb0126f7d3c1f56cb6daea2"></a>

```c
#define RZA2M_DMA_RS_TILE_4_PAEI RZA2M_DMA_RS(0x3DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_4_PAEI](#ace299eb47bb0126f7d3c1f56cb6daea2)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 4 可编程近空（DRP Tile 4 Programmable Almost Empty）。

<a id="r_acac0bb9cf60d3f0d96925db19b433488"></a>

```c
#define RZA2M_DMA_RS_TILE_5_PAFI RZA2M_DMA_RS(0x3E2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

相关声明：[RZA2M_DMA_RS_TILE_5_PAFI](#acac0bb9cf60d3f0d96925db19b433488)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 5 可编程近满（DRP Tile 5 Programmable Almost Full）。

<a id="r_aa2c2874df19d68f2a40869d8de83ba68"></a>

```c
#define RZA2M_DMA_RS_TILE_5_PAEI RZA2M_DMA_RS(0x3E1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

相关声明：[RZA2M_DMA_RS_TILE_5_PAEI](#aa2c2874df19d68f2a40869d8de83ba68)、[RZA2M_DMA_RS](#a391ba1663b69e478fb4c82c35b16e176)。

DRP 单元 5 可编程近空（DRP Tile 5 Programmable Almost Empty）。

<a id="r_acb45792a1764debb7f7f4d7841b0cc7e"></a>

```c
#define RZA2M_DMA_DMARS_EXT_DREQ0 0x003U
```

相关声明：[RZA2M_DMA_DMARS_EXT_DREQ0](#acb45792a1764debb7f7f4d7841b0cc7e)。

外部 `DREQ0` 引脚的 DMARS 请求码（Request Code）。

<a id="r_a9ee90583e90208d851c4fca6f46b0101"></a>

```c
#define RZA2M_DMA_RS_DREQ0
```

相关声明：[RZA2M_DMA_RS_DREQ0](#a9ee90583e90208d851c4fca6f46b0101)。

外部 DMA 请求（External DMA Request）。

## 4.2\_详细说明（Detailed Documentation）

<a id="acb45792a1764debb7f7f4d7841b0cc7e"></a>

### `RZA2M_DMA_DMARS_EXT_DREQ0`

```c
#define RZA2M_DMA_DMARS_EXT_DREQ0 0x003U
```

外部 `DREQ0` 引脚的 DMARS 请求码（Request Code）。

<a id="a2b5170fc1b55ab2fab9da061f42bc9fc"></a>

### `RZA2M_DMA_MEM_2_MEM`

```c
#define RZA2M_DMA_MEM_2_MEM 0x0U
```

内存到内存传输（Memory-to-memory Transfer），由软件触发（Software Triggered）。

<a id="a391ba1663b69e478fb4c82c35b16e176"></a>

### `RZA2M_DMA_RS`

```c
#define RZA2M_DMA_RS ( dmars, lvl, am, reqd )
```

展开值（Value）：

```c
(((dmars) & 0xFFFFU) | (lvl) | (am) | (reqd))
```

将 DMARS 请求码（Request Code）及其固定的 CHCFG 标志（Flags）打包为一个槽位值（Slot Value）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dmars` | DMARS 请求值（Request Value）编码在位 [15:0]。 |
| `lvl` | 检测电平值（Detection Level Value）编码在位 [16]。 |
| `am` | 确认模式值（Acknowledge Mode Value）编码在位 [19:17]。 |
| `reqd` | 请求方向值（Request Direction Value）编码在位 [21:20]。 |

<a id="ac77fa619e6b8e4f0ad6ed834da1f61b1"></a>

### `RZA2M_DMA_RS_ADTRGA_0`

```c
#define RZA2M_DMA_RS_ADTRGA_0 RZA2M_DMA_RS(0x0EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 模数转换启动 A（GPT channel 0, A/D conversion start A）。

<a id="a34ccbbf7062e250a45c5da1334a696ab"></a>

### `RZA2M_DMA_RS_ADTRGA_1`

```c
#define RZA2M_DMA_RS_ADTRGA_1 RZA2M_DMA_RS(0x11FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 模数转换启动 A（GPT channel 1, A/D conversion start A）。

<a id="a2387bce54fc9dc6e0113b7efe0fab9e6"></a>

### `RZA2M_DMA_RS_ADTRGA_2`

```c
#define RZA2M_DMA_RS_ADTRGA_2 RZA2M_DMA_RS(0x153U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 模数转换启动 A（GPT channel 2, A/D conversion start A）。

<a id="ac73970fc88a90ba691424e4a93d32cd2"></a>

### `RZA2M_DMA_RS_ADTRGA_3`

```c
#define RZA2M_DMA_RS_ADTRGA_3 RZA2M_DMA_RS(0x187U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 模数转换启动 A（GPT channel 3, A/D conversion start A）。

<a id="a2ddd577e6d7f2f11074b25741aef8fb2"></a>

### `RZA2M_DMA_RS_ADTRGA_4`

```c
#define RZA2M_DMA_RS_ADTRGA_4 RZA2M_DMA_RS(0x1BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 模数转换启动 A（GPT channel 4, A/D conversion start A）。

<a id="adf40ee3c6c661dacde4a846d9a8d4663"></a>

### `RZA2M_DMA_RS_ADTRGA_5`

```c
#define RZA2M_DMA_RS_ADTRGA_5 RZA2M_DMA_RS(0x1EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 模数转换启动 A（GPT channel 5, A/D conversion start A）。

<a id="aed78a351eb8cc5c082761316d469d299"></a>

### `RZA2M_DMA_RS_ADTRGA_6`

```c
#define RZA2M_DMA_RS_ADTRGA_6 RZA2M_DMA_RS(0x223U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 模数转换启动 A（GPT channel 6, A/D conversion start A）。

<a id="a54c65d5895f9683b7962e0fb065ff592"></a>

### `RZA2M_DMA_RS_ADTRGA_7`

```c
#define RZA2M_DMA_RS_ADTRGA_7 RZA2M_DMA_RS(0x257U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 模数转换启动 A（GPT channel 7, A/D conversion start A）。

<a id="a6fb7cbeab5a0d05a2d58b59705279e2c"></a>

### `RZA2M_DMA_RS_ADTRGB_0`

```c
#define RZA2M_DMA_RS_ADTRGB_0 RZA2M_DMA_RS(0x0EFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 模数转换启动 B（GPT channel 0, A/D conversion start B）。

<a id="a922d8675c78b8937b539cbaeb574bc12"></a>

### `RZA2M_DMA_RS_ADTRGB_1`

```c
#define RZA2M_DMA_RS_ADTRGB_1 RZA2M_DMA_RS(0x123U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 模数转换启动 B（GPT channel 1, A/D conversion start B）。

<a id="a279053cff8f0b65cdb5e708391cbbf2f"></a>

### `RZA2M_DMA_RS_ADTRGB_2`

```c
#define RZA2M_DMA_RS_ADTRGB_2 RZA2M_DMA_RS(0x157U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 模数转换启动 B（GPT channel 2, A/D conversion start B）。

<a id="adce2b9eb22e4ce5365a425aaafb9e753"></a>

### `RZA2M_DMA_RS_ADTRGB_3`

```c
#define RZA2M_DMA_RS_ADTRGB_3 RZA2M_DMA_RS(0x18BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 模数转换启动 B（GPT channel 3, A/D conversion start B）。

<a id="a0866d0dae655a6804a2b3aa44a68dffb"></a>

### `RZA2M_DMA_RS_ADTRGB_4`

```c
#define RZA2M_DMA_RS_ADTRGB_4 RZA2M_DMA_RS(0x1BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 模数转换启动 B（GPT channel 4, A/D conversion start B）。

<a id="ae4cbb52e364034c41b2a45ad565c74ee"></a>

### `RZA2M_DMA_RS_ADTRGB_5`

```c
#define RZA2M_DMA_RS_ADTRGB_5 RZA2M_DMA_RS(0x1F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 模数转换启动 B（GPT channel 5, A/D conversion start B）。

<a id="acc19c22f0d0eb6dc5d2a5c39fd60d3e5"></a>

### `RZA2M_DMA_RS_ADTRGB_6`

```c
#define RZA2M_DMA_RS_ADTRGB_6 RZA2M_DMA_RS(0x227U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 模数转换启动 B（GPT channel 6, A/D conversion start B）。

<a id="ae40a4d166556998062efcea860adae22"></a>

### `RZA2M_DMA_RS_ADTRGB_7`

```c
#define RZA2M_DMA_RS_ADTRGB_7 RZA2M_DMA_RS(0x25BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 模数转换启动 B（GPT channel 7, A/D conversion start B）。

<a id="aef4ed46740b478c7e521e143bb3bdcb8"></a>

### `RZA2M_DMA_RS_CCMPA_0`

```c
#define RZA2M_DMA_RS_CCMPA_0 RZA2M_DMA_RS(0x0C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配／输入捕获 A（GPT channel 0, compare match/input capture A）。

<a id="a72db7dba30d7456ad1dd81325360f04e"></a>

### `RZA2M_DMA_RS_CCMPA_1`

```c
#define RZA2M_DMA_RS_CCMPA_1 RZA2M_DMA_RS(0x0FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配／输入捕获 A（GPT channel 1, compare match/input capture A）。

<a id="a0a3953d2055d7a37ecd73920c764ac19"></a>

### `RZA2M_DMA_RS_CCMPA_2`

```c
#define RZA2M_DMA_RS_CCMPA_2 RZA2M_DMA_RS(0x12FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配／输入捕获 A（GPT channel 2, compare match/input capture A）。

<a id="a775b62673fdf2bc099f9c9744df18398"></a>

### `RZA2M_DMA_RS_CCMPA_3`

```c
#define RZA2M_DMA_RS_CCMPA_3 RZA2M_DMA_RS(0x163U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配／输入捕获 A（GPT channel 3, compare match/input capture A）。

<a id="a930919806c768a6448f52a89afd2c2fe"></a>

### `RZA2M_DMA_RS_CCMPA_4`

```c
#define RZA2M_DMA_RS_CCMPA_4 RZA2M_DMA_RS(0x197U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配／输入捕获 A（GPT channel 4, compare match/input capture A）。

<a id="a34b1033e15f1cef7bde682626a51c237"></a>

### `RZA2M_DMA_RS_CCMPA_5`

```c
#define RZA2M_DMA_RS_CCMPA_5 RZA2M_DMA_RS(0x1CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配／输入捕获 A（GPT channel 5, compare match/input capture A）。

<a id="ad99c4d8ff86be43feb28a59d36aafe23"></a>

### `RZA2M_DMA_RS_CCMPA_6`

```c
#define RZA2M_DMA_RS_CCMPA_6 RZA2M_DMA_RS(0x1FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配／输入捕获 A（GPT channel 6, compare match/input capture A）。

<a id="a56d7db661f49b13a49e169c986c990a0"></a>

### `RZA2M_DMA_RS_CCMPA_7`

```c
#define RZA2M_DMA_RS_CCMPA_7 RZA2M_DMA_RS(0x233U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配／输入捕获 A（GPT channel 7, compare match/input capture A）。

<a id="a689150899bb088f5194109c91369eff7"></a>

### `RZA2M_DMA_RS_CCMPB_0`

```c
#define RZA2M_DMA_RS_CCMPB_0 RZA2M_DMA_RS(0x0CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配／输入捕获 B（GPT channel 0, compare match/input capture B）。

<a id="a02ccc8a1e530c56b2ad92ebb6117693e"></a>

### `RZA2M_DMA_RS_CCMPB_1`

```c
#define RZA2M_DMA_RS_CCMPB_1 RZA2M_DMA_RS(0x0FFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配／输入捕获 B（GPT channel 1, compare match/input capture B）。

<a id="ad7bf1fa4ee518612f120b3920617ce15"></a>

### `RZA2M_DMA_RS_CCMPB_2`

```c
#define RZA2M_DMA_RS_CCMPB_2 RZA2M_DMA_RS(0x133U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配／输入捕获 B（GPT channel 2, compare match/input capture B）。

<a id="a79fe26d9f11d9ade5c17753b6ffc0cf7"></a>

### `RZA2M_DMA_RS_CCMPB_3`

```c
#define RZA2M_DMA_RS_CCMPB_3 RZA2M_DMA_RS(0x167U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配／输入捕获 B（GPT channel 3, compare match/input capture B）。

<a id="aca2adf86cbbe2d76338f21539120262f"></a>

### `RZA2M_DMA_RS_CCMPB_4`

```c
#define RZA2M_DMA_RS_CCMPB_4 RZA2M_DMA_RS(0x19BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配／输入捕获 B（GPT channel 4, compare match/input capture B）。

<a id="a4d5cec13fa602cf1dd68b845c8f024d8"></a>

### `RZA2M_DMA_RS_CCMPB_5`

```c
#define RZA2M_DMA_RS_CCMPB_5 RZA2M_DMA_RS(0x1CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配／输入捕获 B（GPT channel 5, compare match/input capture B）。

<a id="a81fbfe5613b591a79a3aa1f563b597ba"></a>

### `RZA2M_DMA_RS_CCMPB_6`

```c
#define RZA2M_DMA_RS_CCMPB_6 RZA2M_DMA_RS(0x203U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配／输入捕获 B（GPT channel 6, compare match/input capture B）。

<a id="a96eb7929f0764a7a48b1e8511dca5d8f"></a>

### `RZA2M_DMA_RS_CCMPB_7`

```c
#define RZA2M_DMA_RS_CCMPB_7 RZA2M_DMA_RS(0x237U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配／输入捕获 B（GPT channel 7, compare match/input capture B）。

<a id="a4f3a8525da395c46d6d4eb44417754cd"></a>

### `RZA2M_DMA_RS_CMPC_0`

```c
#define RZA2M_DMA_RS_CMPC_0 RZA2M_DMA_RS(0x0CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配 C（GPT channel 0, compare match C）。

<a id="abfc0de01ac870273e400115539e398ea"></a>

### `RZA2M_DMA_RS_CMPC_1`

```c
#define RZA2M_DMA_RS_CMPC_1 RZA2M_DMA_RS(0x103U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配 C（GPT channel 1, compare match C）。

<a id="ac35c2d37a22b3f39ea1f5b8334442eb8"></a>

### `RZA2M_DMA_RS_CMPC_2`

```c
#define RZA2M_DMA_RS_CMPC_2 RZA2M_DMA_RS(0x137U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配 C（GPT channel 2, compare match C）。

<a id="a758fdf3f2b4144d47fd7220a9456dd10"></a>

### `RZA2M_DMA_RS_CMPC_3`

```c
#define RZA2M_DMA_RS_CMPC_3 RZA2M_DMA_RS(0x16BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配 C（GPT channel 3, compare match C）。

<a id="a7fcf9c9696beddfa33af1fd73a43983a"></a>

### `RZA2M_DMA_RS_CMPC_4`

```c
#define RZA2M_DMA_RS_CMPC_4 RZA2M_DMA_RS(0x19FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配 C（GPT channel 4, compare match C）。

<a id="a166de2e44482fd2059f3d1d9fe5c0a21"></a>

### `RZA2M_DMA_RS_CMPC_5`

```c
#define RZA2M_DMA_RS_CMPC_5 RZA2M_DMA_RS(0x1D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配 C（GPT channel 5, compare match C）。

<a id="aa65898905b5e64c3f886d1451d3e1a5a"></a>

### `RZA2M_DMA_RS_CMPC_6`

```c
#define RZA2M_DMA_RS_CMPC_6 RZA2M_DMA_RS(0x207U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配 C（GPT channel 6, compare match C）。

<a id="ad5ae81d3e17d8a207ab21c584e97299b"></a>

### `RZA2M_DMA_RS_CMPC_7`

```c
#define RZA2M_DMA_RS_CMPC_7 RZA2M_DMA_RS(0x23BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配 C（GPT channel 7, compare match C）。

<a id="a58be60629b2b39a2bfa57ce9e37cc076"></a>

### `RZA2M_DMA_RS_CMPD_0`

```c
#define RZA2M_DMA_RS_CMPD_0 RZA2M_DMA_RS(0x0D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配 D（GPT channel 0, compare match D）。

<a id="a655a7efd37cb45e8d9faafcaaac85ae0"></a>

### `RZA2M_DMA_RS_CMPD_1`

```c
#define RZA2M_DMA_RS_CMPD_1 RZA2M_DMA_RS(0x107U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配 D（GPT channel 1, compare match D）。

<a id="a174500c43e9cdafce8a9817933d68e8f"></a>

### `RZA2M_DMA_RS_CMPD_2`

```c
#define RZA2M_DMA_RS_CMPD_2 RZA2M_DMA_RS(0x13BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配 D（GPT channel 2, compare match D）。

<a id="adf8e674c8020932d1224eafc49106c4b"></a>

### `RZA2M_DMA_RS_CMPD_3`

```c
#define RZA2M_DMA_RS_CMPD_3 RZA2M_DMA_RS(0x16FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配 D（GPT channel 3, compare match D）。

<a id="a767c91361a18b5e15a149d8e4972d51a"></a>

### `RZA2M_DMA_RS_CMPD_4`

```c
#define RZA2M_DMA_RS_CMPD_4 RZA2M_DMA_RS(0x1A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配 D（GPT channel 4, compare match D）。

<a id="aa32e5e651d7741e6fbb42f40c0bf64de"></a>

### `RZA2M_DMA_RS_CMPD_5`

```c
#define RZA2M_DMA_RS_CMPD_5 RZA2M_DMA_RS(0x1D7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配 D（GPT channel 5, compare match D）。

<a id="aef67f43795a139ad7b9e92f691417e28"></a>

### `RZA2M_DMA_RS_CMPD_6`

```c
#define RZA2M_DMA_RS_CMPD_6 RZA2M_DMA_RS(0x20BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配 D（GPT channel 6, compare match D）。

<a id="abbca7860c61098afc9f2f6e1bd0e0a2b"></a>

### `RZA2M_DMA_RS_CMPD_7`

```c
#define RZA2M_DMA_RS_CMPD_7 RZA2M_DMA_RS(0x23FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配 D（GPT channel 7, compare match D）。

<a id="a4ce7f0b2e77b9284eeecc50a131f7666"></a>

### `RZA2M_DMA_RS_CMPE_0`

```c
#define RZA2M_DMA_RS_CMPE_0 RZA2M_DMA_RS(0x0E3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配 E（GPT channel 0, compare match E）。

<a id="aae314bf45c7b5bfd44b04f9c8a460eee"></a>

### `RZA2M_DMA_RS_CMPE_1`

```c
#define RZA2M_DMA_RS_CMPE_1 RZA2M_DMA_RS(0x117U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配 E（GPT channel 1, compare match E）。

<a id="a6cf8eac779bb550c3b810a07c5db6315"></a>

### `RZA2M_DMA_RS_CMPE_2`

```c
#define RZA2M_DMA_RS_CMPE_2 RZA2M_DMA_RS(0x14BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配 E（GPT channel 2, compare match E）。

<a id="a8cf1831b2a4487142214f081eb51448f"></a>

### `RZA2M_DMA_RS_CMPE_3`

```c
#define RZA2M_DMA_RS_CMPE_3 RZA2M_DMA_RS(0x17FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配 E（GPT channel 3, compare match E）。

<a id="ab658928a62b08b9bb7a7ab55bf1d77a5"></a>

### `RZA2M_DMA_RS_CMPE_4`

```c
#define RZA2M_DMA_RS_CMPE_4 RZA2M_DMA_RS(0x1B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配 E（GPT channel 4, compare match E）。

<a id="a25f2fbd06abce86ac6e9663cc1df1e32"></a>

### `RZA2M_DMA_RS_CMPE_5`

```c
#define RZA2M_DMA_RS_CMPE_5 RZA2M_DMA_RS(0x1E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配 E（GPT channel 5, compare match E）。

<a id="a32873bb00c33f466c6f93baeccc02fa7"></a>

### `RZA2M_DMA_RS_CMPE_6`

```c
#define RZA2M_DMA_RS_CMPE_6 RZA2M_DMA_RS(0x21BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配 E（GPT channel 6, compare match E）。

<a id="a12f540fa28f0192c11e5204bd88f5217"></a>

### `RZA2M_DMA_RS_CMPE_7`

```c
#define RZA2M_DMA_RS_CMPE_7 RZA2M_DMA_RS(0x24FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配 E（GPT channel 7, compare match E）。

<a id="ae3cb688e4edbfd4f40b76a161c8bfa38"></a>

### `RZA2M_DMA_RS_CMPF_0`

```c
#define RZA2M_DMA_RS_CMPF_0 RZA2M_DMA_RS(0x0E7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 比较匹配 F（GPT channel 0, compare match F）。

<a id="ac8e8117447f3d4631d3b88946564932c"></a>

### `RZA2M_DMA_RS_CMPF_1`

```c
#define RZA2M_DMA_RS_CMPF_1 RZA2M_DMA_RS(0x11BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 比较匹配 F（GPT channel 1, compare match F）。

<a id="a96f6e7b2d20f4700d96e3e3d882a5a02"></a>

### `RZA2M_DMA_RS_CMPF_2`

```c
#define RZA2M_DMA_RS_CMPF_2 RZA2M_DMA_RS(0x14FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 比较匹配 F（GPT channel 2, compare match F）。

<a id="a185a72b0562aa1455e6ead1ee85cb717"></a>

### `RZA2M_DMA_RS_CMPF_3`

```c
#define RZA2M_DMA_RS_CMPF_3 RZA2M_DMA_RS(0x183U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 比较匹配 F（GPT channel 3, compare match F）。

<a id="a03fdeb8ee3ecee0cc546da79891966ca"></a>

### `RZA2M_DMA_RS_CMPF_4`

```c
#define RZA2M_DMA_RS_CMPF_4 RZA2M_DMA_RS(0x1B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 比较匹配 F（GPT channel 4, compare match F）。

<a id="ae2613a5c3d68bcd7beee23930386ed93"></a>

### `RZA2M_DMA_RS_CMPF_5`

```c
#define RZA2M_DMA_RS_CMPF_5 RZA2M_DMA_RS(0x1EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 比较匹配 F（GPT channel 5, compare match F）。

<a id="a0f6943f30cf0c1a615f5194b8e9c10ad"></a>

### `RZA2M_DMA_RS_CMPF_6`

```c
#define RZA2M_DMA_RS_CMPF_6 RZA2M_DMA_RS(0x21FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 比较匹配 F（GPT channel 6, compare match F）。

<a id="abc38d3179ddaccc328b5ecebe379c4ae"></a>

### `RZA2M_DMA_RS_CMPF_7`

```c
#define RZA2M_DMA_RS_CMPF_7 RZA2M_DMA_RS(0x253U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 比较匹配 F（GPT channel 7, compare match F）。

<a id="a3e456126b008f6ca2e49aa300ed3b8dd"></a>

### `RZA2M_DMA_RS_COM_DMA0`

```c
#define RZA2M_DMA_RS_COM_DMA0 RZA2M_DMA_RS(0x2CFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 公共 FIFO DMA 通道 0（CAN, common FIFO DMA channel 0）。

<a id="ab620ddb2e02d5f3a9bd55d8b306e759a"></a>

### `RZA2M_DMA_RS_COM_DMA1`

```c
#define RZA2M_DMA_RS_COM_DMA1 RZA2M_DMA_RS(0x2D3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 公共 FIFO DMA 通道 1（CAN, common FIFO DMA channel 1）。

<a id="a9ee90583e90208d851c4fca6f46b0101"></a>

### `RZA2M_DMA_RS_DREQ0`

```c
#define RZA2M_DMA_RS_DREQ0
```

展开值（Value）：

```c
RZA2M_DMA_RS(RZA2M_DMA_DMARS_EXT_DREQ0, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_NONE,         \
             RZA2M_DMA_F_REQD_AUTO)
```

外部 DMA 请求（External DMA Request）。

<a id="a424d5349b245f3b4b51c55b58a83cd73"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_RX_0`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_0 RZA2M_DMA_RS(0x272U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SSIF 通道 0, DMA 接收（SSIF channel 0, DMA receive）。

<a id="aca770562cba12f664d689d578ac8e061"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_RX_1`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_1 RZA2M_DMA_RS(0x276U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SSIF 通道 1, DMA 接收（SSIF channel 1, DMA receive）。

<a id="a462d83c5f1c67b839279eabb4948eed3"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_RX_2`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_2 RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SSIF 通道 2, DMA 接收（SSIF channel 2, DMA receive）。

<a id="a3040329c3dd6cd6cd7c763308542324a"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_RX_3`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_RX_3 RZA2M_DMA_RS(0x27EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SSIF 通道 3, DMA 接收（SSIF channel 3, DMA receive）。

<a id="a615bba9636d6b50b071467330db990db"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_TX_0`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_0 RZA2M_DMA_RS(0x271U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SSIF 通道 0, DMA 发送（SSIF channel 0, DMA transmit）。

<a id="a5f9cb34b8bed3618ec82dc743d6cb66d"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_TX_1`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_1 RZA2M_DMA_RS(0x275U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SSIF 通道 1, DMA 发送（SSIF channel 1, DMA transmit）。

<a id="a4057badb9ab4c26ae07a44ff8174d6d3"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_TX_2`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_2 RZA2M_DMA_RS(0x27BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SSIF 通道 2, DMA 发送（SSIF channel 2, DMA transmit）。

<a id="a9caff07d4ded76f507e4290f355e1927"></a>

### `RZA2M_DMA_RS_INT_SSIF_DMA_TX_3`

```c
#define RZA2M_DMA_RS_INT_SSIF_DMA_TX_3 RZA2M_DMA_RS(0x27DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SSIF 通道 3, DMA 发送（SSIF channel 3, DMA transmit）。

<a id="a512e50009a95d69d84f258691185396a"></a>

### `RZA2M_DMA_RS_INTRIIC_RI0`

```c
#define RZA2M_DMA_RS_INTRIIC_RI0 RZA2M_DMA_RS(0x28AU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RIIC 通道 0, 接收中断（RIIC channel 0, receive interrupt）。

<a id="a3ccf8181a26704505026cd6ca6e78776"></a>

### `RZA2M_DMA_RS_INTRIIC_RI1`

```c
#define RZA2M_DMA_RS_INTRIIC_RI1 RZA2M_DMA_RS(0x28EU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RIIC 通道 1, 接收中断（RIIC channel 1, receive interrupt）。

<a id="a1bd7dc91baca8523305a9aa7593413e9"></a>

### `RZA2M_DMA_RS_INTRIIC_RI2`

```c
#define RZA2M_DMA_RS_INTRIIC_RI2 RZA2M_DMA_RS(0x292U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RIIC 通道 2, 接收中断（RIIC channel 2, receive interrupt）。

<a id="a0bf3255b1b88d156ecbea326c9e6578c"></a>

### `RZA2M_DMA_RS_INTRIIC_RI3`

```c
#define RZA2M_DMA_RS_INTRIIC_RI3 RZA2M_DMA_RS(0x296U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RIIC 通道 3, 接收中断（RIIC channel 3, receive interrupt）。

<a id="a748fd050ce97162bc6bf8b55dfff6202"></a>

### `RZA2M_DMA_RS_INTRIIC_TI0`

```c
#define RZA2M_DMA_RS_INTRIIC_TI0 RZA2M_DMA_RS(0x289U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RIIC 通道 0, 发送中断（RIIC channel 0, transmit interrupt）。

<a id="aa8cd867c1c9b8a8c8ff7a0e933083979"></a>

### `RZA2M_DMA_RS_INTRIIC_TI1`

```c
#define RZA2M_DMA_RS_INTRIIC_TI1 RZA2M_DMA_RS(0x28DU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RIIC 通道 1, 发送中断（RIIC channel 1, transmit interrupt）。

<a id="a70576d59a7cd36f8866efc457bc9846b"></a>

### `RZA2M_DMA_RS_INTRIIC_TI2`

```c
#define RZA2M_DMA_RS_INTRIIC_TI2 RZA2M_DMA_RS(0x291U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RIIC 通道 2, 发送中断（RIIC channel 2, transmit interrupt）。

<a id="a5f212e541dd402b608ced9b9091c5da4"></a>

### `RZA2M_DMA_RS_INTRIIC_TI3`

```c
#define RZA2M_DMA_RS_INTRIIC_TI3 RZA2M_DMA_RS(0x295U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RIIC 通道 3, 发送中断（RIIC channel 3, transmit interrupt）。

<a id="a5eb36dd01681895e8e93127f37226aee"></a>

### `RZA2M_DMA_RS_IPLS`

```c
#define RZA2M_DMA_RS_IPLS RZA2M_DMA_RS(0x2EBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

以太网 MAC 控制器（Ethernet MAC Controller）的 IPLS。

<a id="ac521f38a9178670684798851196939bc"></a>

### `RZA2M_DMA_RS_OSTM0TINT`

```c
#define RZA2M_DMA_RS_OSTM0TINT RZA2M_DMA_RS(0x023U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

OSTM0 定时器中断（OSTM0 timer interrupt）。

<a id="af861a0ce876f339b3e7f59ca3c83ec10"></a>

### `RZA2M_DMA_RS_OSTM1TINT`

```c
#define RZA2M_DMA_RS_OSTM1TINT RZA2M_DMA_RS(0x027U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

OSTM1 定时器中断（OSTM1 timer interrupt）。

<a id="ab914a5b323ae7fa91f6b8490cc7417f8"></a>

### `RZA2M_DMA_RS_OSTM2TINT`

```c
#define RZA2M_DMA_RS_OSTM2TINT RZA2M_DMA_RS(0x02BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_AUTO)
```

OSTM2 定时器中断（OSTM2 timer interrupt）。

<a id="a6ec09447832d6626096d2434782e6ab1"></a>

### `RZA2M_DMA_RS_OVF_0`

```c
#define RZA2M_DMA_RS_OVF_0 RZA2M_DMA_RS(0x0F3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 上溢（GPT channel 0, overflow）。

<a id="a2fb455da7133660be6ff171638cb9085"></a>

### `RZA2M_DMA_RS_OVF_1`

```c
#define RZA2M_DMA_RS_OVF_1 RZA2M_DMA_RS(0x127U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 上溢（GPT channel 1, overflow）。

<a id="acc1a0c994391fbee33100ff89755c740"></a>

### `RZA2M_DMA_RS_OVF_2`

```c
#define RZA2M_DMA_RS_OVF_2 RZA2M_DMA_RS(0x15BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 上溢（GPT channel 2, overflow）。

<a id="a9e4755f83c4a8aaec0f063f83676b666"></a>

### `RZA2M_DMA_RS_OVF_3`

```c
#define RZA2M_DMA_RS_OVF_3 RZA2M_DMA_RS(0x18FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 上溢（GPT channel 3, overflow）。

<a id="a7e89308b7bb3999dc92c2b1debe6f264"></a>

### `RZA2M_DMA_RS_OVF_4`

```c
#define RZA2M_DMA_RS_OVF_4 RZA2M_DMA_RS(0x1C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 上溢（GPT channel 4, overflow）。

<a id="a3a77cedf37f532e3fb254106f9a48c2f"></a>

### `RZA2M_DMA_RS_OVF_5`

```c
#define RZA2M_DMA_RS_OVF_5 RZA2M_DMA_RS(0x1F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 上溢（GPT channel 5, overflow）。

<a id="aed75e450cf1ca73e617e40e1d77a7f2e"></a>

### `RZA2M_DMA_RS_OVF_6`

```c
#define RZA2M_DMA_RS_OVF_6 RZA2M_DMA_RS(0x22BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 上溢（GPT channel 6, overflow）。

<a id="a3bdff659a036dd2153902e8ba5d16add"></a>

### `RZA2M_DMA_RS_OVF_7`

```c
#define RZA2M_DMA_RS_OVF_7 RZA2M_DMA_RS(0x25FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 上溢（GPT channel 7, overflow）。

<a id="a95e9a78cd37654fb493171c5d2445789"></a>

### `RZA2M_DMA_RS_RXF_DMA0`

```c
#define RZA2M_DMA_RS_RXF_DMA0 RZA2M_DMA_RS(0x2AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 0（CAN, receive FIFO DMA channel 0）。

<a id="a8f473b6e68d0ecbb27cc85450240fcbe"></a>

### `RZA2M_DMA_RS_RXF_DMA1`

```c
#define RZA2M_DMA_RS_RXF_DMA1 RZA2M_DMA_RS(0x2B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 1（CAN, receive FIFO DMA channel 1）。

<a id="ab0c51920a47fe8379e780601df5919b3"></a>

### `RZA2M_DMA_RS_RXF_DMA2`

```c
#define RZA2M_DMA_RS_RXF_DMA2 RZA2M_DMA_RS(0x2B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 2（CAN, receive FIFO DMA channel 2）。

<a id="a1d50c93288a532ef168f1b86ec8692f0"></a>

### `RZA2M_DMA_RS_RXF_DMA3`

```c
#define RZA2M_DMA_RS_RXF_DMA3 RZA2M_DMA_RS(0x2BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 3（CAN, receive FIFO DMA channel 3）。

<a id="ab7f1184156a68ec8d0da0b2912979f32"></a>

### `RZA2M_DMA_RS_RXF_DMA4`

```c
#define RZA2M_DMA_RS_RXF_DMA4 RZA2M_DMA_RS(0x2BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 4（CAN, receive FIFO DMA channel 4）。

<a id="a49d3857e13e2c80c5890edde428edb6b"></a>

### `RZA2M_DMA_RS_RXF_DMA5`

```c
#define RZA2M_DMA_RS_RXF_DMA5 RZA2M_DMA_RS(0x2C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 5（CAN, receive FIFO DMA channel 5）。

<a id="a8b051cd40a1fd1512de65db48ea7a49e"></a>

### `RZA2M_DMA_RS_RXF_DMA6`

```c
#define RZA2M_DMA_RS_RXF_DMA6 RZA2M_DMA_RS(0x2C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 6（CAN, receive FIFO DMA channel 6）。

<a id="a1ab1c31d3c7e4cf6bca4412ac17aa5a4"></a>

### `RZA2M_DMA_RS_RXF_DMA7`

```c
#define RZA2M_DMA_RS_RXF_DMA7 RZA2M_DMA_RS(0x2CBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

CAN, 接收 FIFO DMA 通道 7（CAN, receive FIFO DMA channel 7）。

<a id="a7dd81d3f4b4a338c336efb0fb5748abc"></a>

### `RZA2M_DMA_RS_RXI0`

```c
#define RZA2M_DMA_RS_RXI0 RZA2M_DMA_RS(0x29AU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

SCIF 通道 0, 接收中断（SCIF channel 0, receive interrupt）。

<a id="a08a2bf046ae7193f0cf82db34038ca8d"></a>

### `RZA2M_DMA_RS_RXI1`

```c
#define RZA2M_DMA_RS_RXI1 RZA2M_DMA_RS(0x29EU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

SCIF 通道 1, 接收中断（SCIF channel 1, receive interrupt）。

<a id="a93c5b3e0d31c22fbe710e5e42ca73ed5"></a>

### `RZA2M_DMA_RS_RXI2`

```c
#define RZA2M_DMA_RS_RXI2 RZA2M_DMA_RS(0x2A2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

SCIF 通道 2, 接收中断（SCIF channel 2, receive interrupt）。

<a id="a73afb81051a66a6de0dc1c4665d09304"></a>

### `RZA2M_DMA_RS_RXI3`

```c
#define RZA2M_DMA_RS_RXI3 RZA2M_DMA_RS(0x2A6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

SCIF 通道 3, 接收中断（SCIF channel 3, receive interrupt）。

<a id="ab417d142ddba4bad46a692153202d06b"></a>

### `RZA2M_DMA_RS_RXI4`

```c
#define RZA2M_DMA_RS_RXI4 RZA2M_DMA_RS(0x2AAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_SRC)
```

SCIF 通道 4, 接收中断（SCIF channel 4, receive interrupt）。

<a id="adfffeffc377bfb7236ce602a064f603d"></a>

### `RZA2M_DMA_RS_S12ADI_0`

```c
#define RZA2M_DMA_RS_S12ADI_0 RZA2M_DMA_RS(0x267U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

ADC 扫描结束中断（ADC scan end interrupt）。

<a id="ab30dccf89ae684329c9d39bfcb8838f6"></a>

### `RZA2M_DMA_RS_S12GBADI_0`

```c
#define RZA2M_DMA_RS_S12GBADI_0 RZA2M_DMA_RS(0x26BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

ADC 组 B 扫描结束中断（ADC group B scan end interrupt）。

<a id="abbf1a7432706059fb1786159810e6c40"></a>

### `RZA2M_DMA_RS_S12GCADI_0`

```c
#define RZA2M_DMA_RS_S12GCADI_0 RZA2M_DMA_RS(0x26FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_SRC)
```

ADC 组 C 扫描结束中断（ADC group C scan end interrupt）。

<a id="a7ecda7d5cccfd90fcda09a350f420e3a"></a>

### `RZA2M_DMA_RS_SCI_RXI0`

```c
#define RZA2M_DMA_RS_SCI_RXI0 RZA2M_DMA_RS(0x2E2U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SCI 通道 0, 接收中断（SCI channel 0, receive interrupt）。

<a id="a83a3cc69c4b548c0cae87c68495dabe8"></a>

### `RZA2M_DMA_RS_SCI_RXI1`

```c
#define RZA2M_DMA_RS_SCI_RXI1 RZA2M_DMA_RS(0x2E6U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SCI 通道 1, 接收中断（SCI channel 1, receive interrupt）。

<a id="aa8e3ecdcdcfbf107eae78dc913736ac3"></a>

### `RZA2M_DMA_RS_SCI_TXI0`

```c
#define RZA2M_DMA_RS_SCI_TXI0 RZA2M_DMA_RS(0x2E1U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SCI 通道 0, 发送中断（SCI channel 0, transmit interrupt）。

<a id="a216e8cbeecc148f27638c1edba42f0fd"></a>

### `RZA2M_DMA_RS_SCI_TXI1`

```c
#define RZA2M_DMA_RS_SCI_TXI1 RZA2M_DMA_RS(0x2E5U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SCI 通道 1, 发送中断（SCI channel 1, transmit interrupt）。

<a id="ad063e32fe7421099580d982031680efb"></a>

### `RZA2M_DMA_RS_SPDIFRXI`

```c
#define RZA2M_DMA_RS_SPDIFRXI RZA2M_DMA_RS(0x287U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

SPDIF 接收中断（SPDIF receive interrupt）。

<a id="a6354bbdb9965199e9ab9b76e00182fc4"></a>

### `RZA2M_DMA_RS_SPDIFTXI`

```c
#define RZA2M_DMA_RS_SPDIFTXI RZA2M_DMA_RS(0x283U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

SPDIF 发送中断（SPDIF transmit interrupt）。

<a id="a72a053f7bd6e62562148a40b3b9795de"></a>

### `RZA2M_DMA_RS_SPRI0`

```c
#define RZA2M_DMA_RS_SPRI0 RZA2M_DMA_RS(0x2D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RSPI 通道 0, 接收中断（RSPI channel 0, receive interrupt）。

<a id="adb9fc9139570ff8cd6f654574abaf7b1"></a>

### `RZA2M_DMA_RS_SPRI1`

```c
#define RZA2M_DMA_RS_SPRI1 RZA2M_DMA_RS(0x2DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RSPI 通道 1, 接收中断（RSPI channel 1, receive interrupt）。

<a id="a33412fcf2247e86f10ab8cb2536c9b3e"></a>

### `RZA2M_DMA_RS_SPRI2`

```c
#define RZA2M_DMA_RS_SPRI2 RZA2M_DMA_RS(0x2DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

RSPI 通道 2, 接收中断（RSPI channel 2, receive interrupt）。

<a id="a6231a82cb548bea0d25d6208c3f251e5"></a>

### `RZA2M_DMA_RS_SPTI0`

```c
#define RZA2M_DMA_RS_SPTI0 RZA2M_DMA_RS(0x2D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RSPI 通道 0, 发送中断（RSPI channel 0, transmit interrupt）。

<a id="a5668f986198059bc6ea00fff3f3a5bad"></a>

### `RZA2M_DMA_RS_SPTI1`

```c
#define RZA2M_DMA_RS_SPTI1 RZA2M_DMA_RS(0x2D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RSPI 通道 1, 发送中断（RSPI channel 1, transmit interrupt）。

<a id="a9149fb1b1f9731366556b162dbf493f9"></a>

### `RZA2M_DMA_RS_SPTI2`

```c
#define RZA2M_DMA_RS_SPTI2 RZA2M_DMA_RS(0x2DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

RSPI 通道 2, 发送中断（RSPI channel 2, transmit interrupt）。

<a id="a1065735c9aa60cbc99903810c67cbc3b"></a>

### `RZA2M_DMA_RS_TCIV_4`

```c
#define RZA2M_DMA_RS_TCIV_4 RZA2M_DMA_RS(0x083U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 4, TCNT 的上溢／下溢中断（MTU channel 4, overflow/underflow interrupt of TCNT）。

<a id="a00b1a6cfd73d0194435432ce1fda422f"></a>

### `RZA2M_DMA_RS_TCIV_7`

```c
#define RZA2M_DMA_RS_TCIV_7 RZA2M_DMA_RS(0x0B3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 7, TCNT 的上溢／下溢中断（MTU channel 7, overflow/underflow interrupt of TCNT）。

<a id="a369d818ab82c5b4b0c6502967f6757e4"></a>

### `RZA2M_DMA_RS_TGIA_0`

```c
#define RZA2M_DMA_RS_TGIA_0 RZA2M_DMA_RS(0x043U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 0, 比较匹配／输入捕获 A（MTU channel 0, compare match/input capture A）。

<a id="aab6298b2f1e34f09f4b6044ac9a6f233"></a>

### `RZA2M_DMA_RS_TGIA_1`

```c
#define RZA2M_DMA_RS_TGIA_1 RZA2M_DMA_RS(0x053U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 1, 比较匹配／输入捕获 A（MTU channel 1, compare match/input capture A）。

<a id="a7f2fb65fdf92760fe85b8bf2193a82fc"></a>

### `RZA2M_DMA_RS_TGIA_2`

```c
#define RZA2M_DMA_RS_TGIA_2 RZA2M_DMA_RS(0x05BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 2, 比较匹配／输入捕获 A（MTU channel 2, compare match/input capture A）。

<a id="a446a00d865413f135c105003db9dbf98"></a>

### `RZA2M_DMA_RS_TGIA_3`

```c
#define RZA2M_DMA_RS_TGIA_3 RZA2M_DMA_RS(0x063U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 3, 比较匹配／输入捕获 A（MTU channel 3, compare match/input capture A）。

<a id="a5f6841e43bd15fdfc0816301871fdbda"></a>

### `RZA2M_DMA_RS_TGIA_4`

```c
#define RZA2M_DMA_RS_TGIA_4 RZA2M_DMA_RS(0x073U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 4, 比较匹配／输入捕获 A（MTU channel 4, compare match/input capture A）。

<a id="a1197065cbf95f829932cc150ce27bd91"></a>

### `RZA2M_DMA_RS_TGIA_6`

```c
#define RZA2M_DMA_RS_TGIA_6 RZA2M_DMA_RS(0x093U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 6, 比较匹配／输入捕获 A（MTU channel 6, compare match/input capture A）。

<a id="a123b96db8690952648c20ff32acc49de"></a>

### `RZA2M_DMA_RS_TGIA_7`

```c
#define RZA2M_DMA_RS_TGIA_7 RZA2M_DMA_RS(0x0A3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 7, 比较匹配／输入捕获 A（MTU channel 7, compare match/input capture A）。

<a id="aaa1f3a728a201692557773551a3a9cdf"></a>

### `RZA2M_DMA_RS_TGIA_8`

```c
#define RZA2M_DMA_RS_TGIA_8 RZA2M_DMA_RS(0x0B7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 8, 比较匹配／输入捕获 A（MTU channel 8, compare match/input capture A）。

<a id="ade2b671145723b401570432cc2c8cd54"></a>

### `RZA2M_DMA_RS_TGIB_0`

```c
#define RZA2M_DMA_RS_TGIB_0 RZA2M_DMA_RS(0x047U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 0, 比较匹配／输入捕获 B（MTU channel 0, compare match/input capture B）。

<a id="a23d862e8c0fce9dbfba93285ea32589d"></a>

### `RZA2M_DMA_RS_TGIB_1`

```c
#define RZA2M_DMA_RS_TGIB_1 RZA2M_DMA_RS(0x057U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 1, 比较匹配／输入捕获 B（MTU channel 1, compare match/input capture B）。

<a id="abc0a77e490cd9a3787a1bdafa9e5cf31"></a>

### `RZA2M_DMA_RS_TGIB_2`

```c
#define RZA2M_DMA_RS_TGIB_2 RZA2M_DMA_RS(0x05FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 2, 比较匹配／输入捕获 B（MTU channel 2, compare match/input capture B）。

<a id="a2d49f329a8469a0f8730dfff9574d955"></a>

### `RZA2M_DMA_RS_TGIB_3`

```c
#define RZA2M_DMA_RS_TGIB_3 RZA2M_DMA_RS(0x067U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 3, 比较匹配／输入捕获 B（MTU channel 3, compare match/input capture B）。

<a id="aa0b0855807d72c73cee5b377cd261575"></a>

### `RZA2M_DMA_RS_TGIB_4`

```c
#define RZA2M_DMA_RS_TGIB_4 RZA2M_DMA_RS(0x077U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 4, 比较匹配／输入捕获 B（MTU channel 4, compare match/input capture B）。

<a id="af124980bc5bb74c5ad625c2443392b6b"></a>

### `RZA2M_DMA_RS_TGIB_6`

```c
#define RZA2M_DMA_RS_TGIB_6 RZA2M_DMA_RS(0x097U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 6, 比较匹配／输入捕获 B（MTU channel 6, compare match/input capture B）。

<a id="a2fd591c9dfd12921cad0097d84034a67"></a>

### `RZA2M_DMA_RS_TGIB_7`

```c
#define RZA2M_DMA_RS_TGIB_7 RZA2M_DMA_RS(0x0A7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 7, 比较匹配／输入捕获 B（MTU channel 7, compare match/input capture B）。

<a id="a24a3472223b1f6dba3f79b4bb30f174e"></a>

### `RZA2M_DMA_RS_TGIB_8`

```c
#define RZA2M_DMA_RS_TGIB_8 RZA2M_DMA_RS(0x0BBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 8, 比较匹配／输入捕获 B（MTU channel 8, compare match/input capture B）。

<a id="a472581fa62f8269f60e1b0db4d8b8bda"></a>

### `RZA2M_DMA_RS_TGIC_0`

```c
#define RZA2M_DMA_RS_TGIC_0 RZA2M_DMA_RS(0x04BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 0, 比较匹配／输入捕获 C（MTU channel 0, compare match/input capture C）。

<a id="af19bba4cecb049d8e5fcd2eab79119d5"></a>

### `RZA2M_DMA_RS_TGIC_3`

```c
#define RZA2M_DMA_RS_TGIC_3 RZA2M_DMA_RS(0x06BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 3, 比较匹配／输入捕获 C（MTU channel 3, compare match/input capture C）。

<a id="a7b84b6850efbc5c8070fbc3802e43cf3"></a>

### `RZA2M_DMA_RS_TGIC_4`

```c
#define RZA2M_DMA_RS_TGIC_4 RZA2M_DMA_RS(0x07BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 4, 比较匹配／输入捕获 C（MTU channel 4, compare match/input capture C）。

<a id="a992961b8a4aceca82925e7a0474c0225"></a>

### `RZA2M_DMA_RS_TGIC_6`

```c
#define RZA2M_DMA_RS_TGIC_6 RZA2M_DMA_RS(0x09BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 6, 比较匹配／输入捕获 C（MTU channel 6, compare match/input capture C）。

<a id="a35c6aa421d48382b1f7b0c1496e0cd3b"></a>

### `RZA2M_DMA_RS_TGIC_7`

```c
#define RZA2M_DMA_RS_TGIC_7 RZA2M_DMA_RS(0x0ABU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 7, 比较匹配／输入捕获 C（MTU channel 7, compare match/input capture C）。

<a id="af7a6dfcf39dbaa9249f887c8e82acc00"></a>

### `RZA2M_DMA_RS_TGIC_8`

```c
#define RZA2M_DMA_RS_TGIC_8 RZA2M_DMA_RS(0x0BFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 8, 比较匹配／输入捕获 C（MTU channel 8, compare match/input capture C）。

<a id="ad2c236d2aaae652b3bf52a025241107d"></a>

### `RZA2M_DMA_RS_TGID_0`

```c
#define RZA2M_DMA_RS_TGID_0 RZA2M_DMA_RS(0x04FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 0, 比较匹配／输入捕获 D（MTU channel 0, compare match/input capture D）。

<a id="a704aff4a1226e18e06023fded37142d3"></a>

### `RZA2M_DMA_RS_TGID_3`

```c
#define RZA2M_DMA_RS_TGID_3 RZA2M_DMA_RS(0x06FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 3, 比较匹配／输入捕获 D（MTU channel 3, compare match/input capture D）。

<a id="ac3df895b3451bf2925606dec8ba54e2b"></a>

### `RZA2M_DMA_RS_TGID_4`

```c
#define RZA2M_DMA_RS_TGID_4 RZA2M_DMA_RS(0x07FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 4, 比较匹配／输入捕获 D（MTU channel 4, compare match/input capture D）。

<a id="ab365586d7aa2fb4e8a761d1b102c528b"></a>

### `RZA2M_DMA_RS_TGID_6`

```c
#define RZA2M_DMA_RS_TGID_6 RZA2M_DMA_RS(0x09FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 6, 比较匹配／输入捕获 D（MTU channel 6, compare match/input capture D）。

<a id="ac681f555edcefcda45c5fa2e708e6173"></a>

### `RZA2M_DMA_RS_TGID_7`

```c
#define RZA2M_DMA_RS_TGID_7 RZA2M_DMA_RS(0x0AFU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 7, 比较匹配／输入捕获 D（MTU channel 7, compare match/input capture D）。

<a id="a7a44df400aa8769568192be0d9fa6f18"></a>

### `RZA2M_DMA_RS_TGID_8`

```c
#define RZA2M_DMA_RS_TGID_8 RZA2M_DMA_RS(0x0C3U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 8, 比较匹配／输入捕获 D（MTU channel 8, compare match/input capture D）。

<a id="a16e54abe66cd04ff09d2fb318899e7b7"></a>

### `RZA2M_DMA_RS_TGIU_5`

```c
#define RZA2M_DMA_RS_TGIU_5 RZA2M_DMA_RS(0x087U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 5, 比较匹配／输入捕获 U（MTU channel 5, compare match/input capture U）。

<a id="aac3735c168591e161681bcdf96f3f150"></a>

### `RZA2M_DMA_RS_TGIV_5`

```c
#define RZA2M_DMA_RS_TGIV_5 RZA2M_DMA_RS(0x08BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 5, 比较匹配／输入捕获 V（MTU channel 5, compare match/input capture V）。

<a id="afdebfb68206593eba15765cbf7e96405"></a>

### `RZA2M_DMA_RS_TGIW_5`

```c
#define RZA2M_DMA_RS_TGIW_5 RZA2M_DMA_RS(0x08FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

MTU 通道 5, 比较匹配／输入捕获 W（MTU channel 5, compare match/input capture W）。

<a id="afb75f0c8cd0e4a150ab69d202f3891b0"></a>

### `RZA2M_DMA_RS_TILE_0_PAEI`

```c
#define RZA2M_DMA_RS_TILE_0_PAEI RZA2M_DMA_RS(0x3CDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 0 可编程近空（DRP Tile 0 Programmable Almost Empty）。

<a id="a5aeb8ebfcd18f53cc39ebbe8832c324f"></a>

### `RZA2M_DMA_RS_TILE_0_PAFI`

```c
#define RZA2M_DMA_RS_TILE_0_PAFI RZA2M_DMA_RS(0x3CEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 0 可编程近满（DRP Tile 0 Programmable Almost Full）。

<a id="aae0118afd293747ebdce414548a5b6a7"></a>

### `RZA2M_DMA_RS_TILE_1_PAEI`

```c
#define RZA2M_DMA_RS_TILE_1_PAEI RZA2M_DMA_RS(0x3D1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 1 可编程近空（DRP Tile 1 Programmable Almost Empty）。

<a id="ab3dbfc391e66332a5921ec2c1fdca39f"></a>

### `RZA2M_DMA_RS_TILE_1_PAFI`

```c
#define RZA2M_DMA_RS_TILE_1_PAFI RZA2M_DMA_RS(0x3D2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 1 可编程近满（DRP Tile 1 Programmable Almost Full）。

<a id="acdeb33533030248bb7fcd8afe1c72f09"></a>

### `RZA2M_DMA_RS_TILE_2_PAEI`

```c
#define RZA2M_DMA_RS_TILE_2_PAEI RZA2M_DMA_RS(0x3D5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 2 可编程近空（DRP Tile 2 Programmable Almost Empty）。

<a id="ae4003c09956059f2afa1086f84e162eb"></a>

### `RZA2M_DMA_RS_TILE_2_PAFI`

```c
#define RZA2M_DMA_RS_TILE_2_PAFI RZA2M_DMA_RS(0x3D6U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 2 可编程近满（DRP Tile 2 Programmable Almost Full）。

<a id="a4b4da99cb156f9c2521373b10b9d0318"></a>

### `RZA2M_DMA_RS_TILE_3_PAEI`

```c
#define RZA2M_DMA_RS_TILE_3_PAEI RZA2M_DMA_RS(0x3D9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 3 可编程近空（DRP Tile 3 Programmable Almost Empty）。

<a id="af2da1374c122258426a74758bfa4866c"></a>

### `RZA2M_DMA_RS_TILE_3_PAFI`

```c
#define RZA2M_DMA_RS_TILE_3_PAFI RZA2M_DMA_RS(0x3DAU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 3 可编程近满（DRP Tile 3 Programmable Almost Full）。

<a id="ace299eb47bb0126f7d3c1f56cb6daea2"></a>

### `RZA2M_DMA_RS_TILE_4_PAEI`

```c
#define RZA2M_DMA_RS_TILE_4_PAEI RZA2M_DMA_RS(0x3DDU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 4 可编程近空（DRP Tile 4 Programmable Almost Empty）。

<a id="a1e8d4ec416151d4dd59e1e5fb80900c5"></a>

### `RZA2M_DMA_RS_TILE_4_PAFI`

```c
#define RZA2M_DMA_RS_TILE_4_PAFI RZA2M_DMA_RS(0x3DEU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 4 可编程近满（DRP Tile 4 Programmable Almost Full）。

<a id="aa2c2874df19d68f2a40869d8de83ba68"></a>

### `RZA2M_DMA_RS_TILE_5_PAEI`

```c
#define RZA2M_DMA_RS_TILE_5_PAEI RZA2M_DMA_RS(0x3E1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_DST)
```

DRP 单元 5 可编程近空（DRP Tile 5 Programmable Almost Empty）。

<a id="acac0bb9cf60d3f0d96925db19b433488"></a>

### `RZA2M_DMA_RS_TILE_5_PAFI`

```c
#define RZA2M_DMA_RS_TILE_5_PAFI RZA2M_DMA_RS(0x3E2U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_BUS, RZA2M_DMA_F_REQD_SRC)
```

DRP 单元 5 可编程近满（DRP Tile 5 Programmable Almost Full）。

<a id="a496490e9393b330865cd4553a35d76bf"></a>

### `RZA2M_DMA_RS_TXI0`

```c
#define RZA2M_DMA_RS_TXI0 RZA2M_DMA_RS(0x299U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

SCIF 通道 0, 发送中断（SCIF channel 0, transmit interrupt）。

<a id="a7516731e183b49a7790d0e61b0768e23"></a>

### `RZA2M_DMA_RS_TXI1`

```c
#define RZA2M_DMA_RS_TXI1 RZA2M_DMA_RS(0x29DU, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

SCIF 通道 1, 发送中断（SCIF channel 1, transmit interrupt）。

<a id="a5dd127eca1fd1c1964bd2d7f75438f2c"></a>

### `RZA2M_DMA_RS_TXI2`

```c
#define RZA2M_DMA_RS_TXI2 RZA2M_DMA_RS(0x2A1U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

SCIF 通道 2, 发送中断（SCIF channel 2, transmit interrupt）。

<a id="a3f13c36be6185f9f371411e3c516a38c"></a>

### `RZA2M_DMA_RS_TXI3`

```c
#define RZA2M_DMA_RS_TXI3 RZA2M_DMA_RS(0x2A5U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

SCIF 通道 3, 发送中断（SCIF channel 3, transmit interrupt）。

<a id="a8762f45b557c41d228857a7deede8030"></a>

### `RZA2M_DMA_RS_TXI4`

```c
#define RZA2M_DMA_RS_TXI4 RZA2M_DMA_RS(0x2A9U, RZA2M_DMA_F_LVL_LEVEL, RZA2M_DMA_F_AM_NO_ACK, RZA2M_DMA_F_REQD_DST)
```

SCIF 通道 4, 发送中断（SCIF channel 4, transmit interrupt）。

<a id="a51b8da6256c92ab9bad709bf11ed4707"></a>

### `RZA2M_DMA_RS_UNF_0`

```c
#define RZA2M_DMA_RS_UNF_0 RZA2M_DMA_RS(0x0F7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 0, 下溢（GPT channel 0, underflow）。

<a id="a461c8cacd8900dfddeb0f33569acd39b"></a>

### `RZA2M_DMA_RS_UNF_1`

```c
#define RZA2M_DMA_RS_UNF_1 RZA2M_DMA_RS(0x12BU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 1, 下溢（GPT channel 1, underflow）。

<a id="a4d6bab832a8c9f8040f19e3b3458ad02"></a>

### `RZA2M_DMA_RS_UNF_2`

```c
#define RZA2M_DMA_RS_UNF_2 RZA2M_DMA_RS(0x15FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 2, 下溢（GPT channel 2, underflow）。

<a id="aa875e7915331b5e49542755010366aeb"></a>

### `RZA2M_DMA_RS_UNF_3`

```c
#define RZA2M_DMA_RS_UNF_3 RZA2M_DMA_RS(0x193U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 3, 下溢（GPT channel 3, underflow）。

<a id="ad4d7c222146f01f5f12c5dc4c68c7138"></a>

### `RZA2M_DMA_RS_UNF_4`

```c
#define RZA2M_DMA_RS_UNF_4 RZA2M_DMA_RS(0x1C7U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 4, 下溢（GPT channel 4, underflow）。

<a id="ae9662e33f5bd00f2b1dbea6eda67bacb"></a>

### `RZA2M_DMA_RS_UNF_5`

```c
#define RZA2M_DMA_RS_UNF_5 RZA2M_DMA_RS(0x1FBU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 5, 下溢（GPT channel 5, underflow）。

<a id="ac10ea111ad9060f6eed4976396898e92"></a>

### `RZA2M_DMA_RS_UNF_6`

```c
#define RZA2M_DMA_RS_UNF_6 RZA2M_DMA_RS(0x22FU, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 6, 下溢（GPT channel 6, underflow）。

<a id="ad3fd3d94dd8f4af97717b7da6c27fe04"></a>

### `RZA2M_DMA_RS_UNF_7`

```c
#define RZA2M_DMA_RS_UNF_7 RZA2M_DMA_RS(0x263U, RZA2M_DMA_F_LVL_EDGE, RZA2M_DMA_F_AM_LEVEL, RZA2M_DMA_F_REQD_AUTO)
```

GPT 通道 7, 下溢（GPT channel 7, underflow）。


## 4.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P714_renesas_rza2m_dma.h_源码浏览.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="arenesas__rza2m__dma_8h_html_a391ba1663b69e478fb4c82c35b16e176"></a>
<a id="arenesas__rza2m__dma_8h_html_acb45792a1764debb7f7f4d7841b0cc7e"></a>

---

[上一章](P003_zephyr__net__net_if.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__dt-bindings__pinctrl__rtl8752h-pinctrl.h_文件参考.md)
