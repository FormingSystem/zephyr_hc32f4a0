---
id: learning.zephyr-docs.peripheral-bus-storage-header-reference.page-21
title: zephyr__drivers__peci.h_头文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/peci_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第21章\_zephyr\_\_drivers\_\_peci.h\_头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

平台环境控制接口（Platform Environment Control Interface，PECI）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <zephyr/types.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/syscalls/peci.h>
```

查看此文件的源码。

平台环境控制接口（Platform Environment Control Interface，PECI）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 21.1\_数据结构（Data Structures）

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

<a id="r_peci_5Fdriver_5Fapi"></a>

```c
struct peci_driver_api
```

相关声明：[peci_driver_api](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md)。

驱动操作（Driver Operations）：平台环境控制接口（PECI）驱动操作。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 21.2\_宏定义（Macros）

<a id="define-members-0"></a>

### PECI 读写支持的响应（Supported responses）

<a id="r_gaaa72e987f7345168055de5dc4e206d05"></a>

```c
#define PECI_CC_RSP_SUCCESS (0x40U)
```

相关声明：[PECI_CC_RSP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaaa72e987f7345168055de5dc4e206d05)。

<a id="r_ga797ae69ec374fb64bb89f944f6985c6d"></a>

```c
#define PECI_CC_RSP_TIMEOUT (0x80U)
```

相关声明：[PECI_CC_RSP_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga797ae69ec374fb64bb89f944f6985c6d)。

<a id="r_gaac992f1ccc084c3ea5f517cd3fba8271"></a>

```c
#define PECI_CC_OUT_OF_RESOURCES_TIMEOUT (0x81U)
```

相关声明：[PECI_CC_OUT_OF_RESOURCES_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac992f1ccc084c3ea5f517cd3fba8271)。

<a id="r_gaae8cfb17318fa562c45c797c24e69abe"></a>

```c
#define PECI_CC_RESOURCES_LOWPWR_TIMEOUT (0x82U)
```

相关声明：[PECI_CC_RESOURCES_LOWPWR_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaae8cfb17318fa562c45c797c24e69abe)。

<a id="r_gac26eca50fb7dd2b899ae0e820bbb4412"></a>

```c
#define PECI_CC_ILLEGAL_REQUEST (0x90U)
```

相关声明：[PECI_CC_ILLEGAL_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac26eca50fb7dd2b899ae0e820bbb4412)。

<a id="define-members-1"></a>

### Ping 命令格式（Command format）

<a id="r_ga22a92f0547fd1fe30dd413b071f53d22"></a>

```c
#define PECI_PING_WR_LEN (0U)
```

相关声明：[PECI_PING_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga22a92f0547fd1fe30dd413b071f53d22)。

<a id="r_ga28b67489837aa513c987a56cfd2a52ed"></a>

```c
#define PECI_PING_RD_LEN (0U)
```

相关声明：[PECI_PING_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga28b67489837aa513c987a56cfd2a52ed)。

<a id="r_ga260b7df883f39c44ac77c0504688fcd4"></a>

```c
#define PECI_PING_LEN (3U)
```

相关声明：[PECI_PING_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga260b7df883f39c44ac77c0504688fcd4)。

<a id="define-members-2"></a>

### GetDIB 命令格式（Command format）

<a id="r_ga326203908d537fd303b865a32100d45b"></a>

```c
#define PECI_GET_DIB_WR_LEN (1U)
```

相关声明：[PECI_GET_DIB_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga326203908d537fd303b865a32100d45b)。

<a id="r_gaa3da9245648157eed5d483dd934b3874"></a>

```c
#define PECI_GET_DIB_RD_LEN (8U)
```

相关声明：[PECI_GET_DIB_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa3da9245648157eed5d483dd934b3874)。

<a id="r_gad7c7732a98738308f4f3f5f4e3cc29ee"></a>

```c
#define PECI_GET_DIB_CMD_LEN (4U)
```

相关声明：[PECI_GET_DIB_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad7c7732a98738308f4f3f5f4e3cc29ee)。

<a id="r_ga679c229499e6669bdf577dad45b51da2"></a>

```c
#define PECI_GET_DIB_DEVINFO (0U)
```

相关声明：[PECI_GET_DIB_DEVINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga679c229499e6669bdf577dad45b51da2)。

<a id="r_ga83fab6ba4c3ee0df1997b322bc28d986"></a>

```c
#define PECI_GET_DIB_REVNUM (1U)
```

相关声明：[PECI_GET_DIB_REVNUM](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga83fab6ba4c3ee0df1997b322bc28d986)。

<a id="r_ga4fad3e307b5eee6de75b2e9d5b7c5252"></a>

```c
#define PECI_GET_DIB_DOMAIN_BIT_MASK (0x4U)
```

相关声明：[PECI_GET_DIB_DOMAIN_BIT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga4fad3e307b5eee6de75b2e9d5b7c5252)。

<a id="r_ga56be056f7286d8633a9dcad3904aadc6"></a>

```c
#define PECI_GET_DIB_MAJOR_REV_MASK 0xF0
```

相关声明：[PECI_GET_DIB_MAJOR_REV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga56be056f7286d8633a9dcad3904aadc6)。

<a id="r_gaaaf4e2450fe327826451899458011669"></a>

```c
#define PECI_GET_DIB_MINOR_REV_MASK 0x0F
```

相关声明：[PECI_GET_DIB_MINOR_REV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaaaf4e2450fe327826451899458011669)。

<a id="define-members-3"></a>

### GetTemp 命令格式（Command format）

<a id="r_ga782d004f484ba89a2a85552b1367f5e3"></a>

```c
#define PECI_GET_TEMP_WR_LEN (1U)
```

相关声明：[PECI_GET_TEMP_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga782d004f484ba89a2a85552b1367f5e3)。

<a id="r_ga8abc4778c30a938b891e45595e1a05bb"></a>

```c
#define PECI_GET_TEMP_RD_LEN (2U)
```

相关声明：[PECI_GET_TEMP_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8abc4778c30a938b891e45595e1a05bb)。

<a id="r_gac9eb9af198bcad988f756e5bbfa610e6"></a>

```c
#define PECI_GET_TEMP_CMD_LEN (4U)
```

相关声明：[PECI_GET_TEMP_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac9eb9af198bcad988f756e5bbfa610e6)。

<a id="r_gac57d46b51397b3f86ab1850e45a14d8d"></a>

```c
#define PECI_GET_TEMP_LSB (0U)
```

相关声明：[PECI_GET_TEMP_LSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac57d46b51397b3f86ab1850e45a14d8d)。

<a id="r_gab10cf44c7f53989d0d3eb7646c7a2ebf"></a>

```c
#define PECI_GET_TEMP_MSB (1U)
```

相关声明：[PECI_GET_TEMP_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gab10cf44c7f53989d0d3eb7646c7a2ebf)。

<a id="r_ga0a748818ab3e256a372a1444fbbeb4d2"></a>

```c
#define PECI_GET_TEMP_ERR_MSB (0x80U)
```

相关声明：[PECI_GET_TEMP_ERR_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga0a748818ab3e256a372a1444fbbeb4d2)。

<a id="r_ga5c8b7afaf9e84ffc289551bf65d27888"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_GENERAL (0x0U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_GENERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga5c8b7afaf9e84ffc289551bf65d27888)。

<a id="r_ga5fc4196ce832e80a9219ab66b6018b40"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_RES (0x1U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga5fc4196ce832e80a9219ab66b6018b40)。

<a id="r_ga48cdea4c953b8f9f71fc4d38cc9e1b52"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_LO (0x2U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_TEMP_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga48cdea4c953b8f9f71fc4d38cc9e1b52)。

<a id="r_ga3d13f32e4aa52df7f5a14bfbe7bef310"></a>

```c
#define PECI_GET_TEMP_ERR_LSB_TEMP_HI (0x3U)
```

相关声明：[PECI_GET_TEMP_ERR_LSB_TEMP_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3d13f32e4aa52df7f5a14bfbe7bef310)。

<a id="define-members-4"></a>

### RdPkgConfig 命令格式（Command format）

<a id="r_ga14c5301c855e0fd6d3e6ce2671ca2630"></a>

```c
#define PECI_RD_PKG_WR_LEN (5U)
```

相关声明：[PECI_RD_PKG_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga14c5301c855e0fd6d3e6ce2671ca2630)。

<a id="r_gae73ca3befdbc95c6ed95fa64deca40f2"></a>

```c
#define PECI_RD_PKG_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PKG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae73ca3befdbc95c6ed95fa64deca40f2)。

