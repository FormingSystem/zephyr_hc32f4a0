---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-15
title: zephyr__debug__gcov.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_zephyr\_\_debug\_\_gcov.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/gcov_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于转储GCC gcov代码覆盖率数据（Code Coverage Data）的公共API。

查看此文件的源码。

<a id="details"></a>

用于转储GCC gcov代码覆盖率数据（Code Coverage Data）的公共API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 15.1\_函数（Functions）

<a id="r_ac743263c4f10905987df4c67eafecc44"></a>

```c
void gcov_coverage_dump (void)
```

相关声明：[gcov_coverage_dump](#ac743263c4f10905987df4c67eafecc44)。

转储全部已收集的 gcov 覆盖率数据（Coverage Data）。

<a id="r_a4112c617905e6881b552f641fbf3ff2f"></a>

```c
void gcov_coverage_dump_tagged (const char *tag)
```

相关声明：[gcov_coverage_dump_tagged](#a4112c617905e6881b552f641fbf3ff2f)。

转储带标签（Tag）的 gcov 覆盖率数据（Coverage Data）。

<a id="r_a3868770b5770d928f0c90584f5e66188"></a>

```c
void gcov_coverage_semihost (void)
```

相关声明：[gcov_coverage_semihost](#a3868770b5770d928f0c90584f5e66188)。

通过半主机机制（Semihosting）转储全部已收集的 gcov 覆盖率数据。

<a id="r_a05ec5d137639a269c6df6188caf7bbc8"></a>

```c
void gcov_static_init (void)
```

相关声明：[gcov_static_init](#a05ec5d137639a269c6df6188caf7bbc8)。

初始化 gcov 运行时（Runtime）。

## 15.2\_详细说明（Detailed Documentation）

<a id="ac743263c4f10905987df4c67eafecc44"></a>

### `gcov_coverage_dump()`

```c
void gcov_coverage_dump ( void )
```

转储全部已收集的 gcov 覆盖率数据（Coverage Data）。

获取每个已注册对象（Registered Object）的 gcov 覆盖率数据，并通过覆盖率转储方法（Coverage Dump Method）选定的传输路径发送：`CONFIG_COVERAGE_DUMP` 使用控制台，`CONFIG_COVERAGE_SEMIHOST` 使用主机文件系统。这是不带标签的形式，等价于以 `NULL` 标签调用 `gcov_coverage_dump_tagged()`。

<a id="a4112c617905e6881b552f641fbf3ff2f"></a>

### `gcov_coverage_dump_tagged()`

```c
void gcov_coverage_dump_tagged ( const char * tag)
```

转储带标签（Tag）的 gcov 覆盖率数据（Coverage Data）。

获取 gcov 覆盖率数据，并经配置的传输路径输出；使用 `tag` 将转储关联到一个标签，便于使用者将数据归属于单个产生方（Producer），例如某个测试用例。

根据所选转储方法（Dump Method），标签（Tag）以不同方式携带：

- 控制台（`CONFIG_COVERAGE_DUMP`）：将标签（Tag）追加到界定数据的 `GCOV_COVERAGE_DUMP_START` 标记之后。
- 半主机机制（`CONFIG_COVERAGE_SEMIHOST`）：每个 `.gcda` 文件写入在文件名后追加 `@@` 和标签构成的路径，例如 `foo.gcda@@suite.test`，而不使用规范路径（Canonical Path）。这样，多份独立转储可以与匹配的 `.gcno` 共存，互不覆盖。

`tag` 不为 `NULL` 时，会跳过没有记录任何覆盖率的对象，使带标签、按产生方区分的转储保持较小。传入 `NULL` 则恢复历史上的无标签行为，转储每个对象。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `tag` | 用于标识转储归属的标签（Label）；`NULL` 表示无标签转储（Untagged Dump）。 |

<a id="a3868770b5770d928f0c90584f5e66188"></a>

### `gcov_coverage_semihost()`

```c
void gcov_coverage_semihost ( void )
```

通过半主机机制（Semihosting）转储全部已收集的 gcov 覆盖率数据。

通过半主机机制（Semihosting），将每个已注册对象的 gcov 覆盖率数据写入主机文件系统。仅在选择半主机转储方法 `CONFIG_COVERAGE_SEMIHOST` 时可用。这是不带标签的形式。

<a id="a05ec5d137639a269c6df6188caf7bbc8"></a>

### `gcov_static_init()`

```c
void gcov_static_init ( void )
```

初始化 gcov 运行时（Runtime）。

调用 gcov 构造函数（Constructors），使每个插桩对象（Instrumented Object）向运行时注册自身的 `gcov_info`。必须在转储任何覆盖率数据之前运行。


## 15.3\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_reference/P284_gcov.h_源码浏览.md)
- [CONFIG_COVERAGE_DUMP](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_DUMP)
- [CONFIG_COVERAGE_SEMIHOST](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_SEMIHOST)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P014_zephyr__mgmt__fota_http.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P016_zephyr__dt-bindings__pinctrl__gecko-pinctrl-s1.h_文件参考.md)
