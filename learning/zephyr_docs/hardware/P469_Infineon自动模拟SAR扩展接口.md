---
id: learning.zephyr-docs.hardware.adcdevice-2
title: Infineon自动模拟SAR扩展接口
kind: reference
status: maintained
domains: [zephyr, hardware]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__infineon__autanalog__sar__interface.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

# 第469章\_Infineon自动模拟SAR扩展接口

原文：[group__infineon__autanalog__sar__interface](https://docs.zephyrproject.org/latest/doxygen/html/group__infineon__autanalog__sar__interface.html)。读取日期：2026-10-13，`latest`。

## 469.1\_用途与并发约束

本页为 Infineon（英飞凌）AutAnalog **逐次逼近寄存器（Successive Approximation Register，SAR）模数转换器（Analog-to-Digital Converter，ADC）**扩展应用程序接口（Application Programming Interface，API）。官方注明自 4.5 引入，接口版本为 1.0.0。

```c
#include <zephyr/drivers/adc/infineon_autanalog_sar.h>
```

**这些厂商函数没有与 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3) 做串行化，不得与同一设备上的 ADC 转换并发调用。**它们访问同一个共享 SAR；与正在执行的读取（包括异步 [`adc_read_async()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga009e3733b5b20eb6b26a201c9f9734fc)）重叠，可能破坏转换或有限冲激响应（Finite Impulse Response，FIR）滤波器配置。调用方必须确保没有转换正在进行，例如在执行读取的同一个线程中调用它们。

以下 `dev` 均为 `infineon,autanalog-sar-adc` 实例的 ADC 设备。FIR 索引 `fir_idx` 为 0 或 1；先进先出缓冲区（First In, First Out，FIFO）索引 `buf_idx` 为 0—7，实际取值由 FIFO 分割配置（Split Configuration）决定。

错误码：`-EINVAL` 表示参数无效（Invalid Argument），`-EIO` 表示输入输出错误（Input/Output Error），`-EBUSY` 表示忙（Busy），`-ECANCELED` 表示已取消（Canceled），`-EALREADY` 表示相应状态已存在或无活动操作（Already）。各函数的具体条件见下文。

## 469.2\_FIFO水位中断回调

[`adc_ifx_autanalog_sar_fifo_callback_t`](https://docs.zephyrproject.org/latest/doxygen/html/group__infineon__autanalog__sar__interface.html#gad71c8fb2e66f407a02a2abec62567587) 在 FIFO 水位（Watermark）中断发生时，由中断服务例程（Interrupt Service Routine，ISR）上下文调用。

```c
typedef void (*adc_ifx_autanalog_sar_fifo_callback_t)(
    const struct device *dev, uint32_t fifo_status, void *user_data);
```

`dev` 是 ADC 设备，`fifo_status` 是 `CY_AUTANALOG_INT_FIFO_*` 中断状态位掩码，`user_data` 为通过 [`adc_ifx_autanalog_sar_fifo_set_callback()`](https://docs.zephyrproject.org/latest/doxygen/html/group__infineon__autanalog__sar__interface.html#gac4fac74ab9ae1492b4a085b2c79f956c) 传入的用户数据。

## 469.3\_adc_ifx_autanalog_sar_fifo_get_size

取得指定 FIFO 当前填充量，即保存的数据字数。`buf_idx` 为缓冲区索引，输出 `size` 指向保存字数的位置。成功返回 0，参数无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fifo_get_size( const struct device * dev, uint8_t buf_idx, uint16_t * size );
```

## 469.4\_adc_ifx_autanalog_sar_fifo_read

从 `buf_idx` 指定的 FIFO 最多读取 `max_words` 个转换结果。`data_out` 指向接收 32 位有符号结果的输出缓冲区。返回非负数表示实际读取的字数；参数无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fifo_read( const struct device * dev, uint8_t buf_idx, int32_t * data_out, uint16_t max_words );
```

## 469.5\_adc_ifx_autanalog_sar_fifo_read_all

把 `buf_idx` 指定 FIFO 的全部内容读入 `data_out` 输出数组，元素为 32 位有符号结果。**调用方必须保证数组足够保存 FIFO 分割配置所决定的最大缓冲区容量。**返回非负数表示实际读取的字数；参数无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fifo_read_all( const struct device * dev, uint8_t buf_idx, int32_t * data_out );
```

## 469.6\_adc_ifx_autanalog_sar_fifo_read_chan_id

读取 `buf_idx` 指定 FIFO 的全部数据及关联通道标识。**父 SAR ADC 节点必须启用 `fifo-chan-id` 属性，FIFO 数据中才有通道标识。**

`input` 指定解码通道标识的输入类型：0 为通用输入输出（General-Purpose Input/Output，GPIO），1 为多路复用器（Multiplexer，MUX）。`data_out` 是 32 位有符号结果输出缓冲区，`chan_id_out` 是通道标识输出缓冲区。返回非负数表示实际读取字数；参数无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fifo_read_chan_id( const struct device * dev, uint8_t buf_idx, uint8_t input, int32_t * data_out, uint8_t * chan_id_out );
```

## 469.7\_adc_ifx_autanalog_sar_fifo_set_callback

注册 FIFO 水位中断回调。当填充量达到配置阈值时，在 ISR 上下文调用回调，并传递 FIFO 中断状态位掩码。

`callback` 为回调函数；设为 `NULL` 可注销。`user_data` 为传递给回调的不透明用户指针。成功返回 0。

```c
int adc_ifx_autanalog_sar_fifo_set_callback( const struct device * dev, adc_ifx_autanalog_sar_fifo_callback_t callback, void * user_data );
```

## 469.8\_adc_ifx_autanalog_sar_fir_clear_limit_status

清除 FIR 范围检测（Range Detection，即限值检测）状态位。`fir_idx` 为滤波器索引。成功返回 0；索引无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fir_clear_limit_status( const struct device * dev, uint8_t fir_idx );
```

## 469.9\_adc_ifx_autanalog_sar_fir_get_limit_status

取得 FIR 范围检测状态位图。位 0 对应 FIR 0，位 1 对应 FIR 1，表示哪些滤波器触发了范围检测条件。`fir_idx` 为滤波器索引，`status` 为返回位掩码的输出指针。成功返回 0；参数无效返回 `-EINVAL`。

```c
int adc_ifx_autanalog_sar_fir_get_limit_status( const struct device * dev, uint8_t fir_idx, uint8_t * status );
```

## 469.10\_adc_ifx_autanalog_sar_fir_load_coefficients

运行时替换 `fir_idx` 指定 FIR 的系数集。该 FIR 必须在初始化时通过设备树绑定配置。

**此操作重写读取路径共享的 FIR 硬件配置，不得在本设备进行 ADC 转换时调用，否则可能使一次转换使用到不完整的配置。**

`coefficients` 指向 Q1.15 定点格式（Fixed-point Format）的系数数组，`num_coefficients` 为系数数量，范围 1—64。成功返回 0；参数无效返回 `-EINVAL`；外设驱动库（Peripheral Driver Library，PDL）操作失败返回 `-EIO`。

```c
int adc_ifx_autanalog_sar_fir_load_coefficients( const struct device * dev, uint8_t fir_idx, const int16_t * coefficients, uint8_t num_coefficients );
```

## 469.11\_adc_ifx_autanalog_sar_fir_read_result

读取 `fir_idx` 指定 FIR 的输出结果，通过 `result` 输出 32 位有符号数。成功返回 0；参数无效返回 `-EINVAL`；尚无 FIR 结果时返回 `-EBUSY`。

```c
int adc_ifx_autanalog_sar_fir_read_result( const struct device * dev, uint8_t fir_idx, int32_t * result );
```

## 469.12\_adc_ifx_autanalog_sar_stream_stop

停止活动的实时输入输出（Real-Time Input/Output，RTIO）ADC 流，并拆除其软件状态。将 SAR 序列器切回单次模式（Single-shot），停止自由运行的连续 SAR，清除流状态；若有正在执行的 RTIO 提交，以 `-ECANCELED` 结束。

返回后 SAR 空闲，共享序列器可供后续 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3) 使用；重新调用 [`adc_stream()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga23a55cad65bdbbbbb06cbc7d483b3c2e) 可以重启流。**硬件 FIFO 保持不变，已捕获的样本保留，因此停止后恢复流不会丢失这些数据。**单次 [`adc_read()`](https://docs.zephyrproject.org/latest/doxygen/html/group__adc__interface.html#ga7567ce3b03ebb294620b4e32b7561ab3) 读取结果寄存器而不是 FIFO，不受保留样本影响。

**调用此函数之前，调用方必须先通过 [`rtio_sqe_cancel()`](../rtio_core_reference/P001_RTIO公共接口.md#gac01252e55d2848b38c0ed77b71d600a7) 取消流的多次完成提交队列项（Multishot Submission Queue Entry，SQE）句柄，以免 RTIO 重新提交并启动流。**

唯一参数 `dev` 指定 ADC 设备。成功返回 0；当前没有活动流返回 `-EALREADY`；最后一次转换后 SAR 未返回空闲状态则返回 `-EBUSY`。

```c
int adc_ifx_autanalog_sar_stream_stop( const struct device * dev);
```


---

[上一章：ADS1x4s0x扩展接口](P468_ADS1x4s0x扩展接口.md) · [下一章：LMP90xxx扩展接口](P470_LMP90xxx扩展接口.md) · [返回大纲](大纲.md)
