---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-16
title: uart_async_rx.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_uart\_async\_rx.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](../hardware/P344_UART异步接收辅助接口.md)。

## 16.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="foldopen00022"></a>
<a id="l00022"></a>
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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="foldopen00036"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00062"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="foldopen00079"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructuart__async__rx__buf_html"></a>
<a id="astructuart__async__rx__buf_html_a1baa442e23d9babb701a7fc28d8408a4"></a>
<a id="astructuart__async__rx__buf_html_a4dbeb091bddcd92e1fe242517f53bb93"></a>
<a id="astructuart__async__rx__buf_html_ad03eb3023829258581e54c75e0a66942"></a>
<a id="astructuart__async__rx__config_html"></a>
<a id="astructuart__async__rx__config_html_a2d5d07f7e98ae6743378f75ce3afc4f2"></a>
<a id="astructuart__async__rx__config_html_a73a1c096f5aac03f3426c7320241fcf2"></a>
<a id="astructuart__async__rx__config_html_ad4eabc44a27b06f93b0d6194903b6b97"></a>
<a id="astructuart__async__rx_html"></a>
<a id="astructuart__async__rx_html_a1150d2c365330c4d87a22b44412611f6"></a>
<a id="astructuart__async__rx_html_a15510449c58841c7294e0359a92bf4d0"></a>
<a id="astructuart__async__rx_html_a85ea611224160caee86767b4910e17d9"></a>
<a id="astructuart__async__rx_html_a9a192c4f08f6d946bb562a9bbba8f196"></a>
<a id="astructuart__async__rx_html_abbe20b7426175d7436470f6a26bb578e"></a>
<a id="astructuart__async__rx_html_ac782b9465c3766d5217676a3a97a963b"></a>
<a id="astructuart__async__rx_html_ad75410820beef5a612f602d3017df5f6"></a>
<a id="auart__async__rx_8h_html_a1ac0b3ee0e1840177d07c4fbcbd635df"></a>
<a id="auart__async__rx_8h_html_a1eede7070affe966616148924ba2c519"></a>
<a id="auart__async__rx_8h_html_a2064f3d760adb4cf6912caf12f7a54cc"></a>
<a id="auart__async__rx_8h_html_a8d5ed81dfa4c067f173249744b25561e"></a>
<a id="auart__async__rx_8h_html_a8daddb05f11ad43c8c4510a4312cf38f"></a>
<a id="auart__async__rx_8h_html_a9e51885811653d21e0e8712b09ef800d"></a>
<a id="auart__async__rx_8h_html_acca21c43fa833b4789edbc1bc92bab2b"></a>
<a id="auart__async__rx_8h_html_ad551b1684437c8ab48c0708fb5b0d1f6"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_RX_H_
#define ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_RX_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <zephyr/kernel.h>

/* @brief RX buffer structure which holds the buffer and its state. */
struct uart_async_rx_buf {
        /* Write index which is incremented whenever new data is reported to be
         * received to that buffer.
         */
        uint8_t wr_idx:7;

        /* Set to one if buffer is released by the driver. */
        uint8_t completed:1;

        /* Location which is passed to the UART driver. */
        uint8_t buffer[];
};

struct uart_async_rx {
        /* Pointer to the configuration structure. Structure must be persistent. */
        const struct uart_async_rx_config *config;

        /* Total amount of pending bytes. Bytes may be spread across multiple RX buffers. */
        atomic_t pending_bytes;

        /* Number of buffers which are free. */
        atomic_t free_buf_cnt;

        /* Single buffer size. */
        uint8_t buf_len;

        /* Index of the next buffer to be provided to the driver. */
        uint8_t drv_buf_idx;

        /* Current buffer from which data is being consumed. */
        uint8_t rd_buf_idx;

        /* Current read index in the buffer from which data is being consumed.
         * Read index which is incremented whenever data is consumed from the buffer.
         */
        uint8_t rd_idx;
};

struct uart_async_rx_config {
        /* Pointer to the buffer. */
        uint8_t *buffer;

        /* Buffer length. */
        size_t length;

        /* Number of buffers into provided space shall be split. */
        uint8_t buf_cnt;
};

static inline uint8_t uart_async_rx_get_buf_len(struct uart_async_rx *async_rx)
{
        return async_rx->buf_len;
}

#define UART_ASYNC_RX_BUF_OVERHEAD offsetof(struct uart_async_rx_buf, buffer)

int uart_async_rx_init(struct uart_async_rx *async_rx,
                       const struct uart_async_rx_config *config);

void uart_async_rx_reset(struct uart_async_rx *async_rx);

void uart_async_rx_on_rdy(struct uart_async_rx *async_rx, uint8_t *buffer, size_t length);

uint8_t *uart_async_rx_buf_req(struct uart_async_rx *async_rx);

void uart_async_rx_on_buf_rel(struct uart_async_rx *async_rx, uint8_t *buf);

size_t uart_async_rx_data_claim(struct uart_async_rx *async_rx, uint8_t **data, size_t length);

