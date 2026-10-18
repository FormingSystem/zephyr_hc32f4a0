---
id: learning.zephyr-docs.api-source-reference.page-116
title: tty.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第116章\_tty.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html)。

## 116.1\_原始可见代码（Source Code）

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
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="foldopen00021"></a>
<a id="l00021"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="foldopen00065"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="aconsole_2tty_8h_html_a109fd8ee6b581a796d67025a0e33abde"></a>
<a id="aconsole_2tty_8h_html_a1c19c6ed8207ae711e047f9ae446e399"></a>
<a id="aconsole_2tty_8h_html_a5a880bb61f0bdb0f37c501acc0408d32"></a>
<a id="aconsole_2tty_8h_html_a90ec3fbbe5f0fad19361d23e821c960c"></a>
<a id="aconsole_2tty_8h_html_ad05b854f19b3bd97e2635bc8ebc07ce2"></a>
<a id="aconsole_2tty_8h_html_af60d8a57ac3cb81a0a003a011a0f31e5"></a>
<a id="aconsole_2tty_8h_html_af6383a47f82797af9a45bc81d84de1be"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__timeutil__unit__apis_html_ga6504e9e6fe4955e0bc31eccd4cfc01b7"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html_a5c5d83d87790efd59ea916c2b99f9118"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astructdevice_html"></a>
<a id="astructk__event_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructring__buf_html"></a>
<a id="astructtty__serial_html"></a>

```c
/*
 * Copyright (c) 2018 Linaro Limited
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_CONSOLE_TTY_H_
#define ZEPHYR_INCLUDE_CONSOLE_TTY_H_

#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

struct tty_serial {
        const struct device *uart_dev;

        struct k_event signal_event;

        struct ring_buf rx_buf;
        k_timeout_t rx_timeout;

        struct ring_buf tx_buf;
        k_timeout_t tx_timeout;
        atomic_t tx_busy;
};

int tty_init(struct tty_serial *tty, const struct device *uart_dev);

static inline void tty_set_rx_timeout(struct tty_serial *tty, int32_t timeout)
{
        tty->rx_timeout = SYS_TIMEOUT_MS(timeout);
}

static inline void tty_set_tx_timeout(struct tty_serial *tty, int32_t timeout)
{
        tty->tx_timeout = SYS_TIMEOUT_MS(timeout);
}

int tty_set_rx_buf(struct tty_serial *tty, void *buf, size_t size);

int tty_set_tx_buf(struct tty_serial *tty, void *buf, size_t size);

ssize_t tty_read(struct tty_serial *tty, void *buf, size_t size);

ssize_t tty_write(struct tty_serial *tty, const void *buf, size_t size);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_CONSOLE_TTY_H_ */
```

## 116.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018 Linaro Limited。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 141 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_CONSOLE_TTY_H_`。

## 116.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [tty_serial](../system_service_model_reference/P087_tty_serial_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [k_event](../eventpoll_reference/P002_内核事件结构.md)
- [ring_buf](../ringbuffer_reference/P002_环形缓冲区结构.md)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [tty_init](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#a5a880bb61f0bdb0f37c501acc0408d32)
- [tty_set_rx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#a109fd8ee6b581a796d67025a0e33abde)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [SYS_TIMEOUT_MS](../timeutil_reference/P007_时间单位辅助接口.md#ga6504e9e6fe4955e0bc31eccd4cfc01b7)
- [tty_set_tx_timeout](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#a1c19c6ed8207ae711e047f9ae446e399)
- [tty_set_rx_buf](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#ad05b854f19b3bd97e2635bc8ebc07ce2)
- [tty_set_tx_buf](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#af6383a47f82797af9a45bc81d84de1be)
- [ssize_t](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html#a5c5d83d87790efd59ea916c2b99f9118)
- [tty_read](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#a90ec3fbbe5f0fad19361d23e821c960c)
- [tty_write](https://docs.zephyrproject.org/latest/doxygen/html/console_2tty_8h.html#af60d8a57ac3cb81a0a003a011a0f31e5)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)

---

[上一章](P115_console.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P117_controls.h_源码浏览.md)