<a id="r_ga8b37ea69eb7194fb68162fabcf47abd4"></a>

```c
#define PECI_RD_PKG_LEN_WORD (3U)
```

相关声明：[PECI_RD_PKG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8b37ea69eb7194fb68162fabcf47abd4)。

<a id="r_ga7ffc8df46be38442238e3a1913d80a43"></a>

```c
#define PECI_RD_PKG_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PKG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga7ffc8df46be38442238e3a1913d80a43)。

<a id="r_ga617975c279fa6c25d00c3611388c7c87"></a>

```c
#define PECI_RD_PKG_CMD_LEN (8U)
```

相关声明：[PECI_RD_PKG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga617975c279fa6c25d00c3611388c7c87)。

<a id="define-members-5"></a>

### WrPkgConfig 命令格式（Command format）

<a id="r_ga3a48be4c578e26e0425281d8dc45b675"></a>

```c
#define PECI_WR_PKG_RD_LEN (1U)
```

相关声明：[PECI_WR_PKG_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3a48be4c578e26e0425281d8dc45b675)。

<a id="r_ga25a60618673b02a987049d7bf9e0d177"></a>

```c
#define PECI_WR_PKG_LEN_BYTE (7U)
```

相关声明：[PECI_WR_PKG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga25a60618673b02a987049d7bf9e0d177)。

<a id="r_ga3b3bb82e32dfb47e642485cd90046805"></a>

```c
#define PECI_WR_PKG_LEN_WORD (8U)
```

相关声明：[PECI_WR_PKG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3b3bb82e32dfb47e642485cd90046805)。

<a id="r_gae47cf47f1bacc97b29da8a77754b1856"></a>

```c
#define PECI_WR_PKG_LEN_DWORD (10U)
```

相关声明：[PECI_WR_PKG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae47cf47f1bacc97b29da8a77754b1856)。

<a id="r_ga44721cfff04cf37a9dad8e6290efadd8"></a>

```c
#define PECI_WR_PKG_CMD_LEN (9U)
```

相关声明：[PECI_WR_PKG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga44721cfff04cf37a9dad8e6290efadd8)。

<a id="define-members-6"></a>

### RdIAMSR 命令格式（Command format）

<a id="r_ga32a758a9489a4dc40a6f451a33b3873e"></a>

```c
#define PECI_RD_IAMSR_WR_LEN (5U)
```

相关声明：[PECI_RD_IAMSR_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga32a758a9489a4dc40a6f451a33b3873e)。

<a id="r_gac1a68fb49b86937dbbcea02a6e38678e"></a>

```c
#define PECI_RD_IAMSR_LEN_BYTE (2U)
```

相关声明：[PECI_RD_IAMSR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac1a68fb49b86937dbbcea02a6e38678e)。

<a id="r_gad95974df60609e97652d090aaeb15dbd"></a>

```c
#define PECI_RD_IAMSR_LEN_WORD (3U)
```

相关声明：[PECI_RD_IAMSR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad95974df60609e97652d090aaeb15dbd)。

<a id="r_gaee3af8380685c9162102439790c43bca"></a>

```c
#define PECI_RD_IAMSR_LEN_DWORD (5U)
```

相关声明：[PECI_RD_IAMSR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaee3af8380685c9162102439790c43bca)。

<a id="r_ga6075e0aabf13898467ce99bd32234acd"></a>

```c
#define PECI_RD_IAMSR_LEN_QWORD (9U)
```

相关声明：[PECI_RD_IAMSR_LEN_QWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga6075e0aabf13898467ce99bd32234acd)。

<a id="r_gaac4377037fe078d06ba711ffd92ece3a"></a>

```c
#define PECI_RD_IAMSR_CMD_LEN (8U)
```

相关声明：[PECI_RD_IAMSR_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac4377037fe078d06ba711ffd92ece3a)。

<a id="define-members-7"></a>

### WrIAMSR 命令格式（Command format）

<a id="r_ga84bac67b2d70a27b029ef58a37b18656"></a>

```c
#define PECI_WR_IAMSR_RD_LEN (1U)
```

相关声明：[PECI_WR_IAMSR_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga84bac67b2d70a27b029ef58a37b18656)。

<a id="r_gacff3b7ae6bc7b054a9b14474372a4932"></a>

```c
#define PECI_WR_IAMSR_LEN_BYTE (7U)
```

相关声明：[PECI_WR_IAMSR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacff3b7ae6bc7b054a9b14474372a4932)。

<a id="r_ga2a9278a92885a8dc23254ced8e717dee"></a>

```c
#define PECI_WR_IAMSR_LEN_WORD (8U)
```

相关声明：[PECI_WR_IAMSR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga2a9278a92885a8dc23254ced8e717dee)。

<a id="r_ga0fdcb8d4cddc7f8bf778253f17b8d622"></a>

```c
#define PECI_WR_IAMSR_LEN_DWORD (10U)
```

相关声明：[PECI_WR_IAMSR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga0fdcb8d4cddc7f8bf778253f17b8d622)。

<a id="r_gaa53d79877fa3a8df479edae01fdb02cc"></a>

```c
#define PECI_WR_IAMSR_LEN_QWORD (14U)
```

相关声明：[PECI_WR_IAMSR_LEN_QWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa53d79877fa3a8df479edae01fdb02cc)。

<a id="r_gaf6743aec8256e30c862470d20401c80b"></a>

```c
#define PECI_WR_IAMSR_CMD_LEN (9U)
```

相关声明：[PECI_WR_IAMSR_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf6743aec8256e30c862470d20401c80b)。

<a id="define-members-8"></a>

### RdPCIConfig 命令格式（Command format）

<a id="r_ga28d95625dca7dcd18009b8a9d1af1b40"></a>

```c
#define PECI_RD_PCICFG_WR_LEN (6U)
```

相关声明：[PECI_RD_PCICFG_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga28d95625dca7dcd18009b8a9d1af1b40)。

<a id="r_gae64fc86f4a5dc7ffa4317312eba25ace"></a>

```c
#define PECI_RD_PCICFG_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PCICFG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae64fc86f4a5dc7ffa4317312eba25ace)。

