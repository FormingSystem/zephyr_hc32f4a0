---
id: learning.zephyr-docs.api-extension-topic-reference.page-26
title: 平台环境控制接口（PECI）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第26章\_平台环境控制接口（PECI）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

平台环境控制接口（Platform Environment Control Interface，PECI）设备接口。

<a id="details"></a>

平台环境控制接口设备（Platform Environment Control Interface，PECI）的接口。

自 2.1 版提供（Since 2.1）；接口版本（Version）1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 26.1\_主题（Topics）

<a id="r_peci_5Finterface_5Fbackend"></a>

相关声明：[PECI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html)。

<a id="header-files"></a>
<a id="files"></a>

## 26.2\_文件（Files）

<a id="r_peci_2Eh"></a>

```c
file peci.h
```

相关声明：[peci.h](../peripheral_bus_storage_header_reference/P021_zephyr__drivers__peci.h_头文件参考.md)。

平台环境控制接口（Platform Environment Control Interface，PECI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 26.3\_数据结构（Data Structures）

<a id="r_peci_5Fbuf"></a>

```c
struct peci_buf
```

相关声明：[peci_buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md)。

平台环境控制接口（PECI）的缓冲区结构。

<a id="r_peci_5Fmsg"></a>

```c
struct peci_msg
```

相关声明：[peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)。

平台环境控制接口（PECI）的事务数据包格式。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 26.4\_枚举（Enumerations）

<a id="r_ga76ad37d4317b48311cf23cf516549544"></a>

```c
enum peci_error_code { PECI_GENERAL_SENSOR_ERROR = 0x8000 , PECI_UNDERFLOW_SENSOR_ERROR = 0x8002 , PECI_OVERFLOW_SENSOR_ERROR = 0x8003 }
```

