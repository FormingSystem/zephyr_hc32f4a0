---
id: learning.zephyr-docs.api-file-runtime-reference.page-19
title: zephyr__drivers__i3c__hdr_ddr.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第19章\_zephyr\_\_drivers\_\_i3c\_\_hdr\_ddr.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/hdr__ddr_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <errno.h>
#include <stddef.h>
#include <stdint.h>
#include <zephyr/drivers/i3c.h>
```

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 19.1\_函数（Functions）

<a id="r_ga9bf00a59c3c08f4bf1ffd5ae32c0fad8"></a>

```c
static int i3c_hdr_ddr_write (struct i3c_device_desc *target, uint8_t cmd, uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_hdr_ddr_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用高数据速率双数据速率模式（HDR DDR），向 I3C 目标设备（Target Device）写入指定数量的数据。

<a id="r_ga11e788383aeb52184fdd6483cf702d40"></a>

```c
static int i3c_hdr_ddr_read (struct i3c_device_desc *target, uint8_t cmd, uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_hdr_ddr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga11e788383aeb52184fdd6483cf702d40)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

使用高数据速率双数据速率模式（HDR DDR），从 I3C 目标设备（Target Device）读取指定数量的数据。

<a id="r_gaa752f1095c84ad1b94fb09cc0aeee4fa"></a>

```c
static int i3c_hdr_ddr_write_read (struct i3c_device_desc *target, const void *write_buf, size_t num_write, uint8_t read_cmd, void *read_buf, size_t num_read, uint8_t write_cmd)
```

相关声明：[i3c_hdr_ddr_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#gaa752f1095c84ad1b94fb09cc0aeee4fa)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用高数据速率双数据速率模式（HDR DDR），先向 I3C 目标设备（Target Device）写入数据，再读取数据。


## 19.2\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h_source.html)
- [zephyr/drivers/i3c.h](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P313_hdr_ddr.h_源码浏览.md)
- [i3c_hdr_ddr_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga9bf00a59c3c08f4bf1ffd5ae32c0fad8)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [cmd](https://docs.zephyrproject.org/latest/doxygen/html/group__ft8xx__reference__api.html#gacde1ca3945cbe6c828f65051c5c3a615)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [i3c_hdr_ddr_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#ga11e788383aeb52184fdd6483cf702d40)
- [i3c_hdr_ddr_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__hdr__ddr.html#gaa752f1095c84ad1b94fb09cc0aeee4fa)

---

[上一章](P018_zephyr__net__hdlc_rcp_if__hdlc_rcp_if.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P020_zephyr__bluetooth__mesh__heartbeat.h_文件参考.md)
