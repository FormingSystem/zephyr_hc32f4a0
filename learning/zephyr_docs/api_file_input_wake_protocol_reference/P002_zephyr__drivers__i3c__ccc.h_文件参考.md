---
id: learning.zephyr-docs.api-file-input-wake-protocol-reference.page-2
title: zephyr__drivers__i3c__ccc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_drivers\_\_i3c\_\_ccc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ccc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <stdint.h>
#include <zephyr/device.h>
#include <zephyr/toolchain.h>
#include <zephyr/sys/util.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 2.1\_数据结构（Data Structures）

<a id="r_i3c_5Fccc_5Ftarget_5Fpayload"></a>

```c
struct i3c_ccc_target_payload
```

相关声明：[i3c_ccc_target_payload](../hardware/P418_I3C通用命令目标载荷.md)。

发往单个目标的直接通用命令码（Direct CCC）的载荷结构。

<a id="r_i3c_5Fccc_5Fpayload"></a>

```c
struct i3c_ccc_payload
```

相关声明：[i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)。

一次通用命令码（CCC）事务的载荷结构。

<a id="r_i3c_5Fccc_5Fevents"></a>

```c
struct i3c_ccc_events
```

相关声明：[i3c_ccc_events](../hardware/P411_I3C通用命令事件.md)。

ENEC/DISEC通用命令码（CCC，目标事件命令）的载荷。

<a id="r_i3c_5Fccc_5Fmwl"></a>

```c
struct i3c_ccc_mwl
```

相关声明：[i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)。

SETMWL/GETMWL通用命令码（CCC，设置/获取最大写入长度）的载荷。

<a id="r_i3c_5Fccc_5Fmrl"></a>

```c
struct i3c_ccc_mrl
```

相关声明：[i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)。

SETMRL/GETMRL通用命令码（CCC，设置/获取最大读取长度）的载荷。

<a id="r_i3c_5Fccc_5Fdeftgts_5Factive_5Fcontroller"></a>

```c
struct i3c_ccc_deftgts_active_controller
```

相关声明：[i3c_ccc_deftgts_active_controller](../hardware/P420_I3C目标清单活动控制器.md)。

DEFTGTS通用命令码（CCC）载荷中的活动控制器部分。

<a id="r_i3c_5Fccc_5Fdeftgts_5Ftarget"></a>

```c
struct i3c_ccc_deftgts_target
```

相关声明：[i3c_ccc_deftgts_target](../hardware/P421_I3C目标清单设备项.md)。

DEFTGTS通用命令码（CCC）载荷中的目标设备部分。

<a id="r_i3c_5Fccc_5Fdeftgts"></a>

```c
struct i3c_ccc_deftgts
```

相关声明：[i3c_ccc_deftgts](../hardware/P419_I3C目标清单命令数据.md)。

DEFTGTS通用命令码（CCC，定义目标列表）的载荷。

<a id="r_i3c_5Fccc_5Faddress"></a>

```c
struct i3c_ccc_address
```

相关声明：[i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)。

单个设备地址（Device Address）的载荷。

<a id="r_i3c_5Fccc_5Fgetpid"></a>

```c
struct i3c_ccc_getpid
```

相关声明：[i3c_ccc_getpid](../hardware/P414_I3C预置标识返回数据.md)。

GETPID通用命令码（CCC，获取预置ID）的载荷。

<a id="r_i3c_5Fccc_5Fgetbcr"></a>

```c
struct i3c_ccc_getbcr
```

相关声明：[i3c_ccc_getbcr](../hardware/P412_I3C总线特征返回数据.md)。

GETBCR通用命令码（CCC，获取总线特征寄存器）的载荷。

<a id="r_i3c_5Fccc_5Fgetdcr"></a>

```c
struct i3c_ccc_getdcr
```

相关声明：[i3c_ccc_getdcr](../hardware/P413_I3C设备特征返回数据.md)。

GETDCR通用命令码（CCC，获取设备特征寄存器）的载荷。

<a id="r_i3c_5Fccc_5Fgetstatus"></a>

```c
union i3c_ccc_getstatus
```

相关声明：[i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)。

GETSTATUS通用命令码（CCC，获取设备状态）的载荷。

<a id="r_i3c_5Fccc_5Fsetbrgtgt_5Ftgt"></a>

```c
struct i3c_ccc_setbrgtgt_tgt
```

相关声明：[i3c_ccc_setbrgtgt_tgt](../hardware/P423_I3C桥接目标设备项.md)。

SETBRGTGT载荷中的一个桥接目标（Bridged Target）。

<a id="r_i3c_5Fccc_5Fsetbrgtgt"></a>

```c
struct i3c_ccc_setbrgtgt
```

相关声明：[i3c_ccc_setbrgtgt](../hardware/P422_I3C桥接目标命令数据.md)。

SETBRGTGT通用命令码（CCC，设置桥接目标）的载荷。

<a id="r_i3c_5Fccc_5Fgetmxds"></a>

```c
union i3c_ccc_getmxds
```

相关声明：[i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)。

GETMXDS通用命令码（CCC，获取最大数据速率）的载荷。

<a id="r_i3c_5Fccc_5Fgetcaps"></a>

```c
union i3c_ccc_getcaps
```

相关声明：[i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)。

GETCAPS通用命令码（CCC，获取可选特性能力）的载荷。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.2\_宏定义（Macros）

<a id="r_gaf7b1cbdc790aa1d2c307e1f4ba773ba2"></a>

```c
#define I3C_CCC_BROADCAST_MAX_ID 0x7FU
```

相关声明：[I3C_CCC_BROADCAST_MAX_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)。

广播通用命令码（Common Command Code，CCC）的最大 ID。

<a id="r_ga06fc2296ada6198ab7a00646804ad5ed"></a>

```c
#define I3C_CCC_ENEC(broadcast)
```

相关声明：[I3C_CCC_ENEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga06fc2296ada6198ab7a00646804ad5ed)。

使能事件命令（Enable Events Command）。

<a id="r_ga8798591746e72a8ae1f901e97d45b810"></a>

```c
#define I3C_CCC_DISEC(broadcast)
```

相关声明：[I3C_CCC_DISEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8798591746e72a8ae1f901e97d45b810)。

禁用事件命令（Disable Events Command）。

<a id="r_ga213102b3a8dbd490b02c3c89843c8d2a"></a>

```c
#define I3C_CCC_ENTAS(as, broadcast)
```

相关声明：[I3C_CCC_ENTAS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga213102b3a8dbd490b02c3c89843c8d2a)。

进入活动状态（Enter Activity State）。

<a id="r_ga364ce54e30957f7871e56cd82c1f825c"></a>

```c
#define I3C_CCC_ENTAS0(broadcast)
```

相关声明：[I3C_CCC_ENTAS0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364ce54e30957f7871e56cd82c1f825c)。

进入活动状态 0（Enter Activity State 0）。

<a id="r_ga21c57ce34fe60255c9c8b28dac0a7a85"></a>

```c
#define I3C_CCC_ENTAS1(broadcast)
```

相关声明：[I3C_CCC_ENTAS1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga21c57ce34fe60255c9c8b28dac0a7a85)。

进入活动状态 1（Enter Activity State 1）。

<a id="r_ga3adea01f66748ae2b153bf7eb9eab1eb"></a>

```c
#define I3C_CCC_ENTAS2(broadcast)
```

相关声明：[I3C_CCC_ENTAS2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3adea01f66748ae2b153bf7eb9eab1eb)。

进入活动状态 2（Enter Activity State 2）。

<a id="r_ga4dba9093fe562e3d09470610ab393f21"></a>

```c
#define I3C_CCC_ENTAS3(broadcast)
```

相关声明：[I3C_CCC_ENTAS3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4dba9093fe562e3d09470610ab393f21)。

进入活动状态 3（Enter Activity State 3）。

<a id="r_gaed94df1e670fc3670970f261865d6f63"></a>

```c
#define I3C_CCC_RSTDAA 0x06U
```

相关声明：[I3C_CCC_RSTDAA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaed94df1e670fc3670970f261865d6f63)。

复位动态地址分配（Reset Dynamic Address Assignment），广播。

<a id="r_gad6663cfa56be6bba2187a1d42d64be7b"></a>

```c
#define I3C_CCC_ENTDAA 0x07U
```

相关声明：[I3C_CCC_ENTDAA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad6663cfa56be6bba2187a1d42d64be7b)。

进入动态地址分配（Enter Dynamic Address Assignment），广播。

<a id="r_ga17e63ffe790f279a3e6eb8235c936604"></a>

```c
#define I3C_CCC_DEFTGTS 0x08U
```

相关声明：[I3C_CCC_DEFTGTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga17e63ffe790f279a3e6eb8235c936604)。

定义目标端列表（Define List of Targets），广播。

<a id="r_gaab1ccf6cd47dfecee24811501e123802"></a>

```c
#define I3C_CCC_SETMWL(broadcast)
```

相关声明：[I3C_CCC_SETMWL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaab1ccf6cd47dfecee24811501e123802)。

设置最大写入长度（Set Max Write Length），广播或定向命令。

<a id="r_ga97fd874b2e6c918f2e1262f7600bfd64"></a>

```c
#define I3C_CCC_SETMRL(broadcast)
```

相关声明：[I3C_CCC_SETMRL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga97fd874b2e6c918f2e1262f7600bfd64)。

设置最大读取长度（Set Max Read Length），广播或定向命令。

<a id="r_gace2b7fc835d31ade916aad3126eb0c6c"></a>

```c
#define I3C_CCC_ENTTM 0x0BU
```

相关声明：[I3C_CCC_ENTTM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gace2b7fc835d31ade916aad3126eb0c6c)。

进入测试模式（Enter Test Mode），广播。

<a id="r_gac0f85a020956e3ee1ae8da899a9e06a6"></a>

```c
#define I3C_CCC_SETBUSCON 0x0CU
```

相关声明：[I3C_CCC_SETBUSCON](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac0f85a020956e3ee1ae8da899a9e06a6)。

设置总线上下文（Set Bus Context），广播。

<a id="r_ga4f331e7c21f15dd211a70c1a01c49738"></a>

```c
#define I3C_CCC_ENDXFER(broadcast)
```

相关声明：[I3C_CCC_ENDXFER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4f331e7c21f15dd211a70c1a01c49738)。

数据传输结束过程控制（Data Transfer Ending Procedure Control）。

<a id="r_gae213fc68bf723d8f7aee8c41cb9156c3"></a>

```c
#define I3C_CCC_ENTHDR(x)
```

相关声明：[I3C_CCC_ENTHDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae213fc68bf723d8f7aee8c41cb9156c3)。

进入高数据速率模式（HDR Mode，HDR-DDR），广播。

<a id="r_gae88e44e9469891609ece0b8711162b9d"></a>

```c
#define I3C_CCC_ENTHDR0 0x20U
```

相关声明：[I3C_CCC_ENTHDR0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae88e44e9469891609ece0b8711162b9d)。

进入 HDR 模式 0（HDR-DDR），广播。

<a id="r_gae5319f3916df262579ecaac7497ed006"></a>

```c
#define I3C_CCC_ENTHDR1 0x21U
```

相关声明：[I3C_CCC_ENTHDR1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae5319f3916df262579ecaac7497ed006)。

进入 HDR 模式 1（HDR-TSP），广播。

<a id="r_gaeff48ef5d76e4ea051f5aee1d1e4fc40"></a>

```c
#define I3C_CCC_ENTHDR2 0x22U
```

相关声明：[I3C_CCC_ENTHDR2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeff48ef5d76e4ea051f5aee1d1e4fc40)。

进入 HDR 模式 2（HDR-TSL），广播。

<a id="r_ga24eaa0af83a4a2223f4f84c3c67e05fe"></a>

```c
#define I3C_CCC_ENTHDR3 0x23U
```

相关声明：[I3C_CCC_ENTHDR3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga24eaa0af83a4a2223f4f84c3c67e05fe)。

进入 HDR 模式 3（HDR-BT），广播。

<a id="r_gaf15d188164c8fa9c0bf589eb7c5622d0"></a>

```c
#define I3C_CCC_ENTHDR4 0x24U
```

相关声明：[I3C_CCC_ENTHDR4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf15d188164c8fa9c0bf589eb7c5622d0)。

进入 HDR 模式 4，广播。

<a id="r_gaafcad6bfacab1e42f22c8ee941ed6441"></a>

```c
#define I3C_CCC_ENTHDR5 0x25U
```

相关声明：[I3C_CCC_ENTHDR5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaafcad6bfacab1e42f22c8ee941ed6441)。

进入 HDR 模式 5，广播。

<a id="r_gae55615887425917b202818bb0b7c5ac5"></a>

```c
#define I3C_CCC_ENTHDR6 0x26U
```

相关声明：[I3C_CCC_ENTHDR6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae55615887425917b202818bb0b7c5ac5)。

进入 HDR 模式 6，广播。

<a id="r_ga9ab8c02bb5a80913024a43077fb97ffb"></a>

```c
#define I3C_CCC_ENTHDR7 0x27U
```

相关声明：[I3C_CCC_ENTHDR7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9ab8c02bb5a80913024a43077fb97ffb)。

进入 HDR 模式 7，广播。

<a id="r_ga4203d5fdd9e9ca253803359934f22524"></a>

```c
#define I3C_CCC_SETXTIME(broadcast)
```

相关声明：[I3C_CCC_SETXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4203d5fdd9e9ca253803359934f22524)。

交换时序信息（Exchange Timing Information），广播或定向命令。

<a id="r_gae995ef9e94beb26932b47136bdf89b57"></a>

```c
#define I3C_CCC_SETAASA 0x29U
```

相关声明：[I3C_CCC_SETAASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae995ef9e94beb26932b47136bdf89b57)。

将所有地址设为静态地址（Set All Addresses to Static Addresses），广播。

<a id="r_ga424cb224727d33c1ab18e4149bbea232"></a>

```c
#define I3C_CCC_RSTACT(broadcast)
```

相关声明：[I3C_CCC_RSTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga424cb224727d33c1ab18e4149bbea232)。

