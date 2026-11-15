---
id: learning.zephyr-docs.hardware.emulback-2
title: BBRAM仿真后端接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__bbram__emulator__backend.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第490章\_BBRAM仿真后端接口

原文：[group__bbram__emulator__backend](P490_BBRAM仿真后端接口.md)。读取日期：2026-10-13，`latest`。

**电池后备随机存取存储器（Battery-Backed Random Access Memory，BBRAM）**仿真器提供后端接口，用来设置或读取仿真存储区域中的预期数据。这些**应用程序编程接口（Application Programming Interface，API）**位于 `zephyr/drivers/emul_bbram.h`。

## 490.1\_设置预期数据

[`emul_bbram_backend_set_data()`](P490_BBRAM仿真后端接口.md) 从指定偏移开始写入预期数据，是头文件中定义的静态内联函数（Static Inline Function）。

```c
static inline int emul_bbram_backend_set_data(const struct emul *target,
                                             size_t offset, size_t count,
                                             const uint8_t *data);
```

| 参数 | 含义 |
| --- | --- |
| `target` | 指向待操作仿真器实例的指针 |
| `offset` | 要写入的存储区内偏移 |
| `count` | 要写入的字节数 |
| `data` | 待写入数据 |

成功返回 `0`；没有后端 API 或没有实现 `set_data` 函数时，返回“不支持”错误 `-ENOTSUP`；目标地址超出范围时，返回“范围错误” `-ERANGE`。

## 490.2\_读取预期数据

[`emul_bbram_backend_get_data()`](P490_BBRAM仿真后端接口.md) 读取 BBRAM 区域中的预期数据。

```c
static inline int emul_bbram_backend_get_data(const struct emul *target,
                                             size_t offset, size_t count,
                                             uint8_t *data);
```

参数 `target` 指向待操作仿真器实例，`offset` 为要读取的存储区内偏移，`count` 为读取字节数，`data` 为保存结果的数据缓冲区。

成功返回 `0`；没有后端 API 或没有实现 `get_data` 函数时返回 `-ENOTSUP`；地址超出范围时返回 `-ERANGE`。

---

[上一章：MSPI仿真器链表节点](P489_MSPI仿真器链表节点.md) · [下一章：BC1点2仿真后端接口](P491_BC1点2仿真后端接口.md) · [返回大纲](大纲.md)
