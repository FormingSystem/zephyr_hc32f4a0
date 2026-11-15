---
id: learning.zephyr-docs.api-source-supplement-reference.page-255
title: ztest_mock.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第255章\_ztest\_mock.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html)。

## 255.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00025"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="foldopen00051"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00082"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00110"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00140"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a4788399d1d0b37ccf098a7da82254808"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_TESTSUITE_ZTEST_MOCK_H_
#define ZEPHYR_TESTSUITE_ZTEST_MOCK_H_


#define ztest_expect_value(func, param, value)                                 \
        z_ztest_expect_value(STRINGIFY(func), STRINGIFY(param),                \
                             (uintptr_t)(value))

#define ztest_check_expected_value(param)                                      \
        z_ztest_check_expected_value(__func__, STRINGIFY(param),               \
                                     (uintptr_t)(param))

#define ztest_expect_data(func, param, data)                                   \
        z_ztest_expect_data(STRINGIFY(func), STRINGIFY(param), (void *)(data))

#define ztest_check_expected_data(param, length)                               \
        z_ztest_check_expected_data(__func__, STRINGIFY(param),                \
                                    (void *)(param), (length))

#define ztest_return_data(func, param, data)                                   \
        z_ztest_return_data(STRINGIFY(func), STRINGIFY(param), (void *)(data))

#define ztest_copy_return_data(param, length)                                  \
        z_ztest_copy_return_data(__func__, STRINGIFY(param),                   \
                                 (void *)(param), (length))

#define ztest_returns_value(func, value)                                       \
        z_ztest_returns_value(STRINGIFY(func), (uintptr_t)(value))

#define ztest_get_return_value() z_ztest_get_return_value(__func__)

#define ztest_get_return_value_ptr()                                           \
        ((void *)z_ztest_get_return_value(__func__))


#ifdef CONFIG_ZTEST_MOCKING

#include <zephyr/types.h>

#ifdef __cplusplus
extern "C" {
#endif

void z_init_mock(void);
int z_cleanup_mock(void);

void z_ztest_expect_value(const char *fn, const char *name, uintptr_t value);
void z_ztest_check_expected_value(const char *fn, const char *param,
                                  uintptr_t value);

void z_ztest_expect_data(const char *fn, const char *name, void *val);
void z_ztest_check_expected_data(const char *fn, const char *name, void *data,
                                 uint32_t length);

void z_ztest_return_data(const char *fn, const char *name, void *val);
void z_ztest_copy_return_data(const char *fn, const char *name, void *data,
                              uint32_t length);

void z_ztest_returns_value(const char *fn, uintptr_t value);
uintptr_t z_ztest_get_return_value(const char *fn);

#ifdef __cplusplus
}
#endif

#else /* !CONFIG_ZTEST_MOCKING */

#define z_init_mock()
#define z_cleanup_mock() 0

#endif /* CONFIG_ZTEST_MOCKING */

#endif /* ZEPHYR_TESTSUITE_ZTEST_MOCK_H_ */
```

## 255.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 177 行

条件编译表达式：`!CONFIG_ZTEST_MOCKING`。

### 注释 3：原第 182 行

条件编译配置（Configuration）标记：`CONFIG_ZTEST_MOCKING`。

### 注释 4：原第 184 行

头文件保护宏（Header guard）标记：`ZEPHYR_TESTSUITE_ZTEST_MOCK_H_`。

## 255.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/ztest__mock_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [uintptr_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a4788399d1d0b37ccf098a7da82254808)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)

---

[上一章](P254_xip.h_源码浏览.md) · [返回大纲](大纲.md)