目标端复位动作（Target Reset Action）。

<a id="r_ga89f8f72a7c7e8c9cb4fe8ece75ad78cf"></a>

```c
#define I3C_CCC_DEFGRPA 0x2BU
```

相关声明：[I3C_CCC_DEFGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)。

定义组地址列表（Define List of Group Address），广播。

<a id="r_ga46611eab0c82b74c615a7a7435f79d85"></a>

```c
#define I3C_CCC_RSTGRPA(broadcast)
```

相关声明：[I3C_CCC_RSTGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga46611eab0c82b74c615a7a7435f79d85)。

复位组地址（Reset Group Address）。

<a id="r_ga290cc5511d95b5be31c2c4cfea929085"></a>

```c
#define I3C_CCC_MLANE(broadcast)
```

相关声明：[I3C_CCC_MLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga290cc5511d95b5be31c2c4cfea929085)。

多通道数据传输控制（Multi-Lane Data Transfer Control），广播。

<a id="r_gaee5fb96b2d54df3b1b7aadefd54a608d"></a>

```c
#define I3C_CCC_VENDOR(broadcast, id)
```

相关声明：[I3C_CCC_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaee5fb96b2d54df3b1b7aadefd54a608d)。

厂商／标准扩展（Vendor/Standard Extension）。

<a id="r_ga3fcf2411223f6c39aab1476ed7e3ac8a"></a>

```c
#define I3C_CCC_RSTDAA_DC 0x86U
```

相关声明：[I3C_CCC_RSTDAA_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3fcf2411223f6c39aab1476ed7e3ac8a)。

复位动态地址（Reset Dynamic Address），定向命令。

<a id="r_ga134d5948b056144c83b133f93083a0f8"></a>

```c
#define I3C_CCC_SETDASA 0x87U
```

相关声明：[I3C_CCC_SETDASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga134d5948b056144c83b133f93083a0f8)。

根据静态地址设置动态地址（Set Dynamic Address from Static Address），定向命令。

<a id="r_gae0d6d0047f2c6e73e49e5019ec8d9ff0"></a>

```c
#define I3C_CCC_SETNEWDA 0x88U
```

相关声明：[I3C_CCC_SETNEWDA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0d6d0047f2c6e73e49e5019ec8d9ff0)。

设置新动态地址（Set New Dynamic Address），定向命令。

<a id="r_gae74935317b7ca471c09b767acf359e34"></a>

```c
#define I3C_CCC_GETMWL 0x8BU
```

相关声明：[I3C_CCC_GETMWL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae74935317b7ca471c09b767acf359e34)。

获取最大写入长度（Get Max Write Length），定向命令。

<a id="r_ga92e89b1ba719fbb8833c6e32fe4ef1dc"></a>

```c
#define I3C_CCC_GETMRL 0x8CU
```

相关声明：[I3C_CCC_GETMRL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga92e89b1ba719fbb8833c6e32fe4ef1dc)。

获取最大读取长度（Get Max Read Length），定向命令。

<a id="r_ga04f7386d55742e935fa4dbfeb0120124"></a>

```c
#define I3C_CCC_GETPID 0x8DU
```

相关声明：[I3C_CCC_GETPID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga04f7386d55742e935fa4dbfeb0120124)。

获取预置 ID（Get Provisioned ID），定向命令。

<a id="r_ga1d7d49ab48098e4c2d5f63bd91d005e1"></a>

```c
#define I3C_CCC_GETBCR 0x8EU
```

相关声明：[I3C_CCC_GETBCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1d7d49ab48098e4c2d5f63bd91d005e1)。

获取总线特征寄存器（Get Bus Characteristics Register），定向命令。

<a id="r_ga04ab6d4f0b2bf9d7f195132c0959225c"></a>

```c
#define I3C_CCC_GETDCR 0x8FU
```

相关声明：[I3C_CCC_GETDCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga04ab6d4f0b2bf9d7f195132c0959225c)。

获取设备特征寄存器（Get Device Characteristics Register），定向命令。

<a id="r_ga858603dfc251b684b9d049b90119993d"></a>

```c
#define I3C_CCC_GETSTATUS 0x90U
```

相关声明：[I3C_CCC_GETSTATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga858603dfc251b684b9d049b90119993d)。

获取设备状态（Get Device Status），定向命令。

<a id="r_gaa6807d3113c9c4d19b6fd27db32b3698"></a>

```c
#define I3C_CCC_GETACCCR 0x91U
```

相关声明：[I3C_CCC_GETACCCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa6807d3113c9c4d19b6fd27db32b3698)。

获取控制器角色接受状态（Get Accept Controller Role），定向命令。

<a id="r_gab3cac5de39903cc2331a38ac66c4ff14"></a>

```c
#define I3C_CCC_SETBRGTGT 0x93U
```

相关声明：[I3C_CCC_SETBRGTGT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3cac5de39903cc2331a38ac66c4ff14)。

设置桥接目标端（Set Bridge Targets），定向命令。

<a id="r_ga2c078bf24e36689f34ad90979dd5c687"></a>

```c
#define I3C_CCC_GETMXDS 0x94U
```

相关声明：[I3C_CCC_GETMXDS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2c078bf24e36689f34ad90979dd5c687)。

获取最大数据速率（Get Max Data Speed），定向命令。

<a id="r_gaa913844f97ee35405e9bf50c61a161a8"></a>

```c
#define I3C_CCC_GETCAPS 0x95U
```

相关声明：[I3C_CCC_GETCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa913844f97ee35405e9bf50c61a161a8)。

获取可选特性能力（Get Optional Feature Capabilities），定向命令。

<a id="r_ga5cf5cdb40299d4f8203b8035dacac17a"></a>

```c
#define I3C_CCC_SETROUTE 0x96U
```

相关声明：[I3C_CCC_SETROUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5cf5cdb40299d4f8203b8035dacac17a)。

设置路由（Set Route），定向命令。

<a id="r_gaa2d86faed4f7c36939ce754be852751a"></a>

```c
#define I3C_CCC_D2DXFER 0x97U
```

相关声明：[I3C_CCC_D2DXFER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa2d86faed4f7c36939ce754be852751a)。

设备间隧道控制（Device to Device(s) Tunneling Control），定向命令。

<a id="r_ga66bb5e8027b103298f882f413f8ee6e8"></a>

```c
#define I3C_CCC_GETXTIME 0x99U
```

相关声明：[I3C_CCC_GETXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66bb5e8027b103298f882f413f8ee6e8)。

获取交换时序信息（Get Exchange Timing Information），定向命令。

<a id="r_gaa0bef5d42c9bf2a21e888e5d5998d5cb"></a>

```c
#define I3C_CCC_SETGRPA 0x9BU
```

相关声明：[I3C_CCC_SETGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa0bef5d42c9bf2a21e888e5d5998d5cb)。

设置组地址（Set Group Address），定向命令。

<a id="r_gafe40d9b2ccedca40071c47929ff66e65"></a>

```c
#define I3C_CCC_ENEC_EVT_ENINTR BIT(0)
```

相关声明：[I3C_CCC_ENEC_EVT_ENINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafe40d9b2ccedca40071c47929ff66e65)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能事件（ENEC）：目标端中断请求（Target Interrupt Requests）。

<a id="r_gad73e2e9f31f3a02f52b20d77e64671ff"></a>

```c
#define I3C_CCC_ENEC_EVT_ENCR BIT(1)
```

相关声明：[I3C_CCC_ENEC_EVT_ENCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad73e2e9f31f3a02f52b20d77e64671ff)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能事件（ENEC）：控制器角色请求（Controller Role Requests）。

<a id="r_ga7e705ac95643d0462ac4275eed42153a"></a>

```c
#define I3C_CCC_ENEC_EVT_ENHJ BIT(3)
```

