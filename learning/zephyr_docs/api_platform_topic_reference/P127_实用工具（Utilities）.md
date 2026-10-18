---
id: learning.zephyr-docs.api-platform-topic-reference.page-127
title: 实用工具（Utilities）
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第127章\_实用工具（Utilities）

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__utilities.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

实用工具（Utilities）

<a id="details"></a>

工具（Utilities）。数据结构 API（Data Structure APIs）。

<a id="header-groups"></a>
<a id="groups"></a>

## 127.1\_主题（Topics）

<a id="r_base64"></a>

相关声明：[Base64](../base64_reference/P001_Base64编解码接口.md)。

Base64编码／解码（Encoding / Decoding）函数。

<a id="r_bit_5Frev"></a>

相关声明：[位反转操作（Bit Reverse Operations）](../checksum_reference/P004_位反转接口.md)。

<a id="r_cobs"></a>

相关声明：[一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html)。

支持自定义分隔符的 COBS 编码与解码函数。

<a id="r_math_5Fdsp"></a>

相关声明：[数字信号处理（Digital Signal Processing，DSP）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html)。

数字信号处理（DSP）数学函数和工具。

<a id="r_datastructure_5Fapis"></a>

相关声明：[数据结构 API（Data Structure APIs）](../api_topic_reference/P028_数据结构 API（Data Structure APIs）.md)。

<a id="r_cbprintf_5Fapis"></a>

相关声明：[格式化输出 API（Formatted Output APIs）](../cbprintf_reference/P001_回调格式化输出接口.md)。

<a id="r_json"></a>

相关声明：[JSON](../serialization/P006_JSON接口参考.md)。

<a id="r_linear_5Frange"></a>

相关声明：[线性范围（Linear Range）](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html)。

<a id="r_math_5Filog2"></a>

相关声明：[整数以 2 为底的对数数学函数（Math Ilog2 Functions）](../numeric_reference/P005_整数二进制对数公共接口.md)。

用于数学运算的整数 log2 工具。

<a id="r_math_5Finterpolation"></a>

相关声明：[数学插值函数（Math Interpolation Functions）](../interpolation_reference/P001_插值公共接口.md)。

用于数学运算的线性插值工具（Linear Interpolation Utilities）。

<a id="r_math_5Fextras"></a>

相关声明：[数学扩展（Math extras）](../math_reference/P001_数学辅助公共接口.md)。

额外的算术与位操作函数（Arithmetic and Bit Manipulation Functions）。

<a id="r_navigation"></a>

相关声明：[导航（Navigation）](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html)。

导航工具。

<a id="r_sys_5Fref"></a>

相关声明：[引用计数（Reference counting）](../sysref_reference/P001_引用计数接口.md)。

<a id="r_sys_5Fio_5Fapis"></a>

相关声明：[系统输入输出接口（System I/O APIs）。](../device_reference/P017_系统IO公共接口.md)。

系统输入输出接口（System I/O APIs）。

<a id="r_timeutil_5Fapis"></a>

相关声明：[时间工具 API（Time Utility APIs）](../timeutil_reference/P001_时间工具接口概览.md)。

<a id="r_uuid"></a>

相关声明：[通用唯一标识符（UUID）。](../data_utilities/P023_UUID生成与转换接口.md)。

<a id="r_sys-util"></a>

相关声明：[实用函数（Utility Functions）](../util_reference/P001_通用工具公共接口.md)。

<a id="header-files"></a>
<a id="files"></a>

## 127.2\_文件（Files）

<a id="r_ref_2Eh"></a>

```c
file ref.h
```

相关声明：[ref.h](../sysref_reference/P003_引用计数头文件参考.md)。

引用计数头文件。


## 127.3\_原页交叉引用（Cross References）

- [Base64](../base64_reference/P001_Base64编解码接口.md)
- [位反转操作（Bit Reverse Operations）](../checksum_reference/P004_位反转接口.md)
- [一致开销字节填充（Consistent Overhead Byte Stuffing，COBS）](https://docs.zephyrproject.org/latest/doxygen/html/group__cobs.html)
- [数字信号处理（Digital Signal Processing，DSP）](https://docs.zephyrproject.org/latest/doxygen/html/group__math__dsp.html)
- [数据结构 API（Data Structure APIs）](../api_topic_reference/P028_数据结构 API（Data Structure APIs）.md)
- [格式化输出 API（Formatted Output APIs）](../cbprintf_reference/P001_回调格式化输出接口.md)
- [JSON](../serialization/P006_JSON接口参考.md)
- [线性范围（Linear Range）](https://docs.zephyrproject.org/latest/doxygen/html/group__linear__range.html)
- [整数以 2 为底的对数数学函数（Math Ilog2 Functions）](../numeric_reference/P005_整数二进制对数公共接口.md)
- [数学插值函数（Math Interpolation Functions）](../interpolation_reference/P001_插值公共接口.md)
- [数学扩展（Math extras）](../math_reference/P001_数学辅助公共接口.md)
- [导航（Navigation）](https://docs.zephyrproject.org/latest/doxygen/html/group__navigation.html)
- [引用计数（Reference counting）](../sysref_reference/P001_引用计数接口.md)
- [系统输入输出接口（System I/O APIs）。](../device_reference/P017_系统IO公共接口.md)
- [时间工具 API（Time Utility APIs）](../timeutil_reference/P001_时间工具接口概览.md)
- [通用唯一标识符（UUID）。](../data_utilities/P023_UUID生成与转换接口.md)
- [实用函数（Utility Functions）](../util_reference/P001_通用工具公共接口.md)
- [ref.h](../sysref_reference/P003_引用计数头文件参考.md)

<a id="header-details"></a>

---

[上一章](P126_用户模式内部 API（User Mode Internal APIs）.md) · [返回大纲](大纲.md) · [下一章](P128_视频子系统（Video Subsystem）.md)
