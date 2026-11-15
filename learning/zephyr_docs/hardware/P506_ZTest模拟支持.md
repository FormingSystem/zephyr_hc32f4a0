---
id: learning.zephyr-docs.hardware.ztestmac-3
title: ZTest模拟支持
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第506章\_ZTest模拟支持

原文：[group__ztest__mock](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html)。读取日期：2026-10-13，`latest`。

本模块为**单元测试（Unit Testing）**提供简单的**模拟（Mocking）**功能：测试先登记预期参数或返回值，被调用的模拟函数再检查参数、取得返回值或复制输出数据。需要启用 Kconfig 配置项 `CONFIG_ZTEST_MOCKING=y`。

公开头文件为 `zephyr/ztest_mock.h`，仓库内位置为 `subsys/testsuite/ztest/include/zephyr/ztest_mock.h`。**Zephyr 测试框架（Zephyr Testing Framework，ZTest）**使用函数名和参数名关联这些记录。

> 译注：原页显示官方构建机的绝对头文件路径，这里使用公开包含名。本页所说的“返回数据”是向输出参数指向的内存复制数据，与取得函数返回值是两种操作。

## 506.1\_在被调用函数中检查输入

[`ztest_check_expected_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga805cf99272f147beeeee5ad6ca2553f5) 检查参数 `param` 指向的数据是否匹配 [`ztest_expect_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac1a64d8bf9c877e8666e0c6d93b0dbab) 登记的预期数据。先检查该参数预期应为空还是非空，再比较所指数据；任何一项检查失败，当前测试都会失败。**必须在被调用函数内部调用此宏。**

```c
#define ztest_check_expected_data(param, length)
```

`param` 为待检查参数，`length` 为要比较的数据长度。下列展开中的 `__func__` 是当前函数名，`STRINGIFY` 将参数标识符转换为字符串，`z_ztest_*` 名称是这些宏调用的内部实现函数。

```c
z_ztest_check_expected_data(__func__, STRINGIFY(param),                \
                            (void *)(param), (length))
```

[`ztest_check_expected_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gae9af6ba8e51738e938763c896f17ea8f) 检查参数 `param` 是否匹配 [`ztest_expect_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga58c2f0c0e628e73a2268a3d18b0440d6) 设置的预期值。首先检查该参数是否存在登记的预期值，然后比较实际值和预期值；任意一步失败都会使当前测试失败。**同样必须从被调用函数内部调用。**

```c
#define ztest_check_expected_value(param)
```

`param` 为待检查参数。展开将它转换为 [`uintptr_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)，这是可表示指针值的无符号整数类型。

```c
z_ztest_check_expected_value(__func__, STRINGIFY(param),               \
                             (uintptr_t)(param))
```

## 506.2\_向输出参数复制数据

[`ztest_copy_return_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga12872a3d783d53d564ed94583bc490b0) 把 [`ztest_return_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac79d097a6b274b25286f2b0e80fbd6e9) 登记的数据复制到参数 `param` 指向的内存。它首先检查 `param` 非空，再复制数据；**必须从被调用函数内部调用**。

```c
#define ztest_copy_return_data(param, length)
```

参数 `param` 是用于返回数据的参数，`length` 是要返回的数据长度。

```c
z_ztest_copy_return_data(__func__, STRINGIFY(param),                   \
                         (void *)(param), (length))
```

## 506.3\_登记预期数据和值

[`ztest_expect_data`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac1a64d8bf9c877e8666e0c6d93b0dbab) 为函数 `func` 的参数 `param` 指定预期数据 `data`。后续调用 [`ztest_check_expected_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga805cf99272f147beeeee5ad6ca2553f5) 时，参数所指的数据应与这里登记的数据相同。

```c
#define ztest_expect_data(func, param, data)
```

`func` 是相关函数，`param` 是要设置预期数据的参数名称，`data` 是该参数预期数据的指针。**这里只保存数据指针，因此到 `ztest_check_expected_data` 被调用时，所指数据仍必须有效。**

```c
z_ztest_expect_data(STRINGIFY(func), STRINGIFY(param), (void *)(data))
```

[`ztest_expect_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga58c2f0c0e628e73a2268a3d18b0440d6) 为函数 `func` 的参数 `param` 登记预期值 `value`，供 [`ztest_check_expected_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gae9af6ba8e51738e938763c896f17ea8f) 检查。预期值在内部以 [`uintptr_t`](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808) 保存。

```c
#define ztest_expect_value(func, param, value)
```

`func` 为相关函数，`param` 为要设置预期值的参数，`value` 为该参数的预期值。

```c
z_ztest_expect_value(STRINGIFY(func), STRINGIFY(param),                \
                     (uintptr_t)(value))
```

## 506.4\_取得当前函数的返回值

[`ztest_get_return_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga31dcd5b5a3596a7404a771a2d32f3a39) 取得当前函数应返回的值。该值必须先用 [`ztest_returns_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga2ec539b4c0f3e4efb695213b4fd08c2c) 登记；若不存在返回值，当前测试会失败。此宏无参数，结果是当前函数应返回的值。

```c
#define ztest_get_return_value()
```

```c
z_ztest_get_return_value(__func__)
```

[`ztest_get_return_value_ptr()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gaa2df2eaeba49019b7a83ac769ea95968) 以指针形式取得当前函数应返回的值，同样要求此前调用 [`ztest_returns_value()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga2ec539b4c0f3e4efb695213b4fd08c2c)，否则当前测试失败。此宏无参数，结果类型为 `void *`。

```c
#define ztest_get_return_value_ptr()
```

```c
((void *)z_ztest_get_return_value(__func__))
```

## 506.5\_登记输出数据与函数返回值

`ztest_return_data` 告诉函数 `func`：通过参数 `param` 返回数据 `data`。

```c
#define ztest_return_data(func, param, data)
```

`func` 是相关函数，`param` 是要设置返回数据的参数，`data` 指向要通过该参数返回的数据。原文说明，该参数最终指向的数据应与这里指定的数据相同。**这里只保存数据指针，所以到 `ztest_copy_return_data` 执行时，该数据仍必须有效。**

```c
z_ztest_return_data(STRINGIFY(func), STRINGIFY(param), (void *)(data))
```

> 译注：原页在上述说明中再次写了 [`ztest_return_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#gac79d097a6b274b25286f2b0e80fbd6e9)；实际复制动作由 [`ztest_copy_return_data()`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga12872a3d783d53d564ed94583bc490b0) 完成，前者登记数据指针。这里只澄清两个宏的职责，不改变其声明或展开。

[`ztest_returns_value`](https://docs.zephyrproject.org/latest/doxygen/html/group__ztest__mock.html#ga2ec539b4c0f3e4efb695213b4fd08c2c) 指定函数 `func` 应返回 `value`。

```c
#define ztest_returns_value(func, value)
```

参数 `func` 是要返回指定值的函数，`value` 为其返回值。

```c
z_ztest_returns_value(STRINGIFY(func), (uintptr_t)(value))
```

---

[上一章：ZTest预期检查宏](P505_ZTest预期检查宏.md) · [下一章：ZTest测试定义宏](P507_ZTest测试定义宏.md) · [返回大纲](大纲.md)