相关声明：[I3C_CCC_ENEC_EVT_ENHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7e705ac95643d0462ac4275eed42153a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

使能事件（ENEC）：热加入事件（Hot-Join Event）。

<a id="r_ga7860289b621c4243401e1df21cd84d66"></a>

```c
#define I3C_CCC_ENEC_EVT_ALL (I3C_CCC_ENEC_EVT_ENINTR | I3C_CCC_ENEC_EVT_ENCR | I3C_CCC_ENEC_EVT_ENHJ)
```

相关声明：[I3C_CCC_ENEC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7860289b621c4243401e1df21cd84d66)、[I3C_CCC_ENEC_EVT_ENINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafe40d9b2ccedca40071c47929ff66e65)、[I3C_CCC_ENEC_EVT_ENCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad73e2e9f31f3a02f52b20d77e64671ff)、[I3C_CCC_ENEC_EVT_ENHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7e705ac95643d0462ac4275eed42153a)。

<a id="r_gaf6da0458f1ae2d45ae7337cd4e576484"></a>

```c
#define I3C_CCC_DISEC_EVT_DISINTR BIT(0)
```

相关声明：[I3C_CCC_DISEC_EVT_DISINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6da0458f1ae2d45ae7337cd4e576484)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用事件（DISEC）：目标端中断请求（Target Interrupt Requests）。

<a id="r_ga1f1612a16d2cb68b66f1ca85ba6f450a"></a>

```c
#define I3C_CCC_DISEC_EVT_DISCR BIT(1)
```

相关声明：[I3C_CCC_DISEC_EVT_DISCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1f1612a16d2cb68b66f1ca85ba6f450a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用事件（DISEC）：控制器角色请求（Controller Role Requests）。

<a id="r_gac3ffda84f683f99a0d4e0ad67adfd675"></a>

```c
#define I3C_CCC_DISEC_EVT_DISHJ BIT(3)
```

相关声明：[I3C_CCC_DISEC_EVT_DISHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac3ffda84f683f99a0d4e0ad67adfd675)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

禁用事件（DISEC）：热加入事件（Hot-Join Event）。

<a id="r_gaf177b8fcb7412671a3b8c418336ddde4"></a>

```c
#define I3C_CCC_DISEC_EVT_ALL (I3C_CCC_DISEC_EVT_DISINTR | I3C_CCC_DISEC_EVT_DISCR | I3C_CCC_DISEC_EVT_DISHJ)
```

相关声明：[I3C_CCC_DISEC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf177b8fcb7412671a3b8c418336ddde4)、[I3C_CCC_DISEC_EVT_DISINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6da0458f1ae2d45ae7337cd4e576484)、[I3C_CCC_DISEC_EVT_DISCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1f1612a16d2cb68b66f1ca85ba6f450a)、[I3C_CCC_DISEC_EVT_DISHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac3ffda84f683f99a0d4e0ad67adfd675)。

<a id="r_ga14cbf3628627f965336ac3740858aeea"></a>

```c
#define I3C_CCC_EVT_INTR BIT(0)
```

相关声明：[I3C_CCC_EVT_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga14cbf3628627f965336ac3740858aeea)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事件（Events）：目标端中断请求（Target Interrupt Requests）。

<a id="r_gad515a978c4912ef0c0444f14e51d8e8f"></a>

```c
#define I3C_CCC_EVT_CR BIT(1)
```

相关声明：[I3C_CCC_EVT_CR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad515a978c4912ef0c0444f14e51d8e8f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事件（Events）：控制器角色请求（Controller Role Requests）。

<a id="r_gaedf65a98d59de51a533ff3d2f8cf075a"></a>

```c
#define I3C_CCC_EVT_HJ BIT(3)
```

相关声明：[I3C_CCC_EVT_HJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaedf65a98d59de51a533ff3d2f8cf075a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

事件（Events）：热加入事件（Hot-Join Event）。

<a id="r_ga8ff2055f745c4970bd41850bfd5b2aff"></a>

```c
#define I3C_CCC_EVT_ALL (I3C_CCC_EVT_INTR | I3C_CCC_EVT_CR | I3C_CCC_EVT_HJ)
```

相关声明：[I3C_CCC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8ff2055f745c4970bd41850bfd5b2aff)、[I3C_CCC_EVT_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga14cbf3628627f965336ac3740858aeea)、[I3C_CCC_EVT_CR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad515a978c4912ef0c0444f14e51d8e8f)、[I3C_CCC_EVT_HJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaedf65a98d59de51a533ff3d2f8cf075a)。

所有事件（Events）的位掩码。

<a id="r_gaee3dd61e9ac723a90868c610d0179b7d"></a>

```c
#define I3C_CCC_GETSTATUS_PROTOCOL_ERR BIT(5)
```

相关声明：[I3C_CCC_GETSTATUS_PROTOCOL_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaee3dd61e9ac723a90868c610d0179b7d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETSTATUS 格式 1：协议错误位（Protocol Error Bit）。

<a id="r_ga1006146ca810c06674fbee0ee1f66286"></a>

```c
#define I3C_CCC_GETSTATUS_ACTIVITY_MODE_MASK GENMASK(7U, 6U)
```

相关声明：[I3C_CCC_GETSTATUS_ACTIVITY_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1006146ca810c06674fbee0ee1f66286)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETSTATUS 格式 1：活动模式位掩码（Activity Mode Bitmask）。

<a id="r_ga660e179384e9426b498cd62da5665b15"></a>

```c
#define I3C_CCC_GETSTATUS_ACTIVITY_MODE(status)
```

相关声明：[I3C_CCC_GETSTATUS_ACTIVITY_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga660e179384e9426b498cd62da5665b15)。

GETSTATUS 格式 1：活动模式（Activity Mode）。

<a id="r_ga4bf92ca4dd05387b9d10cb256ad3552b"></a>

```c
#define I3C_CCC_GETSTATUS_ACTIVITY_MODE_NCH 0x3
```

相关声明：[I3C_CCC_GETSTATUS_ACTIVITY_MODE_NCH](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4bf92ca4dd05387b9d10cb256ad3552b)。

GETSTATUS 格式 1：无法参与控制器交接（Controller Handoff）的活动模式。

<a id="r_gae0bcc3ea13a34f63b073d63569d2e53a"></a>

```c
#define I3C_CCC_GETSTATUS_NUM_INT_MASK GENMASK(3U, 0U)
```

相关声明：[I3C_CCC_GETSTATUS_NUM_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0bcc3ea13a34f63b073d63569d2e53a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETSTATUS 格式 1：待处理中断数量位掩码（Number of Pending Interrupts Bitmask）。

<a id="r_ga1436dc4b9f71c6f61fd3e3331857f3bd"></a>

```c
#define I3C_CCC_GETSTATUS_NUM_INT(status)
```

相关声明：[I3C_CCC_GETSTATUS_NUM_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1436dc4b9f71c6f61fd3e3331857f3bd)。

GETSTATUS 格式 1：待处理中断数量（Number of Pending Interrupts）。

<a id="r_ga94afb0ebcfce55b85fc4a81953b4178a"></a>

```c
#define I3C_CCC_GETSTATUS_PRECR_DEEP_SLEEP_DETECTED BIT(0)
```

相关声明：[I3C_CCC_GETSTATUS_PRECR_DEEP_SLEEP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga94afb0ebcfce55b85fc4a81953b4178a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETSTATUS 格式 2 的 PERCR：深度睡眠检测位（Deep Sleep Detected Bit）。

<a id="r_gadda1781cae312f4e588c3d3dcfa74f38"></a>

```c
#define I3C_CCC_GETSTATUS_PRECR_HANDOFF_DELAY_NACK BIT(1)
```

相关声明：[I3C_CCC_GETSTATUS_PRECR_HANDOFF_DELAY_NACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadda1781cae312f4e588c3d3dcfa74f38)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETSTATUS 格式 2 的 PERCR：交接延迟否定应答（Handoff Delay NACK）。

<a id="r_ga65ed8d5c2e6f562215674217f974d608"></a>

```c
#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_MAX 0
```

相关声明：[I3C_CCC_GETMXDS_MAX_SDR_FSCL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga65ed8d5c2e6f562215674217f974d608)。

获取最大数据速率（GETMXDS）：默认最大持续数据速率（Max Sustained Data Rate）。

<a id="r_gaac6dec9aee1e1d5a56c964a4d1fe32b1"></a>

```c
#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_8MHZ 1
```

相关声明：[I3C_CCC_GETMXDS_MAX_SDR_FSCL_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaac6dec9aee1e1d5a56c964a4d1fe32b1)。

GETMXDS：8 MHz 最大持续数据速率（Max Sustained Data Rate）。

<a id="r_gae1ff27ad2b8c9119e2efa88c0a696555"></a>

```c
#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_6MHZ 2
```

相关声明：[I3C_CCC_GETMXDS_MAX_SDR_FSCL_6MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae1ff27ad2b8c9119e2efa88c0a696555)。

GETMXDS：6 MHz 最大持续数据速率（Max Sustained Data Rate）。

<a id="r_ga409666d6a17b53e518d702863826eb28"></a>

```c
#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_4MHZ 3
```

相关声明：[I3C_CCC_GETMXDS_MAX_SDR_FSCL_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga409666d6a17b53e518d702863826eb28)。

GETMXDS：4 MHz 最大持续数据速率（Max Sustained Data Rate）。

<a id="r_ga5a329b3fa12ecafd6958b05bab163a5c"></a>

```c
#define I3C_CCC_GETMXDS_MAX_SDR_FSCL_2MHZ 4
```

相关声明：[I3C_CCC_GETMXDS_MAX_SDR_FSCL_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5a329b3fa12ecafd6958b05bab163a5c)。

GETMXDS：2 MHz 最大持续数据速率（Max Sustained Data Rate）。

<a id="r_gad5e417bc3cabf8a915d1e7938415125a"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_8NS 0
```

相关声明：[I3C_CCC_GETMXDS_TSCO_8NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad5e417bc3cabf8a915d1e7938415125a)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）小于等于 8 ns。

<a id="r_gaaee475f82f3a3759c7d62bb48082ebc2"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_9NS 1
```

相关声明：[I3C_CCC_GETMXDS_TSCO_9NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaee475f82f3a3759c7d62bb48082ebc2)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）小于等于 9 ns。

<a id="r_ga5e264e39aa2d4b602ec5e3218708e2f6"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_10NS 2
```

相关声明：[I3C_CCC_GETMXDS_TSCO_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5e264e39aa2d4b602ec5e3218708e2f6)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）小于等于 10 ns。

<a id="r_ga2b27c9023f447da9c474c078091cf580"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_11NS 3
```

相关声明：[I3C_CCC_GETMXDS_TSCO_11NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2b27c9023f447da9c474c078091cf580)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）小于等于 11 ns。

<a id="r_ga06d33d1884a30d179aace82af956d62d"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_12NS 4
```

相关声明：[I3C_CCC_GETMXDS_TSCO_12NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga06d33d1884a30d179aace82af956d62d)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）小于等于 12 ns。

<a id="r_ga5be034f241ccfb59534ae247d2e31d85"></a>

```c
#define I3C_CCC_GETMXDS_TSCO_GT_12NS 7
```

相关声明：[I3C_CCC_GETMXDS_TSCO_GT_12NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5be034f241ccfb59534ae247d2e31d85)。

GETMXDS：时钟到数据周转时间（Clock to Data Turnaround）大于 12 ns。

<a id="r_ga43fa03b6fea48cca06d07e962c5c04ef"></a>

```c
#define I3C_CCC_GETMXDS_MAXWR_DEFINING_BYTE_SUPPORT BIT(3)
```

相关声明：[I3C_CCC_GETMXDS_MAXWR_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga43fa03b6fea48cca06d07e962c5c04ef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETMXDS 的 `maxWr`：可选定义字节支持（Optional Defining Byte Support）。

<a id="r_ga5f4c6dde339c3467bdb3aea0d680d01f"></a>

```c
#define I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL_MASK GENMASK(2U, 0U)
```

相关声明：[I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5f4c6dde339c3467bdb3aea0d680d01f)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETMXDS：最大持续数据速率位掩码（Max Sustained Data Rate Bitmask）。

<a id="r_gae61b18d964e575809a1ebe2189aae028"></a>

```c
#define I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL(maxwr)
```

相关声明：[I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae61b18d964e575809a1ebe2189aae028)。

GETMXDS 的 `maxWr`：最大持续数据速率（Max Sustained Data Rate）。

<a id="r_gaf5b95266cc911a37a3e46565b7601970"></a>

```c
#define I3C_CCC_GETMXDS_MAXRD_W2R_PERMITS_STOP_BETWEEN BIT(6)
```

相关声明：[I3C_CCC_GETMXDS_MAXRD_W2R_PERMITS_STOP_BETWEEN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5b95266cc911a37a3e46565b7601970)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETMXDS 的 `maxRd`：允许在写入与读取之间插入停止条件（Write-to-Read Permits Stop Between）。

<a id="r_ga41958f7756cc5dec1c0546e7832b764a"></a>

```c
#define I3C_CCC_GETMXDS_MAXRD_TSCO_MASK GENMASK(5U, 3U)
```

相关声明：[I3C_CCC_GETMXDS_MAXRD_TSCO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga41958f7756cc5dec1c0546e7832b764a)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETMXDS 的 `maxRd`：时钟到数据周转时间位掩码（Clock to Data Turnaround Bitmask）。

<a id="r_ga8284130d363dd1898de44c572b3d566c"></a>

```c
#define I3C_CCC_GETMXDS_MAXRD_TSCO(maxrd)
```

相关声明：[I3C_CCC_GETMXDS_MAXRD_TSCO](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8284130d363dd1898de44c572b3d566c)。

GETMXDS 的 `maxRd`：时钟到数据周转时间（Clock to Data Turnaround）。

<a id="r_gad8b14f71cc1d5c1a0daa27703ab0c774"></a>

```c
#define I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL_MASK GENMASK(2U, 0U)
```

相关声明：[I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad8b14f71cc1d5c1a0daa27703ab0c774)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETMXDS 的 `maxRd`：最大持续数据速率位掩码（Max Sustained Data Rate Bitmask）。

<a id="r_gaf5ac7364357e1e123adddcbfc134a0be"></a>

```c
#define I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL(maxrd)
```

相关声明：[I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5ac7364357e1e123adddcbfc134a0be)。

GETMXDS 的 `maxRd`：最大持续数据速率（Max Sustained Data Rate）。

<a id="r_ga9aa4eaf8a537323883d242e9ebb9a985"></a>

```c
#define I3C_CCC_GETMXDS_CRDHLY1_SET_BUS_ACT_STATE BIT(2)
```

相关声明：[I3C_CCC_GETMXDS_CRDHLY1_SET_BUS_ACT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9aa4eaf8a537323883d242e9ebb9a985)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

GETMXDS 的 `CRDHLY1`：设置总线活动状态的移位值（Set Bus Activity State Bit Shift Value）。

<a id="r_ga9ad046b7ec49bbca3f70a5a30fb1524b"></a>

```c
#define I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE_MASK GENMASK(1U, 0U)
```

相关声明：[I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9ad046b7ec49bbca3f70a5a30fb1524b)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

GETMXDS 的 `CRDHLY1`：控制器交接活动状态位掩码（Controller Handoff Activity State Bitmask）。

<a id="r_gab43a5adbcf158086d23c5d796a7e9399"></a>

```c
#define I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE(crhdly1)
```

相关声明：[I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab43a5adbcf158086d23c5d796a7e9399)。

GETMXDS 的 `CRDHLY1`：控制器交接活动状态（Controller Handoff Activity State）。

<a id="r_gab984c6a18a555e4a3c0552684083e330"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_DDR BIT(0)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab984c6a18a555e4a3c0552684083e330)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR-DDR 模式位。

<a id="r_gafe33491b778aa806977a98c3bd12a339"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_TSP BIT(1)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafe33491b778aa806977a98c3bd12a339)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR-TSP 模式位。

<a id="r_gae9b98ab62745f041e4fe6e89ecd3b0e6"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_TSL BIT(2)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae9b98ab62745f041e4fe6e89ecd3b0e6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR-TSL 模式位。

<a id="r_gaac01f085ed1af56d686a33694744081c"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_BT BIT(3)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaac01f085ed1af56d686a33694744081c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR-BT 模式位。

<a id="r_gaae9483f4d5de3ba092b870b20e6b5f4a"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE(x)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaae9483f4d5de3ba092b870b20e6b5f4a)。

获取可选特性能力字节 1（GETCAPS）：高数据速率模式（HDR Mode）。

<a id="r_gad1389fc52c3fec4d6206bc56566bbf5d"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE0 BIT(0)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad1389fc52c3fec4d6206bc56566bbf5d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 0。

<a id="r_gacfd20baf528fcceca7f71719e15d5ea0"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE1 BIT(1)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gacfd20baf528fcceca7f71719e15d5ea0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 1。

<a id="r_ga9e5581743cbbe7363bb0919b95148d85"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE2 BIT(2)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9e5581743cbbe7363bb0919b95148d85)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 2。

<a id="r_ga97b146596467f410ce9f063365ac9aaf"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE3 BIT(3)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga97b146596467f410ce9f063365ac9aaf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 3。

<a id="r_ga0dd98eeb74f493bfb04aeb698e656772"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE4 BIT(4)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0dd98eeb74f493bfb04aeb698e656772)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 4。

<a id="r_ga99bff02c40ccb15797dcf10c6dc00e87"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE5 BIT(5)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga99bff02c40ccb15797dcf10c6dc00e87)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 5。

<a id="r_ga12cead0a8ceb518a5c897f22b1d3dd64"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE6 BIT(6)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga12cead0a8ceb518a5c897f22b1d3dd64)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 6。

<a id="r_ga8b3373f18c0e3b365cc199c19ae82fb0"></a>

```c
#define I3C_CCC_GETCAPS1_HDR_MODE7 BIT(7)
```

相关声明：[I3C_CCC_GETCAPS1_HDR_MODE7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8b3373f18c0e3b365cc199c19ae82fb0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 1（GETCAPS）格式 1：HDR 模式 7。

<a id="r_ga1c2ceeaa44ee641c3d05176baf7e681d"></a>

```c
#define I3C_CCC_GETCAPS2_HDRDDR_WRITE_ABORT BIT(6)
```

相关声明：[I3C_CCC_GETCAPS2_HDRDDR_WRITE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1c2ceeaa44ee641c3d05176baf7e681d)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 2（GETCAPS）格式 1：HDR-DDR 写入中止位（Write Abort Bit）。

<a id="r_ga8faf5ff5b2542a309f114ce4d6d11640"></a>

```c
#define I3C_CCC_GETCAPS2_HDRDDR_ABORT_CRC BIT(7)
```

相关声明：[I3C_CCC_GETCAPS2_HDRDDR_ABORT_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8faf5ff5b2542a309f114ce4d6d11640)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 2（GETCAPS）格式 1：HDR-DDR 中止 CRC 位（Abort CRC Bit）。

<a id="r_ga64f58d1aaf847cf4a7811b20cca13b55"></a>

```c
#define I3C_CCC_GETCAPS2_GRPADDR_CAP_MASK GENMASK(5U, 4U)
```

相关声明：[I3C_CCC_GETCAPS2_GRPADDR_CAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga64f58d1aaf847cf4a7811b20cca13b55)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

获取可选特性能力字节 2（GETCAPS）格式 1：组地址能力位掩码（Group Address Capabilities Bitmask）。

<a id="r_gabeb9acdabd6dce2117e9f5830673b2ed"></a>

```c
#define I3C_CCC_GETCAPS2_GRPADDR_CAP(getcaps2)
```

相关声明：[I3C_CCC_GETCAPS2_GRPADDR_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gabeb9acdabd6dce2117e9f5830673b2ed)。

获取可选特性能力字节 2（GETCAPS）格式 1：组地址能力（Group Address Capabilities）。

<a id="r_gae0015aa7768a8d5c18426a47cdbb67f8"></a>

```c
#define I3C_CCC_GETCAPS2_SPEC_VER_MASK GENMASK(3U, 0U)
```

相关声明：[I3C_CCC_GETCAPS2_SPEC_VER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0015aa7768a8d5c18426a47cdbb67f8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

获取可选特性能力字节 2（GETCAPS）格式 1：I3C 1.x 规范版本位掩码（Specification Version Bitmask）。

<a id="r_ga093449c1cf029bddf1a25181cbfed570"></a>

```c
#define I3C_CCC_GETCAPS2_SPEC_VER(getcaps2)
```

相关声明：[I3C_CCC_GETCAPS2_SPEC_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga093449c1cf029bddf1a25181cbfed570)。

获取可选特性能力字节 2（GETCAPS）格式 1：I3C 1.x 规范版本（Specification Version）。

<a id="r_gaf0a2358f0f5f46c5fa1c084373f09be1"></a>

```c
#define I3C_CCC_GETCAPS3_MLANE_SUPPORT BIT(0)
```

相关声明：[I3C_CCC_GETCAPS3_MLANE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf0a2358f0f5f46c5fa1c084373f09be1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：多通道数据传输支持位（Multi-Lane Data Transfer Support Bit）。

<a id="r_ga08cc3c3976195642282e00ba00c1b283"></a>

```c
#define I3C_CCC_GETCAPS3_D2DXFER_SUPPORT BIT(1)
```

相关声明：[I3C_CCC_GETCAPS3_D2DXFER_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga08cc3c3976195642282e00ba00c1b283)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：设备间传输（Device to Device Transfer，D2DXFER）支持位。

<a id="r_ga73829cd436decbe55d2290dc750b3918"></a>

```c
#define I3C_CCC_GETCAPS3_D2DXFER_IBI_CAPABLE BIT(2)
```

相关声明：[I3C_CCC_GETCAPS3_D2DXFER_IBI_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga73829cd436decbe55d2290dc750b3918)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：设备间传输（D2DXFER）带内中断能力位（IBI Capable Bit）。

<a id="r_gaf40cc6cc08619363056e9650453a9a26"></a>

```c
#define I3C_CCC_GETCAPS3_GETCAPS_DEFINING_BYTE_SUPPORT BIT(3)
```

相关声明：[I3C_CCC_GETCAPS3_GETCAPS_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf40cc6cc08619363056e9650453a9a26)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：GETCAPS 中的定义字节支持位（Defining Byte Support Bit）。

<a id="r_gafbf1e9c947c40d70ae1c45991d093570"></a>

```c
#define I3C_CCC_GETCAPS3_GETSTATUS_DEFINING_BYTE_SUPPORT BIT(4)
```

相关声明：[I3C_CCC_GETCAPS3_GETSTATUS_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafbf1e9c947c40d70ae1c45991d093570)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：GETSTATUS 中的定义字节支持位（Defining Byte Support Bit）。

<a id="r_ga3575eb8aa6fc3b49f2115104dcdfaeec"></a>

```c
#define I3C_CCC_GETCAPS3_HDRBT_CRC32_SUPPORT BIT(5)
```

相关声明：[I3C_CCC_GETCAPS3_HDRBT_CRC32_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3575eb8aa6fc3b49f2115104dcdfaeec)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：HDR-BT CRC-32 支持位。

<a id="r_gac13d1465aa4222be0acccbf5303f3f3e"></a>

```c
#define I3C_CCC_GETCAPS3_IBI_MDR_PENDING_READ_NOTIFICATION BIT(6)
```

相关声明：[I3C_CCC_GETCAPS3_IBI_MDR_PENDING_READ_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac13d1465aa4222be0acccbf5303f3f3e)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取可选特性能力字节 3（GETCAPS）格式 1：待处理读取通知的带内中断强制数据字节支持位（IBI MDB Support for Pending Read Notification Bit）。

<a id="r_ga541ed236f06c20ca98e32d5a17788754"></a>

```c
#define I3C_CCC_GETCAPS_TESTPAT1 0xA5
```

相关声明：[I3C_CCC_GETCAPS_TESTPAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga541ed236f06c20ca98e32d5a17788754)。

获取固定测试模式（GETCAPS）格式 2：固定测试模式字节 1（Fixed Test Pattern Byte 1）。

<a id="r_gafdb7ed7cc72efeb7cd62435084b1b40f"></a>

```c
#define I3C_CCC_GETCAPS_TESTPAT2 0x5A
```

相关声明：[I3C_CCC_GETCAPS_TESTPAT2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafdb7ed7cc72efeb7cd62435084b1b40f)。

获取固定测试模式（GETCAPS）格式 2：固定测试模式字节 2（Fixed Test Pattern Byte 2）。

<a id="r_ga1720b3f54ade943f627b6a4e7284139a"></a>

```c
#define I3C_CCC_GETCAPS_TESTPAT3 0xA5
```

相关声明：[I3C_CCC_GETCAPS_TESTPAT3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1720b3f54ade943f627b6a4e7284139a)。

获取固定测试模式（GETCAPS）格式 2：固定测试模式字节 3（Fixed Test Pattern Byte 3）。

<a id="r_ga2391e23e0b17351e3c28048b85d98ea6"></a>

```c
#define I3C_CCC_GETCAPS_TESTPAT4 0x5A
```

相关声明：[I3C_CCC_GETCAPS_TESTPAT4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2391e23e0b17351e3c28048b85d98ea6)。

获取固定测试模式（GETCAPS）格式 2：固定测试模式字节 4（Fixed Test Pattern Byte 4）。

<a id="r_ga98ee1cc4c436219b9639c5710fa6911b"></a>

```c
#define I3C_CCC_GETCAPS_TESTPAT 0xA55AA55A
```

相关声明：[I3C_CCC_GETCAPS_TESTPAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga98ee1cc4c436219b9639c5710fa6911b)。

获取固定测试模式（GETCAPS）格式 2：大端字节序的固定测试模式字（Fixed Test Pattern Word in Big Endian）。

<a id="r_gad833335c6edb018edb66b99e1dfc16f7"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS1_HJ_SUPPORT BIT(0)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS1_HJ_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad833335c6edb018edb66b99e1dfc16f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 1（GETCAPS）格式 2：热加入支持（Hot-Join Support）。

<a id="r_ga86b22acbba045b037b4ae14abf4b6e5c"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS1_GRP_MANAGEMENT_SUPPORT BIT(1)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS1_GRP_MANAGEMENT_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga86b22acbba045b037b4ae14abf4b6e5c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 1（GETCAPS）格式 2：组管理支持（Group Management Support）。

<a id="r_ga438621df282f451083e9ab9b1b59a2e3"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS1_ML_SUPPORT BIT(2)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS1_ML_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga438621df282f451083e9ab9b1b59a2e3)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 1（GETCAPS）格式 2：多通道支持（Multi-Lane Support）。

<a id="r_ga5bedcb1cb3769ae69779c0b2125b4b21"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS2_IBI_TIR_SUPPORT BIT(0)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS2_IBI_TIR_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5bedcb1cb3769ae69779c0b2125b4b21)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 2（GETCAPS）格式 2：带内中断支持（In-Band Interrupt Support）。

<a id="r_ga3a49b8a44676888fe600aa6b42cc52c6"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS2_CONTROLLER_PASSBACK BIT(1)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS2_CONTROLLER_PASSBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3a49b8a44676888fe600aa6b42cc52c6)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 2（GETCAPS）格式 2：控制器角色交还（Controller Pass-Back）。

<a id="r_gad81d9a56d02db7e8a87279d8772adbec"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS2_DEEP_SLEEP_CAPABLE BIT(2)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS2_DEEP_SLEEP_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad81d9a56d02db7e8a87279d8772adbec)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 2（GETCAPS）格式 2：深度睡眠能力（Deep Sleep Capable）。

<a id="r_gada1a84b1394d6a72dd49e1c87307fbef"></a>

```c
#define I3C_CCC_GETCAPS_CRCAPS2_DELAYED_CONTROLLER_HANDOFF BIT(3)
```

相关声明：[I3C_CCC_GETCAPS_CRCAPS2_DELAYED_CONTROLLER_HANDOFF](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gada1a84b1394d6a72dd49e1c87307fbef)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取控制器交接能力字节 2（GETCAPS）格式 2：深度睡眠能力（Deep Sleep Capable）。

<a id="r_ga382e8db432a701a8b2f6c8be6aba81a8"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE_MASK GENMASK(2U, 0U)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga382e8db432a701a8b2f6c8be6aba81a8)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

获取能力（GETCAPS）的 `VTCAP1`：虚拟目标端类型位掩码（Virtual Target Type Bitmask）。

<a id="r_ga9d0153d2e0b01a045e59e4acf4446206"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE(vtcap1)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9d0153d2e0b01a045e59e4acf4446206)。

获取能力（GETCAPS）的 `VTCAP1`：虚拟目标端类型（Virtual Target Type）。

<a id="r_gaca37ffb4f223c7b723a1b2ed881d28f7"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP1_SIDE_EFFECTS BIT(4)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP1_SIDE_EFFECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaca37ffb4f223c7b723a1b2ed881d28f7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取虚拟目标端能力字节 1（GETCAPS）格式 2：副作用（Side Effects）。

<a id="r_gad1c0b63bb26be245e781e5d32d75dd15"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP1_SHARED_PERIPH_DETECT BIT(5)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP1_SHARED_PERIPH_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad1c0b63bb26be245e781e5d32d75dd15)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取虚拟目标端能力字节 1（GETCAPS）格式 2：共享外设检测（Shared Peripheral Detect）。

<a id="r_gad39e1c3d38b29937166345133ad373d1"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS_MASK GENMASK(1U, 0U)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad39e1c3d38b29937166345133ad373d1)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

获取能力（GETCAPS）的 `VTCAP2`：中断请求位掩码（Interrupt Requests Bitmask）。

<a id="r_ga8ee2a538a2b5efa2e02540aac392c685"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS(vtcap2)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8ee2a538a2b5efa2e02540aac392c685)。

获取能力（GETCAPS）的 `VTCAP2`：中断请求（Interrupt Requests）。

<a id="r_ga1b7562342dbf9fe443386943527d5f29"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP2_ADDRESS_REMAPPING BIT(2)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP2_ADDRESS_REMAPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1b7562342dbf9fe443386943527d5f29)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

获取虚拟目标端能力字节 2（GETCAPS）格式 2：地址重映射（Address Remapping）。

<a id="r_gadc61e60fbc59aca1ff813098f51ca56e"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND_MASK GENMASK(4U, 3U)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadc61e60fbc59aca1ff813098f51ca56e)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

获取能力（GETCAPS）的 `VTCAP2`：总线上下文与条件位掩码（Bus Context and Condition Bitmask）。

<a id="r_ga56112189be57287691d64eabfaa32910"></a>

```c
#define I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND(vtcap2)
```

相关声明：[I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga56112189be57287691d64eabfaa32910)。

获取能力（GETCAPS）的 `VTCAP2`：总线上下文与条件（Bus Context and Condition）。

<a id="define-members-0"></a>

### 设置总线上下文：MIPI I3C 规范 v1.Y 的次版本号（Set Bus Context MIPI I3C Specification v1.Y Minor Version (SETBUSCON)）



示例按 `Bit[5]`、`Bit[4]`、`Bits[3:0]` 的顺序给出：I3C Basic v1.1.0 为 `1’b0 || 1’b1 || 4’b0001`，或 `8’b00010001`；I3C Basic v1.1.1 为 `1’b1 || 1’b1 || 4’b0001`，或 `8’b00110001`；I3C Basic v1.2.0 为 `1’b0 || 1’b1 || 4’b0010`，或 `8’b00010010`。

<a id="r_gae61d6a25793e701524a5cf82c2593fce"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER_MASK GENMASK(3U, 0U)
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae61d6a25793e701524a5cf82c2593fce)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

I3C 规范次版本（Specification Minor Version）的移位掩码。

<a id="r_gaadcfe82c6f945d2233a4a459bb3d0ec1"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER(y)
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaadcfe82c6f945d2233a4a459bb3d0ec1)。

I3C 规范次版本（Specification Minor Version），即 v1.Y。

<a id="r_gadcd0edb4744d934d9336d82cadd24240"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC 0
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadcd0edb4744d934d9336d82cadd24240)。

MIPI I3C 规范（Specification）。

<a id="r_gadde2bf9d69060283b0ed8ef0a5482739"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_BASIC_SPEC BIT(4)
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_I3C_BASIC_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadde2bf9d69060283b0ed8ef0a5482739)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

MIPI I3C 基础规范（Basic Specification）。

<a id="r_ga8f3f783e104f897cfe0eb13481fc12e3"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_0 0
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8f3f783e104f897cfe0eb13481fc12e3)。

版本（Version）1.Y.0。

<a id="r_ga99a1d9182e5aeeaa7f95c9bbdca377c0"></a>

```c
#define I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_1 BIT(5)
```

相关声明：[I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga99a1d9182e5aeeaa7f95c9bbdca377c0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

版本（Version）1.Y.1 或更高版本。

<a id="define-members-1"></a>

### 设置总线上下文：其他标准组织（Set Bus Context Other Standards Organizations (SETBUSCON)）



<a id="r_ga2d2a926414495bab0eae4f4284a8663b"></a>

```c
#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_JEDEC_SIDEBAND 128
```

相关声明：[I3C_CCC_SETBUSCON_OTHER_STANDARDS_JEDEC_SIDEBAND](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2d2a926414495bab0eae4f4284a8663b)。

JEDEC 边带（Sideband）。

<a id="r_ga7c876c18b2fac71a0377dbb043980644"></a>

```c
#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_MCTP 129
```

相关声明：[I3C_CCC_SETBUSCON_OTHER_STANDARDS_MCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7c876c18b2fac71a0377dbb043980644)。

管理组件传输协议（MCTP）

<a id="r_gaeeb4eea07b5c6c2afea64cf2e09a2d06"></a>

```c
#define I3C_CCC_SETBUSCON_OTHER_STANDARDS_ETSI 130
```

相关声明：[I3C_CCC_SETBUSCON_OTHER_STANDARDS_ETSI](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeeb4eea07b5c6c2afea64cf2e09a2d06)。

欧洲电信标准协会（ETSI）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.3\_枚举（Enumerations）

<a id="r_ga364bcd9863f82fcc13aeb59ca7ad6504"></a>

```c
enum i3c_ccc_enttm_defbyte { ENTTM_EXIT_TEST_MODE = 0x00U , ENTTM_VENDOR_TEST_MODE = 0x01U }
```

相关声明：[i3c_ccc_enttm_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364bcd9863f82fcc13aeb59ca7ad6504)、[ENTTM_EXIT_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207)、[ENTTM_VENDOR_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530)。

ENTTM 的定义字节值（Defining Byte Values）。

<a id="r_ga75934ea02ef8eb1c737da3ebfd368648"></a>

```c
enum i3c_ccc_getstatus_fmt { GETSTATUS_FORMAT_1 , GETSTATUS_FORMAT_2 }
```

相关声明：[i3c_ccc_getstatus_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga75934ea02ef8eb1c737da3ebfd368648)、[GETSTATUS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b)、[GETSTATUS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f)。

指示使用哪种 GETSTATUS 格式（Format）。

<a id="r_ga1977f86d4865a97047119e5b3fbcb172"></a>

```c
enum i3c_ccc_getstatus_defbyte { GETSTATUS_FORMAT_2_TGTSTAT = 0x00U , GETSTATUS_FORMAT_2_PRECR = 0x91U , GETSTATUS_FORMAT_2_INVALID = 0x100U }
```

相关声明：[i3c_ccc_getstatus_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1977f86d4865a97047119e5b3fbcb172)、[GETSTATUS_FORMAT_2_TGTSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb)、[GETSTATUS_FORMAT_2_PRECR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877)、[GETSTATUS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19)。

GETSTATUS 格式 2 的定义字节值（Defining Byte Values）。

<a id="r_ga1a91a7d29fc73ea18b9da614773b475f"></a>

```c
enum i3c_ccc_getmxds_fmt { GETMXDS_FORMAT_1 , GETMXDS_FORMAT_2 , GETMXDS_FORMAT_3 }
```

相关声明：[i3c_ccc_getmxds_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1a91a7d29fc73ea18b9da614773b475f)、[GETMXDS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990)、[GETMXDS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9)、[GETMXDS_FORMAT_3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c)。

指示使用哪种 GETMXDS 格式（Format）。

<a id="r_ga609cbfc817ec24b36c71f75092b2d4bf"></a>

```c
enum i3c_ccc_getmxds_defbyte { GETMXDS_FORMAT_3_WRRDTURN = 0x00U , GETMXDS_FORMAT_3_CRHDLY = 0x91U , GETMXDS_FORMAT_3_INVALID = 0x100 }
```

相关声明：[i3c_ccc_getmxds_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga609cbfc817ec24b36c71f75092b2d4bf)、[GETMXDS_FORMAT_3_WRRDTURN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd)、[GETMXDS_FORMAT_3_CRHDLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7)、[GETMXDS_FORMAT_3_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6)。

I3C 获取最大数据速率（GETMXDS）格式 3 定义字节值（Defining Byte Values）的枚举。

<a id="r_gaa22cc011b619b1819416b0aa26f85958"></a>

```c
enum i3c_ccc_getcaps_fmt { GETCAPS_FORMAT_1 , GETCAPS_FORMAT_2 }
```

相关声明：[i3c_ccc_getcaps_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa22cc011b619b1819416b0aa26f85958)、[GETCAPS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0)、[GETCAPS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620)。

指示使用哪种 GETCAPS 格式（Format）。

<a id="r_gadf1c0363ec0d6db7634cb03bd2d402c2"></a>

```c
enum i3c_ccc_getcaps_defbyte { GETCAPS_FORMAT_2_TGTCAPS = 0x00U , GETCAPS_FORMAT_2_TESTPAT = 0x5AU , GETCAPS_FORMAT_2_CRCAPS = 0x91U , GETCAPS_FORMAT_2_VTCAPS = 0x93U , GETCAPS_FORMAT_2_DBGCAPS = 0xD7U , GETCAPS_FORMAT_2_INVALID = 0x100 }
```

相关声明：[i3c_ccc_getcaps_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadf1c0363ec0d6db7634cb03bd2d402c2)、[GETCAPS_FORMAT_2_TGTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e)、[GETCAPS_FORMAT_2_TESTPAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740)、[GETCAPS_FORMAT_2_CRCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484)、[GETCAPS_FORMAT_2_VTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984)、[GETCAPS_FORMAT_2_DBGCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0)、[GETCAPS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86)。

I3C 获取能力（GETCAPS）格式 2 定义字节值（Defining Byte Values）的枚举。

<a id="r_ga61e1a1945a39b374edee5b75fbeb27d1"></a>

```c
enum i3c_ccc_rstact_defining_byte { I3C_CCC_RSTACT_NO_RESET = 0x00U , I3C_CCC_RSTACT_PERIPHERAL_ONLY = 0x01U , I3C_CCC_RSTACT_RESET_WHOLE_TARGET = 0x02U , I3C_CCC_RSTACT_DEBUG_NETWORK_ADAPTER = 0x03U , I3C_CCC_RSTACT_VIRTUAL_TARGET_DETECT = 0x04U , I3C_CCC_RSTACT_RETURN_TIME_TO_RESET_PERIPHERAL = 0x81U , I3C_CCC_RSTACT_RETURN_TIME_TO_WHOLE_TARGET = 0x82U , I3C_CCC_RSTACT_RETURN_TIME_FOR_DEBUG_NETWORK_ADAPTER_RESET = 0x83U , I3C_CCC_RSTACT_RETURN_VIRTUAL_TARGET_INDICATION = 0x84U }
```

相关声明：[i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)、[I3C_CCC_RSTACT_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2)、[I3C_CCC_RSTACT_PERIPHERAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476)、[I3C_CCC_RSTACT_RESET_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879)、[I3C_CCC_RSTACT_DEBUG_NETWORK_ADAPTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519)、[I3C_CCC_RSTACT_VIRTUAL_TARGET_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e)、[I3C_CCC_RSTACT_RETURN_TIME_TO_RESET_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454)、[I3C_CCC_RSTACT_RETURN_TIME_TO_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95)、[I3C_CCC_RSTACT_RETURN_TIME_FOR_DEBUG_NETWORK_ADAPTER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024)、[I3C_CCC_RSTACT_RETURN_VIRTUAL_TARGET_INDICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4)。

I3C 复位动作（RSTACT）定义字节值（Defining Byte Values）的枚举。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.4\_函数（Functions）

<a id="r_gaaf692d0b89fd62a61d93f1577b25ce25"></a>

```c
static bool i3c_ccc_is_payload_broadcast (const struct i3c_ccc_payload *payload)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_ccc_is_payload_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaf692d0b89fd62a61d93f1577b25ce25)、[i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)。

检查 I3C 通用命令码（CCC）载荷是否用于广播（Broadcast）。

<a id="r_ga7d5bb9c8fd88721b858180f503c1af4c"></a>

```c
int i3c_ccc_do_getbcr (struct i3c_device_desc *target, struct i3c_ccc_getbcr *bcr)
```

相关声明：[i3c_ccc_do_getbcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7d5bb9c8fd88721b858180f503c1af4c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getbcr](../hardware/P412_I3C总线特征返回数据.md)。

从目标端获取总线特征寄存器（BCR）。

<a id="r_ga7f886c0dbe0afec07f5678b574dc1101"></a>

```c
int i3c_ccc_do_getdcr (struct i3c_device_desc *target, struct i3c_ccc_getdcr *dcr)
```

相关声明：[i3c_ccc_do_getdcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7f886c0dbe0afec07f5678b574dc1101)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getdcr](../hardware/P413_I3C设备特征返回数据.md)。

从目标端获取设备特征寄存器（DCR）。

<a id="r_ga949810a9a7c862d00ce4eec7e2c4d7df"></a>

```c
int i3c_ccc_do_getpid (struct i3c_device_desc *target, struct i3c_ccc_getpid *pid)
```

相关声明：[i3c_ccc_do_getpid](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga949810a9a7c862d00ce4eec7e2c4d7df)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getpid](../hardware/P414_I3C预置标识返回数据.md)。

从目标端获取预置 ID（PID）。

<a id="r_ga40294e43357f46338a6542f9a03d7ce7"></a>

```c
int i3c_ccc_do_rstact_all (const struct device *controller, enum i3c_ccc_rstact_defining_byte action)
```

相关声明：[i3c_ccc_do_rstact_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga40294e43357f46338a6542f9a03d7ce7)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)。

广播 RSTACT，以复位 I3C 外设（Peripheral），格式 1。

<a id="r_ga8a74bb1b461c6a4cad12220db55d6d7a"></a>

```c
int i3c_ccc_do_rstact (const struct i3c_device_desc *target, enum i3c_ccc_rstact_defining_byte action, bool get, uint8_t *data)
```

相关声明：[i3c_ccc_do_rstact](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8a74bb1b461c6a4cad12220db55d6d7a)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向单个目标端发送 RSTACT，以复位 I3C 外设（Peripheral）。

<a id="r_gad8a5fcaa2dd494f20795ee716ebf0895"></a>

```c
static int i3c_ccc_do_rstact_fmt2 (const struct i3c_device_desc *target, enum i3c_ccc_rstact_defining_byte action)
```

相关声明：[i3c_ccc_do_rstact_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad8a5fcaa2dd494f20795ee716ebf0895)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)。

向单个目标端发送 RSTACT，以复位 I3C 外设（Peripheral），格式 2。

<a id="r_gaf26a8d605ec5d0e95d6ee1f90571946d"></a>

```c
static int i3c_ccc_do_rstact_fmt3 (const struct i3c_device_desc *target, enum i3c_ccc_rstact_defining_byte action, uint8_t *data)
```

相关声明：[i3c_ccc_do_rstact_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf26a8d605ec5d0e95d6ee1f90571946d)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

向单个目标端发送 RSTACT，以复位 I3C 外设（Peripheral），格式 3。

<a id="r_gac8bdf8d14db5e7fd06846637253cbb76"></a>

```c
int i3c_ccc_do_rstdaa (struct i3c_device_desc *target)
```

相关声明：[i3c_ccc_do_rstdaa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac8bdf8d14db5e7fd06846637253cbb76)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

复位目标端的动态地址（Dynamic Addresses）。

<a id="r_gab1102467bb92a2aff7c9c1a66dd273a7"></a>

```c
int i3c_ccc_do_rstdaa_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_rstdaa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab1102467bb92a2aff7c9c1a66dd273a7)、[device](../device_reference/P002_设备对象结构.md)。

广播 RSTDAA，以复位所有目标端的动态地址（Dynamic Addresses）。

<a id="r_gaf4836548527c1a7fe54767c2a7e2ebb9"></a>

```c
int i3c_ccc_do_setdasa (const struct i3c_device_desc *target, struct i3c_ccc_address da)
```

相关声明：[i3c_ccc_do_setdasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf4836548527c1a7fe54767c2a7e2ebb9)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)。

根据目标端的静态地址设置动态地址（Set Dynamic Address from Static Address）。

<a id="r_ga6d19dc9d3b421b4c936c6183977c4eec"></a>

```c
int i3c_ccc_do_setnewda (const struct i3c_device_desc *target, struct i3c_ccc_address new_da)
```

相关声明：[i3c_ccc_do_setnewda](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6d19dc9d3b421b4c936c6183977c4eec)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)。

为目标端设置新动态地址（Set New Dynamic Address）。

<a id="r_gaf5fbaf2108053df855c95233181dc580"></a>

```c
int i3c_ccc_do_events_all_set (const struct device *controller, bool enable, struct i3c_ccc_events *events)
```

相关声明：[i3c_ccc_do_events_all_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5fbaf2108053df855c95233181dc580)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_ccc_events](../hardware/P411_I3C通用命令事件.md)。

广播 ENEC／DISEC，以使能／禁用目标端事件（Target Events）。

<a id="r_gaf6575647b4b8f858f90bf2785a0f0d49"></a>

```c
int i3c_ccc_do_events_set (struct i3c_device_desc *target, bool enable, struct i3c_ccc_events *events)
```

相关声明：[i3c_ccc_do_events_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6575647b4b8f858f90bf2785a0f0d49)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_ccc_events](../hardware/P411_I3C通用命令事件.md)。

发送定向 CCC ENEC／DISEC，以使能／禁用目标端事件（Target Events）。

<a id="r_ga66ffb47bf3dcf53c31fbbf6fd451a221"></a>

```c
int i3c_ccc_do_entas (const struct i3c_device_desc *target, uint8_t as)
```

相关声明：[i3c_ccc_do_entas](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66ffb47bf3dcf53c31fbbf6fd451a221)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

发送定向 ENTAS，以设置活动状态（Activity State）。

<a id="r_gab5bb29579181747c1b7e1eafa98160e6"></a>

```c
static int i3c_ccc_do_entas0 (const struct i3c_device_desc *target)
```

相关声明：[i3c_ccc_do_entas0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab5bb29579181747c1b7e1eafa98160e6)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

定向命令（Direct）：ENTAS0。

<a id="r_ga600409049ad66072d94d39623977c137"></a>

```c
static int i3c_ccc_do_entas1 (const struct i3c_device_desc *target)
```

相关声明：[i3c_ccc_do_entas1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga600409049ad66072d94d39623977c137)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

定向命令（Direct）：ENTAS1。

<a id="r_gaeb58d2e7c779ae8e07b185f9fa290a9b"></a>

```c
static int i3c_ccc_do_entas2 (const struct i3c_device_desc *target)
```

相关声明：[i3c_ccc_do_entas2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeb58d2e7c779ae8e07b185f9fa290a9b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

定向命令（Direct）：ENTAS2。

<a id="r_ga35bf3fe8816d9fce44d70c8a3c8f69cb"></a>

```c
static int i3c_ccc_do_entas3 (const struct i3c_device_desc *target)
```

相关声明：[i3c_ccc_do_entas3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga35bf3fe8816d9fce44d70c8a3c8f69cb)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

定向命令（Direct）：ENTAS3。

<a id="r_gaa14442ecb3768cb4c3c435c0c1138778"></a>

```c
int i3c_ccc_do_entas_all (const struct device *controller, uint8_t as)
```

相关声明：[i3c_ccc_do_entas_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa14442ecb3768cb4c3c435c0c1138778)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播 ENTAS，以设置活动状态（Activity State）。

<a id="r_ga0d4c999391fca23598a4339b6c9d4ad6"></a>

```c
static int i3c_ccc_do_entas0_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_entas0_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0d4c999391fca23598a4339b6c9d4ad6)、[device](../device_reference/P002_设备对象结构.md)。

广播（Broadcast）：ENTAS0。

<a id="r_ga93b5f2cf21cf7a201bf76e3d665fc40f"></a>

```c
static int i3c_ccc_do_entas1_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_entas1_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga93b5f2cf21cf7a201bf76e3d665fc40f)、[device](../device_reference/P002_设备对象结构.md)。

广播（Broadcast）：ENTAS1。

<a id="r_gacf89ee65aafdcab713f30c8e2675e58b"></a>

```c
static int i3c_ccc_do_entas2_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_entas2_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gacf89ee65aafdcab713f30c8e2675e58b)、[device](../device_reference/P002_设备对象结构.md)。

