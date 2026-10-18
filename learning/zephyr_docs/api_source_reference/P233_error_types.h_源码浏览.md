---
id: learning.zephyr-docs.api-source-reference.page-233
title: error_types.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第233章\_error\_types.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html)。

## 233.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="foldopen00024"></a>
<a id="l00024"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="foldopen00057"></a>
<a id="l00057"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a"></a>
<a id="aerror__types_8h_html_a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb"></a>
<a id="aerror__types_8h_html_a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707"></a>

```c
/*
 * Copyright 2024 Meta Platforms, Inc. and its affiliates
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_DRIVERS_I3C_ERROR_TYPES_H_
#define ZEPHYR_INCLUDE_DRIVERS_I3C_ERROR_TYPES_H_

#ifdef __cplusplus
extern "C" {
#endif

enum i3c_sdr_controller_error_types {
        I3C_ERROR_CE0,

        I3C_ERROR_CE1,

        I3C_ERROR_CE2,

        I3C_ERROR_CE3,

        I3C_ERROR_CE_UNKNOWN,

        I3C_ERROR_CE_NONE,

        I3C_ERROR_CE_MAX = I3C_ERROR_CE_UNKNOWN,
        I3C_ERROR_CE_INVALID,
};

enum i3c_sdr_target_error_types {
        I3C_ERROR_TE0,

        I3C_ERROR_TE1,

        I3C_ERROR_TE2,

        I3C_ERROR_TE3,

        I3C_ERROR_TE4,

        I3C_ERROR_TE5,

        I3C_ERROR_TE6,

        I3C_ERROR_DBR,

        I3C_ERROR_TE_UNKNOWN,

        I3C_ERROR_TE_NONE,

        I3C_ERROR_TE_MAX = I3C_ERROR_TE_UNKNOWN,
        I3C_ERROR_TE_INVALID,
};

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_DRIVERS_I3C_ERROR_TYPES_H_ */
```

## 233.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：2024 Meta Platforms, Inc. and its affiliates。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 99 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_DRIVERS_I3C_ERROR_TYPES_H_`。

## 233.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html)
- [i3c_sdr_controller_error_types](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0)
- [I3C_ERROR_CE0](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0a29a9faf9402dbad479d7c72af3074282)
- [I3C_ERROR_CE1](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0ae60ebbf70623d022df65ce8837a5bddb)
- [I3C_ERROR_CE2](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0a46fdc1719e801fbb6a61db7b7675a574)
- [I3C_ERROR_CE3](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0ac18dd1126126aed36d7c4ca399133e1f)
- [I3C_ERROR_CE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0a936f9c9f75c2fef25d9a3a0b6dc45502)
- [I3C_ERROR_CE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0af8c1a2219f28b91b11206f7fafd12707)
- [I3C_ERROR_CE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0a8dfdbe43a58837e87eb08da228c462e7)
- [I3C_ERROR_CE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a79ba58b71019ccd9b76f65aaf4ebe1b0a72a987f540981d0c0ef973cf835707a0)
- [i3c_sdr_target_error_types](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91)
- [I3C_ERROR_TE0](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91ae9d64998fe25f44268fc35944e23661a)
- [I3C_ERROR_TE1](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91aa79f8166d1c6bf18311adf11e6c612fe)
- [I3C_ERROR_TE2](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91ab6d0cb581f823ba39934c835eed7207e)
- [I3C_ERROR_TE3](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a4d5a837d35c5a752fee2cb4cdf761cd3)
- [I3C_ERROR_TE4](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a3fd9d3a819fb1f3d79e53757aaa03dfd)
- [I3C_ERROR_TE5](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91ab014ca57d29162e7cf3116be36693c8f)
- [I3C_ERROR_TE6](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a3f5f0fe6d716fd7df84b99df707c2a8e)
- [I3C_ERROR_DBR](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91ab02aee605de8820b586908bafcd8e285)
- [I3C_ERROR_TE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a24684b50d96bf68a5a4c6f819c393791)
- [I3C_ERROR_TE_NONE](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a5bc59253e371b88471b5d9bc15cd9c3a)
- [I3C_ERROR_TE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91a7e6c2b9e56fc594ca57501adb09b26c7)
- [I3C_ERROR_TE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/error__types_8h.html#a176c3429a9a5b786639223eea9221f91adb9cd0b5e4c5e0ae96f941d39a4af23a)

---

[上一章](P232_eqdc_mcux.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P234_esp-esp32c61-intmux.h_源码浏览.md)
