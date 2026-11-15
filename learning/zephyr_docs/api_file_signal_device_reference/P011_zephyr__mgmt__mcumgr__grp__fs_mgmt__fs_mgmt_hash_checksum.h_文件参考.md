---
id: learning.zephyr-docs.api-file-signal-device-reference.page-11
title: zephyr__mgmt__mcumgr__grp__fs_mgmt__fs_mgmt_hash_checksum.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_mgmt\_\_mcumgr\_\_grp\_\_fs\_mgmt\_\_fs\_mgmt\_hash\_checksum.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/fs__mgmt__hash__checksum_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <zephyr/kernel.h>
#include <zephyr/fs/fs.h>
```

查看此文件的源码。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_fs_5Fmgmt_5Fhash_5Fchecksum_5Fgroup"></a>

```c
struct fs_mgmt_hash_checksum_group
```

相关声明：[fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)。

整个哈希/校验和组（Hash/Checksum Group）的处理程序集合。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.2\_类型定义（Typedefs）

<a id="r_a1a3db209871cb21f90c7feb5fda4db62"></a>

```c
typedef int(* fs_mgmt_hash_checksum_handler_fn) (struct fs_file_t *file, uint8_t *output, size_t *out_len, size_t len)
```

相关声明：[fs_mgmt_hash_checksum_handler_fn](#a1a3db209871cb21f90c7feb5fda4db62)、[fs_file_t](../storage/P038_文件系统文件对象.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

生成散列或校验和（Hash/Checksum）时调用的函数。

<a id="r_a97669e080a8bdaee3bb8f2593ba99639"></a>

```c
typedef void(* fs_mgmt_hash_checksum_list_cb) (const struct fs_mgmt_hash_checksum_group *group, void *user_data)
```

相关声明：[fs_mgmt_hash_checksum_list_cb](#a97669e080a8bdaee3bb8f2593ba99639)、[fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

调用时传入散列／校验和详细信息（Hash/Checksum Details）的函数。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.3\_函数（Functions）

<a id="r_a0f429c6e46361838794a2fe733f4e2cb"></a>

```c
void fs_mgmt_hash_checksum_register_group (struct fs_mgmt_hash_checksum_group *group)
```

相关声明：[fs_mgmt_hash_checksum_register_group](#a0f429c6e46361838794a2fe733f4e2cb)、[fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注册完整的散列／校验和组（Hash/Checksum Group）。

<a id="r_a5f97144885d0a72dcab02de690511452"></a>

```c
void fs_mgmt_hash_checksum_unregister_group (struct fs_mgmt_hash_checksum_group *group)
```

相关声明：[fs_mgmt_hash_checksum_unregister_group](#a5f97144885d0a72dcab02de690511452)、[fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)、[group](../posix_system_model_reference/P003_group_结构体.md)。

注销完整的散列／校验和组（Hash/Checksum Group）。

<a id="r_a5066ea99fe3f80652c364f9f779630d7"></a>

```c
const struct fs_mgmt_hash_checksum_group * fs_mgmt_hash_checksum_find_handler (const char *name)
```

相关声明：[fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)、[fs_mgmt_hash_checksum_find_handler](#a5066ea99fe3f80652c364f9f779630d7)。

查找已注册的散列／校验和处理程序（Hash/Checksum Handler）。

<a id="r_a5b299016aa5dab661395dbfb655af16c"></a>

```c
void fs_mgmt_hash_checksum_find_handlers (fs_mgmt_hash_checksum_list_cb cb, void *user_data)
```

相关声明：[fs_mgmt_hash_checksum_find_handlers](#a5b299016aa5dab661395dbfb655af16c)、[fs_mgmt_hash_checksum_list_cb](#a97669e080a8bdaee3bb8f2593ba99639)。

对所有支持的散列／校验和类型（Hash/Checksum Types）运行回调。

## 11.4\_详细说明（Detailed Documentation）

<a id="a1a3db209871cb21f90c7feb5fda4db62"></a>

### `fs_mgmt_hash_checksum_handler_fn`

```c
typedef int(* fs_mgmt_hash_checksum_handler_fn) (struct fs_file_t *file, uint8_t *output, size_t *out_len, size_t len)
```

生成散列或校验和（Hash/Checksum）时调用的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `file` | 已打开文件的上下文（Opened File Context）。 |
| `output` | 散列／校验和输出缓冲区（Output Buffer）。 |
| `out_len` | 更新为输入数据大小（Input Data Size）。 |
| `len` | 要计算散列／校验和的数据最大长度（Maximum Data Length）。 |

返回（Returns）：成功时为0，失败时为负错误码。

<a id="a97669e080a8bdaee3bb8f2593ba99639"></a>

### `fs_mgmt_hash_checksum_list_cb`

```c
typedef void(* fs_mgmt_hash_checksum_list_cb) (const struct fs_mgmt_hash_checksum_group *group, void *user_data)
```

调用时传入散列／校验和详细信息（Hash/Checksum Details）的函数。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 受支持的散列／校验和（Hash/Checksum）的详细信息。 |
| `user_data` | 用户传给调用函数的值（User-supplied Value）。 |

<a id="a5066ea99fe3f80652c364f9f779630d7"></a>

### `fs_mgmt_hash_checksum_find_handler()`

```c
const struct fs_mgmt_hash_checksum_group * fs_mgmt_hash_checksum_find_handler ( const char * name)
```

查找已注册的散列／校验和处理程序（Hash/Checksum Handler）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `name` | 要查找的散列／校验和组名称（Group Name）。 |

**返回（Returns）**：**返回值（Returns）：**成功返回所请求的散列／校验和处理程序（Handler），失败返回 `NULL`。

<a id="a5b299016aa5dab661395dbfb655af16c"></a>

### `fs_mgmt_hash_checksum_find_handlers()`

```c
void fs_mgmt_hash_checksum_find_handlers ( fs_mgmt_hash_checksum_list_cb cb, void * user_data )
```

对所有支持的散列／校验和类型（Hash/Checksum Types）运行回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `cb` | 为每种散列／校验和类型（Hash/Checksum Type）调用的回调函数。 |
| `user_data` | 随回调函数传回的数据（Data）。 |

<a id="a0f429c6e46361838794a2fe733f4e2cb"></a>

### `fs_mgmt_hash_checksum_register_group()`

```c
void fs_mgmt_hash_checksum_register_group ( struct fs_mgmt_hash_checksum_group * group)
```

注册完整的散列／校验和组（Hash/Checksum Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 要注册的组（Group）。 |

<a id="a5f97144885d0a72dcab02de690511452"></a>

### `fs_mgmt_hash_checksum_unregister_group()`

```c
void fs_mgmt_hash_checksum_unregister_group ( struct fs_mgmt_hash_checksum_group * group)
```

注销完整的散列／校验和组（Hash/Checksum Group）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `group` | 要注册的组（Group）。 |


## 11.5\_原页交叉引用（Cross References）

- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/fs/fs.h](../api_source_supplement_reference/P074_fs.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P276_fs_mgmt_hash_checksum.h_源码浏览.md)
- [fs_mgmt_hash_checksum_group](../system_service_model_reference/P040_fs_mgmt_hash_checksum_group_结构体.md)
- [fs_file_t](../storage/P038_文件系统文件对象.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [group](../posix_system_model_reference/P003_group_结构体.md)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__net__http__frame.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__drivers__interrupt_controller__intc_bcm283x.h_文件参考.md)
