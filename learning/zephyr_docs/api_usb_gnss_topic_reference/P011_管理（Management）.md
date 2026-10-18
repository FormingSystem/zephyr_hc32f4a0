---
id: learning.zephyr-docs.api-usb-gnss-topic-reference.page-11
title: 管理（Management）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_管理（Management）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

MCUmgr 管理 API

<a id="details"></a>

MCUmgr 管理 API（MCUmgr Management API）。起始版本（Since）：1.11。接口版本（Version）：1.0.0。

<a id="header-groups"></a>
<a id="groups"></a>

## 11.1\_主题（Topics）

<a id="r_mcumgr_5Fenum_5Fmgmt"></a>

相关声明：[枚举管理（Enumeration Management）](../api_protocol_topic_reference/P028_枚举管理（Enumeration Management）.md)。

MCUmgr 枚举管理 API

<a id="r_mcumgr_5Ffs_5Fmgmt"></a>

相关声明：[文件系统管理（File System Management）](../api_lifecycle_capability_topic_reference/P007_文件系统管理（File System Management）.md)。

MCUmgr 文件系统管理 API

<a id="r_mcumgr_5Fimg_5Fmgmt"></a>

相关声明：[映像管理（Image Management）](P010_映像管理（Image Management）.md)。

MCUmgr 映像管理 API

<a id="r_mcumgr_5Fos_5Fmgmt"></a>

相关声明：[操作系统管理（OS Management）](../api_lifecycle_capability_topic_reference/P008_操作系统管理（OS Management）.md)。

MCUmgr 操作系统管理 API

<a id="r_mcumgr_5Fsettings_5Fmgmt"></a>

相关声明：[设置管理（Settings Management）](../api_auxiliary_topic_reference/P012_设置管理（Settings Management）.md)。

MCUmgr 设置管理 API

<a id="r_mcumgr_5Fshell_5Fmgmt"></a>

相关声明：[命令行管理（Shell Management）](../shell_management_reference/P004_mcumgr_Shell管理接口.md)。

MCUmgr Shell管理API（Shell Management API）。

<a id="r_mcumgr_5Fstat_5Fmgmt"></a>

相关声明：[统计信息管理（Statistics Management）](../api_service_topic_reference/P014_统计信息管理（Statistics Management）.md)。

MCUmgr 统计信息管理 API

<a id="r_mcumgr_5Ftransport_5Fmgmt"></a>

相关声明：[传输管理（Transport management）](../api_coap_trusted_topic_reference/P010_传输管理（Transport management）.md)。

MCUmgr 传输管理 API

<a id="r_mcumgr_5Fzephyr_5Fbasic_5Fmgmt"></a>

相关声明：[Zephyr 基础管理（Zephyr Basic Management）](../api_extension_topic_reference/P018_Zephyr 基础管理（Zephyr Basic Management）.md)。

MCUmgr Zephyr 基础管理 API

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.2\_数据结构（Data Structures）

<a id="r_mgmt_5Fhandler"></a>

