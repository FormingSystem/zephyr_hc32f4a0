---
id: learning.zephyr-docs.api-file-clock-network-reference.page-2
title: zephyr__bluetooth__att.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_bluetooth\_\_att.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/att_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

属性协议（Attribute Protocol）的处理。

<a id="details"></a>

```c
#include <stdint.h>
#include <stddef.h>
#include <zephyr/bluetooth/conn.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/toolchain.h>
```

查看此文件的源码。

属性协议（Attribute Protocol）的处理。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga0032756d54c08d37c101769be8ef2070"></a>

```c
#define BT_ATT_ERR_SUCCESS 0x00
```

相关声明：[BT_ATT_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga0032756d54c08d37c101769be8ef2070)。

属性协议操作（ATT Operation）成功。

<a id="r_gab8d9a6870360f0e5dd7290895202879f"></a>

```c
#define BT_ATT_ERR_INVALID_HANDLE 0x01
```

相关声明：[BT_ATT_ERR_INVALID_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gab8d9a6870360f0e5dd7290895202879f)。

给定属性句柄（Attribute Handle）在服务器上无效。

<a id="r_gac26ed224b7f8fb7717b40fe3a545be7e"></a>

```c
#define BT_ATT_ERR_READ_NOT_PERMITTED 0x02
```

相关声明：[BT_ATT_ERR_READ_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac26ed224b7f8fb7717b40fe3a545be7e)。

属性（Attribute）不可读。

<a id="r_ga2378ff92f5afaff1e4392b1dc2e7326c"></a>

```c
#define BT_ATT_ERR_WRITE_NOT_PERMITTED 0x03
```

相关声明：[BT_ATT_ERR_WRITE_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2378ff92f5afaff1e4392b1dc2e7326c)。

属性（Attribute）不可写。

<a id="r_ga7f1cbe6eb3ed0999bafab729c7b0a6a6"></a>

```c
#define BT_ATT_ERR_INVALID_PDU 0x04
```

相关声明：[BT_ATT_ERR_INVALID_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)。

属性协议数据单元（Attribute PDU）无效。

<a id="r_ga269e711af78a7a30a770b3d7db210c8a"></a>

```c
#define BT_ATT_ERR_AUTHENTICATION 0x05
```

相关声明：[BT_ATT_ERR_AUTHENTICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga269e711af78a7a30a770b3d7db210c8a)。

读写属性之前需要认证（Authentication）。

<a id="r_gafcfa214f6f5b600647886f27cebecb49"></a>

```c
#define BT_ATT_ERR_NOT_SUPPORTED 0x06
```

相关声明：[BT_ATT_ERR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gafcfa214f6f5b600647886f27cebecb49)。

ATT 服务器不支持从客户端收到的请求。

<a id="r_ga997d113b71af6b4019c26ca3893f3dbb"></a>

```c
#define BT_ATT_ERR_INVALID_OFFSET 0x07
```

相关声明：[BT_ATT_ERR_INVALID_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga997d113b71af6b4019c26ca3893f3dbb)。

指定偏移（Offset）超出属性末尾。

<a id="r_ga30b28071d7057c2c68b10da34ba32faf"></a>

```c
#define BT_ATT_ERR_AUTHORIZATION 0x08
```

相关声明：[BT_ATT_ERR_AUTHORIZATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga30b28071d7057c2c68b10da34ba32faf)。

读写属性之前需要授权（Authorization）。

<a id="r_gaa135b2315173e7852afe4e1624169ce2"></a>

```c
#define BT_ATT_ERR_PREPARE_QUEUE_FULL 0x09
```

相关声明：[BT_ATT_ERR_PREPARE_QUEUE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaa135b2315173e7852afe4e1624169ce2)。

队列中的预备写操作（Prepare Writes）过多。

<a id="r_ga5dfcd07918dc665bf600a25608b0736d"></a>

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_FOUND 0x0a
```

相关声明：[BT_ATT_ERR_ATTRIBUTE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga5dfcd07918dc665bf600a25608b0736d)。

在给定属性句柄范围（Attribute Handle Range）内未找到属性。

<a id="r_ga240561711499f11b267d2e5ed8fc99f5"></a>

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_LONG 0x0b
```

