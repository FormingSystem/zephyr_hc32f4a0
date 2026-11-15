---
id: learning.zephyr-docs.api-file-network-device-reference.page-45
title: ____w__zephyr__zephyr__subsys__testsuite__ztest__include__zephyr__ztest_mock.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_\_\_\_\_w\_\_zephyr\_\_zephyr\_\_subsys\_\_testsuite\_\_ztest\_\_include\_\_zephyr\_\_ztest\_mock.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Ztest的模拟（Mocking）支持。

查看此文件的源码。

<a id="details"></a>

Ztest的模拟（Mocking）支持。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 45.1\_宏定义（Macros）

<a id="r_ga58c2f0c0e628e73a2268a3d18b0440d6"></a>

```c
#define ztest_expect_value(func, param, value)
```

相关声明：[ztest_expect_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga58c2f0c0e628e73a2268a3d18b0440d6)。

告知函数 `func`：参数 `param` 的期望值（Expected Value）为 `value`。

<a id="r_gae9af6ba8e51738e938763c896f17ea8f"></a>

```c
#define ztest_check_expected_value(param)
```

相关声明：[ztest_check_expected_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gae9af6ba8e51738e938763c896f17ea8f)。

若 `param` 不匹配 `ztest_expect_value()` 设置的值，则使测试失败。

<a id="r_gac1a64d8bf9c877e8666e0c6d93b0dbab"></a>

```c
#define ztest_expect_data(func, param, data)
```

相关声明：[ztest_expect_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac1a64d8bf9c877e8666e0c6d93b0dbab)。

告知函数 `func`：参数 `param` 的期望数据（Expected Data）为 `data`。

<a id="r_ga805cf99272f147beeeee5ad6ca2553f5"></a>

```c
#define ztest_check_expected_data(param, length)
```

相关声明：[ztest_check_expected_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga805cf99272f147beeeee5ad6ca2553f5)。

若 `param` 指向的数据不匹配 `ztest_expect_data()` 设置的数据，则使测试失败。

<a id="r_gac79d097a6b274b25286f2b0e80fbd6e9"></a>

```c
#define ztest_return_data(func, param, data)
```

相关声明：[ztest_return_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac79d097a6b274b25286f2b0e80fbd6e9)。

告知函数 `func`：应通过参数 `param` 返回数据 `data`。

<a id="r_ga12872a3d783d53d564ed94583bc490b0"></a>

```c
#define ztest_copy_return_data(param, length)
```

相关声明：[ztest_copy_return_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga12872a3d783d53d564ed94583bc490b0)。

将 `ztest_return_data` 设置的数据复制到 `param` 指向的内存。

<a id="r_ga2ec539b4c0f3e4efb695213b4fd08c2c"></a>

```c
#define ztest_returns_value(func, value)
```

相关声明：[ztest_returns_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga2ec539b4c0f3e4efb695213b4fd08c2c)。

告知 `func`：它应返回 `value`。

<a id="r_ga31dcd5b5a3596a7404a771a2d32f3a39"></a>

```c
#define ztest_get_return_value()
```

相关声明：[ztest_get_return_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga31dcd5b5a3596a7404a771a2d32f3a39)。

获取当前函数的返回值（Return Value）。

<a id="r_gaa2df2eaeba49019b7a83ac769ea95968"></a>

```c
#define ztest_get_return_value_ptr()
```

相关声明：[ztest_get_return_value_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gaa2df2eaeba49019b7a83ac769ea95968)。

将当前函数的返回值作为指针（Pointer）获取。


## 45.2\_原页交叉引用（Cross References）

- [查看此文件的源码。](../api_source_supplement_reference/P255_ztest_mock.h_源码浏览.md)
- [ztest_expect_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga58c2f0c0e628e73a2268a3d18b0440d6)
- [ztest_check_expected_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gae9af6ba8e51738e938763c896f17ea8f)
- [ztest_expect_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac1a64d8bf9c877e8666e0c6d93b0dbab)
- [ztest_check_expected_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga805cf99272f147beeeee5ad6ca2553f5)
- [ztest_return_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac79d097a6b274b25286f2b0e80fbd6e9)
- [ztest_copy_return_data](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga12872a3d783d53d564ed94583bc490b0)
- [ztest_returns_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga2ec539b4c0f3e4efb695213b4fd08c2c)
- [ztest_get_return_value](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga31dcd5b5a3596a7404a771a2d32f3a39)
- [ztest_get_return_value_ptr](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gaa2df2eaeba49019b7a83ac769ea95968)

<a id="header-details"></a>

---

[上一章](P044_zephyr__net__wifi_nm.h_文件参考.md) · [返回大纲](大纲.md)
