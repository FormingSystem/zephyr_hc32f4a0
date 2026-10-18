---
id: learning.zephyr-docs.rtio-work-reference.page-2
title: RTIO寄存器映射头文件源码
kind: reference
status: maintained
domains: [zephyr, hardware, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regmap_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_RTIO寄存器映射头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/regmap_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](P001_RTIO寄存器映射头文件参考.md)和[公共API](../rtio_core_reference/P001_RTIO公共接口.md)。

## 2.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="foldopen00026"></a>
<a id="foldopen00031"></a>
<a id="foldopen00049"></a>
<a id="foldopen00060"></a>
<a id="foldopen00070"></a>
<a id="foldopen00080"></a>
<a id="foldopen00119"></a>
<a id="agroup__rtio__i2c__flags_html_gadba1c5eddeecc431000bd92054f55c3a"></a>
<a id="agroup__rtio__i2c__flags_html_gaf923e862d2c6a3fbce5eb96781cf86d8"></a>
<a id="agroup__rtio__i3c__flags_html_ga671a479885f4d9abbdad677ddfbc47df"></a>
<a id="agroup__rtio__i3c__flags_html_ga9d30e1b8f22da07a25fd379c27dc2afe"></a>
<a id="agroup__rtio__sqe__flags_html_ga07f09cc0c95be6cfdddb23f8acacb1ea"></a>
<a id="agroup__rtio__sqe__flags_html_gae9191d521d4ab602b53fefb74020d06b"></a>
<a id="agroup__rtio__sqe__prio_html_gab02e27e01b7dd4eb3439df557899ce92"></a>
<a id="agroup__rtio_html_ga31be14ece09e061a8d42ca8f2395286a"></a>
<a id="agroup__rtio_html_ga5d5b7d440eab064918424b0261455a9f"></a>
<a id="agroup__rtio_html_ga89c7cc2494e3dda50737f78f1a1376cf"></a>
<a id="agroup__rtio_html_ga8b47c954d15a334621def53acceb6799"></a>
<a id="agroup__rtio_html_ga9486fb7b50e8d2409a50da235203536b"></a>
<a id="agroup__rtio_html_gaada07aa6acefa548743b525225fa482f"></a>
<a id="agroup__rtio_html_gae87be354087d038953dae07c7f9cd3b0"></a>
<a id="agroup__rtio_html_gafee27c64a4a4989c4eb774addde8eb2e"></a>
<a id="agroup__system__errno_html_ga6a05c923dad0c1208043e9c20a58c8e5"></a>
<a id="aregmap_8h_html_a3a3c3ee815644c5bb902632d4b3640ad"></a>
<a id="aregmap_8h_html_aa75738a91bc261196c140a9899ef3026"></a>
<a id="aregmap_8h_html_aa75738a91bc261196c140a9899ef3026a0d014a0d843d6e8bae70039ef03fcf4a"></a>
<a id="aregmap_8h_html_aa75738a91bc261196c140a9899ef3026a79d24e2954651825c0919c340303fddb"></a>
<a id="aregmap_8h_html_aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3"></a>
<a id="aregmap_8h_html_ab2aad1556946d53016741a158ef7ad44"></a>
<a id="aregmap_8h_html_ac660021ade3146276519b665c23aeb4e"></a>
<a id="aregmap_8h_html_afb342104c67b6f7939412e88d673aee2"></a>
<a id="artio_2rtio_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructdevice_html"></a>
<a id="astructrtio__iodev__sqe_html"></a>
<a id="astructrtio__iodev_html"></a>
<a id="astructrtio__regs_1_1rtio__regs__list_html"></a>
<a id="astructrtio__regs_1_1rtio__regs__list_html_a3a35dd42e3fdd4159b35da38f327bfbd"></a>
<a id="astructrtio__regs_1_1rtio__regs__list_html_ac5fc22a14818e9beb4e9952122f0753a"></a>
<a id="astructrtio__regs_1_1rtio__regs__list_html_afbcfb27d914d7c7c55c0efa214df1274"></a>
<a id="astructrtio__regs_html"></a>
<a id="astructrtio__regs_html_a1234a064ccc401b70dcc78b12938722c"></a>
<a id="astructrtio__regs_html_adc88caf9fee2e0a8d5bcc83355d361dd"></a>
<a id="astructrtio__sqe_html"></a>
<a id="astructrtio__sqe_html_a6c784702f011592c84feacd57915bbfc"></a>
<a id="astructrtio__sqe_html_a8bebe5d55aa8549d749466e444fadf91"></a>
<a id="astructrtio__sqe_html_aad2ff8524df0e24b812e77e2393bf5b0"></a>
<a id="astructrtio_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2025 STMicroelectronics
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>#ifndef ZEPHYR_INCLUDE_RTIO_REGMAP_H_
<a id="l00014"></a>#define ZEPHYR_INCLUDE_RTIO_REGMAP_H_
<a id="l00015"></a>
<a id="l00016"></a>#include &lt;zephyr/rtio/rtio.h&gt;
<a id="l00017"></a>
<a id="l00018"></a>#ifdef __cplusplus
<a id="l00019"></a>extern "C" {
<a id="l00020"></a>#endif
<a id="l00021"></a>
<a id="l00026"></a>struct rtio_regs {
<a id="l00028"></a>        size_t rtio_regs_num;
<a id="l00029"></a>
<a id="l00031"></a>        struct rtio_regs_list {
<a id="l00033"></a>                uint8_t reg_addr;
<a id="l00034"></a>
<a id="l00036"></a>                uint8_t *bufp;
<a id="l00037"></a>
<a id="l00039"></a>                size_t len;
<a id="l00040"></a>        } *rtio_regs_list;
<a id="l00041"></a>};
<a id="l00042"></a>
<a id="l00049"></a>typedef enum {
<a id="l00050"></a>        RTIO_BUS_I2C,
<a id="l00051"></a>        RTIO_BUS_SPI,
<a id="l00052"></a>        RTIO_BUS_I3C,
<a id="l00053"></a>} rtio_bus_type;
<a id="l00054"></a>
<a id="l00060"></a>static inline bool rtio_is_spi(rtio_bus_type bus_type)
<a id="l00061"></a>{
<a id="l00062"></a>        return (bus_type == RTIO_BUS_SPI);
<a id="l00063"></a>}
<a id="l00064"></a>
<a id="l00070"></a>static inline bool rtio_is_i2c(rtio_bus_type bus_type)
<a id="l00071"></a>{
<a id="l00072"></a>        return (bus_type == RTIO_BUS_I2C);
<a id="l00073"></a>}
<a id="l00074"></a>
<a id="l00080"></a>static inline bool rtio_is_i3c(rtio_bus_type bus_type)
<a id="l00081"></a>{
<a id="l00082"></a>        return (bus_type == RTIO_BUS_I3C);
<a id="l00083"></a>}
<a id="l00084"></a>
<a id="l00119"></a>static inline void rtio_read_regs_async(struct rtio *r, struct rtio_iodev *iodev,
<a id="l00120"></a>                                        rtio_bus_type bus_type, struct rtio_regs *regs,
<a id="l00121"></a>                                        struct rtio_iodev_sqe *iodev_sqe, const struct device *dev,
<a id="l00122"></a>                                        rtio_callback_t complete_op_cb)
<a id="l00123"></a>{
<a id="l00124"></a>        struct rtio_sqe *write_addr;
<a id="l00125"></a>        struct rtio_sqe *read_reg;
<a id="l00126"></a>        struct rtio_sqe *complete_op;
<a id="l00127"></a>
<a id="l00128"></a>        for (uint8_t i = 0; i &lt; regs-&gt;rtio_regs_num; i++) {
<a id="l00129"></a>
<a id="l00130"></a>                write_addr = rtio_sqe_acquire(r);
<a id="l00131"></a>                read_reg = rtio_sqe_acquire(r);
<a id="l00132"></a>
<a id="l00133"></a>                if (write_addr == NULL || read_reg == NULL) {
<a id="l00134"></a>                        rtio_iodev_sqe_err(iodev_sqe, -ENOMEM);
<a id="l00135"></a>                        rtio_sqe_drop_all(r);
<a id="l00136"></a>                        return;
<a id="l00137"></a>                }
<a id="l00138"></a>
<a id="l00139"></a>                rtio_sqe_prep_tiny_write(write_addr, iodev, RTIO_PRIO_NORM,
<a id="l00140"></a>                                         &amp;regs-&gt;rtio_regs_list[i].reg_addr, 1, NULL);
<a id="l00141"></a>                write_addr-&gt;flags = RTIO_SQE_TRANSACTION;
<a id="l00142"></a>
<a id="l00143"></a>                rtio_sqe_prep_read(read_reg, iodev, RTIO_PRIO_NORM, regs-&gt;rtio_regs_list[i].bufp,
<a id="l00144"></a>                                   regs-&gt;rtio_regs_list[i].len, NULL);
<a id="l00145"></a>                read_reg-&gt;flags = RTIO_SQE_CHAINED;
<a id="l00146"></a>
<a id="l00147"></a>                switch (bus_type) {
<a id="l00148"></a>                case RTIO_BUS_I2C:
<a id="l00149"></a>                        read_reg-&gt;iodev_flags |= RTIO_IODEV_I2C_STOP | RTIO_IODEV_I2C_RESTART;
<a id="l00150"></a>                        break;
<a id="l00151"></a>                case RTIO_BUS_I3C:
<a id="l00152"></a>                        read_reg-&gt;iodev_flags |= RTIO_IODEV_I3C_STOP | RTIO_IODEV_I3C_RESTART;
<a id="l00153"></a>                        break;
<a id="l00154"></a>                case RTIO_BUS_SPI:
<a id="l00155"></a>                default:
<a id="l00156"></a>                        break;
<a id="l00157"></a>                }
<a id="l00158"></a>        }
<a id="l00159"></a>
<a id="l00160"></a>        complete_op = rtio_sqe_acquire(r);
<a id="l00161"></a>        if (complete_op == NULL) {
<a id="l00162"></a>                rtio_iodev_sqe_err(iodev_sqe, -ENOMEM);
<a id="l00163"></a>                rtio_sqe_drop_all(r);
<a id="l00164"></a>                return;
<a id="l00165"></a>        }
<a id="l00166"></a>
<a id="l00167"></a>        rtio_sqe_prep_callback_no_cqe(complete_op, complete_op_cb, (void *)dev, iodev_sqe);
<a id="l00168"></a>
<a id="l00169"></a>        rtio_submit(r, 0);
<a id="l00170"></a>}
<a id="l00171"></a>
<a id="l00172"></a>#ifdef __cplusplus
<a id="l00173"></a>}
<a id="l00174"></a>#endif
<a id="l00175"></a>
<a id="l00176"></a>#endif /* ZEPHYR_INCLUDE_RTIO_REGMAP_H_ */
</code></pre>