<a id="r_gaac909c672633eb8aea767eca556e9684"></a>

```c
#define PECI_RD_PCICFG_LEN_WORD (3U)
```

相关声明：[PECI_RD_PCICFG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac909c672633eb8aea767eca556e9684)。

<a id="r_gaee3c84370914cb27509ea9a91ca5f6b9"></a>

```c
#define PECI_RD_PCICFG_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PCICFG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaee3c84370914cb27509ea9a91ca5f6b9)。

<a id="r_ga8bec0be2c5762df6a451b322f4652f8a"></a>

```c
#define PECI_RD_PCICFG_CMD_LEN (9U)
```

相关声明：[PECI_RD_PCICFG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8bec0be2c5762df6a451b322f4652f8a)。

<a id="define-members-9"></a>

### WrPCIConfig 命令格式（Command format）

<a id="r_gac81baf9413648e72cd12c5a0a4afafb1"></a>

```c
#define PECI_WR_PCICFG_RD_LEN (1U)
```

相关声明：[PECI_WR_PCICFG_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac81baf9413648e72cd12c5a0a4afafb1)。

<a id="r_ga74d1759fc8b25a191af7a50f929b3ccc"></a>

```c
#define PECI_WR_PCICFG_LEN_BYTE (8U)
```

相关声明：[PECI_WR_PCICFG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga74d1759fc8b25a191af7a50f929b3ccc)。

<a id="r_ga94107bc6d6384cac4a93f2dc31d4ff0a"></a>

```c
#define PECI_WR_PCICFG_LEN_WORD (9U)
```

相关声明：[PECI_WR_PCICFG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga94107bc6d6384cac4a93f2dc31d4ff0a)。

<a id="r_gab2ec9a3f5b1cd095c510b8526ecfb788"></a>

```c
#define PECI_WR_PCICFG_LEN_DWORD (11U)
```

相关声明：[PECI_WR_PCICFG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gab2ec9a3f5b1cd095c510b8526ecfb788)。

<a id="r_ga431b61c8b4a2e3d12aa681abec3433fa"></a>

```c
#define PECI_WR_PCICFG_CMD_LEN (10U)
```

相关声明：[PECI_WR_PCICFG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga431b61c8b4a2e3d12aa681abec3433fa)。

<a id="define-members-10"></a>

### RdPCIConfigLocal 命令格式（Command format）

<a id="r_ga60ba164ab5036ce14dc2f18daf0c264e"></a>

```c
#define PECI_RD_PCICFGL_WR_LEN (5U)
```

相关声明：[PECI_RD_PCICFGL_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga60ba164ab5036ce14dc2f18daf0c264e)。

<a id="r_ga712626f9f7ec395fa0781b3a2f7b5cfb"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_BYTE (2U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga712626f9f7ec395fa0781b3a2f7b5cfb)。

<a id="r_ga27dfea893aa66268fcb938152cff4974"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_WORD (3U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga27dfea893aa66268fcb938152cff4974)。

<a id="r_ga3df08231dc4cec3f8c8706c7a63421d1"></a>

```c
#define PECI_RD_PCICFGL_RD_LEN_DWORD (5U)
```

相关声明：[PECI_RD_PCICFGL_RD_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3df08231dc4cec3f8c8706c7a63421d1)。

<a id="r_gaf9fd6d6eefe3133aec4e6ee2d682a238"></a>

```c
#define PECI_RD_PCICFGL_CMD_LEN (8U)
```

相关声明：[PECI_RD_PCICFGL_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf9fd6d6eefe3133aec4e6ee2d682a238)。

<a id="define-members-11"></a>

### WrPCIConfigLocal 命令格式（Command format）

<a id="r_ga8063cf05f9f26b28219e5fece331717d"></a>

```c
#define PECI_WR_PCICFGL_RD_LEN (1U)
```

相关声明：[PECI_WR_PCICFGL_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8063cf05f9f26b28219e5fece331717d)。

<a id="r_gac3cd61027ba11b6a0304c51616e17be9"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_BYTE (7U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac3cd61027ba11b6a0304c51616e17be9)。

<a id="r_ga240fcf510dc8f3aae66ca45750b6939f"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_WORD (8U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga240fcf510dc8f3aae66ca45750b6939f)。

<a id="r_gad33f4be78198ba75fdcde410a5660b39"></a>

```c
#define PECI_WR_PCICFGL_WR_LEN_DWORD (10U)
```

相关声明：[PECI_WR_PCICFGL_WR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad33f4be78198ba75fdcde410a5660b39)。

<a id="r_gaa9fcd8acb3578585afbbda38b76e40c3"></a>

```c
#define PECI_WR_PCICFGL_CMD_LEN (9U)
```

相关声明：[PECI_WR_PCICFGL_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa9fcd8acb3578585afbbda38b76e40c3)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 21.3\_类型定义（Typedefs）

<a id="r_gabdb55d1aeea952970562c58f7c901361"></a>

```c
typedef int(* peci_config_t) (const struct device *dev, uint32_t bitrate)
```

相关声明：[peci_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#gabdb55d1aeea952970562c58f7c901361)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置 PECI 接口的回调 API。

<a id="r_ga3addf7ae61d89626f7d8889910c6f5b9"></a>

```c
typedef int(* peci_transfer_t) (const struct device *dev, struct peci_msg *msg)
```

相关声明：[peci_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga3addf7ae61d89626f7d8889910c6f5b9)、[device](../device_reference/P002_设备对象结构.md)、[peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)。

执行 PECI 事务的回调 API。

<a id="r_ga97cd68ca4d0b79a6ff8fc19828e0cb76"></a>

```c
typedef int(* peci_disable_t) (const struct device *dev)
```

相关声明：[peci_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga97cd68ca4d0b79a6ff8fc19828e0cb76)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PECI 接口的回调 API。

<a id="r_ga60a85f356ed8f18050f1a4cd02389c77"></a>

```c
typedef int(* peci_enable_t) (const struct device *dev)
```

相关声明：[peci_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga60a85f356ed8f18050f1a4cd02389c77)、[device](../device_reference/P002_设备对象结构.md)。

启用 PECI 接口的回调 API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 21.4\_枚举（Enumerations）

<a id="r_ga76ad37d4317b48311cf23cf516549544"></a>

```c
enum peci_error_code { PECI_GENERAL_SENSOR_ERROR = 0x8000 , PECI_UNDERFLOW_SENSOR_ERROR = 0x8002 , PECI_OVERFLOW_SENSOR_ERROR = 0x8003 }
```

相关声明：[peci_error_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga76ad37d4317b48311cf23cf516549544)、[PECI_GENERAL_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f)、[PECI_UNDERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41)、[PECI_OVERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2)。

PECI 错误码（Error codes）。

<a id="r_gacd243f64973f7bdcc8c999dc14ed2bd6"></a>

```c
enum peci_command_code { PECI_CMD_PING = 0x00 , PECI_CMD_GET_TEMP0 = 0x01 , PECI_CMD_GET_TEMP1 = 0x02 , PECI_CMD_RD_PCI_CFG0 = 0x61 , PECI_CMD_RD_PCI_CFG1 = 0x62 , PECI_CMD_WR_PCI_CFG0 = 0x65 , PECI_CMD_WR_PCI_CFG1 = 0x66 , PECI_CMD_RD_PKG_CFG0 = 0xA1 , PECI_CMD_RD_PKG_CFG1 = 0xA2 , PECI_CMD_WR_PKG_CFG0 = 0xA5 , PECI_CMD_WR_PKG_CFG1 = 0xA6 , PECI_CMD_RD_IAMSR0 = 0xB1 , PECI_CMD_RD_IAMSR1 = 0xB2 , PECI_CMD_WR_IAMSR0 = 0xB5 , PECI_CMD_WR_IAMSR1 = 0xB6 , PECI_CMD_RD_PCI_CFG_LOCAL0 = 0xE1 , PECI_CMD_RD_PCI_CFG_LOCAL1 = 0xE2 , PECI_CMD_WR_PCI_CFG_LOCAL0 = 0xE5 , PECI_CMD_WR_PCI_CFG_LOCAL1 = 0xE6 , PECI_CMD_GET_DIB = 0xF7 }
```

相关声明：[peci_command_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacd243f64973f7bdcc8c999dc14ed2bd6)、[PECI_CMD_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d)、[PECI_CMD_GET_TEMP0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf)、[PECI_CMD_GET_TEMP1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c)、[PECI_CMD_RD_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d)、[PECI_CMD_RD_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa)、[PECI_CMD_WR_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc)、[PECI_CMD_WR_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12)、[PECI_CMD_RD_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523)、[PECI_CMD_RD_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed)、[PECI_CMD_WR_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55)、[PECI_CMD_WR_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95)、[PECI_CMD_RD_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10)、[PECI_CMD_RD_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53)、[PECI_CMD_WR_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2)、[PECI_CMD_WR_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3)、[PECI_CMD_RD_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5)、[PECI_CMD_RD_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c)、[PECI_CMD_WR_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158)、[PECI_CMD_WR_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd)、[PECI_CMD_GET_DIB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8)。

PECI 命令。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 21.5\_函数（Functions）

<a id="r_gaa1fee6839b68eed73f0a8d93b3a3ec82"></a>

```c
int peci_config (const struct device *dev, uint32_t bitrate)
```

相关声明：[peci_config](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa1fee6839b68eed73f0a8d93b3a3ec82)、[device](../device_reference/P002_设备对象结构.md)、[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)。

配置平台环境控制接口（PECI）。

<a id="r_gaa42e2e015a2c778a9eaf2dc1b697630f"></a>

```c
int peci_enable (const struct device *dev)
```

相关声明：[peci_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa42e2e015a2c778a9eaf2dc1b697630f)、[device](../device_reference/P002_设备对象结构.md)。

启用 PECI 接口。

<a id="r_gaf197262cd58db5eb7691d1ce816057de"></a>

```c
int peci_disable (const struct device *dev)
```

相关声明：[peci_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf197262cd58db5eb7691d1ce816057de)、[device](../device_reference/P002_设备对象结构.md)。

禁用 PECI 接口。

<a id="r_gacf15bdae6483ad3e9498ed984a959687"></a>

```c
int peci_transfer (const struct device *dev, struct peci_msg *msg)
```

相关声明：[peci_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacf15bdae6483ad3e9498ed984a959687)、[device](../device_reference/P002_设备对象结构.md)、[peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)。

执行 PECI 事务。


## 21.6\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h_source.html)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码](https://docs.zephyrproject.org/latest/doxygen/html/peci_8h_source.html)
- [peci_buf](../peripheral_bus_storage_model_reference/P066_peci_buf_结构体.md)
- [peci_msg](../peripheral_bus_storage_model_reference/P068_peci_msg_结构体.md)
- [peci_driver_api](../peripheral_bus_storage_model_reference/P067_peci_driver_api_结构体.md)
- [PECI_CC_RSP_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaaa72e987f7345168055de5dc4e206d05)
- [PECI_CC_RSP_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga797ae69ec374fb64bb89f944f6985c6d)
- [PECI_CC_OUT_OF_RESOURCES_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac992f1ccc084c3ea5f517cd3fba8271)
- [PECI_CC_RESOURCES_LOWPWR_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaae8cfb17318fa562c45c797c24e69abe)
- [PECI_CC_ILLEGAL_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac26eca50fb7dd2b899ae0e820bbb4412)
- [PECI_PING_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga22a92f0547fd1fe30dd413b071f53d22)
- [PECI_PING_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga28b67489837aa513c987a56cfd2a52ed)
- [PECI_PING_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga260b7df883f39c44ac77c0504688fcd4)
- [PECI_GET_DIB_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga326203908d537fd303b865a32100d45b)
- [PECI_GET_DIB_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa3da9245648157eed5d483dd934b3874)
- [PECI_GET_DIB_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad7c7732a98738308f4f3f5f4e3cc29ee)
- [PECI_GET_DIB_DEVINFO](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga679c229499e6669bdf577dad45b51da2)
- [PECI_GET_DIB_REVNUM](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga83fab6ba4c3ee0df1997b322bc28d986)
- [PECI_GET_DIB_DOMAIN_BIT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga4fad3e307b5eee6de75b2e9d5b7c5252)
- [PECI_GET_DIB_MAJOR_REV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga56be056f7286d8633a9dcad3904aadc6)
- [PECI_GET_DIB_MINOR_REV_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaaaf4e2450fe327826451899458011669)
- [PECI_GET_TEMP_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga782d004f484ba89a2a85552b1367f5e3)
- [PECI_GET_TEMP_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8abc4778c30a938b891e45595e1a05bb)
- [PECI_GET_TEMP_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac9eb9af198bcad988f756e5bbfa610e6)
- [PECI_GET_TEMP_LSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac57d46b51397b3f86ab1850e45a14d8d)
- [PECI_GET_TEMP_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gab10cf44c7f53989d0d3eb7646c7a2ebf)
- [PECI_GET_TEMP_ERR_MSB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga0a748818ab3e256a372a1444fbbeb4d2)
- [PECI_GET_TEMP_ERR_LSB_GENERAL](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga5c8b7afaf9e84ffc289551bf65d27888)
- [PECI_GET_TEMP_ERR_LSB_RES](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga5fc4196ce832e80a9219ab66b6018b40)
- [PECI_GET_TEMP_ERR_LSB_TEMP_LO](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga48cdea4c953b8f9f71fc4d38cc9e1b52)
- [PECI_GET_TEMP_ERR_LSB_TEMP_HI](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3d13f32e4aa52df7f5a14bfbe7bef310)
- [PECI_RD_PKG_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga14c5301c855e0fd6d3e6ce2671ca2630)
- [PECI_RD_PKG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae73ca3befdbc95c6ed95fa64deca40f2)
- [PECI_RD_PKG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8b37ea69eb7194fb68162fabcf47abd4)
- [PECI_RD_PKG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga7ffc8df46be38442238e3a1913d80a43)
- [PECI_RD_PKG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga617975c279fa6c25d00c3611388c7c87)
- [PECI_WR_PKG_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3a48be4c578e26e0425281d8dc45b675)
- [PECI_WR_PKG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga25a60618673b02a987049d7bf9e0d177)
- [PECI_WR_PKG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3b3bb82e32dfb47e642485cd90046805)
- [PECI_WR_PKG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae47cf47f1bacc97b29da8a77754b1856)
- [PECI_WR_PKG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga44721cfff04cf37a9dad8e6290efadd8)
- [PECI_RD_IAMSR_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga32a758a9489a4dc40a6f451a33b3873e)
- [PECI_RD_IAMSR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac1a68fb49b86937dbbcea02a6e38678e)
- [PECI_RD_IAMSR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad95974df60609e97652d090aaeb15dbd)
- [PECI_RD_IAMSR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaee3af8380685c9162102439790c43bca)
- [PECI_RD_IAMSR_LEN_QWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga6075e0aabf13898467ce99bd32234acd)
- [PECI_RD_IAMSR_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac4377037fe078d06ba711ffd92ece3a)
- [PECI_WR_IAMSR_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga84bac67b2d70a27b029ef58a37b18656)
- [PECI_WR_IAMSR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacff3b7ae6bc7b054a9b14474372a4932)
- [PECI_WR_IAMSR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga2a9278a92885a8dc23254ced8e717dee)
- [PECI_WR_IAMSR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga0fdcb8d4cddc7f8bf778253f17b8d622)
- [PECI_WR_IAMSR_LEN_QWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa53d79877fa3a8df479edae01fdb02cc)
- [PECI_WR_IAMSR_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf6743aec8256e30c862470d20401c80b)
- [PECI_RD_PCICFG_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga28d95625dca7dcd18009b8a9d1af1b40)
- [PECI_RD_PCICFG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gae64fc86f4a5dc7ffa4317312eba25ace)
- [PECI_RD_PCICFG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaac909c672633eb8aea767eca556e9684)
- [PECI_RD_PCICFG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaee3c84370914cb27509ea9a91ca5f6b9)
- [PECI_RD_PCICFG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8bec0be2c5762df6a451b322f4652f8a)
- [PECI_WR_PCICFG_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac81baf9413648e72cd12c5a0a4afafb1)
- [PECI_WR_PCICFG_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga74d1759fc8b25a191af7a50f929b3ccc)
- [PECI_WR_PCICFG_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga94107bc6d6384cac4a93f2dc31d4ff0a)
- [PECI_WR_PCICFG_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gab2ec9a3f5b1cd095c510b8526ecfb788)
- [PECI_WR_PCICFG_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga431b61c8b4a2e3d12aa681abec3433fa)
- [PECI_RD_PCICFGL_WR_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga60ba164ab5036ce14dc2f18daf0c264e)
- [PECI_RD_PCICFGL_RD_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga712626f9f7ec395fa0781b3a2f7b5cfb)
- [PECI_RD_PCICFGL_RD_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga27dfea893aa66268fcb938152cff4974)
- [PECI_RD_PCICFGL_RD_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga3df08231dc4cec3f8c8706c7a63421d1)
- [PECI_RD_PCICFGL_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf9fd6d6eefe3133aec4e6ee2d682a238)
- [PECI_WR_PCICFGL_RD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga8063cf05f9f26b28219e5fece331717d)
- [PECI_WR_PCICFGL_WR_LEN_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gac3cd61027ba11b6a0304c51616e17be9)
- [PECI_WR_PCICFGL_WR_LEN_WORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga240fcf510dc8f3aae66ca45750b6939f)
- [PECI_WR_PCICFGL_WR_LEN_DWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gad33f4be78198ba75fdcde410a5660b39)
- [PECI_WR_PCICFGL_CMD_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa9fcd8acb3578585afbbda38b76e40c3)
- [peci_config_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#gabdb55d1aeea952970562c58f7c901361)
- [device](../device_reference/P002_设备对象结构.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [peci_transfer_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga3addf7ae61d89626f7d8889910c6f5b9)
- [peci_disable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga97cd68ca4d0b79a6ff8fc19828e0cb76)
- [peci_enable_t](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface__backend.html#ga60a85f356ed8f18050f1a4cd02389c77)
- [peci_error_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ga76ad37d4317b48311cf23cf516549544)
- [PECI_GENERAL_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544ae443a31c6771f672eecbdcbc1839215f)
- [PECI_UNDERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544a3444a28dba8e6a5d0eec8a3128e73c41)
- [PECI_OVERFLOW_SENSOR_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gga76ad37d4317b48311cf23cf516549544afd2181728ca4397f39c9d632df015ed2)
- [peci_command_code](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacd243f64973f7bdcc8c999dc14ed2bd6)
- [PECI_CMD_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aeb58e4fba76910717759cb6e2ea7189d)
- [PECI_CMD_GET_TEMP0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6afbb78950e41573a7d0e1e5c4d63e96bf)
- [PECI_CMD_GET_TEMP1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a13c808d7543b5cd45afbefc8eb21611c)
- [PECI_CMD_RD_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6aa38f576d83e4fc3555cd7bffb5c5ce6d)
- [PECI_CMD_RD_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a709af27dd39811f4ee57ee6b9f4675fa)
- [PECI_CMD_WR_PCI_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acb02d1f73e2b9701a108f595763c84bc)
- [PECI_CMD_WR_PCI_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a572da95ca81979ad1444a4bd302c7f12)
- [PECI_CMD_RD_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a4323adb5af1251cb30f3cdffb485b523)
- [PECI_CMD_RD_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a21c9a89c7a6411fc16c0a651d0239fed)
- [PECI_CMD_WR_PKG_CFG0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ac43d5530697b1e3ca0d6dd2b210cbc55)
- [PECI_CMD_WR_PKG_CFG1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a42fe60d1ad58a3182c42217ef3b87a95)
- [PECI_CMD_RD_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ae944a14033aecc7323578cac792b9e10)
- [PECI_CMD_RD_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a6769388430077f82dca456470a76ae53)
- [PECI_CMD_WR_IAMSR0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a31e61a2e884286a53663dfcd932d28a2)
- [PECI_CMD_WR_IAMSR1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6ab1ba81b33438013543b7b61cc34a04b3)
- [PECI_CMD_RD_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a16549485b6fcd531afcda48c323f30a5)
- [PECI_CMD_RD_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6acd12ed51a5dd15b29d82913149775f2c)
- [PECI_CMD_WR_PCI_CFG_LOCAL0](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6af737a18cbf850948594519eacfe33158)
- [PECI_CMD_WR_PCI_CFG_LOCAL1](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a7ddc4229ec37021b78ea50d0cde69cdd)
- [PECI_CMD_GET_DIB](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#ggacd243f64973f7bdcc8c999dc14ed2bd6a000d0e023fd6382fb1a503a3317495d8)
- [peci_config](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa1fee6839b68eed73f0a8d93b3a3ec82)
- [peci_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaa42e2e015a2c778a9eaf2dc1b697630f)
- [peci_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gaf197262cd58db5eb7691d1ce816057de)
- [peci_transfer](https://docs.zephyrproject.org/latest/doxygen/html/group__peci__interface.html#gacf15bdae6483ad3e9498ed984a959687)

<a id="header-details"></a>

---

[上一章](P020_zephyr__mgmt__osdp.h_头文件参考.md) · [返回大纲](大纲.md) · [下一章](P022_zephyr__drivers__ps2.h_头文件参考.md)