相关声明：[BT_ATT_ERR_ATTRIBUTE_NOT_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga240561711499f11b267d2e5ed8fc99f5)。

无法使用 ATT_READ_BLOB_REQ PDU 读取此属性。

<a id="r_ga2ed58d79dfbd701a97377b171f1b0793"></a>

```c
#define BT_ATT_ERR_ENCRYPTION_KEY_SIZE 0x0c
```

相关声明：[BT_ATT_ERR_ENCRYPTION_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2ed58d79dfbd701a97377b171f1b0793)。

用于加密此链路的加密密钥长度（Encryption Key Size）过短。

<a id="r_ga21207d5beb27fe50856f001bd18e1efa"></a>

```c
#define BT_ATT_ERR_INVALID_ATTRIBUTE_LEN 0x0d
```

相关声明：[BT_ATT_ERR_INVALID_ATTRIBUTE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga21207d5beb27fe50856f001bd18e1efa)。

属性值长度（Attribute Value Length）对此操作无效。

<a id="r_ga992baa1f0d763a00f314bdcf59965bdd"></a>

```c
#define BT_ATT_ERR_UNLIKELY 0x0e
```

相关声明：[BT_ATT_ERR_UNLIKELY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga992baa1f0d763a00f314bdcf59965bdd)。

请求的属性操作遇到一个通常不会发生的错误（Unlikely Error）。

<a id="r_ga8a5235e39b05fa85b5b4f4bfb449683b"></a>

```c
#define BT_ATT_ERR_INSUFFICIENT_ENCRYPTION 0x0f
```

相关声明：[BT_ATT_ERR_INSUFFICIENT_ENCRYPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8a5235e39b05fa85b5b4f4bfb449683b)。

读写属性之前需要加密（Encryption）。

<a id="r_ga0611fc39d9d09ea4f0e556b4910f09ed"></a>

```c
#define BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE 0x10
```

相关声明：[BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga0611fc39d9d09ea4f0e556b4910f09ed)。

此属性类型不是受支持的分组属性（Grouping Attribute）。

<a id="r_gaf4a81bc81cad14bf91463d4376a3a868"></a>

```c
#define BT_ATT_ERR_INSUFFICIENT_RESOURCES 0x11
```

相关声明：[BT_ATT_ERR_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaf4a81bc81cad14bf91463d4376a3a868)。

资源不足（Insufficient Resources），无法完成请求。

<a id="r_ga2b9a58bf48f1b76e743cb7fef3aed3a8"></a>

```c
#define BT_ATT_ERR_DB_OUT_OF_SYNC 0x12
```

相关声明：[BT_ATT_ERR_DB_OUT_OF_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2b9a58bf48f1b76e743cb7fef3aed3a8)。

服务器要求客户端重新发现数据库（Rediscover Database）。

<a id="r_ga52ffe5ff2eb092bcdc2ebb05684030d7"></a>

```c
#define BT_ATT_ERR_VALUE_NOT_ALLOWED 0x13
```

相关声明：[BT_ATT_ERR_VALUE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga52ffe5ff2eb092bcdc2ebb05684030d7)。

不允许此属性参数值（Attribute Parameter Value）。

<a id="r_ga8363770d0832f3df8fb1d0a22bc3551e"></a>

```c
#define BT_ATT_ERR_WRITE_REQ_REJECTED 0xfc
```

相关声明：[BT_ATT_ERR_WRITE_REQ_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8363770d0832f3df8fb1d0a22bc3551e)。

写请求被拒绝（Write Request Rejected）。

<a id="r_ga8f623146d7fda4b71514277cfbcd4b21"></a>

```c
#define BT_ATT_ERR_CCC_IMPROPER_CONF 0xfd
```

相关声明：[BT_ATT_ERR_CCC_IMPROPER_CONF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8f623146d7fda4b71514277cfbcd4b21)。

客户端特征配置描述符（Client Characteristic Configuration Descriptor）配置不正确。

<a id="r_gaf9e46c363487c61dbff50790993107f7"></a>