相关声明：[peci_error_code](#ga76ad37d4317b48311cf23cf516549544)、[PECI_GENERAL_SENSOR_ERROR](#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f)、[PECI_UNDERFLOW_SENSOR_ERROR](#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41)、[PECI_OVERFLOW_SENSOR_ERROR](#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2)。

PECI 错误码（Error codes）。

<a id="r_gacd243f64973f7bdcc8c999dc14ed2bd6"></a>

```c
enum peci_command_code { PECI_CMD_PING = 0x00 , PECI_CMD_GET_TEMP0 = 0x01 , PECI_CMD_GET_TEMP1 = 0x02 , PECI_CMD_RD_PCI_CFG0 = 0x61 , PECI_CMD_RD_PCI_CFG1 = 0x62 , PECI_CMD_WR_PCI_CFG0 = 0x65 , PECI_CMD_WR_PCI_CFG1 = 0x66 , PECI_CMD_RD_PKG_CFG0 = 0xA1 , PECI_CMD_RD_PKG_CFG1 = 0xA2 , PECI_CMD_WR_PKG_CFG0 = 0xA5 , PECI_CMD_WR_PKG_CFG1 = 0xA6 , PECI_CMD_RD_IAMSR0 = 0xB1 , PECI_CMD_RD_IAMSR1 = 0xB2 , PECI_CMD_WR_IAMSR0 = 0xB5 , PECI_CMD_WR_IAMSR1 = 0xB6 , PECI_CMD_RD_PCI_CFG_LOCAL0 = 0xE1 , PECI_CMD_RD_PCI_CFG_LOCAL1 = 0xE2 , PECI_CMD_WR_PCI_CFG_LOCAL0 = 0xE5 , PECI_CMD_WR_PCI_CFG_LOCAL1 = 0xE6 , PECI_CMD_GET_DIB = 0xF7 }
```

相关声明：[peci_command_code](#gacd243f64973f7bdcc8c999dc14ed2bd6)、[PECI_CMD_PING](#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d)、[PECI_CMD_GET_TEMP0](#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf)、[PECI_CMD_GET_TEMP1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c)、[PECI_CMD_RD_PCI_CFG0](#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d)、[PECI_CMD_RD_PCI_CFG1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa)、[PECI_CMD_WR_PCI_CFG0](#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc)、[PECI_CMD_WR_PCI_CFG1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12)、[PECI_CMD_RD_PKG_CFG0](#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523)、[PECI_CMD_RD_PKG_CFG1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed)、[PECI_CMD_WR_PKG_CFG0](#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55)、[PECI_CMD_WR_PKG_CFG1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95)、[PECI_CMD_RD_IAMSR0](#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10)、[PECI_CMD_RD_IAMSR1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53)、[PECI_CMD_WR_IAMSR0](#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2)、[PECI_CMD_WR_IAMSR1](#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3)、[PECI_CMD_RD_PCI_CFG_LOCAL0](#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5)、[PECI_CMD_RD_PCI_CFG_LOCAL1](#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c)、[PECI_CMD_WR_PCI_CFG_LOCAL0](#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158)、[PECI_CMD_WR_PCI_CFG_LOCAL1](#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd)、[PECI_CMD_GET_DIB](#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8)。

PECI 命令。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 26.5\_函数（Functions）

<a id="r_gaa1fee6839b68eed73f0a8d93b3a3ec82"></a>

```c
int peci_config (const struct device *dev, uint32_t bitrate)
```

相关声明：[peci_config](#gaa1fee6839b68eed73f0a8d93b3a3ec82)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

配置平台环境控制接口（PECI）。

<a id="r_gaa42e2e015a2c778a9eaf2dc1b697630f"></a>

```c
int peci_enable (const struct device *dev)
```

相关声明：[peci_enable](#gaa42e2e015a2c778a9eaf2dc1b697630f)、[device](../device_reference/P002_设备对象结构.md)。

启用 PECI 接口。

<a id="r_gaf197262cd58db5eb7691d1ce816057de"></a>

```c
int peci_disable (const struct device *dev)
```

相关声明：[peci_disable](#gaf197262cd58db5eb7691d1ce816057de)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PECI 接口。

<a id="r_gacf15bdae6483ad3e9498ed984a959687"></a>

```c
int peci_transfer (const struct device *dev, struct peci_msg *msg)
```

相关声明：[peci_transfer](#gacf15bdae6483ad3e9498ed984a959687)、[device](../device_reference/P002_设备对象结构.md)、[peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)。

执行 PECI 事务。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 26.6\_PECI 读写支持的响应（Supported responses）

<a id="r_gaaa72e987f7345168055de5dc4e206d05"></a>

```c
#define PECI_CC_RSP_SUCCESS (0x40U)
```

相关声明：[PECI_CC_RSP_SUCCESS](#gaaa72e987f7345168055de5dc4e206d05)。

<a id="r_ga797ae69ec374fb64bb89f944f6985c6d"></a>

```c
#define PECI_CC_RSP_TIMEOUT (0x80U)
```

相关声明：[PECI_CC_RSP_TIMEOUT](#ga797ae69ec374fb64bb89f944f6985c6d)。

<a id="r_gaac992f1ccc084c3ea5f517cd3fba8271"></a>

```c
#define PECI_CC_OUT_OF_RESOURCES_TIMEOUT (0x81U)
```

相关声明：[PECI_CC_OUT_OF_RESOURCES_TIMEOUT](#gaac992f1ccc084c3ea5f517cd3fba8271)。

<a id="r_gaae8cfb17318fa562c45c797c24e69abe"></a>

```c
#define PECI_CC_RESOURCES_LOWPWR_TIMEOUT (0x82U)
```

相关声明：[PECI_CC_RESOURCES_LOWPWR_TIMEOUT](#gaae8cfb17318fa562c45c797c24e69abe)。

<a id="r_gac26eca50fb7dd2b899ae0e820bbb4412"></a>

```c
#define PECI_CC_ILLEGAL_REQUEST (0x90U)
```

相关声明：[PECI_CC_ILLEGAL_REQUEST](#gac26eca50fb7dd2b899ae0e820bbb4412)。

## 26.7\_Ping 命令格式（Command Format）

<a id="r_ga22a92f0547fd1fe30dd413b071f53d22"></a>

```c
#define PECI_PING_WR_LEN (0U)
```

相关声明：[PECI_PING_WR_LEN](#ga22a92f0547fd1fe30dd413b071f53d22)。

<a id="r_ga28b67489837aa513c987a56cfd2a52ed"></a>

```c
#define PECI_PING_RD_LEN (0U)
```

相关声明：[PECI_PING_RD_LEN](#ga28b67489837aa513c987a56cfd2a52ed)。

<a id="r_ga260b7df883f39c44ac77c0504688fcd4"></a>

```c
#define PECI_PING_LEN (3U)
```

相关声明：[PECI_PING_LEN](#ga260b7df883f39c44ac77c0504688fcd4)。

## 26.8\_GetDIB 命令格式（Command Format）

<a id="r_ga326203908d537fd303b865a32100d45b"></a>

```c
#define PECI_GET_DIB_WR_LEN (1U)
```

相关声明：[PECI_GET_DIB_WR_LEN](#ga326203908d537fd303b865a32100d45b)。

<a id="r_gaa3da9245648157eed5d483dd934b3874"></a>

```c
#define PECI_GET_DIB_RD_LEN (8U)
```

相关声明：[PECI_GET_DIB_RD_LEN](#gaa3da9245648157eed5d483dd934b3874)。

<a id="r_gad7c7732a98738308f4f3f5f4e3cc29ee"></a>

```c
#define PECI_GET_DIB_CMD_LEN (4U)
```

相关声明：[PECI_GET_DIB_CMD_LEN](#gad7c7732a98738308f4f3f5f4e3cc29ee)。

<a id="r_ga679c229499e6669bdf577dad45b51da2"></a>

```c
#define PECI_GET_DIB_DEVINFO (0U)
```

相关声明：[PECI_GET_DIB_DEVINFO](#ga679c229499e6669bdf577dad45b51da2)。

<a id="r_ga83fab6ba4c3ee0df1997b322bc28d986"></a>

```c
#define PECI_GET_DIB_REVNUM (1U)
```

相关声明：[PECI_GET_DIB_REVNUM](#ga83fab6ba4c3ee0df1997b322bc28d986)。

<a id="r_ga4fad3e307b5eee6de75b2e9d5b7c5252"></a>

```c
#define PECI_GET_DIB_DOMAIN_BIT_MASK (0x4U)
```

相关声明：[PECI_GET_DIB_DOMAIN_BIT_MASK](#ga4fad3e307b5eee6de75b2e9d5b7c5252)。

<a id="r_ga56be056f7286d8633a9dcad3904aadc6"></a>

```c
#define PECI_GET_DIB_MAJOR_REV_MASK 0xF0
```

相关声明：[PECI_GET_DIB_MAJOR_REV_MASK](#ga56be056f7286d8633a9dcad3904aadc6)。

<a id="r_gaaaf4e2450fe327826451899458011669"></a>

```c
#define PECI_GET_DIB_MINOR_REV_MASK 0x0F
```

相关声明：[PECI_GET_DIB_MINOR_REV_MASK](#gaaaf4e2450fe327826451899458011669)。

## 26.9\_GetTemp 命令格式（Command Format）

<a id="r_ga782d004f484ba89a2a85552b1367f5e3"></a>

```c
#define PECI_GET_TEMP_WR_LEN (1U)
```

相关声明：[PECI_GET_TEMP_WR_LEN](#ga782d004f484ba89a2a85552b1367f5e3)。

<a id="r_ga8abc4778c30a938b891e45595e1a05bb"></a>

```c
#define PECI_GET_TEMP_RD_LEN (2U)
```

相关声明：[PECI_GET_TEMP_RD_LEN](#ga8abc4778c30a938b891e45595e1a05bb)。

<a id="r_gac9eb9af198bcad988f756e5bbfa610e6"></a>

```c
#define PECI_GET_TEMP_CMD_LEN (4U)
```

相关声明：[PECI_GET_TEMP_CMD_LEN](#gac9eb9af198bcad988f756e5bbfa610e6)。

<a id="r_gac57d46b51397b3f86ab1850e45a14d8d"></a>

```c
#define PECI_GET_TEMP_LSB (0U)
```

相关声明：[PECI_GET_TEMP_LSB](#gac57d46b51397b3f86ab1850e45a14d8d)。

<a id="r_gab10cf44c7f53989d0d3eb7646c7a2ebf"></a>

```c
#define PECI_GET_TEMP_MSB (1U)
```

相关声明：[PECI_GET_TEMP_MSB](#gab10cf44c7f53989d0d3eb7646c7a2ebf)。

<a id="r_ga0a748818ab3e256a372a1444fbbeb4d2"></a>

```c
#define PECI_GET_TEMP_ERR_MSB (0x80U)
```

相关声明：[PECI_GET_TEMP_ERR_MSB](#ga0a748818ab3e256a372a1444fbbeb4d2)。

<a id="r_ga5c8b7afaf9e84ffc289551bf65d27888"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_GENERAL (0x0U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_GENERAL](#ga5c8b7afaf9e84ffc289551bf65d27888)。

<a id="r_ga5fc4196ce832e80a9219ab66b6018b40"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_RES (0x1U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_RES](#ga5fc4196ce832e80a9219ab66b6018b40)。

<a id="r_ga48cdea4c953b8f9f71fc4d38cc9e1b52"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_LO (0x2U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_TEMP_LO](#ga48cdea4c953b8f9f71fc4d38cc9e1b52)。

<a id="r_ga3d13f32e4aa52df7f5a14bfbe7bef310"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_HI (0x3U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_TEMP_HI](#ga3d13f32e4aa52df7f5a14bfbe7bef310)。

## 26.10\_RdPkgConfig 命令格式（Command Format）

<a id="r_ga14c5301c855e0fd6d3e6ce2671ca2630"></a>

```c
#define PECI_RD_PKG_WR_LEN (5U)
```

相关声明：[PECI_RD_PKG_WR_LEN](#ga14c5301c855e0fd6d3e6ce2671ca2630)。

<a id="r_gae73ca3befdbc95c6ed95fa64deca40f2"></a>

```c
#define PECI_RD_PKG_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PKG_LEN_BYTE](#gae73ca3befdbc95c6ed95fa64deca40f2)。

<a id="r_ga8b37ea69eb7194fb68162fabcf47abd4"></a>

```c
#define PECI_RD_PKG_LEN_WORD (3U)
```

相关声明：[PECI_RD_PKG_LEN_WORD](#ga8b37ea69eb7194fb68162fabcf47abd4)。

<a id="r_ga7ffc8df46be38442238e3a1913d80a43"></a>

```c
#define PECI_RD_PKG_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PKG_LEN_DWORD](#ga7ffc8df46be38442238e3a1913d80a43)。

<a id="r_ga617975c279fa6c25d00c3611388c7c87"></a>

```c
#define PECI_RD_PKG_CMD_LEN (8U)
```

相关声明：[PECI_RD_PKG_CMD_LEN](#ga617975c279fa6c25d00c3611388c7c87)。

## 26.11\_WrPkgConfig 命令格式（Command Format）

<a id="r_ga3a48be4c578e26e0425281d8dc45b675"></a>

```c
#define PECI_WR_PKG_RD_LEN (1U)
```

相关声明：[PECI_WR_PKG_RD_LEN](#ga3a48be4c578e26e0425281d8dc45b675)。

<a id="r_ga25a60618673b02a987049d7bf9e0d177"></a>

```c
#define PECI_WR_PKG_LEN_BYTE (7U)
```

相关声明：[PECI_WR_PKG_LEN_BYTE](#ga25a60618673b02a987049d7bf9e0d177)。

<a id="r_ga3b3bb82e32dfb47e642485cd90046805"></a>

```c
#define PECI_WR_PKG_LEN_WORD (8U)
```

相关声明：[PECI_WR_PKG_LEN_WORD](#ga3b3bb82e32dfb47e642485cd90046805)。

<a id="r_gae47cf47f1bacc97b29da8a77754b1856"></a>

```c
#define PECI_WR_PKG_LEN_DWORD (10U)
```

相关声明：[PECI_WR_PKG_LEN_DWORD](#gae47cf47f1bacc97b29da8a77754b1856)。

<a id="r_ga44721cfff04cf37a9dad8e6290efadd8"></a>

```c
#define PECI_WR_PKG_CMD_LEN (9U)
```

相关声明：[PECI_WR_PKG_CMD_LEN](#ga44721cfff04cf37a9dad8e6290efadd8)。

## 26.12\_RdIAMSR 命令格式（Command Format）

<a id="r_ga32a758a9489a4dc40a6f451a33b3873e"></a>

```c
#define PECI_RD_IAMSR_WR_LEN (5U)
```

相关声明：[PECI_RD_IAMSR_WR_LEN](#ga32a758a9489a4dc40a6f451a33b3873e)。

<a id="r_gac1a68fb49b86937dbbcea02a6e38678e"></a>

```c
#define PECI_RD_IAMSR_LEN_BYTE (2U)
```

相关声明：[PECI_RD_IAMSR_LEN_BYTE](#gac1a68fb49b86937dbbcea02a6e38678e)。

<a id="r_gad95974df60609e97652d090aaeb15dbd"></a>

```c
#define PECI_RD_IAMSR_LEN_WORD (3U)
```

相关声明：[PECI_RD_IAMSR_LEN_WORD](#gad95974df60609e97652d090aaeb15dbd)。

<a id="r_gaee3af8380685c9162102439790c43bca"></a>

```c
#define PECI_RD_IAMSR_LEN_DWORD (5U)
```

相关声明：[PECI_RD_IAMSR_LEN_DWORD](#gaee3af8380685c9162102439790c43bca)。

<a id="r_ga6075e0aabf13898467ce99bd32234acd"></a>

```c
#define PECI_RD_IAMSR_LEN_QWORD (9U)
```

相关声明：[PECI_RD_IAMSR_LEN_QWORD](#ga6075e0aabf13898467ce99bd32234acd)。

<a id="r_gaac4377037fe078d06ba711ffd92ece3a"></a>

```c
#define PECI_RD_IAMSR_CMD_LEN (8U)
```

相关声明：[PECI_RD_IAMSR_CMD_LEN](#gaac4377037fe078d06ba711ffd92ece3a)。

## 26.13\_WrIAMSR 命令格式（Command Format）

<a id="r_ga84bac67b2d70a27b029ef58a37b18656"></a>

```c
#define PECI_WR_IAMSR_RD_LEN (1U)
```

相关声明：[PECI_WR_IAMSR_RD_LEN](#ga84bac67b2d70a27b029ef58a37b18656)。

<a id="r_gacff3b7ae6bc7b054a9b14474372a4932"></a>

```c
#define PECI_WR_IAMSR_LEN_BYTE (7U)
```

相关声明：[PECI_WR_IAMSR_LEN_BYTE](#gacff3b7ae6bc7b054a9b14474372a4932)。

<a id="r_ga2a9278a92885a8dc23254ced8e717dee"></a>

```c
#define PECI_WR_IAMSR_LEN_WORD (8U)
```

相关声明：[PECI_WR_IAMSR_LEN_WORD](#ga2a9278a92885a8dc23254ced8e717dee)。

<a id="r_ga0fdcb8d4cddc7f8bf778253f17b8d622"></a>

```c
#define PECI_WR_IAMSR_LEN_DWORD (10U)
```

相关声明：[PECI_WR_IAMSR_LEN_DWORD](#ga0fdcb8d4cddc7f8bf778253f17b8d622)。

<a id="r_gaa53d79877fa3a8df479edae01fdb02cc"></a>

```c
#define PECI_WR_IAMSR_LEN_QWORD (14U)
```

相关声明：[PECI_WR_IAMSR_LEN_QWORD](#gaa53d79877fa3a8df479edae01fdb02cc)。

<a id="r_gaf6743aec8256e30c862470d20401c80b"></a>

```c
#define PECI_WR_IAMSR_CMD_LEN (9U)
```

相关声明：[PECI_WR_IAMSR_CMD_LEN](#gaf6743aec8256e30c862470d20401c80b)。

## 26.14\_RdPCIConfig 命令格式（Command Format）

<a id="r_ga28d95625dca7dcd18009b8a9d1af1b40"></a>

```c
#define PECI_RD_PCICFG_WR_LEN (6U)
```

相关声明：[PECI_RD_PCICFG_WR_LEN](#ga28d95625dca7dcd18009b8a9d1af1b40)。

<a id="r_gae64fc86f4a5dc7ffa4317312eba25ace"></a>

```c
#define PECI_RD_PCICFG_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PCICFG_LEN_BYTE](#gae64fc86f4a5dc7ffa4317312eba25ace)。

<a id="r_gaac909c672633eb8aea767eca556e9684"></a>

```c
#define PECI_RD_PCICFG_LEN_WORD (3U)
```

相关声明：[PECI_RD_PCICFG_LEN_WORD](#gaac909c672633eb8aea767eca556e9684)。

<a id="r_gaee3c84370914cb27509ea9a91ca5f6b9"></a>

```c
#define PECI_RD_PCICFG_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PCICFG_LEN_DWORD](#gaee3c84370914cb27509ea9a91ca5f6b9)。

<a id="r_ga8bec0be2c5762df6a451b322f4652f8a"></a>

```c
#define PECI_RD_PCICFG_CMD_LEN (9U)
```

相关声明：[PECI_RD_PCICFG_CMD_LEN](#ga8bec0be2c5762df6a451b322f4652f8a)。

## 26.15\_WrPCIConfig 命令格式（Command Format）

<a id="r_gac81baf9413648e72cd12c5a0a4afafb1"></a>

```c
#define PECI_WR_PCICFG_RD_LEN (1U)
```

相关声明：[PECI_WR_PCICFG_RD_LEN](#gac81baf9413648e72cd12c5a0a4afafb1)。

<a id="r_ga74d1759fc8b25a191af7a50f929b3ccc"></a>

```c
#define PECI_WR_PCICFG_LEN_BYTE (8U)
```

相关声明：[PECI_WR_PCICFG_LEN_BYTE](#ga74d1759fc8b25a191af7a50f929b3ccc)。

<a id="r_ga94107bc6d6384cac4a93f2dc31d4ff0a"></a>

```c
#define PECI_WR_PCICFG_LEN_WORD (9U)
```

相关声明：[PECI_WR_PCICFG_LEN_WORD](#ga94107bc6d6384cac4a93f2dc31d4ff0a)。

<a id="r_gab2ec9a3f5b1cd095c510b8526ecfb788"></a>

```c
#define PECI_WR_PCICFG_LEN_DWORD (11U)
```

相关声明：[PECI_WR_PCICFG_LEN_DWORD](#gab2ec9a3f5b1cd095c510b8526ecfb788)。

<a id="r_ga431b61c8b4a2e3d12aa681abec3433fa"></a>

```c
#define PECI_WR_PCICFG_CMD_LEN (10U)
```

相关声明：[PECI_WR_PCICFG_CMD_LEN](#ga431b61c8b4a2e3d12aa681abec3433fa)。

## 26.16\_RdPCIConfigLocal 命令格式（Command Format）

<a id="r_ga60ba164ab5036ce14dc2f18daf0c264e"></a>

```c
#define PECI_RD_PCICFGL_WR_LEN (5U)
```

相关声明：[PECI_RD_PCICFGL_WR_LEN](#ga60ba164ab5036ce14dc2f18daf0c264e)。

<a id="r_ga712626f9f7ec395fa0781b3a2f7b5cfb"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_BYTE](#ga712626f9f7ec395fa0781b3a2f7b5cfb)。

<a id="r_ga27dfea893aa66268fcb938152cff4974"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_WORD (3U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_WORD](#ga27dfea893aa66268fcb938152cff4974)。

<a id="r_ga3df08231dc4cec3f8c8706c7a63421d1"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_DWORD](#ga3df08231dc4cec3f8c8706c7a63421d1)。

<a id="r_gaf9fd6d6eefe3133aec4e6ee2d682a238"></a>

```c
#define PECI_RD_PCICFGL_CMD_LEN (8U)
```

相关声明：[PECI_RD_PCICFGL_CMD_LEN](#gaf9fd6d6eefe3133aec4e6ee2d682a238)。

## 26.17\_WrPCIConfigLocal 命令格式（Command Format）

<a id="r_ga8063cf05f9f26b28219e5fece331717d"></a>

```c
#define PECI_WR_PCICFGL_RD_LEN (1U)
```

相关声明：[PECI_WR_PCICFGL_RD_LEN](#ga8063cf05f9f26b28219e5fece331717d)。

<a id="r_gac3cd61027ba11b6a0304c51616e17be9"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_BYTE (7U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_BYTE](#gac3cd61027ba11b6a0304c51616e17be9)。

<a id="r_ga240fcf510dc8f3aae66ca45750b6939f"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_WORD (8U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_WORD](#ga240fcf510dc8f3aae66ca45750b6939f)。

<a id="r_gad33f4be78198ba75fdcde410a5660b39"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_DWORD (10U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_DWORD](#gad33f4be78198ba75fdcde410a5660b39)。

<a id="r_gaa9fcd8acb3578585afbbda38b76e40c3"></a>

```c
#define PECI_WR_PCICFGL_CMD_LEN (9U)
```

相关声明：[PECI_WR_PCICFGL_CMD_LEN](#gaa9fcd8acb3578585afbbda38b76e40c3)。

## 26.18\_详细说明（Detailed Documentation）

<a id="gac26eca50fb7dd2b899ae0e820bbb4412"></a>

### `PECI_CC_ILLEGAL_REQUEST`

```c
#define PECI_CC_ILLEGAL_REQUEST (0x90U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaac992f1ccc084c3ea5f517cd3fba8271"></a>

### `PECI_CC_OUT_OF_RESOURCES_TIMEOUT`

```c
#define PECI_CC_OUT_OF_RESOURCES_TIMEOUT (0x81U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaae8cfb17318fa562c45c797c24e69abe"></a>

### `PECI_CC_RESOURCES_LOWPWR_TIMEOUT`

```c
#define PECI_CC_RESOURCES_LOWPWR_TIMEOUT (0x82U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaaa72e987f7345168055de5dc4e206d05"></a>

### `PECI_CC_RSP_SUCCESS`

```c
#define PECI_CC_RSP_SUCCESS (0x40U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga797ae69ec374fb64bb89f944f6985c6d"></a>

### `PECI_CC_RSP_TIMEOUT`

```c
#define PECI_CC_RSP_TIMEOUT (0x80U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gad7c7732a98738308f4f3f5f4e3cc29ee"></a>

### `PECI_GET_DIB_CMD_LEN`

```c
#define PECI_GET_DIB_CMD_LEN (4U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga679c229499e6669bdf577dad45b51da2"></a>

### `PECI_GET_DIB_DEVINFO`

```c
#define PECI_GET_DIB_DEVINFO (0U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga4fad3e307b5eee6de75b2e9d5b7c5252"></a>

### `PECI_GET_DIB_DOMAIN_BIT_MASK`

```c
#define PECI_GET_DIB_DOMAIN_BIT_MASK (0x4U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga56be056f7286d8633a9dcad3904aadc6"></a>

### `PECI_GET_DIB_MAJOR_REV_MASK`

```c
#define PECI_GET_DIB_MAJOR_REV_MASK 0xF0
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaaaf4e2450fe327826451899458011669"></a>

### `PECI_GET_DIB_MINOR_REV_MASK`

```c
#define PECI_GET_DIB_MINOR_REV_MASK 0x0F
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaa3da9245648157eed5d483dd934b3874"></a>

### `PECI_GET_DIB_RD_LEN`

```c
#define PECI_GET_DIB_RD_LEN (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga83fab6ba4c3ee0df1997b322bc28d986"></a>

### `PECI_GET_DIB_REVNUM`

```c
#define PECI_GET_DIB_REVNUM (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga326203908d537fd303b865a32100d45b"></a>

### `PECI_GET_DIB_WR_LEN`

```c
#define PECI_GET_DIB_WR_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gac9eb9af198bcad988f756e5bbfa610e6"></a>

### `PECI_GET_TEMP_CMD_LEN`

```c
#define PECI_GET_TEMP_CMD_LEN (4U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga5c8b7afaf9e84ffc289551bf65d27888"></a>

### `PECI_GET_TEMP_ERR_LSB_GENERAL`

```c
#define PECI_GET_TEMP_ERR_LSB_GENERAL (0x0U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga5fc4196ce832e80a9219ab66b6018b40"></a>

### `PECI_GET_TEMP_ERR_LSB_RES`

```c
#define PECI_GET_TEMP_ERR_LSB_RES (0x1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga3d13f32e4aa52df7f5a14bfbe7bef310"></a>

### `PECI_GET_TEMP_ERR_LSB_TEMP_HI`

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_HI (0x3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga48cdea4c953b8f9f71fc4d38cc9e1b52"></a>

### `PECI_GET_TEMP_ERR_LSB_TEMP_LO`

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_LO (0x2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga0a748818ab3e256a372a1444fbbeb4d2"></a>

### `PECI_GET_TEMP_ERR_MSB`

```c
#define PECI_GET_TEMP_ERR_MSB (0x80U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gac57d46b51397b3f86ab1850e45a14d8d"></a>

### `PECI_GET_TEMP_LSB`

```c
#define PECI_GET_TEMP_LSB (0U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gab10cf44c7f53989d0d3eb7646c7a2ebf"></a>

### `PECI_GET_TEMP_MSB`

```c
#define PECI_GET_TEMP_MSB (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga8abc4778c30a938b891e45595e1a05bb"></a>

### `PECI_GET_TEMP_RD_LEN`

```c
#define PECI_GET_TEMP_RD_LEN (2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga782d004f484ba89a2a85552b1367f5e3"></a>

### `PECI_GET_TEMP_WR_LEN`

```c
#define PECI_GET_TEMP_WR_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga260b7df883f39c44ac77c0504688fcd4"></a>

### `PECI_PING_LEN`

```c
#define PECI_PING_LEN (3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga28b67489837aa513c987a56cfd2a52ed"></a>

### `PECI_PING_RD_LEN`

```c
#define PECI_PING_RD_LEN (0U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga22a92f0547fd1fe30dd413b071f53d22"></a>

### `PECI_PING_WR_LEN`

```c
#define PECI_PING_WR_LEN (0U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaac4377037fe078d06ba711ffd92ece3a"></a>

### `PECI_RD_IAMSR_CMD_LEN`

```c
#define PECI_RD_IAMSR_CMD_LEN (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gac1a68fb49b86937dbbcea02a6e38678e"></a>

### `PECI_RD_IAMSR_LEN_BYTE`

```c
#define PECI_RD_IAMSR_LEN_BYTE (2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaee3af8380685c9162102439790c43bca"></a>

### `PECI_RD_IAMSR_LEN_DWORD`

```c
#define PECI_RD_IAMSR_LEN_DWORD (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga6075e0aabf13898467ce99bd32234acd"></a>

### `PECI_RD_IAMSR_LEN_QWORD`

```c
#define PECI_RD_IAMSR_LEN_QWORD (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gad95974df60609e97652d090aaeb15dbd"></a>

### `PECI_RD_IAMSR_LEN_WORD`

```c
#define PECI_RD_IAMSR_LEN_WORD (3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga32a758a9489a4dc40a6f451a33b3873e"></a>

### `PECI_RD_IAMSR_WR_LEN`

```c
#define PECI_RD_IAMSR_WR_LEN (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga8bec0be2c5762df6a451b322f4652f8a"></a>

### `PECI_RD_PCICFG_CMD_LEN`

```c
#define PECI_RD_PCICFG_CMD_LEN (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gae64fc86f4a5dc7ffa4317312eba25ace"></a>

### `PECI_RD_PCICFG_LEN_BYTE`

```c
#define PECI_RD_PCICFG_LEN_BYTE (2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaee3c84370914cb27509ea9a91ca5f6b9"></a>

### `PECI_RD_PCICFG_LEN_DWORD`

```c
#define PECI_RD_PCICFG_LEN_DWORD (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaac909c672633eb8aea767eca556e9684"></a>

### `PECI_RD_PCICFG_LEN_WORD`

```c
#define PECI_RD_PCICFG_LEN_WORD (3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga28d95625dca7dcd18009b8a9d1af1b40"></a>

### `PECI_RD_PCICFG_WR_LEN`

```c
#define PECI_RD_PCICFG_WR_LEN (6U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaf9fd6d6eefe3133aec4e6ee2d682a238"></a>

### `PECI_RD_PCICFGL_CMD_LEN`

```c
#define PECI_RD_PCICFGL_CMD_LEN (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga712626f9f7ec395fa0781b3a2f7b5cfb"></a>

### `PECI_RD_PCICFGL_RD_LEN_BYTE`

```c
#define PECI_RD_PCICFGL_RD_LEN_BYTE (2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga3df08231dc4cec3f8c8706c7a63421d1"></a>

### `PECI_RD_PCICFGL_RD_LEN_DWORD`

```c
#define PECI_RD_PCICFGL_RD_LEN_DWORD (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga27dfea893aa66268fcb938152cff4974"></a>

### `PECI_RD_PCICFGL_RD_LEN_WORD`

```c
#define PECI_RD_PCICFGL_RD_LEN_WORD (3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga60ba164ab5036ce14dc2f18daf0c264e"></a>

### `PECI_RD_PCICFGL_WR_LEN`

```c
#define PECI_RD_PCICFGL_WR_LEN (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga617975c279fa6c25d00c3611388c7c87"></a>

### `PECI_RD_PKG_CMD_LEN`

```c
#define PECI_RD_PKG_CMD_LEN (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gae73ca3befdbc95c6ed95fa64deca40f2"></a>

### `PECI_RD_PKG_LEN_BYTE`

```c
#define PECI_RD_PKG_LEN_BYTE (2U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga7ffc8df46be38442238e3a1913d80a43"></a>

### `PECI_RD_PKG_LEN_DWORD`

```c
#define PECI_RD_PKG_LEN_DWORD (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga8b37ea69eb7194fb68162fabcf47abd4"></a>

### `PECI_RD_PKG_LEN_WORD`

```c
#define PECI_RD_PKG_LEN_WORD (3U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga14c5301c855e0fd6d3e6ce2671ca2630"></a>

### `PECI_RD_PKG_WR_LEN`

```c
#define PECI_RD_PKG_WR_LEN (5U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaf6743aec8256e30c862470d20401c80b"></a>

### `PECI_WR_IAMSR_CMD_LEN`

```c
#define PECI_WR_IAMSR_CMD_LEN (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gacff3b7ae6bc7b054a9b14474372a4932"></a>

### `PECI_WR_IAMSR_LEN_BYTE`

```c
#define PECI_WR_IAMSR_LEN_BYTE (7U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga0fdcb8d4cddc7f8bf778253f17b8d622"></a>

### `PECI_WR_IAMSR_LEN_DWORD`

```c
#define PECI_WR_IAMSR_LEN_DWORD (10U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaa53d79877fa3a8df479edae01fdb02cc"></a>

### `PECI_WR_IAMSR_LEN_QWORD`

```c
#define PECI_WR_IAMSR_LEN_QWORD (14U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga2a9278a92885a8dc23254ced8e717dee"></a>

### `PECI_WR_IAMSR_LEN_WORD`

```c
#define PECI_WR_IAMSR_LEN_WORD (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga84bac67b2d70a27b029ef58a37b18656"></a>

### `PECI_WR_IAMSR_RD_LEN`

```c
#define PECI_WR_IAMSR_RD_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga431b61c8b4a2e3d12aa681abec3433fa"></a>

### `PECI_WR_PCICFG_CMD_LEN`

```c
#define PECI_WR_PCICFG_CMD_LEN (10U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga74d1759fc8b25a191af7a50f929b3ccc"></a>

### `PECI_WR_PCICFG_LEN_BYTE`

```c
#define PECI_WR_PCICFG_LEN_BYTE (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gab2ec9a3f5b1cd095c510b8526ecfb788"></a>

### `PECI_WR_PCICFG_LEN_DWORD`

```c
#define PECI_WR_PCICFG_LEN_DWORD (11U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga94107bc6d6384cac4a93f2dc31d4ff0a"></a>

### `PECI_WR_PCICFG_LEN_WORD`

```c
#define PECI_WR_PCICFG_LEN_WORD (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gac81baf9413648e72cd12c5a0a4afafb1"></a>

### `PECI_WR_PCICFG_RD_LEN`

```c
#define PECI_WR_PCICFG_RD_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gaa9fcd8acb3578585afbbda38b76e40c3"></a>

### `PECI_WR_PCICFGL_CMD_LEN`

```c
#define PECI_WR_PCICFGL_CMD_LEN (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga8063cf05f9f26b28219e5fece331717d"></a>

### `PECI_WR_PCICFGL_RD_LEN`

```c
#define PECI_WR_PCICFGL_RD_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gac3cd61027ba11b6a0304c51616e17be9"></a>

### `PECI_WR_PCICFGL_WR_LEN_BYTE`

```c
#define PECI_WR_PCICFGL_WR_LEN_BYTE (7U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gad33f4be78198ba75fdcde410a5660b39"></a>

### `PECI_WR_PCICFGL_WR_LEN_DWORD`

```c
#define PECI_WR_PCICFGL_WR_LEN_DWORD (10U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga240fcf510dc8f3aae66ca45750b6939f"></a>

### `PECI_WR_PCICFGL_WR_LEN_WORD`

```c
#define PECI_WR_PCICFGL_WR_LEN_WORD (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga44721cfff04cf37a9dad8e6290efadd8"></a>

### `PECI_WR_PKG_CMD_LEN`

```c
#define PECI_WR_PKG_CMD_LEN (9U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga25a60618673b02a987049d7bf9e0d177"></a>

### `PECI_WR_PKG_LEN_BYTE`

```c
#define PECI_WR_PKG_LEN_BYTE (7U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gae47cf47f1bacc97b29da8a77754b1856"></a>

### `PECI_WR_PKG_LEN_DWORD`

```c
#define PECI_WR_PKG_LEN_DWORD (10U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga3b3bb82e32dfb47e642485cd90046805"></a>

### `PECI_WR_PKG_LEN_WORD`

```c
#define PECI_WR_PKG_LEN_WORD (8U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="ga3a48be4c578e26e0425281d8dc45b675"></a>

### `PECI_WR_PKG_RD_LEN`

```c
#define PECI_WR_PKG_RD_LEN (1U)
```

```c
#include <zephyr/drivers/peci.h>
```

<a id="gacd243f64973f7bdcc8c999dc14ed2bd6"></a>

### `peci_command_code`

```c
enum peci_command_code
```

```c
#include <zephyr/drivers/peci.h>
```

PECI 命令。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PECI_CMD_PING` |  |
| `PECI_CMD_GET_TEMP0` |  |
| `PECI_CMD_GET_TEMP1` |  |
| `PECI_CMD_RD_PCI_CFG0` |  |
| `PECI_CMD_RD_PCI_CFG1` |  |
| `PECI_CMD_WR_PCI_CFG0` |  |
| `PECI_CMD_WR_PCI_CFG1` |  |
| `PECI_CMD_RD_PKG_CFG0` |  |
| `PECI_CMD_RD_PKG_CFG1` |  |
| `PECI_CMD_WR_PKG_CFG0` |  |
| `PECI_CMD_WR_PKG_CFG1` |  |
| `PECI_CMD_RD_IAMSR0` |  |
| `PECI_CMD_RD_IAMSR1` |  |
| `PECI_CMD_WR_IAMSR0` |  |
| `PECI_CMD_WR_IAMSR1` |  |
| `PECI_CMD_RD_PCI_CFG_LOCAL0` |  |
| `PECI_CMD_RD_PCI_CFG_LOCAL1` |  |
| `PECI_CMD_WR_PCI_CFG_LOCAL0` |  |
| `PECI_CMD_WR_PCI_CFG_LOCAL1` |  |
| `PECI_CMD_GET_DIB` |  |

<a id="ga76ad37d4317b48311cf23cf516549544"></a>

### `peci_error_code`

```c
enum peci_error_code
```

```c
#include <zephyr/drivers/peci.h>
```

PECI 错误码（Error codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `PECI_GENERAL_SENSOR_ERROR` |  |
| `PECI_UNDERFLOW_SENSOR_ERROR` |  |
| `PECI_OVERFLOW_SENSOR_ERROR` |  |

<a id="gaa1fee6839b68eed73f0a8d93b3a3ec82"></a>

### `peci_config()`

```c
int peci_config ( const struct device * dev, uint32_t bitrate )
```

```c
#include <zephyr/drivers/peci.h>
```

配置平台环境控制接口（PECI）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `bitrate` | 所选比特率（Bitrate），以 Kbps 表示。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaf197262cd58db5eb7691d1ce816057de"></a>

### `peci_disable()`

```c
int peci_disable ( const struct device * dev)
```

```c
#include <zephyr/drivers/peci.h>
```

禁用 PECI 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gaa42e2e015a2c778a9eaf2dc1b697630f"></a>

### `peci_enable()`

```c
int peci_enable ( const struct device * dev)
```

```c
#include <zephyr/drivers/peci.h>
```

启用 PECI 接口。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。

<a id="gacf15bdae6483ad3e9498ed984a959687"></a>

### `peci_transfer()`

```c
int peci_transfer ( const struct device * dev, struct peci_msg * msg )
```

```c
#include <zephyr/drivers/peci.h>
```

执行 PECI 事务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 指向驱动实例的设备结构（Device Structure）。 |
| `msg` | 表示 PECI 事务（Transaction）的结构体（Structure）。 |

返回（Returns）：成功时返回0，失败时返回负错误码（Negative errno Value）。


## 26.19\_原页交叉引用（Cross References）

- [PECI 驱动后端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html)
- [peci.h](../peripheral_bus_storage_header_reference/P021_zephyr__drivers__peci.h_头文件参考.md)
- [peci_buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md)
- [peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd"></a>
<a id="ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8"></a>
<a id="gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f"></a>
<a id="gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41"></a>
<a id="gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P025_PCIe 主机精确时间测量（PTM）接口.md) · [返回大纲](大纲.md) · [下一章](P027_瑞萨（Renesas）RA CTSU.md)