## 2.2\_可见注释译文（Comments）

1. 版权属于STMicroelectronics（2025年），许可证为Apache-2.0；原始版权与SPDX记录保留。

2. 头文件保护宏`ZEPHYR_INCLUDE_RTIO_REGMAP_H_`结束。

## 2.3\_原页符号提示（Symbol Descriptions）

### `RTIO_IODEV_I2C_RESTART`

```c
#define RTIO_IODEV_I2C_RESTART
```

等效于`I2C_MSG_RESTART`重新开始（Restart）标志。

定义位置（Definition）：sqe.h:200。

符号定位：[RTIO_IODEV_I2C_RESTART](../hardware/P442_RTIO的I2C标志.md#gadba1c5eddeecc431000bd92054f55c3a)。

### `RTIO_IODEV_I2C_STOP`

```c
#define RTIO_IODEV_I2C_STOP
```

等效于`I2C_MSG_STOP`停止（Stop）标志。

定义位置（Definition）：sqe.h:195。

符号定位：[RTIO_IODEV_I2C_STOP](../hardware/P442_RTIO的I2C标志.md#gaf923e862d2c6a3fbce5eb96781cf86d8)。

### `RTIO_IODEV_I3C_STOP`

```c
#define RTIO_IODEV_I3C_STOP
```

等效于`I3C_MSG_STOP`停止（Stop）标志。

定义位置（Definition）：sqe.h:221。

符号定位：[RTIO_IODEV_I3C_STOP](../hardware/P434_RTIO的I3C标志.md#ga671a479885f4d9abbdad677ddfbc47df)。

### `RTIO_IODEV_I3C_RESTART`

```c
#define RTIO_IODEV_I3C_RESTART
```

等效于`I3C_MSG_RESTART`重新开始（Restart）标志。

定义位置（Definition）：sqe.h:226。

符号定位：[RTIO_IODEV_I3C_RESTART](../hardware/P434_RTIO的I3C标志.md#ga9d30e1b8f22da07a25fd379c27dc2afe)。

### `RTIO_SQE_TRANSACTION`

```c
#define RTIO_SQE_TRANSACTION
```

队列中的下一个请求属于同一事务（Transaction）。

定义位置（Definition）：sqe.h:94。

符号定位：[RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)。

### `RTIO_SQE_CHAINED`

```c
#define RTIO_SQE_CHAINED
```

队列中的下一个请求应等待此请求。

定义位置（Definition）：sqe.h:82。

符号定位：[RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)。

### `RTIO_PRIO_NORM`

```c
#define RTIO_PRIO_NORM
```

普通优先级（Normal Priority）。

定义位置（Definition）：sqe.h:56。

符号定位：[RTIO_PRIO_NORM](../rtio_model_reference/P011_RTIO优先级.md#gab02e27e01b7dd4eb3439df557899ce92)。

### `rtio_sqe_prep_tiny_write`

```c
static void rtio_sqe_prep_tiny_write(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, const uint8_t *tiny_write_data, uint8_t tiny_write_len, void *userdata)
```

准备一个微量写操作（Tiny Write）提交。

定义位置（Definition）：sqe.h:533。

符号定位：[rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)。

### `rtio_callback_t`

```c
void(* rtio_callback_t)(struct rtio *r, const struct rtio_sqe *sqe, int res, void *arg0)
```

`RTIO_OP_CALLBACK`的回调函数签名（Callback Signature）。

定义位置（Definition）：sqe.h:297。

符号定位：[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)。

### `rtio_sqe_prep_read`

```c
static void rtio_sqe_prep_read(struct rtio_sqe *sqe, const struct rtio_iodev *iodev, int8_t prio, uint8_t *buf, uint32_t len, void *userdata)
```

准备一个读操作（Read Operation）提交。

定义位置（Definition）：sqe.h:462。

符号定位：[rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)。

### `rtio_sqe_acquire`

```c
static struct rtio_sqe * rtio_sqe_acquire(struct rtio *r)
```

如果可用，获取一个提交队列事件（SQE）。

定义位置（Definition）：rtio.h:362。

符号定位：[rtio_sqe_acquire](../rtio_core_reference/P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)。

### `rtio_sqe_drop_all`

```c
static void rtio_sqe_drop_all(struct rtio *r)
```

丢弃先前获取的全部SQE。

定义位置（Definition）：rtio.h:428。

符号定位：[rtio_sqe_drop_all](../rtio_core_reference/P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)。

### `rtio_iodev_sqe_err`

```c
static void rtio_iodev_sqe_err(struct rtio_iodev_sqe *iodev_sqe, int result)
```

通知执行器（Executor）：一次提交已出错完成。

定义位置（Definition）：rtio.h:735。

符号定位：[rtio_iodev_sqe_err](../rtio_core_reference/P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)。

### `rtio_sqe_prep_callback_no_cqe`

```c
static void rtio_sqe_prep_callback_no_cqe(struct rtio_sqe *sqe, rtio_callback_t callback, void *arg0, void *userdata)
```

准备一个不产生CQE的回调操作提交。

定义位置（Definition）：sqe.h:584。

符号定位：[rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)。

### `rtio_submit`

```c
int rtio_submit(struct rtio *r, uint32_t wait_count)
```

向底层执行器（Executor）提交I/O请求。

符号定位：[rtio_submit](../rtio_core_reference/P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)。

### `ENOMEM`

```c
#define ENOMEM
```

内存不足（Not Enough Core）。

定义位置（Definition）：errno.h:51。

符号定位：[ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)。

### `rtio_read_regs_async`

```c
static void rtio_read_regs_async(struct rtio *r, struct rtio_iodev *iodev, rtio_bus_type bus_type, struct rtio_regs *regs, struct rtio_iodev_sqe *iodev_sqe, const struct device *dev, rtio_callback_t complete_op_cb)
```

创建一条提交队列事件链（SQE Chain），表示用于读取寄存器的总线事务（Bus Transaction）。

定义位置（Definition）：regmap.h:119。

符号定位：[rtio_read_regs_async](P001_RTIO寄存器映射头文件参考.md#a3a3c3ee815644c5bb902632d4b3640ad)。

### `rtio_bus_type`

```c
rtio_bus_type
```

总线类型（Bus Type）。

定义位置（Definition）：regmap.h:49。

符号定位：[rtio_bus_type](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026)。

### `RTIO_BUS_I2C`

```c
@ RTIO_BUS_I2C
```

I2C总线（Inter-Integrated Circuit）。

定义位置（Definition）：regmap.h:50。

符号定位：[RTIO_BUS_I2C](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a0d014a0d843d6e8bae70039ef03fcf4a)。

### `RTIO_BUS_I3C`

```c
@ RTIO_BUS_I3C
```

I3C总线（Improved Inter-Integrated Circuit）。

定义位置（Definition）：regmap.h:52。

符号定位：[RTIO_BUS_I3C](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a79d24e2954651825c0919c340303fddb)。

### `RTIO_BUS_SPI`

```c
@ RTIO_BUS_SPI
```

SPI总线（Serial Peripheral Interface）。

定义位置（Definition）：regmap.h:51。

符号定位：[RTIO_BUS_SPI](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3)。

### `rtio_is_i3c`

```c
static bool rtio_is_i3c(rtio_bus_type bus_type)
```

检查总线是否为I3C。

定义位置（Definition）：regmap.h:80。

符号定位：[rtio_is_i3c](P001_RTIO寄存器映射头文件参考.md#ab2aad1556946d53016741a158ef7ad44)。

### `rtio_is_spi`

```c
static bool rtio_is_spi(rtio_bus_type bus_type)
```

检查总线是否为SPI。

定义位置（Definition）：regmap.h:60。

符号定位：[rtio_is_spi](P001_RTIO寄存器映射头文件参考.md#ac660021ade3146276519b665c23aeb4e)。

### `rtio_is_i2c`

```c
static bool rtio_is_i2c(rtio_bus_type bus_type)
```

检查总线是否为I2C。

定义位置（Definition）：regmap.h:70。

符号定位：[rtio_is_i2c](P001_RTIO寄存器映射头文件参考.md#afb342104c67b6f7939412e88d673aee2)。

### `rtio.h`

以较少工作量移动字节的实时输入输出（Real-Time I/O，RTIO）设备API。

符号定位：[rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)。

### `uint8_t`

```c
__UINT8_TYPE__ uint8_t
```

定义位置（Definition）：stdint.h:88。

符号定位：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

### `device`

每个驱动实例对应的运行时设备结构体（Runtime Device Structure），存放于只读存储器（ROM）中。

定义位置（Definition）：device.h:543。

符号定位：[device](../device_reference/P002_设备对象结构.md)。

### `rtio_iodev_sqe`

输入输出设备提交队列条目（I/O Device Submission Queue Entry）。

定义位置（Definition）：sqe.h:403。

符号定位：[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

### `rtio_iodev`

具有请求提交函数表（Function Table）的输入输出设备（I/O Device）。

定义位置（Definition）：iodev.h:49。

符号定位：[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)。

### `rtio_regs::rtio_regs_list`

单个内存块的描述。

定义位置（Definition）：regmap.h:31。

符号定位：[rtio_regs::rtio_regs_list](P004_RTIO寄存器列表.md)。

### `rtio_regs::rtio_regs_list::bufp`

```c
uint8_t * bufp
```

指向数据缓冲区的有效指针。

定义位置（Definition）：regmap.h:36。

符号定位：[rtio_regs::rtio_regs_list::bufp](P004_RTIO寄存器列表.md#a3a35dd42e3fdd4159b35da38f327bfbd)。

### `rtio_regs::rtio_regs_list::len`

```c
size_t len
```

缓冲区长度，单位为字节。

定义位置（Definition）：regmap.h:39。

符号定位：[rtio_regs::rtio_regs_list::len](P004_RTIO寄存器列表.md#ac5fc22a14818e9beb4e9952122f0753a)。

### `rtio_regs::rtio_regs_list::reg_addr`

```c
uint8_t reg_addr
```

寄存器地址（Register Address）。

定义位置（Definition）：regmap.h:33。

符号定位：[rtio_regs::rtio_regs_list::reg_addr](P004_RTIO寄存器列表.md#afbcfb27d914d7c7c55c0efa214df1274)。

### `rtio_regs`

用于描述RTIO操作所涉及的一组不连续内存块（Non-consecutive Memory Chunks）的结构体。

定义位置（Definition）：regmap.h:26。

符号定位：[rtio_regs](P003_RTIO寄存器配置.md)。

### `rtio_regs::rtio_regs_num`

```c
size_t rtio_regs_num
```

列表中的寄存器数量。

定义位置（Definition）：regmap.h:28。

符号定位：[rtio_regs::rtio_regs_num](P003_RTIO寄存器配置.md#a1234a064ccc401b70dcc78b12938722c)。

### `rtio_regs::rtio_regs_list`

```c
struct rtio_regs::rtio_regs_list * rtio_regs_list
```

包含`rtio_regs_num`个内存块的数组。

符号定位：[rtio_regs::rtio_regs_list](P003_RTIO寄存器配置.md#adc88caf9fee2e0a8d5bcc83355d361dd)。

### `rtio_sqe`

一个提交队列事件（Submission Queue Event，SQE）。

定义位置（Definition）：sqe.h:310。

符号定位：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)。

### `rtio_sqe::iodev`

```c
const struct rtio_iodev * iodev
```

要在其上执行操作的设备。

定义位置（Definition）：sqe.h:319。

符号定位：[rtio_sqe::iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)。

### `rtio_sqe::iodev_flags`

```c
uint32_t iodev_flags
```

操作的IODEV标志。

定义位置（Definition）：sqe.h:317。

符号定位：[rtio_sqe::iodev_flags](../rtio_model_reference/P007_RTIO提交事件.md#a8bebe5d55aa8549d749466e444fadf91)。

### `rtio_sqe::flags`

```c
uint16_t flags
```

操作标志（Operation Flags）。

定义位置（Definition）：sqe.h:315。

符号定位：[rtio_sqe::flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)。

### `rtio`

一个RTIO上下文（Context），其内容可以视为一对队列。

定义位置（Definition）：rtio.h:83。

符号定位：[rtio](../rtio_model_reference/P001_RTIO上下文.md)。

## 2.4\_源码跟踪译注

> 译注——原示例写作`struct rtio_reg_list`，本次头文件实际声明为`struct rtio_regs_list`，多一个s；示例中的寄存器名和省略号也是示意内容。本页完整保留官方原例，不把它描述成无需修改就可编译的程序。

> 译注——对列表中的每一项，辅助函数先准备一个1字节tiny_write发送寄存器地址，再准备一个read读取数据。前者设置TRANSACTION，使地址与读取成为一个事务；后者设置CHAINED，使下一项或末尾回调在之后执行。I2C／I3C读取条目还设置STOP和RESTART；SPI分支不自动设置读方向位，调用者必须按设备协议预先设置reg_addr。

> 译注——非空列表N项会取得2N个读写SQE和1个末尾回调SQE，全部准备完才调用rtio_submit(r, 0)。应考虑上下文已有待提交请求以及整组2N+1个条目的容量。获取失败时通过rtio_iodev_sqe_err(iodev_sqe, -ENOMEM)报告，并调用rtio_sqe_drop_all(r)清理整个上下文待提交队列，不仅是当前寄存器列表。

> 译注——寄存器地址在准备时复制到tiny_write的内部数组，读取目标bufp只保存引用，数据缓冲区必须在异步使用期间有效；不能因函数返回就释放。reg_addr是uint8_t，len是size_t，但read准备函数的长度参数为uint32_t；使用方应遵守实际地址和长度表示范围，不能把此辅助函数当作任意宽度寄存器地址传输器。

> 译注——rtio_regs_num是size_t，但本次遍历变量为uint8_t。对超过255项的列表，循环变量会回绕，不能据size_t类型认为任意大列表都受支持。此处记录源码限制，没有修改官方实现。

> 译注——末尾使用rtio_sqe_prep_callback_no_cqe，回调arg0保存dev，SQE的userdata保存传入iodev_sqe。这个末尾回调本身不再产生CQE，辅助函数也没有统一消费前面的CQE；完成报告与结果清理由调用方的complete_op_cb按协议处理。void返回和rtio_submit(r, 0)都不表示总线已经完成。原文把iodev_sqe称为await操作提交，但本辅助函数没有创建AWAIT操作，而是把该参数用于错误报告和末尾回调的关联数据。

> 译注——rtio_is_spi／i2c／i3c只比较枚举值，不探测实际设备能力。未知bus_type在当前switch中与SPI一样不设置I2C／I3C标志，但这不代表它是已受支持的总线类型。

头文件相对定位：[include/zephyr/rtio/regmap.h](../../../include/zephyr/rtio/regmap.h)，关联实现／接口：[include/zephyr/rtio/sqe.h](../../../include/zephyr/rtio/sqe.h)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/regmap.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/rtio/sqe.h)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 2.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P001_RTIO寄存器映射头文件参考.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P002_RTIO核心头文件参考.md)
- [rtio_regs](P003_RTIO寄存器配置.md)
- [rtio_regs_num](P003_RTIO寄存器配置.md#a1234a064ccc401b70dcc78b12938722c)
- [rtio_regs_list](P004_RTIO寄存器列表.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [reg_addr](P004_RTIO寄存器列表.md#afbcfb27d914d7c7c55c0efa214df1274)
- [bufp](P004_RTIO寄存器列表.md#a3a35dd42e3fdd4159b35da38f327bfbd)
- [len](P004_RTIO寄存器列表.md#ac5fc22a14818e9beb4e9952122f0753a)
- [rtio_regs_list](P003_RTIO寄存器配置.md#adc88caf9fee2e0a8d5bcc83355d361dd)
- [RTIO_BUS_I2C](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a0d014a0d843d6e8bae70039ef03fcf4a)
- [RTIO_BUS_SPI](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3)
- [RTIO_BUS_I3C](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026a79d24e2954651825c0919c340303fddb)
- [rtio_bus_type](P001_RTIO寄存器映射头文件参考.md#aa75738a91bc261196c140a9899ef3026)
- [rtio_is_spi](P001_RTIO寄存器映射头文件参考.md#ac660021ade3146276519b665c23aeb4e)
- [rtio_is_i2c](P001_RTIO寄存器映射头文件参考.md#afb342104c67b6f7939412e88d673aee2)
- [rtio_is_i3c](P001_RTIO寄存器映射头文件参考.md#ab2aad1556946d53016741a158ef7ad44)
- [rtio_read_regs_async](P001_RTIO寄存器映射头文件参考.md#a3a3c3ee815644c5bb902632d4b3640ad)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [device](../device_reference/P002_设备对象结构.md)
- [rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [rtio_sqe_acquire](../rtio_core_reference/P001_RTIO公共接口.md#ga8b47c954d15a334621def53acceb6799)
- [rtio_iodev_sqe_err](../rtio_core_reference/P001_RTIO公共接口.md#gaada07aa6acefa548743b525225fa482f)
- [ENOMEM](../error_reference/P003_系统错误号公共接口.md#ga6a05c923dad0c1208043e9c20a58c8e5)
- [rtio_sqe_drop_all](../rtio_core_reference/P001_RTIO公共接口.md#ga9486fb7b50e8d2409a50da235203536b)
- [rtio_sqe_prep_tiny_write](../rtio_core_reference/P001_RTIO公共接口.md#ga31be14ece09e061a8d42ca8f2395286a)
- [iodev](../rtio_model_reference/P007_RTIO提交事件.md#a6c784702f011592c84feacd57915bbfc)
- [RTIO_PRIO_NORM](../rtio_model_reference/P011_RTIO优先级.md#gab02e27e01b7dd4eb3439df557899ce92)
- [flags](../rtio_model_reference/P007_RTIO提交事件.md#aad2ff8524df0e24b812e77e2393bf5b0)
- [RTIO_SQE_TRANSACTION](../rtio_model_reference/P010_RTIO提交事件标志.md#ga07f09cc0c95be6cfdddb23f8acacb1ea)
- [rtio_sqe_prep_read](../rtio_core_reference/P001_RTIO公共接口.md#ga89c7cc2494e3dda50737f78f1a1376cf)
- [RTIO_SQE_CHAINED](../rtio_model_reference/P010_RTIO提交事件标志.md#gae9191d521d4ab602b53fefb74020d06b)
- [iodev_flags](../rtio_model_reference/P007_RTIO提交事件.md#a8bebe5d55aa8549d749466e444fadf91)
- [RTIO_IODEV_I2C_STOP](../hardware/P442_RTIO的I2C标志.md#gaf923e862d2c6a3fbce5eb96781cf86d8)
- [RTIO_IODEV_I2C_RESTART](../hardware/P442_RTIO的I2C标志.md#gadba1c5eddeecc431000bd92054f55c3a)
- [RTIO_IODEV_I3C_STOP](../hardware/P434_RTIO的I3C标志.md#ga671a479885f4d9abbdad677ddfbc47df)
- [RTIO_IODEV_I3C_RESTART](../hardware/P434_RTIO的I3C标志.md#ga9d30e1b8f22da07a25fd379c27dc2afe)
- [rtio_sqe_prep_callback_no_cqe](../rtio_core_reference/P001_RTIO公共接口.md#gae87be354087d038953dae07c7f9cd3b0)
- [rtio_submit](../rtio_core_reference/P001_RTIO公共接口.md#gafee27c64a4a4989c4eb774addde8eb2e)

---

[上一章](P001_RTIO寄存器映射头文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_RTIO寄存器配置.md)