```c
#define BT_ATT_ERR_PROCEDURE_IN_PROGRESS 0xfe
```

相关声明：[BT_ATT_ERR_PROCEDURE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaf9e46c363487c61dbff50790993107f7)。

过程已在进行中（Procedure Already in Progress）。

<a id="r_gad49773d5e7a39f49c5a06bbaa4f8c365"></a>

```c
#define BT_ATT_ERR_OUT_OF_RANGE 0xff
```

相关声明：[BT_ATT_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad49773d5e7a39f49c5a06bbaa4f8c365)。

超出范围（Out of Range）。

<a id="r_ga3c4df4336916e082115d43f9716acb36"></a>

```c
#define BT_ATT_MAX_ATTRIBUTE_LEN 512
```

相关声明：[BT_ATT_MAX_ATTRIBUTE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga3c4df4336916e082115d43f9716acb36)。

<a id="r_gad0aa088f621b8965013c3ced27480df7"></a>

```c
#define BT_ATT_FIRST_ATTRIBUTE_HANDLE 0x0001
```

相关声明：[BT_ATT_FIRST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad0aa088f621b8965013c3ced27480df7)。

<a id="r_ga1b3dc5fedec8d8632d3650405d1ff988"></a>

```c
#define BT_ATT_LAST_ATTRIBUTE_HANDLE 0xffff
```

相关声明：[BT_ATT_LAST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga1b3dc5fedec8d8632d3650405d1ff988)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_gac593a27ecf029f33f50f990b2947562c"></a>

```c
enum bt_att_chan_opt { BT_ATT_CHAN_OPT_NONE = 0x0 , BT_ATT_CHAN_OPT_UNENHANCED_ONLY = (1UL << (0)) , BT_ATT_CHAN_OPT_ENHANCED_ONLY = (1UL << (1)) }
```

相关声明：[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)、[BT_ATT_CHAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)、[BT_ATT_CHAN_OPT_UNENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4)、[BT_ATT_CHAN_OPT_ENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6)。

ATT 通道选项位字段值（Channel Option Bit Field Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gad2305f28744276d97aefd26bdb79023c"></a>

```c
static const char * bt_att_err_to_str (uint8_t att_err)
```

