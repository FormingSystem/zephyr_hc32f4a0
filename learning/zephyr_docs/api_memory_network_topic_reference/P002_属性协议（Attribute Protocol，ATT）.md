---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-2
title: 属性协议（Attribute Protocol，ATT）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_属性协议（Attribute Protocol，ATT）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__att.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

属性协议（Attribute Protocol，ATT）

<a id="details"></a>

属性协议（Attribute Protocol，ATT）。引入版本（Since）：1.1；API 版本（Version）：1.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_ga0032756d54c08d37c101769be8ef2070"></a>

```c
#define BT_ATT_ERR_SUCCESS 0x00
```

相关声明：[BT_ATT_ERR_SUCCESS](#ga0032756d54c08d37c101769be8ef2070)。

属性协议操作（ATT Operation）成功。

<a id="r_gab8d9a6870360f0e5dd7290895202879f"></a>

```c
#define BT_ATT_ERR_INVALID_HANDLE 0x01
```

相关声明：[BT_ATT_ERR_INVALID_HANDLE](#gab8d9a6870360f0e5dd7290895202879f)。

给定属性句柄（Attribute Handle）在服务器上无效。

<a id="r_gac26ed224b7f8fb7717b40fe3a545be7e"></a>

```c
#define BT_ATT_ERR_READ_NOT_PERMITTED 0x02
```

相关声明：[BT_ATT_ERR_READ_NOT_PERMITTED](#gac26ed224b7f8fb7717b40fe3a545be7e)。

属性（Attribute）不可读。

<a id="r_ga2378ff92f5afaff1e4392b1dc2e7326c"></a>

```c
#define BT_ATT_ERR_WRITE_NOT_PERMITTED 0x03
```

相关声明：[BT_ATT_ERR_WRITE_NOT_PERMITTED](#ga2378ff92f5afaff1e4392b1dc2e7326c)。

属性（Attribute）不可写。

<a id="r_ga7f1cbe6eb3ed0999bafab729c7b0a6a6"></a>

```c
#define BT_ATT_ERR_INVALID_PDU 0x04
```

相关声明：[BT_ATT_ERR_INVALID_PDU](#ga7f1cbe6eb3ed0999bafab729c7b0a6a6)。

属性协议数据单元（Attribute PDU）无效。

<a id="r_ga269e711af78a7a30a770b3d7db210c8a"></a>

```c
#define BT_ATT_ERR_AUTHENTICATION 0x05
```

相关声明：[BT_ATT_ERR_AUTHENTICATION](#ga269e711af78a7a30a770b3d7db210c8a)。

读写属性之前需要认证（Authentication）。

<a id="r_gafcfa214f6f5b600647886f27cebecb49"></a>

```c
#define BT_ATT_ERR_NOT_SUPPORTED 0x06
```

相关声明：[BT_ATT_ERR_NOT_SUPPORTED](#gafcfa214f6f5b600647886f27cebecb49)。

ATT 服务器不支持从客户端收到的请求。

<a id="r_ga997d113b71af6b4019c26ca3893f3dbb"></a>

```c
#define BT_ATT_ERR_INVALID_OFFSET 0x07
```

相关声明：[BT_ATT_ERR_INVALID_OFFSET](#ga997d113b71af6b4019c26ca3893f3dbb)。

指定偏移（Offset）超出属性末尾。

<a id="r_ga30b28071d7057c2c68b10da34ba32faf"></a>

```c
#define BT_ATT_ERR_AUTHORIZATION 0x08
```

相关声明：[BT_ATT_ERR_AUTHORIZATION](#ga30b28071d7057c2c68b10da34ba32faf)。

读写属性之前需要授权（Authorization）。

<a id="r_gaa135b2315173e7852afe4e1624169ce2"></a>

```c
#define BT_ATT_ERR_PREPARE_QUEUE_FULL 0x09
```

相关声明：[BT_ATT_ERR_PREPARE_QUEUE_FULL](#gaa135b2315173e7852afe4e1624169ce2)。

队列中的预备写操作（Prepare Writes）过多。

<a id="r_ga5dfcd07918dc665bf600a25608b0736d"></a>

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_FOUND 0x0a
```

相关声明：[BT_ATT_ERR_ATTRIBUTE_NOT_FOUND](#ga5dfcd07918dc665bf600a25608b0736d)。

在给定属性句柄范围（Attribute Handle Range）内未找到属性。

<a id="r_ga240561711499f11b267d2e5ed8fc99f5"></a>

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_LONG 0x0b
```

相关声明：[BT_ATT_ERR_ATTRIBUTE_NOT_LONG](#ga240561711499f11b267d2e5ed8fc99f5)。

无法使用 ATT_READ_BLOB_REQ PDU 读取此属性。

<a id="r_ga2ed58d79dfbd701a97377b171f1b0793"></a>

```c
#define BT_ATT_ERR_ENCRYPTION_KEY_SIZE 0x0c
```

相关声明：[BT_ATT_ERR_ENCRYPTION_KEY_SIZE](#ga2ed58d79dfbd701a97377b171f1b0793)。

用于加密此链路的加密密钥长度（Encryption Key Size）过短。

<a id="r_ga21207d5beb27fe50856f001bd18e1efa"></a>

```c
#define BT_ATT_ERR_INVALID_ATTRIBUTE_LEN 0x0d
```

相关声明：[BT_ATT_ERR_INVALID_ATTRIBUTE_LEN](#ga21207d5beb27fe50856f001bd18e1efa)。

属性值长度（Attribute Value Length）对此操作无效。

<a id="r_ga992baa1f0d763a00f314bdcf59965bdd"></a>

```c
#define BT_ATT_ERR_UNLIKELY 0x0e
```

相关声明：[BT_ATT_ERR_UNLIKELY](#ga992baa1f0d763a00f314bdcf59965bdd)。

请求的属性操作遇到一个通常不会发生的错误（Unlikely Error）。

<a id="r_ga8a5235e39b05fa85b5b4f4bfb449683b"></a>

```c
#define BT_ATT_ERR_INSUFFICIENT_ENCRYPTION 0x0f
```

相关声明：[BT_ATT_ERR_INSUFFICIENT_ENCRYPTION](#ga8a5235e39b05fa85b5b4f4bfb449683b)。

读写属性之前需要加密（Encryption）。

<a id="r_ga0611fc39d9d09ea4f0e556b4910f09ed"></a>

```c
#define BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE 0x10
```

相关声明：[BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE](#ga0611fc39d9d09ea4f0e556b4910f09ed)。

此属性类型不是受支持的分组属性（Grouping Attribute）。

<a id="r_gaf4a81bc81cad14bf91463d4376a3a868"></a>

```c
#define BT_ATT_ERR_INSUFFICIENT_RESOURCES 0x11
```

相关声明：[BT_ATT_ERR_INSUFFICIENT_RESOURCES](#gaf4a81bc81cad14bf91463d4376a3a868)。

资源不足（Insufficient Resources），无法完成请求。

<a id="r_ga2b9a58bf48f1b76e743cb7fef3aed3a8"></a>

```c
#define BT_ATT_ERR_DB_OUT_OF_SYNC 0x12
```

相关声明：[BT_ATT_ERR_DB_OUT_OF_SYNC](#ga2b9a58bf48f1b76e743cb7fef3aed3a8)。

服务器要求客户端重新发现数据库（Rediscover Database）。

<a id="r_ga52ffe5ff2eb092bcdc2ebb05684030d7"></a>

```c
#define BT_ATT_ERR_VALUE_NOT_ALLOWED 0x13
```

相关声明：[BT_ATT_ERR_VALUE_NOT_ALLOWED](#ga52ffe5ff2eb092bcdc2ebb05684030d7)。

不允许此属性参数值（Attribute Parameter Value）。

<a id="r_ga8363770d0832f3df8fb1d0a22bc3551e"></a>

```c
#define BT_ATT_ERR_WRITE_REQ_REJECTED 0xfc
```

相关声明：[BT_ATT_ERR_WRITE_REQ_REJECTED](#ga8363770d0832f3df8fb1d0a22bc3551e)。

写请求被拒绝（Write Request Rejected）。

<a id="r_ga8f623146d7fda4b71514277cfbcd4b21"></a>

```c
#define BT_ATT_ERR_CCC_IMPROPER_CONF 0xfd
```

相关声明：[BT_ATT_ERR_CCC_IMPROPER_CONF](#ga8f623146d7fda4b71514277cfbcd4b21)。

客户端特征配置描述符（Client Characteristic Configuration Descriptor）配置不正确。

<a id="r_gaf9e46c363487c61dbff50790993107f7"></a>

```c
#define BT_ATT_ERR_PROCEDURE_IN_PROGRESS 0xfe
```

相关声明：[BT_ATT_ERR_PROCEDURE_IN_PROGRESS](#gaf9e46c363487c61dbff50790993107f7)。

过程已在进行中（Procedure Already in Progress）。

<a id="r_gad49773d5e7a39f49c5a06bbaa4f8c365"></a>

```c
#define BT_ATT_ERR_OUT_OF_RANGE 0xff
```

相关声明：[BT_ATT_ERR_OUT_OF_RANGE](#gad49773d5e7a39f49c5a06bbaa4f8c365)。

超出范围（Out of Range）。

<a id="r_ga3c4df4336916e082115d43f9716acb36"></a>

```c
#define BT_ATT_MAX_ATTRIBUTE_LEN 512
```

相关声明：[BT_ATT_MAX_ATTRIBUTE_LEN](#ga3c4df4336916e082115d43f9716acb36)。

<a id="r_gad0aa088f621b8965013c3ced27480df7"></a>

```c
#define BT_ATT_FIRST_ATTRIBUTE_HANDLE 0x0001
```

相关声明：[BT_ATT_FIRST_ATTRIBUTE_HANDLE](#gad0aa088f621b8965013c3ced27480df7)。

<a id="r_ga1b3dc5fedec8d8632d3650405d1ff988"></a>

```c
#define BT_ATT_LAST_ATTRIBUTE_HANDLE 0xffff
```

相关声明：[BT_ATT_LAST_ATTRIBUTE_HANDLE](#ga1b3dc5fedec8d8632d3650405d1ff988)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 2.2\_枚举（Enumerations）

<a id="r_gac593a27ecf029f33f50f990b2947562c"></a>

```c
enum bt_att_chan_opt { BT_ATT_CHAN_OPT_NONE = 0x0 , BT_ATT_CHAN_OPT_UNENHANCED_ONLY = (1UL << (0)) , BT_ATT_CHAN_OPT_ENHANCED_ONLY = (1UL << (1)) }
```

相关声明：[bt_att_chan_opt](#gac593a27ecf029f33f50f990b2947562c)、[BT_ATT_CHAN_OPT_NONE](#ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739)、[BT_ATT_CHAN_OPT_UNENHANCED_ONLY](#ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4)、[BT_ATT_CHAN_OPT_ENHANCED_ONLY](#ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6)。

ATT 通道选项位字段值（Channel Option Bit Field Values）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.3\_函数（Functions）

<a id="r_gad2305f28744276d97aefd26bdb79023c"></a>

```c
static const char * bt_att_err_to_str (uint8_t att_err)
```

相关声明：[bt_att_err_to_str](#gad2305f28744276d97aefd26bdb79023c)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 ATT 错误（Error）转换为字符串。

<a id="r_ga748194cbbd54a3336d3c788f08e3de99"></a>

```c
int bt_eatt_connect (struct bt_conn *conn, size_t num_channels)
```

相关声明：[bt_eatt_connect](#ga748194cbbd54a3336d3c788f08e3de99)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

连接增强型 ATT 通道（Enhanced ATT Channels）。

<a id="r_ga3cabc05e8f5c0418ff02dd7122b7565e"></a>

```c
size_t bt_eatt_count (struct bt_conn *conn)
```

相关声明：[bt_eatt_count](#ga3cabc05e8f5c0418ff02dd7122b7565e)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)。

获取已连接的增强型 ATT 通道（EATT Channels）数量。

<a id="r_ga653a0fc8803d7deebb0be93c8cf7910a"></a>

```c
int bt_att_get_max_notify_size (struct bt_conn *conn, enum bt_att_chan_opt chan_opt)
```

相关声明：[bt_att_get_max_notify_size](#ga653a0fc8803d7deebb0be93c8cf7910a)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_att_chan_opt](#gac593a27ecf029f33f50f990b2947562c)。

获取连接的最大通知值大小（Notification Value Size）。

<a id="r_ga2edca82fff038f16e6f7d09bc1db59a8"></a>

```c
static int bt_att_get_max_indicate_size (struct bt_conn *conn, enum bt_att_chan_opt chan_opt)
```

相关声明：[bt_att_get_max_indicate_size](#ga2edca82fff038f16e6f7d09bc1db59a8)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[bt_att_chan_opt](#gac593a27ecf029f33f50f990b2947562c)。

获取连接的最大指示值大小（Indication Value Size）。

## 2.4\_详细说明（Detailed Documentation）

<a id="ga5dfcd07918dc665bf600a25608b0736d"></a>

### `BT_ATT_ERR_ATTRIBUTE_NOT_FOUND`

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_FOUND 0x0a
```

```c
#include <zephyr/bluetooth/att.h>
```

在给定属性句柄范围（Attribute Handle Range）内未找到属性。

<a id="ga240561711499f11b267d2e5ed8fc99f5"></a>

### `BT_ATT_ERR_ATTRIBUTE_NOT_LONG`

```c
#define BT_ATT_ERR_ATTRIBUTE_NOT_LONG 0x0b
```

```c
#include <zephyr/bluetooth/att.h>
```

无法使用 ATT_READ_BLOB_REQ PDU 读取此属性。

<a id="ga269e711af78a7a30a770b3d7db210c8a"></a>

### `BT_ATT_ERR_AUTHENTICATION`

```c
#define BT_ATT_ERR_AUTHENTICATION 0x05
```

```c
#include <zephyr/bluetooth/att.h>
```

读写属性之前需要认证（Authentication）。

<a id="ga30b28071d7057c2c68b10da34ba32faf"></a>

### `BT_ATT_ERR_AUTHORIZATION`

```c
#define BT_ATT_ERR_AUTHORIZATION 0x08
```

```c
#include <zephyr/bluetooth/att.h>
```

读写属性之前需要授权（Authorization）。

<a id="ga8f623146d7fda4b71514277cfbcd4b21"></a>

### `BT_ATT_ERR_CCC_IMPROPER_CONF`

```c
#define BT_ATT_ERR_CCC_IMPROPER_CONF 0xfd
```

```c
#include <zephyr/bluetooth/att.h>
```

客户端特征配置描述符（Client Characteristic Configuration Descriptor）配置不正确。

<a id="ga2b9a58bf48f1b76e743cb7fef3aed3a8"></a>

### `BT_ATT_ERR_DB_OUT_OF_SYNC`

```c
#define BT_ATT_ERR_DB_OUT_OF_SYNC 0x12
```

```c
#include <zephyr/bluetooth/att.h>
```

服务器要求客户端重新发现数据库（Rediscover Database）。

<a id="ga2ed58d79dfbd701a97377b171f1b0793"></a>

### `BT_ATT_ERR_ENCRYPTION_KEY_SIZE`

```c
#define BT_ATT_ERR_ENCRYPTION_KEY_SIZE 0x0c
```

```c
#include <zephyr/bluetooth/att.h>
```

用于加密此链路的加密密钥长度（Encryption Key Size）过短。

<a id="ga8a5235e39b05fa85b5b4f4bfb449683b"></a>

### `BT_ATT_ERR_INSUFFICIENT_ENCRYPTION`

```c
#define BT_ATT_ERR_INSUFFICIENT_ENCRYPTION 0x0f
```

```c
#include <zephyr/bluetooth/att.h>
```

读写属性之前需要加密（Encryption）。

<a id="gaf4a81bc81cad14bf91463d4376a3a868"></a>

### `BT_ATT_ERR_INSUFFICIENT_RESOURCES`

```c
#define BT_ATT_ERR_INSUFFICIENT_RESOURCES 0x11
```

```c
#include <zephyr/bluetooth/att.h>
```

资源不足（Insufficient Resources），无法完成请求。

<a id="ga21207d5beb27fe50856f001bd18e1efa"></a>

### `BT_ATT_ERR_INVALID_ATTRIBUTE_LEN`

```c
#define BT_ATT_ERR_INVALID_ATTRIBUTE_LEN 0x0d
```

```c
#include <zephyr/bluetooth/att.h>
```

属性值长度（Attribute Value Length）对此操作无效。

<a id="gab8d9a6870360f0e5dd7290895202879f"></a>

### `BT_ATT_ERR_INVALID_HANDLE`

```c
#define BT_ATT_ERR_INVALID_HANDLE 0x01
```

```c
#include <zephyr/bluetooth/att.h>
```

给定属性句柄（Attribute Handle）在服务器上无效。

<a id="ga997d113b71af6b4019c26ca3893f3dbb"></a>

### `BT_ATT_ERR_INVALID_OFFSET`

```c
#define BT_ATT_ERR_INVALID_OFFSET 0x07
```

```c
#include <zephyr/bluetooth/att.h>
```

指定偏移（Offset）超出属性末尾。

<a id="ga7f1cbe6eb3ed0999bafab729c7b0a6a6"></a>

### `BT_ATT_ERR_INVALID_PDU`

```c
#define BT_ATT_ERR_INVALID_PDU 0x04
```

```c
#include <zephyr/bluetooth/att.h>
```

属性协议数据单元（Attribute PDU）无效。

<a id="gafcfa214f6f5b600647886f27cebecb49"></a>

### `BT_ATT_ERR_NOT_SUPPORTED`

```c
#define BT_ATT_ERR_NOT_SUPPORTED 0x06
```

```c
#include <zephyr/bluetooth/att.h>
```

ATT 服务器不支持从客户端收到的请求。

<a id="gad49773d5e7a39f49c5a06bbaa4f8c365"></a>

### `BT_ATT_ERR_OUT_OF_RANGE`

```c
#define BT_ATT_ERR_OUT_OF_RANGE 0xff
```

```c
#include <zephyr/bluetooth/att.h>
```

超出范围（Out of Range）。

<a id="gaa135b2315173e7852afe4e1624169ce2"></a>

### `BT_ATT_ERR_PREPARE_QUEUE_FULL`

```c
#define BT_ATT_ERR_PREPARE_QUEUE_FULL 0x09
```

```c
#include <zephyr/bluetooth/att.h>
```

队列中的预备写操作（Prepare Writes）过多。

<a id="gaf9e46c363487c61dbff50790993107f7"></a>

### `BT_ATT_ERR_PROCEDURE_IN_PROGRESS`

```c
#define BT_ATT_ERR_PROCEDURE_IN_PROGRESS 0xfe
```

```c
#include <zephyr/bluetooth/att.h>
```

过程已在进行中（Procedure Already in Progress）。

<a id="gac26ed224b7f8fb7717b40fe3a545be7e"></a>

### `BT_ATT_ERR_READ_NOT_PERMITTED`

```c
#define BT_ATT_ERR_READ_NOT_PERMITTED 0x02
```

```c
#include <zephyr/bluetooth/att.h>
```

属性（Attribute）不可读。

<a id="ga0032756d54c08d37c101769be8ef2070"></a>

### `BT_ATT_ERR_SUCCESS`

```c
#define BT_ATT_ERR_SUCCESS 0x00
```

```c
#include <zephyr/bluetooth/att.h>
```

属性协议操作（ATT Operation）成功。

<a id="ga992baa1f0d763a00f314bdcf59965bdd"></a>

### `BT_ATT_ERR_UNLIKELY`

```c
#define BT_ATT_ERR_UNLIKELY 0x0e
```

```c
#include <zephyr/bluetooth/att.h>
```

请求的属性操作遇到一个通常不会发生的错误（Unlikely Error）。

因此无法按请求完成属性操作（Attribute Request）。

<a id="ga0611fc39d9d09ea4f0e556b4910f09ed"></a>

### `BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE`

```c
#define BT_ATT_ERR_UNSUPPORTED_GROUP_TYPE 0x10
```

```c
#include <zephyr/bluetooth/att.h>
```

此属性类型不是受支持的分组属性（Grouping Attribute）。

此属性类型不是高层规范定义的受支持分组属性（Grouping Attribute）。

<a id="ga52ffe5ff2eb092bcdc2ebb05684030d7"></a>

### `BT_ATT_ERR_VALUE_NOT_ALLOWED`

```c
#define BT_ATT_ERR_VALUE_NOT_ALLOWED 0x13
```

```c
#include <zephyr/bluetooth/att.h>
```

不允许此属性参数值（Attribute Parameter Value）。

<a id="ga2378ff92f5afaff1e4392b1dc2e7326c"></a>

### `BT_ATT_ERR_WRITE_NOT_PERMITTED`

```c
#define BT_ATT_ERR_WRITE_NOT_PERMITTED 0x03
```

```c
#include <zephyr/bluetooth/att.h>
```

属性（Attribute）不可写。

<a id="ga8363770d0832f3df8fb1d0a22bc3551e"></a>

### `BT_ATT_ERR_WRITE_REQ_REJECTED`

```c
#define BT_ATT_ERR_WRITE_REQ_REJECTED 0xfc
```

```c
#include <zephyr/bluetooth/att.h>
```

写请求被拒绝（Write Request Rejected）。

<a id="gad0aa088f621b8965013c3ced27480df7"></a>

### `BT_ATT_FIRST_ATTRIBUTE_HANDLE`

```c
#define BT_ATT_FIRST_ATTRIBUTE_HANDLE 0x0001
```

```c
#include <zephyr/bluetooth/att.h>
```

<a id="ga1b3dc5fedec8d8632d3650405d1ff988"></a>

### `BT_ATT_LAST_ATTRIBUTE_HANDLE`

```c
#define BT_ATT_LAST_ATTRIBUTE_HANDLE 0xffff
```

```c
#include <zephyr/bluetooth/att.h>
```

<a id="ga3c4df4336916e082115d43f9716acb36"></a>

### `BT_ATT_MAX_ATTRIBUTE_LEN`

```c
#define BT_ATT_MAX_ATTRIBUTE_LEN 512
```

```c
#include <zephyr/bluetooth/att.h>
```

<a id="gac593a27ecf029f33f50f990b2947562c"></a>

### `bt_att_chan_opt`

```c
enum bt_att_chan_opt
```

```c
#include <zephyr/bluetooth/att.h>
```

ATT 通道选项位字段值（Channel Option Bit Field Values）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `BT_ATT_CHAN_OPT_NONE` | 可使用增强型和非增强型通道（Enhanced and Unenhanced Channels）。 |
| `BT_ATT_CHAN_OPT_UNENHANCED_ONLY` | 仅使用非增强型通道（Unenhanced Channels）。 |
| `BT_ATT_CHAN_OPT_ENHANCED_ONLY` | 仅使用增强型通道（Enhanced Channels）。 |

**说明（Note）**：注意（Note）：BT_ATT_CHAN_OPT_UNENHANCED_ONLY 与 BT_ATT_CHAN_OPT_ENHANCED_ONLY 互斥，不能同时设置两个位。

<a id="gad2305f28744276d97aefd26bdb79023c"></a>

### `bt_att_err_to_str()`

```c
const char * bt_att_err_to_str ( uint8_t att_err)
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/att.h>
```

将 ATT 错误（Error）转换为字符串。

错误码见《蓝牙核心规范》（Bluetooth Core Specification）卷 3、F 部分、第 3.4.1.1 节，以及《蓝牙核心规范补充》（Core Specification Supplement，CSS）v11、B 部分、第 1.2 节。

卷 4、F 部分和 G 部分中的 ATT 与 GATT 文档说明不同错误码的使用场景。

另请参阅已定义的 BT_ATT_ERR_* 宏。

**返回（Returns）**：返回值（Returns）：ATT 错误码的字符串表示。未启用 CONFIG_BT_ATT_ERR_TO_STR 时仅返回空字符串。

<a id="ga2edca82fff038f16e6f7d09bc1db59a8"></a>

### `bt_att_get_max_indicate_size()`

```c
int bt_att_get_max_indicate_size ( struct bt_conn * conn, enum bt_att_chan_opt chan_opt )
```

声明属性：`inline`、`static`。

```c
#include <zephyr/bluetooth/att.h>
```

获取连接的最大指示值大小（Indication Value Size）。

ATT_HANDLE_VALUE_IND PDU 的值大小上限为 ATT_MTU - 3；其中 3 个八位组用于操作码与属性句柄，见《蓝牙核心规范》6.1 版、卷 3、F 部分、第 3.4.7.2 节。该上限与通知（Notifications）相同。

更大的值须由发送方截断，或由客户端通过读请求（Read Request）读取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要获取其最大指示值大小（Indication Value Size）的 LE ACL 连接。 |
| `chan_opt` | 要获取其最大指示值大小的承载（Bearer），须为 BT_ATT_CHAN_OPT_NONE、BT_ATT_CHAN_OPT_UNENHANCED_ONLY 或 BT_ATT_CHAN_OPT_ENHANCED_ONLY；后者仅在启用 CONFIG_BT_EATT 时可用。BT_ATT_CHAN_OPT_NONE 获取任意承载的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | conn 为 NULL、不是 ACL 连接，或 chan_opt 无效。 |
| `-ENOTCONN` | conn 未连接。 |

**说明（Note）**：注意（Note）：ATT_MTU 在连接存续期间可能变化，因此不得缓存此函数的结果。

**返回（Returns）**：返回值（Returns）：成功时返回最大指示值大小，单位为八位组（Octets）。

<a id="ga653a0fc8803d7deebb0be93c8cf7910a"></a>

### `bt_att_get_max_notify_size()`

```c
int bt_att_get_max_notify_size ( struct bt_conn * conn, enum bt_att_chan_opt chan_opt )
```

```c
#include <zephyr/bluetooth/att.h>
```

获取连接的最大通知值大小（Notification Value Size）。

ATT_HANDLE_VALUE_NTF PDU 的值大小上限为 ATT_MTU - 3；其中 3 个八位组用于操作码与属性句柄，见《蓝牙核心规范》6.1 版、卷 3、F 部分、第 3.4.7.1 节。

更大的值须由发送方截断，或由客户端通过读请求（Read Request）读取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要获取其最大通知值大小（Notification Value Size）的 LE ACL 连接。 |
| `chan_opt` | 要获取其最大通知值大小的承载（Bearer），须为 BT_ATT_CHAN_OPT_NONE、BT_ATT_CHAN_OPT_UNENHANCED_ONLY 或 BT_ATT_CHAN_OPT_ENHANCED_ONLY；后者仅在启用 CONFIG_BT_EATT 时可用。BT_ATT_CHAN_OPT_NONE 获取任意承载的值。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | conn 为 NULL、不是 ACL 连接，或 chan_opt 无效。 |
| `-ENOTCONN` | conn 未连接。 |

**说明（Note）**：注意（Note）：ATT_MTU 在连接存续期间可能变化，因此不得缓存此函数的结果。

**返回（Returns）**：返回值（Returns）：成功时返回最大通知值大小，单位为八位组（Octets）。

<a id="ga748194cbbd54a3336d3c788f08e3de99"></a>

### `bt_eatt_connect()`

```c
int bt_eatt_connect ( struct bt_conn * conn, size_t num_channels )
```

```c
#include <zephyr/bluetooth/att.h>
```

连接增强型 ATT 通道（Enhanced ATT Channels）。

发送一系列基于信用的连接请求（Credit Based Connection Requests），连接 num_channels 个增强型 ATT 通道。对端资源可能有限，实际创建的通道可能少于请求数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 用于发送请求的连接（Connection） |
| `num_channels` | 请求的增强型 ATT 承载（Enhanced ATT Bearers）数量，范围为 1～CONFIG_BT_EATT_MAX，包含两端。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `-EINVAL` | num_channels 超出允许范围或 conn 为 NULL 时。 |
| `-ENOMEM` | 分配数量少于 num_channels 时。 |
| `0` | 成功时。 |

**注意（Attention）**：注意（Attention）：仅启用 Kconfig 选项 CONFIG_BT_EATT 时可用。

**返回（Returns）**：成功返回 0，出错时返回负值。

<a id="ga3cabc05e8f5c0418ff02dd7122b7565e"></a>

### `bt_eatt_count()`

```c
size_t bt_eatt_count ( struct bt_conn * conn)
```

```c
#include <zephyr/bluetooth/att.h>
```

获取已连接的增强型 ATT 通道（EATT Channels）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `conn` | 要获取其 EATT 通道数量的连接。 |

**注意（Attention）**：注意（Attention）：仅启用 Kconfig 选项 CONFIG_BT_EATT 时可用。

**返回（Returns）**：返回值（Returns）：已连接的 EATT 通道数量；conn 为 NULL 或未连接时返回 0。


## 2.5\_原页交叉引用（Cross References）

- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [zephyr/bluetooth/att.h](../api_file_clock_network_reference/P002_zephyr__bluetooth__att.h_文件参考.md)
- [CONFIG_BT_ATT_ERR_TO_STR](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ATT_ERR_TO_STR)
- [CONFIG_BT_EATT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EATT)
- [CONFIG_BT_EATT_MAX](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_EATT_MAX)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac593a27ecf029f33f50f990b2947562ca14e709b93e78dcc511339a99360ba739"></a>
<a id="ggac593a27ecf029f33f50f990b2947562ca72c7152b997d4726347c2bfda7da94c4"></a>
<a id="ggac593a27ecf029f33f50f990b2947562ca7bfd06bd0c22eb16b82a4cbed6675ed6"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P001_数字麦克风接口（Digital Microphone Interface）.md) · [返回大纲](大纲.md) · [下一章](P003_BAP 广播 API（Broadcast APIs）.md)
