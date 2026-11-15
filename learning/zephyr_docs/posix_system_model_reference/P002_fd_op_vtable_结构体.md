---
id: learning.zephyr-docs.posix-system-model-reference.page-2
title: fd_op_vtable_结构体
kind: reference
status: maintained
domains: [zephyr, posix, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structfd__op__vtable.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_fd\_op\_vtable\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structfd__op__vtable.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

文件描述符（File Descriptor）的虚方法表。

```c
#include <zephyr/sys/fdtable.h>
```

<a id="details"></a>

文件描述符虚方法表（File descriptor virtual method table）。目前，除读取、写入和关闭（read/write/close）之外的所有操作都通过 `ioctl` 方法执行。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a3cb055e9f1e5c62ec26d722476671062"></a>

```c
ssize_t(* read )(void *obj, void *buf, size_t sz)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[read](#a8caad0c1e96cdb67ef02f918ab8aff17)。

<a id="r_aa2e65b5916218e5c8b06e143d41e0257"></a>

```c
ssize_t(* read_offs )(void *obj, void *buf, size_t sz, size_t offset)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[read_offs](#a6748a61747f3ffd0c16174e5ad6d9829)。

<a id="r_a2cc13673e6545c6a0c65658e94a24290"></a>

```c
};
```

```c
union {
```

<a id="r_a5fe4bb6f728db0a8bee8cf30525e0168"></a>

```c
ssize_t(* write )(void *obj, const void *buf, size_t sz)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[write](#ac59ee326ff54a6a2324bf3425f4a3d5a)。

<a id="r_ac7f5c0bc51cc0210776c3ccc54004404"></a>

```c
ssize_t(* write_offs )(void *obj, const void *buf, size_t sz, size_t offset)
```

相关声明：[ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)、[write_offs](#a48338a129571b7c76abc4a1b5a6372af)。

<a id="r_a5bab4b02306d78ec1943219d2478ca51"></a>

```c
};
```

```c
union {
```

<a id="r_aa5eb03c4b2aff4131d4232309d201fd5"></a>

```c
int(* close )(void *obj)
```

相关声明：[close](#a80704417dfe01e8289d1f7fca819f5f1)。

<a id="r_af564578c498ddf646038ad83b2f196e3"></a>

```c
int(* close2 )(void *obj, int fd)
```

相关声明：[close2](#a139c24a21d141ccfdc7b00cf821f9a5e)。

<a id="r_a857669958f9ff29d4f29aca68ff53943"></a>

```c
};
```

<a id="r_aff079f05422413a0df3394ddfecc0298"></a>

```c
int(* ioctl )(void *obj, unsigned int request, va_list args)
```

相关声明：[ioctl](#aff079f05422413a0df3394ddfecc0298)、[unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)。

## 2.2\_详细说明（Detailed Documentation）

<a id="a2cc13673e6545c6a0c65658e94a24290"></a>

### `[union]`

```c
union { ... } fd_op_vtable
```

<a id="a857669958f9ff29d4f29aca68ff53943"></a>

### `[union]`

```c
union { ... } fd_op_vtable
```

<a id="a5bab4b02306d78ec1943219d2478ca51"></a>

### `[union]`

```c
union { ... } fd_op_vtable
```

<a id="a80704417dfe01e8289d1f7fca819f5f1"></a>

### `close`

```c
int(* fd_op_vtable::close) (void *obj)
```

<a id="a139c24a21d141ccfdc7b00cf821f9a5e"></a>

### `close2`

```c
int(* fd_op_vtable::close2) (void *obj, int fd)
```

<a id="aff079f05422413a0df3394ddfecc0298"></a>

### `ioctl`

```c
int(* fd_op_vtable::ioctl) (void *obj, unsigned int request, va_list args)
```

<a id="a8caad0c1e96cdb67ef02f918ab8aff17"></a>

### `read`

```c
ssize_t(* fd_op_vtable::read) (void *obj, void *buf, size_t sz)
```

<a id="a6748a61747f3ffd0c16174e5ad6d9829"></a>

### `read_offs`

```c
ssize_t(* fd_op_vtable::read_offs) (void *obj, void *buf, size_t sz, size_t offset)
```

<a id="ac59ee326ff54a6a2324bf3425f4a3d5a"></a>

### `write`

```c
ssize_t(* fd_op_vtable::write) (void *obj, const void *buf, size_t sz)
```

<a id="a48338a129571b7c76abc4a1b5a6372af"></a>

### `write_offs`

```c
ssize_t(* fd_op_vtable::write_offs) (void *obj, const void *buf, size_t sz, size_t offset)
```

本数据类型文档由以下文件生成：

- `zephyr/sys/fdtable.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/sys/fdtable.h](https://docs.zephyrproject.org/latest/doxygen/html/fdtable_8h_source.html)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [unsigned](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a4089fb16419d359081465355db05f846)
- [fd_op_vtable](P002_fd_op_vtable_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_dirent_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_group_结构体.md)
