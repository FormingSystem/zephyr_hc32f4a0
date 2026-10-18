---
id: learning.zephyr-docs.api-file-display-management-reference.page-15
title: zephyr__drivers__uart__serial_test.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_drivers\_\_uart\_\_serial\_test.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/serial__test_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <errno.h>
#include <zephyr/device.h>
```

查看此文件的源码。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 15.1\_类型定义（Typedefs）

<a id="r_a04f02df85d720ccd5ce02ab9e217dba3"></a>

```c
typedef void(* serial_vnd_write_cb_t) (const struct device *dev, void *user_data)
```

相关声明：[serial_vnd_write_cb_t](#a04f02df85d720ccd5ce02ab9e217dba3)、[device](../device_reference/P002_设备对象结构.md)。

向虚拟串口（Virtual Serial Port）写入字节后调用的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.2\_函数（Functions）

<a id="r_a2b7d97302cb3546cfc8f384f4a7c1a4a"></a>

```c
int serial_vnd_queue_in_data (const struct device *dev, const unsigned char *data, uint32_t size)
```

相关声明：[serial_vnd_queue_in_data](#a2b7d97302cb3546cfc8f384f4a7c1a4a)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

将数据入队，供虚拟串口（Virtual Serial Port）读取。

<a id="r_a4275edbc443677d2c0f08100834977a7"></a>

```c
uint32_t serial_vnd_out_data_size_get (const struct device *dev)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[serial_vnd_out_data_size_get](#a4275edbc443677d2c0f08100834977a7)、[device](../device_reference/P002_设备对象结构.md)。

返回已写入但尚未读取的数据大小（Unread Written Data Size）。

<a id="r_ab9b60bf8d62db2be3ad530cd0a78aedd"></a>

```c
uint32_t serial_vnd_read_out_data (const struct device *dev, unsigned char *data, uint32_t size)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[serial_vnd_read_out_data](#ab9b60bf8d62db2be3ad530cd0a78aedd)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

读取写入虚拟串口（Virtual Serial Port）的数据。

<a id="r_a1e2a3d82504b34d5b4590afc67172c9e"></a>

```c
uint32_t serial_vnd_peek_out_data (const struct device *dev, unsigned char *data, uint32_t size)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[serial_vnd_peek_out_data](#a1e2a3d82504b34d5b4590afc67172c9e)、[device](../device_reference/P002_设备对象结构.md)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

查看写入虚拟串口（Virtual Serial Port）的数据而不消耗它，即窥视（Peek）。

<a id="r_a4908343c26e5846abf977befe2c5dbbe"></a>

```c
void serial_vnd_set_callback (const struct device *dev, serial_vnd_write_cb_t callback, void *user_data)
```

相关声明：[serial_vnd_set_callback](#a4908343c26e5846abf977befe2c5dbbe)、[device](../device_reference/P002_设备对象结构.md)、[serial_vnd_write_cb_t](#a04f02df85d720ccd5ce02ab9e217dba3)。

设置虚拟串口（Virtual Serial Port）的写入回调。

## 15.3\_详细说明（Detailed Documentation）

<a id="a04f02df85d720ccd5ce02ab9e217dba3"></a>

### `serial_vnd_write_cb_t`

```c
typedef void(* serial_vnd_write_cb_t) (const struct device *dev, void *user_data)
```

向虚拟串口（Virtual Serial Port）写入字节后调用的回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |
| `user_data` | 用户数据（User Data）。 |

<a id="a4275edbc443677d2c0f08100834977a7"></a>

### `serial_vnd_out_data_size_get()`

```c
uint32_t serial_vnd_out_data_size_get ( const struct device * dev)
```

返回已写入但尚未读取的数据大小（Unread Written Data Size）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |

**返回（Returns）**：返回值：输出数据大小（Output Data Size），单位为字节。

<a id="a1e2a3d82504b34d5b4590afc67172c9e"></a>

### `serial_vnd_peek_out_data()`

```c
uint32_t serial_vnd_peek_out_data ( const struct device * dev, unsigned char * data, uint32_t size )
```

查看写入虚拟串口（Virtual Serial Port）的数据而不消耗它，即窥视（Peek）。

读取数据而不消耗它。后续调用 `serial_vnd_peek_out_data()` 或 `serial_vnd_read_out_data()` 时，仍会再次返回这些数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |
| `data` | 输出缓冲区地址（Output Buffer Address），不得为 `NULL`。 |
| `size` | 数据大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Number` | 写入输出缓冲区的字节数（Bytes）。 |

**警告（Warning）**：警告：涉及多次读取数据的场景必须防止并发读取（Concurrent Reads），可禁止所有读取者被抢占（Preempted），或使用互斥锁（Mutex）控制读取。

<a id="a2b7d97302cb3546cfc8f384f4a7c1a4a"></a>

### `serial_vnd_queue_in_data()`

```c
int serial_vnd_queue_in_data ( const struct device * dev, const unsigned char * data, uint32_t size )
```

将数据入队，供虚拟串口（Virtual Serial Port）读取。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |
| `data` | 数据地址（Data Address）。 |
| `size` | 数据大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Number` | 已写入的字节数（Bytes）。 |

**警告（Warning）**：警告：涉及多个写入者写入虚拟串口的场景必须防止并发写入（Concurrent Writes），可禁止所有写入者被抢占（Preempted），或使用互斥锁（Mutex）控制写入。

<a id="ab9b60bf8d62db2be3ad530cd0a78aedd"></a>

### `serial_vnd_read_out_data()`

```c
uint32_t serial_vnd_read_out_data ( const struct device * dev, unsigned char * data, uint32_t size )
```

读取写入虚拟串口（Virtual Serial Port）的数据。

消耗数据，因此后续调用 `serial_vnd_read_out_data()` 时将不再包含这些数据。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |
| `data` | 输出缓冲区地址（Output Buffer Address），可为 `NULL` 以丢弃数据。 |
| `size` | 数据大小，单位为字节。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `Number` | 写入输出缓冲区的字节数（Bytes）。 |

**警告（Warning）**：警告：涉及多次读取数据的场景必须防止并发读取（Concurrent Reads），可禁止所有读取者被抢占（Preempted），或使用互斥锁（Mutex）控制读取。

<a id="a4908343c26e5846abf977befe2c5dbbe"></a>

### `serial_vnd_set_callback()`

```c
void serial_vnd_set_callback ( const struct device * dev, serial_vnd_write_cb_t callback, void * user_data )
```

设置虚拟串口（Virtual Serial Port）的写入回调。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | 虚拟串口地址（Virtual Serial Port Address）。 |
| `callback` | 每次向端口写入后调用的函数（Function）。 |
| `user_data` | 传给回调的不透明数据（Opaque Data）。 |


## 15.4\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [查看此文件的源码。](../api_source_supplement_reference/P177_serial_test.h_源码浏览.md)
- [device](../device_reference/P002_设备对象结构.md)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)

<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_zephyr__mpipe__mpipe_structure.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__drivers__uaol.h_文件参考.md)