广播（Broadcast）：ENTAS2。

<a id="r_gaeecb153a2cb3bdc196d00fb60c3e3b24"></a>

```c
static int i3c_ccc_do_entas3_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_entas3_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeecb153a2cb3bdc196d00fb60c3e3b24)、[device](../device_reference/P002_设备对象结构.md)。

广播（Broadcast）：ENTAS3。

<a id="r_ga66c8c6318134d6287f4a14f6c31af02d"></a>

```c
int i3c_ccc_do_setmwl_all (const struct device *controller, const struct i3c_ccc_mwl *mwl)
```

相关声明：[i3c_ccc_do_setmwl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66c8c6318134d6287f4a14f6c31af02d)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)。

广播 SETMWL，以设置最大写入长度（Maximum Write Length）。

<a id="r_gab3de109c73dd58f6d2cf0a9229408f49"></a>

```c
int i3c_ccc_do_setmwl (const struct i3c_device_desc *target, const struct i3c_ccc_mwl *mwl)
```

相关声明：[i3c_ccc_do_setmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3de109c73dd58f6d2cf0a9229408f49)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)。

向单个目标端发送 SETMWL，以设置最大写入长度（Maximum Write Length）。

<a id="r_gaf1077e3d6cf8a7e1f0e02e985058e507"></a>

```c
int i3c_ccc_do_getmwl (const struct i3c_device_desc *target, struct i3c_ccc_mwl *mwl)
```

相关声明：[i3c_ccc_do_getmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf1077e3d6cf8a7e1f0e02e985058e507)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)。

向单个目标端发送 GETMWL，以获取最大写入长度（Maximum Write Length）。

<a id="r_ga2542f4ebcc0c2bb31bc8e334955620b0"></a>

```c
int i3c_ccc_do_setmrl_all (const struct device *controller, const struct i3c_ccc_mrl *mrl, bool has_ibi_size)
```

相关声明：[i3c_ccc_do_setmrl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2542f4ebcc0c2bb31bc8e334955620b0)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

广播 SETMRL，以设置最大读取长度（Maximum Read Length）。

<a id="r_ga6e4f26d23919a619c89624b15d16390a"></a>

```c
int i3c_ccc_do_setmrl (const struct i3c_device_desc *target, const struct i3c_ccc_mrl *mrl)
```

相关声明：[i3c_ccc_do_setmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6e4f26d23919a619c89624b15d16390a)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)。

向单个目标端发送 SETMRL，以设置最大读取长度（Maximum Read Length）。

<a id="r_gac4331a4c7dbb7af0eaea63b01bb08485"></a>

```c
int i3c_ccc_do_getmrl (const struct i3c_device_desc *target, struct i3c_ccc_mrl *mrl)
```

相关声明：[i3c_ccc_do_getmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac4331a4c7dbb7af0eaea63b01bb08485)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)。

向单个目标端发送 GETMRL，以获取最大读取长度（Maximum Read Length）。

<a id="r_ga5c1b2aa3b5915db2540a1affb17a4f10"></a>

```c
int i3c_ccc_do_enttm (const struct device *controller, enum i3c_ccc_enttm_defbyte defbyte)
```

相关声明：[i3c_ccc_do_enttm](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5c1b2aa3b5915db2540a1affb17a4f10)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_enttm_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364bcd9863f82fcc13aeb59ca7ad6504)。

广播（Broadcast）：ENTTM。

<a id="r_ga4fe9d056a5ac78ff83513763a71c7dfe"></a>

```c
int i3c_ccc_do_getstatus (const struct i3c_device_desc *target, union i3c_ccc_getstatus *status, enum i3c_ccc_getstatus_fmt fmt, enum i3c_ccc_getstatus_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getstatus](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4fe9d056a5ac78ff83513763a71c7dfe)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)、[i3c_ccc_getstatus_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga75934ea02ef8eb1c737da3ebfd368648)、[i3c_ccc_getstatus_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1977f86d4865a97047119e5b3fbcb172)。