bool uart_async_rx_data_consume(struct uart_async_rx *async_rx, size_t length);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_RX_H_ */
```

## 16.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 21 行

@brief 接收缓冲区（RX buffer）结构体，保存缓冲区及其状态。

### 注释 3：原第 23 行

写入索引（write index），每次报告有新数据接收到该缓冲区时递增。

### 注释 4：原第 28 行

驱动释放缓冲区时设为 1。

### 注释 5：原第 31 行

传给 UART 驱动的位置。

### 注释 6：原第 37 行

指向配置结构体的指针。该结构体必须持续有效（persistent）。

### 注释 7：原第 40 行

待处理字节总数（pending bytes）。这些字节可能分布在多个 RX 缓冲区中。

### 注释 8：原第 43 行

空闲缓冲区数量。

### 注释 9：原第 46 行

单个缓冲区大小。

### 注释 10：原第 49 行

下一个将提供给驱动的缓冲区索引。

### 注释 11：原第 52 行

当前正在消费数据的缓冲区。

### 注释 12：原第 55 行

当前正在消费数据的缓冲区内的读取索引（read index）。每次从缓冲区消费数据时递增。

### 注释 13：原第 63 行

指向缓冲区的指针。

### 注释 14：原第 66 行

缓冲区长度。

### 注释 15：原第 69 行

要将所提供空间划分成的缓冲区数量。

### 注释 16：原第 176 行

头文件保护宏（Header guard）标记：`ZEPHYR_DRIVERS_SERIAL_UART_ASYNC_RX_H_`。

## 16.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](../hardware/P344_UART异步接收辅助接口.md)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [uart_async_rx_buf](../hardware/P346_UART异步接收块结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [wr_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a4dbeb091bddcd92e1fe242517f53bb93)
- [completed](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a1baa442e23d9babb701a7fc28d8408a4)
- [buffer](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#ad03eb3023829258581e54c75e0a66942)
- [uart_async_rx](../hardware/P345_UART异步接收状态结构.md)
- [uart_async_rx_config](../hardware/P347_UART异步接收配置结构.md)
- [config](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#abbe20b7426175d7436470f6a26bb578e)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [pending_bytes](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a1150d2c365330c4d87a22b44412611f6)
- [free_buf_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a15510449c58841c7294e0359a92bf4d0)
- [buf_len](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a85ea611224160caee86767b4910e17d9)
- [drv_buf_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ac782b9465c3766d5217676a3a97a963b)
- [rd_buf_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a9a192c4f08f6d946bb562a9bbba8f196)
- [rd_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ad75410820beef5a612f602d3017df5f6)
- [buffer](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a2d5d07f7e98ae6743378f75ce3afc4f2)
- [length](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#ad4eabc44a27b06f93b0d6194903b6b97)
- [buf_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a73a1c096f5aac03f3426c7320241fcf2)
- [uart_async_rx_get_buf_len](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a9e51885811653d21e0e8712b09ef800d)
- [uart_async_rx_init](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a8daddb05f11ad43c8c4510a4312cf38f)
- [uart_async_rx_reset](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#ad551b1684437c8ab48c0708fb5b0d1f6)
- [uart_async_rx_on_rdy](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#acca21c43fa833b4789edbc1bc92bab2b)
- [uart_async_rx_buf_req](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a1eede7070affe966616148924ba2c519)
- [uart_async_rx_on_buf_rel](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a2064f3d760adb4cf6912caf12f7a54cc)
- [uart_async_rx_data_claim](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a8d5ed81dfa4c067f173249744b25561e)
- [uart_async_rx_data_consume](https://docs.zephyrproject.org/latest/doxygen/html/uart__async__rx_8h.html#a1ac0b3ee0e1840177d07c4fbcbd635df)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [uart_async_rx_buf::completed](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a1baa442e23d9babb701a7fc28d8408a4)
- [uart_async_rx_buf::wr_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#a4dbeb091bddcd92e1fe242517f53bb93)
- [uart_async_rx_buf::buffer](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__buf.html#ad03eb3023829258581e54c75e0a66942)
- [uart_async_rx_config::buffer](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a2d5d07f7e98ae6743378f75ce3afc4f2)
- [uart_async_rx_config::buf_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#a73a1c096f5aac03f3426c7320241fcf2)
- [uart_async_rx_config::length](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx__config.html#ad4eabc44a27b06f93b0d6194903b6b97)
- [uart_async_rx::pending_bytes](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a1150d2c365330c4d87a22b44412611f6)
- [uart_async_rx::free_buf_cnt](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a15510449c58841c7294e0359a92bf4d0)
- [uart_async_rx::buf_len](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a85ea611224160caee86767b4910e17d9)
- [uart_async_rx::rd_buf_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#a9a192c4f08f6d946bb562a9bbba8f196)
- [uart_async_rx::config](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#abbe20b7426175d7436470f6a26bb578e)
- [uart_async_rx::drv_buf_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ac782b9465c3766d5217676a3a97a963b)
- [uart_async_rx::rd_idx](https://docs.zephyrproject.org/latest/doxygen/html/structuart__async__rx.html#ad75410820beef5a612f602d3017df5f6)

---

[上一章](P015_tisci.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P017_veml60xx-common.h_源码浏览.md)
