---
id: learning.zephyr-docs.bluetooth-service-model-reference.page-136
title: bt_ots_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第136章\_bt\_ots\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__ots__cb.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

对象传输服务（OTS）的回调结构。

```c
#include <zephyr/bluetooth/services/ots.h>
```

<a id="details"></a>

对象传输服务（OTS）的回调结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 136.1\_数据成员（Data Fields）

<a id="r_a0c95b2bc382474be3c1ae849936a8206"></a>

```c
int(* obj_created )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const struct bt_ots_obj_add_param *add_param, struct bt_ots_obj_created_desc *created_desc)
```

相关声明：[obj_created](#a0c95b2bc382474be3c1ae849936a8206)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[bt_ots_obj_add_param](P142_bt_ots_obj_add_param_结构体.md)、[bt_ots_obj_created_desc](P143_bt_ots_obj_created_desc_结构体.md)。

对象已创建（Object created）回调。

<a id="r_a2fd78b43691e83c1faa86c1748ab2359"></a>

```c
int(* obj_deleted )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id)
```

相关声明：[obj_deleted](#a2fd78b43691e83c1faa86c1748ab2359)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

对象已删除（Object deleted）回调。

<a id="r_ae8602aef0fd001d6768dc20c8873742d"></a>

```c
void(* obj_selected )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id)
```

相关声明：[obj_selected](#ae8602aef0fd001d6768dc20c8873742d)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

对象已选中（Object selected）回调。

<a id="r_ab67ca0032b8b2fd9b8fbe6c117c186dd"></a>

```c
ssize_t(* obj_read )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id, void **data, size_t len, off_t offset)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[obj_read](#ab67ca0032b8b2fd9b8fbe6c117c186dd)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

对象读取（Object read）回调。

<a id="r_ae31da190c9c6bee086e4d7f8fcd6fbb5"></a>

```c
ssize_t(* obj_write )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const void *data, size_t len, off_t offset, size_t rem)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[obj_write](#ae31da190c9c6bee086e4d7f8fcd6fbb5)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

对象写入（Object write）回调。

<a id="r_a600fa13a97f39e3bd53c524039e2733c"></a>

```c
void(* obj_name_written )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const char *cur_name, const char *new_name)
```

相关声明：[obj_name_written](#a600fa13a97f39e3bd53c524039e2733c)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)。

对象名称写入（Object name written）回调。

<a id="r_a2ef2245c017015b81c0f276f00fd6f79"></a>

```c
int(* obj_cal_checksum )(struct bt_ots *ots, struct bt_conn *conn, uint64_t id, off_t offset, size_t len, void **data)
```

相关声明：[obj_cal_checksum](#a2ef2245c017015b81c0f276f00fd6f79)、[bt_ots](P135_bt_ots_结构体.md)、[bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)、[uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)、[off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)。

对象校验和计算（Object Calculate checksum）回调。

## 136.2\_详细说明（Detailed Documentation）

<a id="a2ef2245c017015b81c0f276f00fd6f79"></a>

### `obj_cal_checksum`

```c
int(* bt_ots_cb::obj_cal_checksum) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id, off_t offset, size_t len, void **data)
```

对象校验和计算（Object Calculate checksum）回调。

执行对象动作控制点（OACP）的计算校验和（Calculate Checksum）过程时，会调用此回调。由于对象数据对对象传输服务（OTS）是不透明的，只有应用知道数据位于何处，因此应用应返回实际对象数据的指针。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] ots` | 对象传输服务（OTS）实例。 |
| `[in] conn` | 写入对象的连接。 |
| `[in] id` | 对象标识（Object ID）。 |
| `[in] offset` | 需要进行计算的对象内容的第一个八位字节。 |
| `[in] len` | 对象名称的长度，以八位字节计。

译注：官方原文此处写作“object name”；该参数位于对象校验和计算回调中，原文表述照录保留。 |
| `[out] data` | 实际对象数据的指针。 |

**返回（Returns）**：返回值：返回 0 表示接受，任何负值表示拒绝。

<a id="a0c95b2bc382474be3c1ae849936a8206"></a>

### `obj_created`

```c
int(* bt_ots_cb::obj_created) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const struct bt_ots_obj_add_param *add_param, struct bt_ots_obj_created_desc *created_desc)
```

对象已创建（Object created）回调。

每当创建新对象时都会调用此回调。如果应用没有足够资源保存此新对象，可返回错误以拒绝请求。当服务器通过 `bt_ots_obj_add()` API 创建新对象时，也会触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 请求创建对象的连接；如果对象由 `bt_ots_obj_add()` 创建，则为 `NULL`。 |
| `id` | 对象标识（Object ID）。 |
| `add_param` | 请求创建对象时的参数。 |
| `created_desc` | 已创建对象的描述符，必须由此回调的接收方填写。 |

**返回（Returns）**：返回值：成功时返回 0，错误时返回负值。不支持对象类型时返回 `-ENOTSUP`；没有可用空间存储新对象时返回 `-ENOMEM`；所提供参数无效时返回 `-EINVAL`；其他负值被视为一般操作失败。

<a id="a2fd78b43691e83c1faa86c1748ab2359"></a>

### `obj_deleted`

```c
int(* bt_ots_cb::obj_deleted) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id)
```

对象已删除（Object deleted）回调。

每当删除对象时都会调用此回调。当服务器通过 `bt_ots_obj_delete()` API 删除对象时，也会触发此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 删除对象的连接；如果请求来自服务器，则为 `NULL`。 |
| `id` | 对象标识（Object ID）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `When` | 使用负值表示错误，此时对象删除过程会中止，并向客户端返回相应的失败状态。 |

**返回（Returns）**：返回值：成功时返回 0。对象已锁定时返回 `-EBUSY`；通常不应由应用返回此值，因为 OTS 层会跟踪对象访问情况，此时向客户端返回对象已锁定状态。其他错误返回其他负值，并向客户端返回一般操作失败状态。

<a id="a600fa13a97f39e3bd53c524039e2733c"></a>

### `obj_name_written`

```c
void(* bt_ots_cb::obj_name_written) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const char *cur_name, const char *new_name)
```

对象名称写入（Object name written）回调。

写入对象名称时调用此回调，用于通知应用：OTS 服务实现即将更新对象名称。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 写入对象名称的连接。 |
| `id` | 对象标识（Object ID）。 |
| `cur_name` | 当前对象名称。 |
| `new_name` | 新对象名称。 |

<a id="ab67ca0032b8b2fd9b8fbe6c117c186dd"></a>

### `obj_read`

```c
ssize_t(* bt_ots_cb::obj_read) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id, void **data, size_t len, off_t offset)
```

对象读取（Object read）回调。

在对象读取操作期间，会多次调用此回调。OTS 模块将不断向应用请求后续对象分片，直到读取操作完成。`data` 参数为 `NULL` 表示读取操作结束。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 读取对象的连接。 |
| `id` | 对象标识（Object ID）。 |
| `data` | 输入：读取操作完成时为 `NULL`。输出：下一个待发送的数据块。 |
| `len` | 客户端请求的剩余长度。 |
| `offset` | 对象数据偏移量。 |

**返回（Returns）**：返回值：通过 `data` 参数发送的数据长度。此值必须小于或等于 `len` 参数；错误时返回负值。

<a id="ae8602aef0fd001d6768dc20c8873742d"></a>

### `obj_selected`

```c
void(* bt_ots_cb::obj_selected) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id)
```

对象已选中（Object selected）回调。

成功选择对象时调用此回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 选择新对象的连接。 |
| `id` | 对象标识（Object ID）。 |

<a id="ae31da190c9c6bee086e4d7f8fcd6fbb5"></a>

### `obj_write`

```c
ssize_t(* bt_ots_cb::obj_write) (struct bt_ots *ots, struct bt_conn *conn, uint64_t id, const void *data, size_t len, off_t offset, size_t rem)
```

对象写入（Object write）回调。

在对象写入操作期间，会多次调用此回调。OTS 模块将不断向应用提供后续对象分片，直到写入操作完成。OTS 模块会验证每个写入分片的偏移量和长度，确保其位于对象已分配大小的范围内。剩余长度表示尚待写入的数据长度，每次写入都会减少，直到最后一个写入分片时降为 0。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `ots` | 对象传输服务（OTS）实例。 |
| `conn` | 写入对象的连接。 |
| `id` | 对象标识（Object ID）。 |
| `data` | 下一个待写入的数据块。 |
| `len` | 缓冲区中当前数据块的长度。 |
| `offset` | 对象数据偏移量。 |
| `rem` | 写入操作的剩余长度。 |

**返回（Returns）**：返回值：成功时返回写入的字节数；如果写入字节数与 `len` 不符，则向 L2CAP 层返回 `-EIO`。错误时返回负值。`-EINPROGRESS` 有特殊含义，目前不受支持，不应返回此值。

本数据类型文档由以下文件生成：

- `zephyr/bluetooth/services/ots.h`

## 136.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/services/ots.h](https://docs.zephyrproject.org/latest/doxygen/html/ots_8h_source.html)
- [bt_ots](P135_bt_ots_结构体.md)
- [bt_conn](../bluetooth_connection_model_reference/P002_bt_conn_结构体.md)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [bt_ots_obj_add_param](P142_bt_ots_obj_add_param_结构体.md)
- [bt_ots_obj_created_desc](P143_bt_ots_obj_created_desc_结构体.md)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [off_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a98a5cc5f4a350bf5652565021a2f239f)
- [bt_ots_obj_add()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#gabf59844edd0ffd434acd94bad9a7b52c)
- [bt_ots_obj_delete()](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__ots.html#ga872ba5a73fa4e617b9d48e7361af74c7)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P135_bt_ots_结构体.md) · [返回大纲](大纲.md) · [下一章](P137_bt_ots_client_结构体.md)