向单个目标端发送 GETSTATUS，以获取目标端状态（Target Status）。

<a id="r_ga1cb2804fc7dcbb322cd26001d7953c95"></a>

```c
static int i3c_ccc_do_getstatus_fmt1 (const struct i3c_device_desc *target, union i3c_ccc_getstatus *status)
```

相关声明：[i3c_ccc_do_getstatus_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1cb2804fc7dcbb322cd26001d7953c95)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)。

向单个目标端发送 GETSTATUS，以获取目标端状态（Target Status），格式 1。

<a id="r_ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb"></a>

```c
static int i3c_ccc_do_getstatus_fmt2 (const struct i3c_device_desc *target, union i3c_ccc_getstatus *status, enum i3c_ccc_getstatus_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getstatus_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)、[i3c_ccc_getstatus_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1977f86d4865a97047119e5b3fbcb172)。

向单个目标端发送 GETSTATUS，以获取目标端状态（Target Status），格式 2。

<a id="r_ga94df3bbf8d0de54edd57e2ab4d44474e"></a>

```c
int i3c_ccc_do_getcaps (const struct i3c_device_desc *target, union i3c_ccc_getcaps *caps, enum i3c_ccc_getcaps_fmt fmt, enum i3c_ccc_getcaps_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getcaps](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga94df3bbf8d0de54edd57e2ab4d44474e)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)、[i3c_ccc_getcaps_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa22cc011b619b1819416b0aa26f85958)、[i3c_ccc_getcaps_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadf1c0363ec0d6db7634cb03bd2d402c2)。