```c
struct mgmt_handler
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)。

单个命令ID的读取处理程序和写入处理程序（Read / Write Handler）。

<a id="r_mgmt_5Fgroup"></a>

```c
struct mgmt_group
```

相关声明：[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)。

整个命令组（Command Group）的处理程序集合。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.3\_宏定义（Macros）

<a id="r_ga8027c2a587a835d92450f2935e66eea0"></a>

```c
#define MGMT_CTXT_SET_RC_RSN(mc, rsn)
```

相关声明：[MGMT_CTXT_SET_RC_RSN](#ga8027c2a587a835d92450f2935e66eea0)。

<a id="r_ga4d22641395a665a911be715c2531fbd8"></a>

```c
#define MGMT_CTXT_RC_RSN(mc)
```

相关声明：[MGMT_CTXT_RC_RSN](#ga4d22641395a665a911be715c2531fbd8)。

<a id="r_gabdd715ff5b7efe040f205edf0b00bc43"></a>

```c
#define MGMT_RETURN_CHECK(ok)
```

相关声明：[MGMT_RETURN_CHECK](#gabdd715ff5b7efe040f205edf0b00bc43)。

在 MCUmgr 处理器（Handlers）的末尾使用：若达到消息大小限制（Message Size Limit），则返回错误；否则返回成功（OK）。

<a id="r_gabb62e7697ffb2a2f4e6d96abe28808a6"></a>

```c
#define MGMT_HDR_SIZE 8
```

相关声明：[MGMT_HDR_SIZE](#gabb62e7697ffb2a2f4e6d96abe28808a6)。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.4\_类型定义（Typedefs）

<a id="r_ga292686c742179758ca5b853fc21fe302"></a>

```c
typedef void *(* mgmt_alloc_rsp_fn) (const void *src_buf, void *arg)
```

相关声明：[mgmt_alloc_rsp_fn](#ga292686c742179758ca5b853fc21fe302)。

分配适合保存响应（Response）的缓冲区。

<a id="r_ga1346d5160823c5e43fce3e6cba9f8607"></a>

```c
typedef void(* mgmt_reset_buf_fn) (void *buf, void *arg)
```

相关声明：[mgmt_reset_buf_fn](#ga1346d5160823c5e43fce3e6cba9f8607)。

将缓冲区长度重置为 0。

<a id="r_gaaafc2c73e1616340e29df6a1ba94c241"></a>

```c
typedef int(* mgmt_handler_fn) (struct smp_streamer *ctxt)
```

相关声明：[mgmt_handler_fn](#gaaafc2c73e1616340e29df6a1ba94c241)、[smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)。

处理请求（Request）并写入对应响应（Response）。

<a id="r_ga9f63f42cd468ce85d0f800dc1472a5c8"></a>

```c
typedef bool(* mgmt_groups_cb_t) (const struct mgmt_group *group, void *user_data)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[mgmt_groups_cb_t](#ga9f63f42cd468ce85d0f800dc1472a5c8)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

组遍历回调（Group Iteration Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.5\_枚举（Enumerations）

<a id="r_gae06a618f492f18e856742b4affab80dd"></a>

```c
enum mcumgr_op_t { MGMT_OP_READ = 0 , MGMT_OP_READ_RSP , MGMT_OP_WRITE , MGMT_OP_WRITE_RSP , MGMT_OP_COUNT }
```

相关声明：[mcumgr_op_t](#gae06a618f492f18e856742b4affab80dd)、[MGMT_OP_READ](#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4)、[MGMT_OP_READ_RSP](#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7)、[MGMT_OP_WRITE](#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9)、[MGMT_OP_WRITE_RSP](#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543)、[MGMT_OP_COUNT](#ggae06a618f492f18e856742b4affab80dda4105c10d17622b7de6a8f14c036f3498)。

操作码（Opcodes），编码于头部（Header）的第一个字节中。

<a id="r_ga81f98b9a0c3810f7d607b783f8e259b5"></a>

```c
enum mcumgr_group_t { MGMT_GROUP_ID_OS = 0 , MGMT_GROUP_ID_IMAGE , MGMT_GROUP_ID_STAT , MGMT_GROUP_ID_SETTINGS , MGMT_GROUP_ID_LOG , MGMT_GROUP_ID_CRASH , MGMT_GROUP_ID_SPLIT , MGMT_GROUP_ID_RUN , MGMT_GROUP_ID_FS , MGMT_GROUP_ID_SHELL , MGMT_GROUP_ID_ENUM , MGMT_GROUP_ID_TRANSPORT , MGMT_GROUP_ID_PERUSER = 64 , ZEPHYR_MGMT_GRP_BASIC = (MGMT_GROUP_ID_PERUSER - 1) }
```

相关声明：[mcumgr_group_t](#ga81f98b9a0c3810f7d607b783f8e259b5)、[MGMT_GROUP_ID_OS](#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120)、[MGMT_GROUP_ID_IMAGE](#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c)、[MGMT_GROUP_ID_STAT](#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc)、[MGMT_GROUP_ID_SETTINGS](#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb)、[MGMT_GROUP_ID_LOG](#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309)、[MGMT_GROUP_ID_CRASH](#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204)、[MGMT_GROUP_ID_SPLIT](#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527)、[MGMT_GROUP_ID_RUN](#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a)、[MGMT_GROUP_ID_FS](#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5)、[MGMT_GROUP_ID_SHELL](#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85)、[MGMT_GROUP_ID_ENUM](#gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c)、[MGMT_GROUP_ID_TRANSPORT](#gga81f98b9a0c3810f7d607b783f8e259b5ad5273bf46818cd7b6530fb3353ad35f2)、[MGMT_GROUP_ID_PERUSER](#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)、[ZEPHYR_MGMT_GRP_BASIC](#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68)。

MCUmgr 组（Groups）。

<a id="r_gac5d8757a7ca945c77f405764b85ad5c5"></a>

```c
enum mcumgr_err_t { MGMT_ERR_EOK = 0 , MGMT_ERR_EUNKNOWN , MGMT_ERR_ENOMEM , MGMT_ERR_EINVAL , MGMT_ERR_ETIMEOUT , MGMT_ERR_ENOENT , MGMT_ERR_EBADSTATE , MGMT_ERR_EMSGSIZE , MGMT_ERR_ENOTSUP , MGMT_ERR_ECORRUPT , MGMT_ERR_EBUSY , MGMT_ERR_EACCESSDENIED , MGMT_ERR_UNSUPPORTED_TOO_OLD , MGMT_ERR_UNSUPPORTED_TOO_NEW , MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE , MGMT_ERR_EPERUSER = 256 }
```

相关声明：[mcumgr_err_t](#gac5d8757a7ca945c77f405764b85ad5c5)、[MGMT_ERR_EOK](#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)、[MGMT_ERR_EUNKNOWN](#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be)、[MGMT_ERR_ENOMEM](#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe)、[MGMT_ERR_EINVAL](#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7)、[MGMT_ERR_ETIMEOUT](#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55)、[MGMT_ERR_ENOENT](#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e)、[MGMT_ERR_EBADSTATE](#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787)、[MGMT_ERR_EMSGSIZE](#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)、[MGMT_ERR_ENOTSUP](#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758)、[MGMT_ERR_ECORRUPT](#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5)、[MGMT_ERR_EBUSY](#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1)、[MGMT_ERR_EACCESSDENIED](#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde)、[MGMT_ERR_UNSUPPORTED_TOO_OLD](#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054)、[MGMT_ERR_UNSUPPORTED_TOO_NEW](#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00)、[MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE](#ggac5d8757a7ca945c77f405764b85ad5c5a5f234dd0b9781bedcefb5c4627dccb1c)、[MGMT_ERR_EPERUSER](#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8)。

MCUmgr 错误码（Error Codes）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.6\_函数（Functions）

<a id="r_ga70379f21faacddb5cc4a66f37a576ea0"></a>

```c
void mgmt_register_group (struct mgmt_group *group)
```

相关声明：[mgmt_register_group](#ga70379f21faacddb5cc4a66f37a576ea0)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注册完整命令组（Command Group）。

<a id="r_ga87e98bdf47d1c7798098444f69ccf8b8"></a>

```c
void mgmt_unregister_group (struct mgmt_group *group)
```

相关声明：[mgmt_unregister_group](#ga87e98bdf47d1c7798098444f69ccf8b8)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注销完整命令组（Command Group）。

<a id="r_ga125e3a6d076cade80f2080915a06ac67"></a>

```c
void mgmt_groups_foreach (mgmt_groups_cb_t user_cb, void *user_data)
```

相关声明：[mgmt_groups_foreach](#ga125e3a6d076cade80f2080915a06ac67)、[mgmt_groups_cb_t](#ga9f63f42cd468ce85d0f800dc1472a5c8)。

遍历各组（Groups）。

<a id="r_ga620862436fad440b9d2b9d8112be4ad1"></a>

```c
const struct mgmt_handler * mgmt_find_handler (uint16_t group_id, uint16_t command_id)
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)、[mgmt_find_handler](#ga620862436fad440b9d2b9d8112be4ad1)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令处理程序（Command Handler）。

<a id="r_gae88bc30026fbff6530179a94ba8f11ae"></a>

```c
const struct mgmt_group * mgmt_find_group (uint16_t group_id)
```

相关声明：[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[mgmt_find_group](#gae88bc30026fbff6530179a94ba8f11ae)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令组（Command Group）。

<a id="r_gaec6ccbcaf28404b4b3662d5059f0a32b"></a>

```c
const struct mgmt_handler * mgmt_get_handler (const struct mgmt_group *group, uint16_t command_id)
```

相关声明：[mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)、[mgmt_get_handler](#gaec6ccbcaf28404b4b3662d5059f0a32b)、[mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

查找已注册的命令处理程序（Command Handler）。

## 11.7\_详细说明（Detailed Documentation）

<a id="ga4d22641395a665a911be715c2531fbd8"></a>

### `MGMT_CTXT_RC_RSN`

```c
#define MGMT_CTXT_RC_RSN ( mc)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

展开值（Value）：

```c
NULL
```

<a id="ga8027c2a587a835d92450f2935e66eea0"></a>

### `MGMT_CTXT_SET_RC_RSN`

```c
#define MGMT_CTXT_SET_RC_RSN ( mc, rsn )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

<a id="gabb62e7697ffb2a2f4e6d96abe28808a6"></a>

### `MGMT_HDR_SIZE`

```c
#define MGMT_HDR_SIZE 8
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

<a id="gabdd715ff5b7efe040f205edf0b00bc43"></a>

### `MGMT_RETURN_CHECK`

```c
#define MGMT_RETURN_CHECK ( ok)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

展开值（Value）：

```c
ok ? MGMT_ERR_EOK : MGMT_ERR_EMSGSIZE
```

在 MCUmgr 处理器（Handlers）的末尾使用：若达到消息大小限制（Message Size Limit），则返回错误；否则返回成功（OK）。

<a id="ga292686c742179758ca5b853fc21fe302"></a>

### `mgmt_alloc_rsp_fn`

```c
typedef void *(* mgmt_alloc_rsp_fn) (const void *src_buf, void *arg)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

分配适合保存响应（Response）的缓冲区。

如果提供源缓冲区（Source Buffer）`buf`，则将其用户数据（User Data）复制到新缓冲区中。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `src_buf` | 可选的源缓冲区（Source Buffer），用于从中复制用户数据（User Data）。 |
| `arg` | 可选的流处理器参数（Streamer Argument）。 |

**返回（Returns）**：返回值（Returns）：成功时为新分配的缓冲区（Buffer），失败时为 `NULL`。

<a id="ga9f63f42cd468ce85d0f800dc1472a5c8"></a>

### `mgmt_groups_cb_t`

```c
typedef bool(* mgmt_groups_cb_t) (const struct mgmt_group *group, void *user_data)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

组遍历回调（Group Iteration Callback）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 组（Group）。 |
| `user_data` | 用户提供的数据（User-supplied Data）。 |

**返回（Returns）**：返回值（Returns）：`true` 表示继续执行逐项回调（Foreach Callback），`false` 表示中止。

<a id="gaaafc2c73e1616340e29df6a1ba94c241"></a>

### `mgmt_handler_fn`

```c
typedef int(* mgmt_handler_fn) (struct smp_streamer *ctxt)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

处理请求（Request）并写入对应响应（Response）。

每个受支持的操作—标识符对（Op-ID Pair）都需要单独的处理程序（Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ctxt` | 要使用的 MCUmgr 上下文（Context）。 |

**返回（Returns）**：返回值（Returns）：成功编码响应时为 0，失败时为 `mcumgr_err_t` 错误码。

<a id="ga1346d5160823c5e43fce3e6cba9f8607"></a>

### `mgmt_reset_buf_fn`

```c
typedef void(* mgmt_reset_buf_fn) (void *buf, void *arg)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

将缓冲区长度重置为 0。

保留缓冲区的用户数据（User Data），但清除其有效载荷（Payload）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `buf` | 要重置的缓冲区（Buffer）。 |
| `arg` | 可选的流处理器参数（Streamer Argument）。 |

<a id="gac5d8757a7ca945c77f405764b85ad5c5"></a>

### `mcumgr_err_t`

```c
enum mcumgr_err_t
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

MCUmgr 错误码（Error Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_ERR_EOK` | 无错误，即成功（Success）。 |
| `MGMT_ERR_EUNKNOWN` | 未知错误（Unknown Error）。 |
| `MGMT_ERR_ENOMEM` | 内存不足（Insufficient Memory），可能没有足够空间容纳 CBOR 对象。 |
| `MGMT_ERR_EINVAL` | 输入值错误（Error in Input Value）。 |
| `MGMT_ERR_ETIMEOUT` | 操作超时（Operation Timed Out）。 |
| `MGMT_ERR_ENOENT` | 没有该文件／条目（No Such File/Entry）。 |
| `MGMT_ERR_EBADSTATE` | 当前状态（Current State）不允许执行该命令。 |
| `MGMT_ERR_EMSGSIZE` | 响应过大（Response Too Large）。 |
| `MGMT_ERR_ENOTSUP` | 不支持该命令（Command Not Supported）。 |
| `MGMT_ERR_ECORRUPT` | 数据损坏（Corrupt）。 |
| `MGMT_ERR_EBUSY` | 命令被其他命令的处理过程阻塞（Blocked）。 |
| `MGMT_ERR_EACCESSDENIED` | 访问特定函数、命令或资源（Resource）被拒绝。 |
| `MGMT_ERR_UNSUPPORTED_TOO_OLD` | 请求的 SMP MCUmgr 协议版本（Protocol Version）不受支持，版本过旧。 |
| `MGMT_ERR_UNSUPPORTED_TOO_NEW` | 请求的 SMP MCUmgr 协议版本（Protocol Version）不受支持，版本过新。 |
| `MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE` | 桥接连接（Bridged Connection）不可用。 |
| `MGMT_ERR_EPERUSER` | 用户错误（User Errors）从 256 开始定义。 |

<a id="ga81f98b9a0c3810f7d607b783f8e259b5"></a>

### `mcumgr_group_t`

```c
enum mcumgr_group_t
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

MCUmgr 组（Groups）。

前 64 个组（Group）保留供系统级 MCUmgr 命令使用。随后从组编号 64 起定义用户命令（Per-user Commands）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_GROUP_ID_OS` | 操作系统组（OS Group，Operating System Group）。 |
| `MGMT_GROUP_ID_IMAGE` | 镜像管理组（Image Management Group），用于上传固件镜像（Firmware Image）。 |
| `MGMT_GROUP_ID_STAT` | 统计管理组（Statistic Management Group），用于获取统计信息（Statistics）。 |
| `MGMT_GROUP_ID_SETTINGS` | 设置管理组（Settings Management Group，Config），用于读写设置。 |
| `MGMT_GROUP_ID_LOG` | 日志管理组（Log Management Group），未使用。 |
| `MGMT_GROUP_ID_CRASH` | 崩溃组（Crash Group），未使用。 |
| `MGMT_GROUP_ID_SPLIT` | 拆分镜像管理组（Split Image Management Group），未使用。 |
| `MGMT_GROUP_ID_RUN` | 运行组（Run Group），未使用。 |
| `MGMT_GROUP_ID_FS` | 文件系统组（FS Group，File System Group），用于执行文件输入／输出操作（File I/O）。 |
| `MGMT_GROUP_ID_SHELL` | Shell 管理组（Shell Management Group），用于执行 Shell 命令。 |
| `MGMT_GROUP_ID_ENUM` | 枚举管理组（Enumeration Management Group），用于列出受支持的命令组（Command Group）。 |
| `MGMT_GROUP_ID_TRANSPORT` | 传输管理组（Transport Management Group），采用默认组 ID，用于桥接传输（Bridging Transports）。 |
| `MGMT_GROUP_ID_PERUSER` | 用户组（User Groups）从 64 开始定义。 |
| `ZEPHYR_MGMT_GRP_BASIC` | Zephyr 特定组（Zephyr-specific Groups）的编号从 `PERUSER` 向下递减，以免与上游及用户定义的组冲突。此处为 Zephyr 特定的基本组（Basic Group）。 |

<a id="gae06a618f492f18e856742b4affab80dd"></a>

### `mcumgr_op_t`

```c
enum mcumgr_op_t
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h>
```

操作码（Opcodes），编码于头部（Header）的第一个字节中。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `MGMT_OP_READ` | 读取操作码（Read Op-code）。 |
| `MGMT_OP_READ_RSP` | 读取响应操作码（Read Response Op-code）。 |
| `MGMT_OP_WRITE` | 写入操作码（Write Op-code）。 |
| `MGMT_OP_WRITE_RSP` | 写入响应操作码（Write Response Op-code）。 |
| `MGMT_OP_COUNT` |  |

<a id="gae88bc30026fbff6530179a94ba8f11ae"></a>

### `mgmt_find_group()`

```c
const struct mgmt_group * mgmt_find_group ( uint16_t group_id)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

查找已注册的命令组（Command Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group_id` | 要查找的命令组的组标识符（Group ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为请求的组（Group），失败时为 `NULL`。

<a id="ga620862436fad440b9d2b9d8112be4ad1"></a>

### `mgmt_find_handler()`

```c
const struct mgmt_handler * mgmt_find_handler ( uint16_t group_id, uint16_t command_id )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

查找已注册的命令处理程序（Command Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group_id` | 要查找的命令所属的组（Group）。 |
| `command_id` | 要查找的命令标识符（Command ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为请求的命令处理程序（Command Handler），失败时为 `NULL`。

<a id="gaec6ccbcaf28404b4b3662d5059f0a32b"></a>

### `mgmt_get_handler()`

```c
const struct mgmt_handler * mgmt_get_handler ( const struct mgmt_group * group, uint16_t command_id )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

查找已注册的命令处理程序（Command Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 要查找的命令所属的组（Group）。 |
| `command_id` | 要查找的命令标识符（Command ID）。 |

**返回（Returns）**：返回值（Returns）：成功时为请求的命令处理程序（Command Handler），失败时为 `NULL`。

<a id="ga125e3a6d076cade80f2080915a06ac67"></a>

### `mgmt_groups_foreach()`

```c
void mgmt_groups_foreach ( mgmt_groups_cb_t user_cb, void * user_data )
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

遍历各组（Groups）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `user_cb` | 用户回调（User Callback） |
| `user_data` | 用户提供的数据（User-supplied Data）。 |

<a id="ga70379f21faacddb5cc4a66f37a576ea0"></a>

### `mgmt_register_group()`

```c
void mgmt_register_group ( struct mgmt_group * group)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

注册完整命令组（Command Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 要注册的组（Group）。 |

<a id="ga87e98bdf47d1c7798098444f69ccf8b8"></a>

### `mgmt_unregister_group()`

```c
void mgmt_unregister_group ( struct mgmt_group * group)
```

```c
#include <zephyr/mgmt/mcumgr/mgmt/mgmt.h>
```

注销完整命令组（Command Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 要注册的组（Group）。 |


## 11.8\_原页交叉引用（Cross References）

- [枚举管理（Enumeration Management）](../api_protocol_topic_reference/P028_枚举管理（Enumeration Management）.md)
- [文件系统管理（File System Management）](../api_lifecycle_capability_topic_reference/P007_文件系统管理（File System Management）.md)
- [映像管理（Image Management）](P010_映像管理（Image Management）.md)
- [操作系统管理（OS Management）](../api_lifecycle_capability_topic_reference/P008_操作系统管理（OS Management）.md)
- [设置管理（Settings Management）](../api_auxiliary_topic_reference/P012_设置管理（Settings Management）.md)
- [命令行管理（Shell Management）](../shell_management_reference/P004_mcumgr_Shell管理接口.md)
- [统计信息管理（Statistics Management）](../api_service_topic_reference/P014_统计信息管理（Statistics Management）.md)
- [传输管理（Transport management）](../api_coap_trusted_topic_reference/P010_传输管理（Transport management）.md)
- [Zephyr 基础管理（Zephyr Basic Management）](../api_extension_topic_reference/P018_Zephyr 基础管理（Zephyr Basic Management）.md)
- [mgmt_handler](../system_service_model_reference/P069_mgmt_handler_结构体.md)
- [mgmt_group](../system_service_model_reference/P068_mgmt_group_结构体.md)
- [smp_streamer](../system_service_model_reference/P080_smp_streamer_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [group](../posix_system_model_reference/P003_group_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [zephyr/mgmt/mcumgr/mgmt/mgmt.h](../api_file_network_device_reference/P023_zephyr__mgmt__mcumgr__mgmt__mgmt.h_文件参考.md)
- [zephyr/mgmt/mcumgr/mgmt/mgmt_defines.h](../api_file_service_reference/P022_zephyr__mgmt__mcumgr__mgmt__mgmt_defines.h_文件参考.md)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a5f234dd0b9781bedcefb5c4627dccb1c"></a>
<a id="ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5ad5273bf46818cd7b6530fb3353ad35f2"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726"></a>
<a id="gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68"></a>
<a id="ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4"></a>
<a id="ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7"></a>
<a id="ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9"></a>
<a id="ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543"></a>
<a id="ggae06a618f492f18e856742b4affab80dda4105c10d17622b7de6a8f14c036f3498"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_映像管理（Image Management）.md) · [返回大纲](大纲.md) · [下一章](P012_连接端口（Pad）.md)