相关声明：[bt_att_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad2305f28744276d97aefd26bdb79023c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 ATT 错误（Error）转换为字符串。

<a id="r_ga748194cbbd54a3336d3c788f08e3de99"></a>

```c
int bt_eatt_connect (struct bt_conn *conn, size_t num_channels)
```

相关声明：[bt_eatt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga748194cbbd54a3336d3c788f08e3de99)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

连接增强型 ATT 通道（Enhanced ATT Channels）。

<a id="r_ga3cabc05e8f5c0418ff02dd7122b7565e"></a>

```c
size_t bt_eatt_count (struct bt_conn *conn)
```

相关声明：[bt_eatt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga3cabc05e8f5c0418ff02dd7122b7565e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取已连接的增强型 ATT 通道（EATT Channels）数量。

<a id="r_ga653a0fc8803d7deebb0be93c8cf7910a"></a>

```c
int bt_att_get_max_notify_size (struct bt_conn *conn, enum bt_att_chan_opt chan_opt)
```

相关声明：[bt_att_get_max_notify_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga653a0fc8803d7deebb0be93c8cf7910a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)。

获取连接的最大通知值大小（Notification Value Size）。

<a id="r_ga2edca82fff038f16e6f7d09bc1db59a8"></a>

```c
static int bt_att_get_max_indicate_size (struct bt_conn *conn, enum bt_att_chan_opt chan_opt)
```

相关声明：[bt_att_get_max_indicate_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2edca82fff038f16e6f7d09bc1db59a8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)。

获取连接的最大指示值大小（Indication Value Size）。


## 2.4\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/bluetooth/conn.h](../api_source_register_time_reference/P002_conn.h_源码浏览.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/toolchain.h](../api_source_compiler_device_reference/P023_toolchain.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P001_att.h_源码浏览.md)
- [BT_ATT_ERR_SUCCESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga0032756d54c08d37c101769be8ef2070)
- [BT_ATT_ERR_INVALID_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gab8d9a6870360f0e5dd7290895202879f)
- [BT_ATT_ERR_READ_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac26ed224b7f8fb7717b40fe3a545be7e)
- [BT_ATT_ERR_WRITE_NOT_PERMITTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2378ff92f5afaff1e4392b1dc2e7326c)
- [BT_ATT_ERR_INVALID_PDU](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)
- [BT_ATT_ERR_AUTHENTICATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga269e711af78a7a30a770b3d7db210c8a)
- [BT_ATT_ERR_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gafcfa214f6f5b600647886f27cebecb49)
- [BT_ATT_ERR_INVALID_OFFSET](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga997d113b71af6b4019c26ca3893f3dbb)
- [BT_ATT_ERR_AUTHORIZATION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga30b28071d7057c2c68b10da34ba32faf)
- [BT_ATT_ERR_PREPARE_QUEUE_FULL](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaa135b2315173e7852afe4e1624169ce2)
- [BT_ATT_ERR_ATTRIBUTE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga5dfcd07918dc665bf600a25608b0736d)
- [BT_ATT_ERR_ATTRIBUTE_NOT_LONG](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga240561711499f11b267d2e5ed8fc99f5)
- [BT_ATT_ERR_ENCRYPTION_KEY_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2ed58d79dfbd701a97377b171f1b0793)
- [BT_ATT_ERR_INVALID_ATTRIBUTE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga21207d5beb27fe50856f001bd18e1efa)
- [BT_ATT_ERR_UNLIKELY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga992baa1f0d763a00f314bdcf59965bdd)
- [BT_ATT_ERR_INSUFFICIENT_ENCRYPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8a5235e39b05fa85b5b4f4bfb449683b)
- [BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga0611fc39d9d09ea4f0e556b4910f09ed)
- [BT_ATT_ERR_INSUFFICIENT_RESOURCES](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaf4a81bc81cad14bf91463d4376a3a868)
- [BT_ATT_ERR_DB_OUT_OF_SYNC](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2b9a58bf48f1b76e743cb7fef3aed3a8)
- [BT_ATT_ERR_VALUE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga52ffe5ff2eb092bcdc2ebb05684030d7)
- [BT_ATT_ERR_WRITE_REQ_REJECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8363770d0832f3df8fb1d0a22bc3551e)
- [BT_ATT_ERR_CCC_IMPROPER_CONF](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga8f623146d7fda4b71514277cfbcd4b21)
- [BT_ATT_ERR_PROCEDURE_IN_PROGRESS](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gaf9e46c363487c61dbff50790993107f7)
- [BT_ATT_ERR_OUT_OF_RANGE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad49773d5e7a39f49c5a06bbaa4f8c365)
- [BT_ATT_MAX_ATTRIBUTE_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga3c4df4336916e082115d43f9716acb36)
- [BT_ATT_FIRST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad0aa088f621b8965013c3ced27480df7)
- [BT_ATT_LAST_ATTRIBUTE_HANDLE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga1b3dc5fedec8d8632d3650405d1ff988)
- [bt_att_chan_opt](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gac593a27ecf029f33f50f990b2947562c)
- [BT_ATT_CHAN_OPT_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)
- [BT_ATT_CHAN_OPT_UNENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4)
- [BT_ATT_CHAN_OPT_ENHANCED_ONLY](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6)
- [bt_att_err_to_str](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#gad2305f28744276d97aefd26bdb79023c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_eatt_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga748194cbbd54a3336d3c788f08e3de99)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [bt_eatt_count](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga3cabc05e8f5c0418ff02dd7122b7565e)
- [bt_att_get_max_notify_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga653a0fc8803d7deebb0be93c8cf7910a)
- [bt_att_get_max_indicate_size](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html#ga2edca82fff038f16e6f7d09bc1db59a8)

<a id="header-details"></a>

---

[上一章](P001_zephyr__bluetooth__addr.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__dt-bindings__clock__ch32v10x-clocks.h_文件参考.md)