向单个目标端发送 GETCAPS，以获取目标端状态（Target Status）。译注：原文此处使用“状态”，命令名称及后续格式说明则为获取能力（Capabilities）；此处保留原文措辞。

<a id="r_gaeca8e7c74ee867cdeedf586f5af07a89"></a>

```c
static int i3c_ccc_do_getcaps_fmt1 (const struct i3c_device_desc *target, union i3c_ccc_getcaps *caps)
```

相关声明：[i3c_ccc_do_getcaps_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeca8e7c74ee867cdeedf586f5af07a89)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)。

向单个目标端发送 GETCAPS，以获取能力（Capabilities），格式 1。

<a id="r_gaaa684ac58000e05316eac016a7f048cd"></a>

```c
static int i3c_ccc_do_getcaps_fmt2 (const struct i3c_device_desc *target, union i3c_ccc_getcaps *caps, enum i3c_ccc_getcaps_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getcaps_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaa684ac58000e05316eac016a7f048cd)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)、[i3c_ccc_getcaps_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadf1c0363ec0d6db7634cb03bd2d402c2)。

向单个目标端发送 GETCAPS，以获取能力（Capabilities），格式 2。

<a id="r_ga72e76917e96f8ac572c42c6598f3bce4"></a>

```c
int i3c_ccc_do_setvendor (const struct i3c_device_desc *target, uint8_t id, uint8_t *payload, size_t len)
```

相关声明：[i3c_ccc_do_setvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga72e76917e96f8ac572c42c6598f3bce4)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

针对单个目标端设置厂商／标准扩展通用命令码（Vendor/Standard Extension CCC）。

<a id="r_ga2a1786ee4a809b50dad7e1d42c9afb0b"></a>

```c
int i3c_ccc_do_getvendor (const struct i3c_device_desc *target, uint8_t id, uint8_t *payload, size_t len, size_t *num_xfer)
```

相关声明：[i3c_ccc_do_getvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2a1786ee4a809b50dad7e1d42c9afb0b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

针对单个目标端获取厂商／标准扩展通用命令码（Vendor/Standard Extension CCC）。

<a id="r_ga4cbdcbc2d991bc1e542a562fdbc2563c"></a>

```c
int i3c_ccc_do_getvendor_defbyte (const struct i3c_device_desc *target, uint8_t id, uint8_t defbyte, uint8_t *payload, size_t len, size_t *num_xfer)
```

相关声明：[i3c_ccc_do_getvendor_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4cbdcbc2d991bc1e542a562fdbc2563c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

针对单个目标端获取带定义字节（Defining Byte）的厂商／标准扩展通用命令码（CCC）。

<a id="r_ga7ce52b4e19f3721e3b054455be42e3d0"></a>

```c
int i3c_ccc_do_setvendor_all (const struct device *controller, uint8_t id, uint8_t *payload, size_t len)
```

相关声明：[i3c_ccc_do_setvendor_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7ce52b4e19f3721e3b054455be42e3d0)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

广播设置厂商／标准扩展通用命令码（Vendor/Standard Extension CCC）。

<a id="r_gab3c93ba0a6e606508a59e65c931dd144"></a>

```c
int i3c_ccc_do_setaasa_all (const struct device *controller)
```

相关声明：[i3c_ccc_do_setaasa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3c93ba0a6e606508a59e65c931dd144)、[device](../device_reference/P002_设备对象结构.md)。

广播 SETAASA，将所有目标端的动态地址（Dynamic Address）设为其静态地址（Static Address）。

<a id="r_ga6949426eaf9c3a30dc402e2e11da1dcd"></a>

```c
int i3c_ccc_do_getmxds (const struct i3c_device_desc *target, union i3c_ccc_getmxds *caps, enum i3c_ccc_getmxds_fmt fmt, enum i3c_ccc_getmxds_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getmxds](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6949426eaf9c3a30dc402e2e11da1dcd)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)、[i3c_ccc_getmxds_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1a91a7d29fc73ea18b9da614773b475f)、[i3c_ccc_getmxds_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga609cbfc817ec24b36c71f75092b2d4bf)。

向单个目标端发送 GETMXDS，以获取最大数据速率（Max Data Speed）。

<a id="r_gaa58e1bff5cc9b9e4a32ae4159494125b"></a>

```c
static int i3c_ccc_do_getmxds_fmt1 (const struct i3c_device_desc *target, union i3c_ccc_getmxds *caps)
```

相关声明：[i3c_ccc_do_getmxds_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa58e1bff5cc9b9e4a32ae4159494125b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)。

向单个目标端发送 GETMXDS，以获取最大数据速率（Max Data Speed），格式 1。

<a id="r_ga5a111a0e9ba5037861585d5356d4e950"></a>

```c
static int i3c_ccc_do_getmxds_fmt2 (const struct i3c_device_desc *target, union i3c_ccc_getmxds *caps)
```

相关声明：[i3c_ccc_do_getmxds_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5a111a0e9ba5037861585d5356d4e950)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)。

向单个目标端发送 GETMXDS，以获取最大数据速率（Max Data Speed），格式 2。

<a id="r_ga58a37d7bb50937a936923e3e6b74fc96"></a>

```c
static int i3c_ccc_do_getmxds_fmt3 (const struct i3c_device_desc *target, union i3c_ccc_getmxds *caps, enum i3c_ccc_getmxds_defbyte defbyte)
```

相关声明：[i3c_ccc_do_getmxds_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga58a37d7bb50937a936923e3e6b74fc96)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)、[i3c_ccc_getmxds_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga609cbfc817ec24b36c71f75092b2d4bf)。

向单个目标端发送 GETMXDS，以获取最大数据速率（Max Data Speed），格式 3。

<a id="r_ga0f04a73d8b26b93091108fc55d7a54d3"></a>

```c
int i3c_ccc_do_deftgts_all (const struct device *controller, struct i3c_ccc_deftgts *deftgts)
```

相关声明：[i3c_ccc_do_deftgts_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0f04a73d8b26b93091108fc55d7a54d3)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_deftgts](../hardware/P419_I3C目标清单命令数据.md)。

广播（Broadcast）：DEFTGTS。

<a id="r_ga71e5cbf818b17eb35196ef773b992ed5"></a>

```c
int i3c_ccc_do_setbuscon (const struct device *controller, uint8_t *context, uint16_t length)
```

相关声明：[i3c_ccc_do_setbuscon](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga71e5cbf818b17eb35196ef773b992ed5)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

广播 SETBUSCON，以设置总线上下文（Bus Context）。

<a id="r_ga87c42055b8b03871558df6be56dc1bd6"></a>

```c
int i3c_ccc_do_getacccr (const struct i3c_device_desc *target, struct i3c_ccc_address *handoff_address)
```

相关声明：[i3c_ccc_do_getacccr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga87c42055b8b03871558df6be56dc1bd6)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)。

发送定向 GETACCCR，以进行控制器交接（Controller Handoff）。


