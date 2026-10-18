---
id: learning.zephyr-docs.storage.nvmemextra-2
title: NVMEM公共头文件
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nvmem_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第20章\_NVMEM公共头文件

原文：[nvmem_8h](https://docs.zephyrproject.org/latest/doxygen/html/nvmem_8h.html)。读取日期：2026-10-13，`latest`。

`zephyr/nvmem.h` 是**非易失性存储器（Non-Volatile Memory，NVMEM）**公共头文件。官方页面列出其依赖头文件、数据结构、宏和函数，源文件见[官方头文件源码](../memory_retention_reference/P001_NVMEM公共头文件源码.md)。

## 20.1\_依赖与数据结构

原页列出的头文件依赖如下：

```c
#include <sys/types.h>
#include <zephyr/device.h>
#include <zephyr/devicetree.h>
#include <zephyr/devicetree/nvmem.h>
#include <zephyr/sys/byteorder.h>
```

数据结构 [`struct nvmem_cell`](P019_NVMEM数据单元结构.md) 表示 NVMEM 数据单元。详细的宏参数和函数约束见[NVMEM接口参考](P013_NVMEM接口参考.md)。

## 20.2\_静态初始化宏

下列宏都用于取得 `struct nvmem_cell` 的**静态初始化器（Static Initializer）**。`node_id` 是设备树节点标识；`name` 为名称，`idx` 为索引；`inst` 是驱动兼容类型 `DT_DRV_COMPAT` 的实例编号；`default_value` 是回退值。

| 宏声明 | 中文说明 |
| --- | --- |
| `NVMEM_CELL_INIT(node_id)` | 从数据单元节点取得初始化器 |
| `NVMEM_CELL_GET_BY_NAME(node_id, name)` | 按名称取得初始化器 |
| `NVMEM_CELL_INST_GET_BY_NAME(inst, name)` | 从驱动兼容类型实例中按名称取得初始化器 |
| `NVMEM_CELL_GET_BY_NAME_OR(node_id, name, default_value)` | 按名称取得初始化器，带回退值 |
| `NVMEM_CELL_INST_GET_BY_NAME_OR(inst, name, default_value)` | 从驱动实例中按名称取得初始化器，带回退值 |
| `NVMEM_CELL_GET_BY_IDX(node_id, idx)` | 按索引取得初始化器 |
| `NVMEM_CELL_INST_GET_BY_IDX(inst, idx)` | 从驱动实例中按索引取得初始化器 |
| `NVMEM_CELL_GET_BY_IDX_OR(node_id, idx, default_value)` | 按索引取得初始化器，带回退值 |
| `NVMEM_CELL_INST_GET_BY_IDX_OR(inst, idx, default_value)` | 从驱动实例中按索引取得初始化器，带回退值 |

## 20.3\_读写与状态检查

以下函数读取或写入数据单元，并查询是否就绪、是否只读。原页声明中的 `static` 表示静态函数。

```c
int nvmem_cell_read(const struct nvmem_cell *cell, void *data, off_t off, size_t len);
int nvmem_cell_write(const struct nvmem_cell *cell, const void *data, off_t off, size_t len);
static bool nvmem_cell_is_ready(const struct nvmem_cell *cell);
static bool nvmem_cell_is_read_only(const struct nvmem_cell *cell);
```

[`nvmem_cell_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga5db94733cecfd4b46dd87ee07128d58d) 从数据单元读取数据；[`nvmem_cell_write()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gaef749ffc4b49e2e37b489fab2d8fa6b4) 向数据单元写入数据；[`nvmem_cell_is_ready()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#ga614cac8acc913cb2f7b62c2f0d625421) 检查就绪状态；[`nvmem_cell_is_read_only()`](https://docs.zephyrproject.org/latest/doxygen/html/group__nvmem__interface.html#gac8abd20a158e3c304c73d6cb7e8cc50a) 检查只读状态。

## 20.4\_整数的字节序读写

函数名中的 `le` 表示**小端字节序（Little Endian，LE）**，`be` 表示**大端字节序（Big Endian，BE）**；末尾数字表示读写值的位数。读取接口把值存入指针参数，写入接口直接接受值。48 位数据使用 [`uint64_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1) 承载，完整声明如下。

```c
static int nvmem_cell_read_le16(const struct nvmem_cell *cell, uint16_t *val, off_t off);
static int nvmem_cell_read_be16(const struct nvmem_cell *cell, uint16_t *val, off_t off);
static int nvmem_cell_read_le32(const struct nvmem_cell *cell, uint32_t *val, off_t off);
static int nvmem_cell_read_be32(const struct nvmem_cell *cell, uint32_t *val, off_t off);
static int nvmem_cell_read_le48(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static int nvmem_cell_read_be48(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static int nvmem_cell_read_le64(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static int nvmem_cell_read_be64(const struct nvmem_cell *cell, uint64_t *val, off_t off);
static int nvmem_cell_write_le16(const struct nvmem_cell *cell, uint16_t val, off_t off);
static int nvmem_cell_write_be16(const struct nvmem_cell *cell, uint16_t val, off_t off);
static int nvmem_cell_write_le32(const struct nvmem_cell *cell, uint32_t val, off_t off);
static int nvmem_cell_write_be32(const struct nvmem_cell *cell, uint32_t val, off_t off);
static int nvmem_cell_write_le48(const struct nvmem_cell *cell, uint64_t val, off_t off);
static int nvmem_cell_write_be48(const struct nvmem_cell *cell, uint64_t val, off_t off);
static int nvmem_cell_write_le64(const struct nvmem_cell *cell, uint64_t val, off_t off);
static int nvmem_cell_write_be64(const struct nvmem_cell *cell, uint64_t val, off_t off);
```


---

[上一章：NVMEM数据单元结构](P019_NVMEM数据单元结构.md) · [下一章：安全存储服务](P021_安全存储服务.md) · [返回大纲](大纲.md)