## 2.5\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P023_ccc.h_源码浏览.md)
- [i3c_ccc_target_payload](../hardware/P418_I3C通用命令目标载荷.md)
- [i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)
- [i3c_ccc_events](../hardware/P411_I3C通用命令事件.md)
- [i3c_ccc_mwl](../hardware/P416_I3C最大写入长度命令数据.md)
- [i3c_ccc_mrl](../hardware/P415_I3C最大读取长度命令数据.md)
- [i3c_ccc_deftgts_active_controller](../hardware/P420_I3C目标清单活动控制器.md)
- [i3c_ccc_deftgts_target](../hardware/P421_I3C目标清单设备项.md)
- [i3c_ccc_deftgts](../hardware/P419_I3C目标清单命令数据.md)
- [i3c_ccc_address](../hardware/P410_I3C通用命令地址.md)
- [i3c_ccc_getpid](../hardware/P414_I3C预置标识返回数据.md)
- [i3c_ccc_getbcr](../hardware/P412_I3C总线特征返回数据.md)
- [i3c_ccc_getdcr](../hardware/P413_I3C设备特征返回数据.md)
- [i3c_ccc_getstatus](../hardware/P426_I3C状态返回联合体.md)
- [i3c_ccc_setbrgtgt_tgt](../hardware/P423_I3C桥接目标设备项.md)
- [i3c_ccc_setbrgtgt](../hardware/P422_I3C桥接目标命令数据.md)
- [i3c_ccc_getmxds](../hardware/P427_I3C最大速度返回联合体.md)
- [i3c_ccc_getcaps](../hardware/P428_I3C能力返回联合体.md)
- [I3C_CCC_BROADCAST_MAX_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf7b1cbdc790aa1d2c307e1f4ba773ba2)
- [I3C_CCC_ENEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga06fc2296ada6198ab7a00646804ad5ed)
- [I3C_CCC_DISEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8798591746e72a8ae1f901e97d45b810)
- [I3C_CCC_ENTAS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga213102b3a8dbd490b02c3c89843c8d2a)
- [I3C_CCC_ENTAS0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364ce54e30957f7871e56cd82c1f825c)
- [I3C_CCC_ENTAS1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga21c57ce34fe60255c9c8b28dac0a7a85)
- [I3C_CCC_ENTAS2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3adea01f66748ae2b153bf7eb9eab1eb)
- [I3C_CCC_ENTAS3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4dba9093fe562e3d09470610ab393f21)
- [I3C_CCC_RSTDAA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaed94df1e670fc3670970f261865d6f63)
- [I3C_CCC_ENTDAA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad6663cfa56be6bba2187a1d42d64be7b)
- [I3C_CCC_DEFTGTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga17e63ffe790f279a3e6eb8235c936604)
- [I3C_CCC_SETMWL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaab1ccf6cd47dfecee24811501e123802)
- [I3C_CCC_SETMRL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga97fd874b2e6c918f2e1262f7600bfd64)
- [I3C_CCC_ENTTM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gace2b7fc835d31ade916aad3126eb0c6c)
- [I3C_CCC_SETBUSCON](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac0f85a020956e3ee1ae8da899a9e06a6)
- [I3C_CCC_ENDXFER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4f331e7c21f15dd211a70c1a01c49738)
- [I3C_CCC_ENTHDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae213fc68bf723d8f7aee8c41cb9156c3)
- [I3C_CCC_ENTHDR0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae88e44e9469891609ece0b8711162b9d)
- [I3C_CCC_ENTHDR1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae5319f3916df262579ecaac7497ed006)
- [I3C_CCC_ENTHDR2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeff48ef5d76e4ea051f5aee1d1e4fc40)
- [I3C_CCC_ENTHDR3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga24eaa0af83a4a2223f4f84c3c67e05fe)
- [I3C_CCC_ENTHDR4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf15d188164c8fa9c0bf589eb7c5622d0)
- [I3C_CCC_ENTHDR5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaafcad6bfacab1e42f22c8ee941ed6441)
- [I3C_CCC_ENTHDR6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae55615887425917b202818bb0b7c5ac5)
- [I3C_CCC_ENTHDR7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9ab8c02bb5a80913024a43077fb97ffb)
- [I3C_CCC_SETXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4203d5fdd9e9ca253803359934f22524)
- [I3C_CCC_SETAASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae995ef9e94beb26932b47136bdf89b57)
- [I3C_CCC_RSTACT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga424cb224727d33c1ab18e4149bbea232)
- [I3C_CCC_DEFGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga89f8f72a7c7e8c9cb4fe8ece75ad78cf)
- [I3C_CCC_RSTGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga46611eab0c82b74c615a7a7435f79d85)
- [I3C_CCC_MLANE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga290cc5511d95b5be31c2c4cfea929085)
- [I3C_CCC_VENDOR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaee5fb96b2d54df3b1b7aadefd54a608d)
- [I3C_CCC_RSTDAA_DC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3fcf2411223f6c39aab1476ed7e3ac8a)
- [I3C_CCC_SETDASA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga134d5948b056144c83b133f93083a0f8)
- [I3C_CCC_SETNEWDA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0d6d0047f2c6e73e49e5019ec8d9ff0)
- [I3C_CCC_GETMWL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae74935317b7ca471c09b767acf359e34)
- [I3C_CCC_GETMRL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga92e89b1ba719fbb8833c6e32fe4ef1dc)
- [I3C_CCC_GETPID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga04f7386d55742e935fa4dbfeb0120124)
- [I3C_CCC_GETBCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1d7d49ab48098e4c2d5f63bd91d005e1)
- [I3C_CCC_GETDCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga04ab6d4f0b2bf9d7f195132c0959225c)
- [I3C_CCC_GETSTATUS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga858603dfc251b684b9d049b90119993d)
- [I3C_CCC_GETACCCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa6807d3113c9c4d19b6fd27db32b3698)
- [I3C_CCC_SETBRGTGT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3cac5de39903cc2331a38ac66c4ff14)
- [I3C_CCC_GETMXDS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2c078bf24e36689f34ad90979dd5c687)
- [I3C_CCC_GETCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa913844f97ee35405e9bf50c61a161a8)
- [I3C_CCC_SETROUTE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5cf5cdb40299d4f8203b8035dacac17a)
- [I3C_CCC_D2DXFER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa2d86faed4f7c36939ce754be852751a)
- [I3C_CCC_GETXTIME](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66bb5e8027b103298f882f413f8ee6e8)
- [I3C_CCC_SETGRPA](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa0bef5d42c9bf2a21e888e5d5998d5cb)
- [I3C_CCC_ENEC_EVT_ENINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafe40d9b2ccedca40071c47929ff66e65)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [I3C_CCC_ENEC_EVT_ENCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad73e2e9f31f3a02f52b20d77e64671ff)
- [I3C_CCC_ENEC_EVT_ENHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7e705ac95643d0462ac4275eed42153a)
- [I3C_CCC_ENEC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7860289b621c4243401e1df21cd84d66)
- [I3C_CCC_DISEC_EVT_DISINTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6da0458f1ae2d45ae7337cd4e576484)
- [I3C_CCC_DISEC_EVT_DISCR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1f1612a16d2cb68b66f1ca85ba6f450a)
- [I3C_CCC_DISEC_EVT_DISHJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac3ffda84f683f99a0d4e0ad67adfd675)
- [I3C_CCC_DISEC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf177b8fcb7412671a3b8c418336ddde4)
- [I3C_CCC_EVT_INTR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga14cbf3628627f965336ac3740858aeea)
- [I3C_CCC_EVT_CR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad515a978c4912ef0c0444f14e51d8e8f)
- [I3C_CCC_EVT_HJ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaedf65a98d59de51a533ff3d2f8cf075a)
- [I3C_CCC_EVT_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8ff2055f745c4970bd41850bfd5b2aff)
- [I3C_CCC_GETSTATUS_PROTOCOL_ERR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaee3dd61e9ac723a90868c610d0179b7d)
- [I3C_CCC_GETSTATUS_ACTIVITY_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1006146ca810c06674fbee0ee1f66286)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [I3C_CCC_GETSTATUS_ACTIVITY_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga660e179384e9426b498cd62da5665b15)
- [I3C_CCC_GETSTATUS_ACTIVITY_MODE_NCH](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4bf92ca4dd05387b9d10cb256ad3552b)
- [I3C_CCC_GETSTATUS_NUM_INT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0bcc3ea13a34f63b073d63569d2e53a)
- [I3C_CCC_GETSTATUS_NUM_INT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1436dc4b9f71c6f61fd3e3331857f3bd)
- [I3C_CCC_GETSTATUS_PRECR_DEEP_SLEEP_DETECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga94afb0ebcfce55b85fc4a81953b4178a)
- [I3C_CCC_GETSTATUS_PRECR_HANDOFF_DELAY_NACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadda1781cae312f4e588c3d3dcfa74f38)
- [I3C_CCC_GETMXDS_MAX_SDR_FSCL_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga65ed8d5c2e6f562215674217f974d608)
- [I3C_CCC_GETMXDS_MAX_SDR_FSCL_8MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaac6dec9aee1e1d5a56c964a4d1fe32b1)
- [I3C_CCC_GETMXDS_MAX_SDR_FSCL_6MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae1ff27ad2b8c9119e2efa88c0a696555)
- [I3C_CCC_GETMXDS_MAX_SDR_FSCL_4MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga409666d6a17b53e518d702863826eb28)
- [I3C_CCC_GETMXDS_MAX_SDR_FSCL_2MHZ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5a329b3fa12ecafd6958b05bab163a5c)
- [I3C_CCC_GETMXDS_TSCO_8NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad5e417bc3cabf8a915d1e7938415125a)
- [I3C_CCC_GETMXDS_TSCO_9NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaee475f82f3a3759c7d62bb48082ebc2)
- [I3C_CCC_GETMXDS_TSCO_10NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5e264e39aa2d4b602ec5e3218708e2f6)
- [I3C_CCC_GETMXDS_TSCO_11NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2b27c9023f447da9c474c078091cf580)
- [I3C_CCC_GETMXDS_TSCO_12NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga06d33d1884a30d179aace82af956d62d)
- [I3C_CCC_GETMXDS_TSCO_GT_12NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5be034f241ccfb59534ae247d2e31d85)
- [I3C_CCC_GETMXDS_MAXWR_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga43fa03b6fea48cca06d07e962c5c04ef)
- [I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5f4c6dde339c3467bdb3aea0d680d01f)
- [I3C_CCC_GETMXDS_MAXWR_MAX_SDR_FSCL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae61b18d964e575809a1ebe2189aae028)
- [I3C_CCC_GETMXDS_MAXRD_W2R_PERMITS_STOP_BETWEEN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5b95266cc911a37a3e46565b7601970)
- [I3C_CCC_GETMXDS_MAXRD_TSCO_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga41958f7756cc5dec1c0546e7832b764a)
- [I3C_CCC_GETMXDS_MAXRD_TSCO](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8284130d363dd1898de44c572b3d566c)
- [I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad8b14f71cc1d5c1a0daa27703ab0c774)
- [I3C_CCC_GETMXDS_MAXRD_MAX_SDR_FSCL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5ac7364357e1e123adddcbfc134a0be)
- [I3C_CCC_GETMXDS_CRDHLY1_SET_BUS_ACT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9aa4eaf8a537323883d242e9ebb9a985)
- [I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9ad046b7ec49bbca3f70a5a30fb1524b)
- [I3C_CCC_GETMXDS_CRDHLY1_CTRL_HANDOFF_ACT_STATE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab43a5adbcf158086d23c5d796a7e9399)
- [I3C_CCC_GETCAPS1_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab984c6a18a555e4a3c0552684083e330)
- [I3C_CCC_GETCAPS1_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafe33491b778aa806977a98c3bd12a339)
- [I3C_CCC_GETCAPS1_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae9b98ab62745f041e4fe6e89ecd3b0e6)
- [I3C_CCC_GETCAPS1_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaac01f085ed1af56d686a33694744081c)
- [I3C_CCC_GETCAPS1_HDR_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaae9483f4d5de3ba092b870b20e6b5f4a)
- [I3C_CCC_GETCAPS1_HDR_MODE0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad1389fc52c3fec4d6206bc56566bbf5d)
- [I3C_CCC_GETCAPS1_HDR_MODE1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gacfd20baf528fcceca7f71719e15d5ea0)
- [I3C_CCC_GETCAPS1_HDR_MODE2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9e5581743cbbe7363bb0919b95148d85)
- [I3C_CCC_GETCAPS1_HDR_MODE3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga97b146596467f410ce9f063365ac9aaf)
- [I3C_CCC_GETCAPS1_HDR_MODE4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0dd98eeb74f493bfb04aeb698e656772)
- [I3C_CCC_GETCAPS1_HDR_MODE5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga99bff02c40ccb15797dcf10c6dc00e87)
- [I3C_CCC_GETCAPS1_HDR_MODE6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga12cead0a8ceb518a5c897f22b1d3dd64)
- [I3C_CCC_GETCAPS1_HDR_MODE7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8b3373f18c0e3b365cc199c19ae82fb0)
- [I3C_CCC_GETCAPS2_HDRDDR_WRITE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1c2ceeaa44ee641c3d05176baf7e681d)
- [I3C_CCC_GETCAPS2_HDRDDR_ABORT_CRC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8faf5ff5b2542a309f114ce4d6d11640)
- [I3C_CCC_GETCAPS2_GRPADDR_CAP_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga64f58d1aaf847cf4a7811b20cca13b55)
- [I3C_CCC_GETCAPS2_GRPADDR_CAP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gabeb9acdabd6dce2117e9f5830673b2ed)
- [I3C_CCC_GETCAPS2_SPEC_VER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae0015aa7768a8d5c18426a47cdbb67f8)
- [I3C_CCC_GETCAPS2_SPEC_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga093449c1cf029bddf1a25181cbfed570)
- [I3C_CCC_GETCAPS3_MLANE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf0a2358f0f5f46c5fa1c084373f09be1)
- [I3C_CCC_GETCAPS3_D2DXFER_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga08cc3c3976195642282e00ba00c1b283)
- [I3C_CCC_GETCAPS3_D2DXFER_IBI_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga73829cd436decbe55d2290dc750b3918)
- [I3C_CCC_GETCAPS3_GETCAPS_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf40cc6cc08619363056e9650453a9a26)
- [I3C_CCC_GETCAPS3_GETSTATUS_DEFINING_BYTE_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafbf1e9c947c40d70ae1c45991d093570)
- [I3C_CCC_GETCAPS3_HDRBT_CRC32_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3575eb8aa6fc3b49f2115104dcdfaeec)
- [I3C_CCC_GETCAPS3_IBI_MDR_PENDING_READ_NOTIFICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac13d1465aa4222be0acccbf5303f3f3e)
- [I3C_CCC_GETCAPS_TESTPAT1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga541ed236f06c20ca98e32d5a17788754)
- [I3C_CCC_GETCAPS_TESTPAT2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gafdb7ed7cc72efeb7cd62435084b1b40f)
- [I3C_CCC_GETCAPS_TESTPAT3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1720b3f54ade943f627b6a4e7284139a)
- [I3C_CCC_GETCAPS_TESTPAT4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2391e23e0b17351e3c28048b85d98ea6)
- [I3C_CCC_GETCAPS_TESTPAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga98ee1cc4c436219b9639c5710fa6911b)
- [I3C_CCC_GETCAPS_CRCAPS1_HJ_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad833335c6edb018edb66b99e1dfc16f7)
- [I3C_CCC_GETCAPS_CRCAPS1_GRP_MANAGEMENT_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga86b22acbba045b037b4ae14abf4b6e5c)
- [I3C_CCC_GETCAPS_CRCAPS1_ML_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga438621df282f451083e9ab9b1b59a2e3)
- [I3C_CCC_GETCAPS_CRCAPS2_IBI_TIR_SUPPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5bedcb1cb3769ae69779c0b2125b4b21)
- [I3C_CCC_GETCAPS_CRCAPS2_CONTROLLER_PASSBACK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga3a49b8a44676888fe600aa6b42cc52c6)
- [I3C_CCC_GETCAPS_CRCAPS2_DEEP_SLEEP_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad81d9a56d02db7e8a87279d8772adbec)
- [I3C_CCC_GETCAPS_CRCAPS2_DELAYED_CONTROLLER_HANDOFF](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gada1a84b1394d6a72dd49e1c87307fbef)
- [I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga382e8db432a701a8b2f6c8be6aba81a8)
- [I3C_CCC_GETCAPS_VTCAP1_VITRUAL_TARGET_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga9d0153d2e0b01a045e59e4acf4446206)
- [I3C_CCC_GETCAPS_VTCAP1_SIDE_EFFECTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaca37ffb4f223c7b723a1b2ed881d28f7)
- [I3C_CCC_GETCAPS_VTCAP1_SHARED_PERIPH_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad1c0b63bb26be245e781e5d32d75dd15)
- [I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad39e1c3d38b29937166345133ad373d1)
- [I3C_CCC_GETCAPS_VTCAP2_INTERRUPT_REQUESTS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8ee2a538a2b5efa2e02540aac392c685)
- [I3C_CCC_GETCAPS_VTCAP2_ADDRESS_REMAPPING](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1b7562342dbf9fe443386943527d5f29)
- [I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadc61e60fbc59aca1ff813098f51ca56e)
- [I3C_CCC_GETCAPS_VTCAP2_BUS_CONTEXT_AND_COND](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga56112189be57287691d64eabfaa32910)
- [I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gae61d6a25793e701524a5cf82c2593fce)
- [I3C_CCC_SETBUSCON_I3C_SPEC_MINOR_VER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaadcfe82c6f945d2233a4a459bb3d0ec1)
- [I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadcd0edb4744d934d9336d82cadd24240)
- [I3C_CCC_SETBUSCON_I3C_SPEC_I3C_BASIC_SPEC](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadde2bf9d69060283b0ed8ef0a5482739)
- [I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8f3f783e104f897cfe0eb13481fc12e3)
- [I3C_CCC_SETBUSCON_I3C_SPEC_I3C_SPEC_EDITORIAL_1_Y_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga99a1d9182e5aeeaa7f95c9bbdca377c0)
- [I3C_CCC_SETBUSCON_OTHER_STANDARDS_JEDEC_SIDEBAND](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2d2a926414495bab0eae4f4284a8663b)
- [I3C_CCC_SETBUSCON_OTHER_STANDARDS_MCTP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7c876c18b2fac71a0377dbb043980644)
- [I3C_CCC_SETBUSCON_OTHER_STANDARDS_ETSI](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeeb4eea07b5c6c2afea64cf2e09a2d06)
- [i3c_ccc_enttm_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga364bcd9863f82fcc13aeb59ca7ad6504)
- [ENTTM_EXIT_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504a67ee57431fe7b181792507f9ec7d7207)
- [ENTTM_VENDOR_TEST_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga364bcd9863f82fcc13aeb59ca7ad6504aaf523080c395d41aaf0ea5112d93e530)
- [i3c_ccc_getstatus_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga75934ea02ef8eb1c737da3ebfd368648)
- [GETSTATUS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648ae42215e3898baa40cc90e35c5777b57b)
- [GETSTATUS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga75934ea02ef8eb1c737da3ebfd368648a08af2d5d884af32b46b7e0f2f429c68f)
- [i3c_ccc_getstatus_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1977f86d4865a97047119e5b3fbcb172)
- [GETSTATUS_FORMAT_2_TGTSTAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172ac485e9d12c2a4855fd40ddcb6ab938eb)
- [GETSTATUS_FORMAT_2_PRECR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a536a82ce39767e0cd3c25ebc56974877)
- [GETSTATUS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1977f86d4865a97047119e5b3fbcb172a83ccf53b5520866ec71e2c0824347e19)
- [i3c_ccc_getmxds_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1a91a7d29fc73ea18b9da614773b475f)
- [GETMXDS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa76fbd4e41066bf448f2d39f238ade990)
- [GETMXDS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fa1bbc19ae8831c87bc3756bf9d8d587f9)
- [GETMXDS_FORMAT_3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga1a91a7d29fc73ea18b9da614773b475fac4b63e2655bce05f0a02c08599208f0c)
- [i3c_ccc_getmxds_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga609cbfc817ec24b36c71f75092b2d4bf)
- [GETMXDS_FORMAT_3_WRRDTURN](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfad7bea353891962a2942cb0f58fcff2dd)
- [GETMXDS_FORMAT_3_CRHDLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa2b24114d14a6d43638c3a226a13abaf7)
- [GETMXDS_FORMAT_3_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga609cbfc817ec24b36c71f75092b2d4bfa140bcd34752bd931fc44268035a389d6)
- [i3c_ccc_getcaps_fmt](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa22cc011b619b1819416b0aa26f85958)
- [GETCAPS_FORMAT_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a4d5d9ad0745a71bddbea1da09f0b49a0)
- [GETCAPS_FORMAT_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggaa22cc011b619b1819416b0aa26f85958a6bb52959483be5cfc0ddc31f9a574620)
- [i3c_ccc_getcaps_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gadf1c0363ec0d6db7634cb03bd2d402c2)
- [GETCAPS_FORMAT_2_TGTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a494b6a8c368d34d96433041de7e7448e)
- [GETCAPS_FORMAT_2_TESTPAT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ae4cd2f2c4638057ae8fdcceb9d7ba740)
- [GETCAPS_FORMAT_2_CRCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2081a7f62d3175a8b84454daf54f3484)
- [GETCAPS_FORMAT_2_VTCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2ab37ceea59619902ac073183694852984)
- [GETCAPS_FORMAT_2_DBGCAPS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2aaf97763f5fe2819c502e3923501c86d0)
- [GETCAPS_FORMAT_2_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ggadf1c0363ec0d6db7634cb03bd2d402c2a2cd7e3a4d3bce532dfda07e9f9ae8c86)
- [i3c_ccc_rstact_defining_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga61e1a1945a39b374edee5b75fbeb27d1)
- [I3C_CCC_RSTACT_NO_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1aaba42ef747745ca61cf3aa91068fe7c2)
- [I3C_CCC_RSTACT_PERIPHERAL_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a5875b237e23a0a2ad01051ca1d612476)
- [I3C_CCC_RSTACT_RESET_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1af7b7e39dd7a9b214e13f1bdc7f869879)
- [I3C_CCC_RSTACT_DEBUG_NETWORK_ADAPTER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a860a409d86fdb60d9d03df670a724519)
- [I3C_CCC_RSTACT_VIRTUAL_TARGET_DETECT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1ac56441fa6318702856ca6d2ae5ea328e)
- [I3C_CCC_RSTACT_RETURN_TIME_TO_RESET_PERIPHERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a236748388eb84292c65c204b79ae1454)
- [I3C_CCC_RSTACT_RETURN_TIME_TO_WHOLE_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a30d784f66b28d3a3937e136ec1e38d95)
- [I3C_CCC_RSTACT_RETURN_TIME_FOR_DEBUG_NETWORK_ADAPTER_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1adc3e1d5dfe97ba25fdd1d4d270a65024)
- [I3C_CCC_RSTACT_RETURN_VIRTUAL_TARGET_INDICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gga61e1a1945a39b374edee5b75fbeb27d1a0e5a066d008689305ae455bc96b644f4)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [i3c_ccc_is_payload_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaf692d0b89fd62a61d93f1577b25ce25)
- [i3c_ccc_do_getbcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7d5bb9c8fd88721b858180f503c1af4c)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [i3c_ccc_do_getdcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7f886c0dbe0afec07f5678b574dc1101)
- [i3c_ccc_do_getpid](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga949810a9a7c862d00ce4eec7e2c4d7df)
- [i3c_ccc_do_rstact_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga40294e43357f46338a6542f9a03d7ce7)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_ccc_do_rstact](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga8a74bb1b461c6a4cad12220db55d6d7a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_ccc_do_rstact_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gad8a5fcaa2dd494f20795ee716ebf0895)
- [i3c_ccc_do_rstact_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf26a8d605ec5d0e95d6ee1f90571946d)
- [i3c_ccc_do_rstdaa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac8bdf8d14db5e7fd06846637253cbb76)
- [i3c_ccc_do_rstdaa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab1102467bb92a2aff7c9c1a66dd273a7)
- [i3c_ccc_do_setdasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf4836548527c1a7fe54767c2a7e2ebb9)
- [i3c_ccc_do_setnewda](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6d19dc9d3b421b4c936c6183977c4eec)
- [i3c_ccc_do_events_all_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf5fbaf2108053df855c95233181dc580)
- [i3c_ccc_do_events_set](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf6575647b4b8f858f90bf2785a0f0d49)
- [i3c_ccc_do_entas](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66ffb47bf3dcf53c31fbbf6fd451a221)
- [i3c_ccc_do_entas0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab5bb29579181747c1b7e1eafa98160e6)
- [i3c_ccc_do_entas1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga600409049ad66072d94d39623977c137)
- [i3c_ccc_do_entas2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeb58d2e7c779ae8e07b185f9fa290a9b)
- [i3c_ccc_do_entas3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga35bf3fe8816d9fce44d70c8a3c8f69cb)
- [i3c_ccc_do_entas_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa14442ecb3768cb4c3c435c0c1138778)
- [i3c_ccc_do_entas0_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0d4c999391fca23598a4339b6c9d4ad6)
- [i3c_ccc_do_entas1_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga93b5f2cf21cf7a201bf76e3d665fc40f)
- [i3c_ccc_do_entas2_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gacf89ee65aafdcab713f30c8e2675e58b)
- [i3c_ccc_do_entas3_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeecb153a2cb3bdc196d00fb60c3e3b24)
- [i3c_ccc_do_setmwl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga66c8c6318134d6287f4a14f6c31af02d)
- [i3c_ccc_do_setmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3de109c73dd58f6d2cf0a9229408f49)
- [i3c_ccc_do_getmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaf1077e3d6cf8a7e1f0e02e985058e507)
- [i3c_ccc_do_setmrl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2542f4ebcc0c2bb31bc8e334955620b0)
- [i3c_ccc_do_setmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6e4f26d23919a619c89624b15d16390a)
- [i3c_ccc_do_getmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gac4331a4c7dbb7af0eaea63b01bb08485)
- [i3c_ccc_do_enttm](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5c1b2aa3b5915db2540a1affb17a4f10)
- [i3c_ccc_do_getstatus](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4fe9d056a5ac78ff83513763a71c7dfe)
- [i3c_ccc_do_getstatus_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga1cb2804fc7dcbb322cd26001d7953c95)
- [i3c_ccc_do_getstatus_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4eaaaf7b7e9f2f8dd657d4f6a0de8bfb)
- [i3c_ccc_do_getcaps](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga94df3bbf8d0de54edd57e2ab4d44474e)
- [i3c_ccc_do_getcaps_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaeca8e7c74ee867cdeedf586f5af07a89)
- [i3c_ccc_do_getcaps_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaaa684ac58000e05316eac016a7f048cd)
- [i3c_ccc_do_setvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga72e76917e96f8ac572c42c6598f3bce4)
- [i3c_ccc_do_getvendor](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga2a1786ee4a809b50dad7e1d42c9afb0b)
- [i3c_ccc_do_getvendor_defbyte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga4cbdcbc2d991bc1e542a562fdbc2563c)
- [i3c_ccc_do_setvendor_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga7ce52b4e19f3721e3b054455be42e3d0)
- [i3c_ccc_do_setaasa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gab3c93ba0a6e606508a59e65c931dd144)
- [i3c_ccc_do_getmxds](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga6949426eaf9c3a30dc402e2e11da1dcd)
- [i3c_ccc_do_getmxds_fmt1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#gaa58e1bff5cc9b9e4a32ae4159494125b)
- [i3c_ccc_do_getmxds_fmt2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga5a111a0e9ba5037861585d5356d4e950)
- [i3c_ccc_do_getmxds_fmt3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga58a37d7bb50937a936923e3e6b74fc96)
- [i3c_ccc_do_deftgts_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga0f04a73d8b26b93091108fc55d7a54d3)
- [i3c_ccc_do_setbuscon](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga71e5cbf818b17eb35196ef773b992ed5)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [i3c_ccc_do_getacccr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ccc.html#ga87c42055b8b03871558df6be56dc1bd6)

<a id="I3C_CCC_SETBUSCON_I3C_SPEC"></a>
<a id="I3C_CCC_SETBUSCON_OTHER_STANDARDS"></a>

---

[上一章](P001_zephyr__bluetooth__assigned_numbers.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__input__input-event-codes.h_文件参考.md)
