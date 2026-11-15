---
id: learning.zephyr-docs.rtio-model-reference.page-7
title: RTIO提交事件
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structrtio__sqe.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第7章\_RTIO提交事件

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structrtio__sqe.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入RTIO数据结构、事件标志、操作码及优先级说明，再通过交叉引用连接核心接口。源码跟踪译注与官方原文分开标示。

一个提交队列事件（Submission Queue Event，SQE）。

```c
#include <zephyr/rtio/sqe.h>
```

<a id="details"></a>

一个提交队列事件（Submission Queue Event，SQE）。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 7.1\_数据成员（Data Fields）

<a id="r_a1d8d3e3426e47a2c7f54d98f51acd953"></a>

```c
uint8_t op
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[op](#a1d8d3e3426e47a2c7f54d98f51acd953)。

操作码（Operation Code）。

<a id="r_a528eb9b721be7b8a8898ab16a7e2d9a7"></a>

```c
uint8_t prio
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[prio](#a528eb9b721be7b8a8898ab16a7e2d9a7)。

操作优先级（Operation Priority）。

<a id="r_aad2ff8524df0e24b812e77e2393bf5b0"></a>

```c
uint16_t flags
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[flags](#aad2ff8524df0e24b812e77e2393bf5b0)。

操作标志（Operation Flags）。

<a id="r_a8bebe5d55aa8549d749466e444fadf91"></a>

```c
uint32_t iodev_flags
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[iodev_flags](#a8bebe5d55aa8549d749466e444fadf91)。

操作的IODEV标志。

<a id="r_a6c784702f011592c84feacd57915bbfc"></a>

```c
const struct rtio_iodev * iodev
```

相关声明：[rtio_iodev](P003_RTIO输入输出设备.md)、[iodev](#a6c784702f011592c84feacd57915bbfc)。

要在其上执行操作的设备。

<a id="r_a0ed519ee0b5867ff73bdaf37f983c971"></a>

```c
void * userdata
```

相关声明：[userdata](#a0ed519ee0b5867ff73bdaf37f983c971)。

用户提供的数据，在操作完成时返回。

```c
union {
```

```c
struct {
```

<a id="r_ad6597416e68b55e42042d12b5bb2bde0"></a>

```c
uint32_t buf_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[buf_len](#a67376f40a13960b152a23da250275722)。

缓冲区长度。

<a id="r_a897730c06498657b2004935fd98d6c3d"></a>

```c
const uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#ab71176c084e8b8eb65dfeb3018ae2a49)。

写操作的数据来源缓冲区。

<a id="r_ad6cd4108feb2de77ec5cc8805a633722"></a>

```c
} tx
```

相关声明：[tx](#af1bd1edaaf32a58fb0461c989ac2a456)。

`OP_TX`发送操作。

```c
struct {
```

<a id="r_a27b80f62cafa0050a361ed7b54d6f4a1"></a>

```c
uint32_t buf_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[buf_len](#a67376f40a13960b152a23da250275722)。

缓冲区长度。

<a id="r_a36b704452dbfe15f5a1ad5dceabf12b5"></a>

```c
uint8_t * buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a55e98f27b26393fee8e179b7bdb6a52e)。

读操作的数据目标缓冲区。

<a id="r_aef19410b590cfc514e974e96674df201"></a>

```c
} rx
```

相关声明：[rx](#a29e0c1b06b6f7b604af147a231b46319)。

`OP_RX`接收操作。

```c
struct {
```

<a id="r_a5ee669323bb173c8231d14d59b979bac"></a>

```c
uint8_t buf_len
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf_len](#a4125148f520b61d0fe3ba156fbb53322)。

微量缓冲区（Tiny Buffer）的长度。

<a id="r_a1fbe11f7b54d62d7c438ae18b16900cd"></a>

```c
uint8_t buf [7]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[buf](#a8f0544318fa972be2541ae1e85efc33f)。

微量缓冲区（Tiny Buffer）。

<a id="r_addae1c29b5a0c7c5039e0b9ab53df93d"></a>

```c
} tiny_tx
```

相关声明：[tiny_tx](#a2b73e59283f6dc79cef3c804ed973160)。

`OP_TINY_TX`微量发送操作。

```c
struct {
```

<a id="r_a42b4623a3ac87174fd74bebdd035ae5f"></a>

```c
rtio_callback_t callback
```

相关声明：[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)、[callback](#af8c31c33e9fedebe55cac73595d0f696)。

要运行的函数。

<a id="r_a6329336c6692a0c6f38808f45fe4761c"></a>

```c
void * arg0
```

相关声明：[arg0](#a438d2156a61aef9ca840af9c01d5dfa4)。

传给回调的最后一个参数。

<a id="r_a6ed1104e0b00ef80e1c48d6331f676db"></a>

```c
} callback
```

相关声明：[callback](#ab23bc156a99135533b94ebaaba4ebef1)。

`OP_CALLBACK`回调操作。

```c
struct {
```

<a id="r_a0968e99baa1260e774f2b27424601b54"></a>

```c
uint32_t buf_len
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[buf_len](#a67376f40a13960b152a23da250275722)。

发送和接收缓冲区的长度。

<a id="r_ac201aac4f47d72030497ab5803005463"></a>

```c
const uint8_t * tx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[tx_buf](#a18bfa63542954f4bb8b924c92c48e931)。

写操作的数据来源缓冲区。

<a id="r_a8a767988df30e9eb4c7f2eba5ff2732a"></a>

```c
uint8_t * rx_buf
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[rx_buf](#a4d2090fc11b897724a883ad1087d9f73)。

读操作的数据目标缓冲区。

<a id="r_a320e58123775ade78efae5c88f75d2d1"></a>

```c
} txrx
```

相关声明：[txrx](#a927a43f86f65484179c8113caa775c9c)。

`OP_TXRX`收发操作。

<a id="r_a48505a169fab484653eb7f099d0d2fdb"></a>

```c
uint32_t i2c_config
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[i2c_config](#a07bf344b1b1063b8bea80cf5ba1c1cc5)。

`OP_I2C_CONFIGURE`，即I2C配置操作。

```c
struct {
```

<a id="r_a29004110ce403876edfa59adbb916865"></a>

```c
int type
```

相关声明：[type](#aa09a0c93a6e8cfc73278a87942e4af33)。

配置类型，为`enum i3c_config_type`中的一个值。

<a id="r_af97caedbf9d7a8adca11dd03247a708a"></a>

```c
void * config
```

相关声明：[config](#ac07a16c50a067acc90bd4ab08aae4184)。

要应用的配置。

<a id="r_aa45fb1f9ef3f46a4f6aeb611838cf6f9"></a>

```c
} i3c_config
```

相关声明：[i3c_config](#a4bb4f86411b4892be4906901b099f606)。

`OP_I3C_CONFIGURE`，即I3C配置操作。

<a id="r_a8bce159b7e816abfdaa41955185e0b22"></a>

```c
void * ccc_payload
```

相关声明：[ccc_payload](#a8d78973983abca8b97cfc5bcdc2dd2f1)。

`OP_I3C_CCC`，即I3C公共命令码（Common Command Code，CCC）操作。

```c
struct {
```

<a id="r_a06315b0c05c73a5e27a320e399de08fa"></a>

```c
rtio_signaled_t callback
```

相关声明：[rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)、[callback](#a597587210c0a574d95c7c84ae9002267)。

收到信号后要运行的函数。

<a id="r_a79f8e8de2d51b18e4449a0f7896c6610"></a>

```c
void * userdata
```

相关声明：[userdata](#a0ed519ee0b5867ff73bdaf37f983c971)。

<a id="r_a14e0437096b5c99d949ac10f86307897"></a>

```c
} await
```

相关声明：[await](#a64f5db04d58882832f86477628c25be3)。

`OP_AWAIT`等待操作。

<a id="r_a891d2f6c520ead08384d2bae8e646e65"></a>

```c
};
```

操作专用参数，由操作码选择。

## 7.2\_详细说明（Detailed Documentation）

<a id="a891d2f6c520ead08384d2bae8e646e65"></a>

### `[union]`

```c
union { ... } rtio_sqe
```

操作专用参数，由操作码选择。

<a id="a438d2156a61aef9ca840af9c01d5dfa4"></a>

### `arg0`

```c
void* rtio_sqe::arg0
```

传给回调的最后一个参数。

<a id="a64f5db04d58882832f86477628c25be3"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::await
```

`OP_AWAIT`等待操作。

<a id="a8f0544318fa972be2541ae1e85efc33f"></a>

### `buf [1/3]`

```c
uint8_t rtio_sqe::buf[7]
```

微量缓冲区（Tiny Buffer）。

<a id="a55e98f27b26393fee8e179b7bdb6a52e"></a>

### `buf [2/3]`

```c
uint8_t* rtio_sqe::buf
```

读操作的数据目标缓冲区。

<a id="ab71176c084e8b8eb65dfeb3018ae2a49"></a>

### `buf [3/3]`

```c
const uint8_t* rtio_sqe::buf
```

写操作的数据来源缓冲区。

<a id="a4125148f520b61d0fe3ba156fbb53322"></a>

### `buf_len [1/2]`

```c
uint8_t rtio_sqe::buf_len
```

微量缓冲区（Tiny Buffer）的长度。

<a id="a67376f40a13960b152a23da250275722"></a>

### `buf_len [2/2]`

```c
uint32_t rtio_sqe::buf_len
```

缓冲区长度。

发送和接收缓冲区的长度。

<a id="a597587210c0a574d95c7c84ae9002267"></a>

### `callback [1/3]`

```c
rtio_signaled_t rtio_sqe::callback
```

收到信号后要运行的函数。

<a id="ab23bc156a99135533b94ebaaba4ebef1"></a>

### `[struct] [2/3]`

```c
struct { ... } rtio_sqe::callback
```

`OP_CALLBACK`回调操作。

<a id="af8c31c33e9fedebe55cac73595d0f696"></a>

### `callback [3/3]`

```c
rtio_callback_t rtio_sqe::callback
```

要运行的函数。

<a id="a8d78973983abca8b97cfc5bcdc2dd2f1"></a>

### `ccc_payload`

```c
void* rtio_sqe::ccc_payload
```

`OP_I3C_CCC`，即I3C公共命令码（Common Command Code，CCC）操作。

<a id="ac07a16c50a067acc90bd4ab08aae4184"></a>

### `config`

```c
void* rtio_sqe::config
```

要应用的配置。

<a id="aad2ff8524df0e24b812e77e2393bf5b0"></a>

### `flags`

```c
uint16_t rtio_sqe::flags
```

操作标志（Operation Flags）。

<a id="a07bf344b1b1063b8bea80cf5ba1c1cc5"></a>

### `i2c_config`

```c
uint32_t rtio_sqe::i2c_config
```

`OP_I2C_CONFIGURE`，即I2C配置操作。

<a id="a4bb4f86411b4892be4906901b099f606"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::i3c_config
```

`OP_I3C_CONFIGURE`，即I3C配置操作。

<a id="a6c784702f011592c84feacd57915bbfc"></a>

### `iodev`

```c
const struct rtio_iodev* rtio_sqe::iodev
```

要在其上执行操作的设备。

<a id="a8bebe5d55aa8549d749466e444fadf91"></a>

### `iodev_flags`

```c
uint32_t rtio_sqe::iodev_flags
```

操作的IODEV标志。

<a id="a1d8d3e3426e47a2c7f54d98f51acd953"></a>

### `op`

```c
uint8_t rtio_sqe::op
```

操作码（Operation Code）。

<a id="a528eb9b721be7b8a8898ab16a7e2d9a7"></a>

### `prio`

```c
uint8_t rtio_sqe::prio
```

操作优先级（Operation Priority）。

<a id="a29e0c1b06b6f7b604af147a231b46319"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::rx
```

`OP_RX`接收操作。

<a id="a4d2090fc11b897724a883ad1087d9f73"></a>

### `rx_buf`

```c
uint8_t* rtio_sqe::rx_buf
```

读操作的数据目标缓冲区。

<a id="a2b73e59283f6dc79cef3c804ed973160"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::tiny_tx
```

`OP_TINY_TX`微量发送操作。

<a id="af1bd1edaaf32a58fb0461c989ac2a456"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::tx
```

`OP_TX`发送操作。

<a id="a18bfa63542954f4bb8b924c92c48e931"></a>

### `tx_buf`

```c
const uint8_t* rtio_sqe::tx_buf
```

写操作的数据来源缓冲区。

<a id="a927a43f86f65484179c8113caa775c9c"></a>

### `[struct]`

```c
struct { ... } rtio_sqe::txrx
```

`OP_TXRX`收发操作。

<a id="aa09a0c93a6e8cfc73278a87942e4af33"></a>

### `type`

```c
int rtio_sqe::type
```

配置类型，为`enum i3c_config_type`中的一个值。

<a id="a0ed519ee0b5867ff73bdaf37f983c971"></a>

### `userdata`

```c
void* rtio_sqe::userdata
```

用户提供的数据，在操作完成时返回。

可以是指针，也可以是整数。

如果需要唯一标识完成事件，此值也应保持唯一。

## 7.3\_源码定位与版本边界

相对源码定位：[RTIO核心头文件](../../../include/zephyr/rtio/rtio.h)、[提交队列辅助函数](../../../include/zephyr/rtio/sqe.h)、[完成队列定义](../../../include/zephyr/rtio/cqe.h)、[IODEV接口](../../../include/zephyr/rtio/iodev.h)、[执行器](../../../subsys/rtio/rtio_executor.c)、[对象池初始化](../../../subsys/rtio/rtio_init.c)、[系统调用校验](../../../subsys/rtio/rtio_syscalls.c)、[延时实现](../../../subsys/rtio/rtio_timeout.c)、[配置选项](../../../subsys/rtio/Kconfig)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：操作码（Operation Code）选择匿名联合体（Anonymous Union）中的有效参数。写操作使用`tx.buf`／`tx.buf_len`，读操作使用`rx.buf`／`rx.buf_len`，微量写使用`tiny_tx.buf`／`tiny_tx.buf_len`，收发使用`txrx.tx_buf`、`txrx.rx_buf`与共同长度。Doxygen把多个同名成员列为buf、buf_len或[struct]，本页保留这些原始标题及锚点；实际C表达式仍应带上正确的外层成员。

> 译注——源码核对：普通读写准备函数保存缓冲区指针，不复制有效载荷；异步完成前相应内存必须有效。`tiny_tx.buf`在本次头文件中为7字节，微量写辅助函数会把数据复制进去。这不允许向普通写缓冲区提前释放内存，也不允许超过微量缓冲区容量。

> 译注——源码核对：最外层`userdata`随操作完成返回，`callback.arg0`是回调参数，`await.userdata`是等待信号回调的数据，三者职责不同。原文说userdata也可表示整数，但其C类型仍是`void *`；应使用目标平台合适的指针宽度整数转换，不能据此假定所有整数值都可无损往返。

> 译注——源码核对：本页公开成员没有展示等待状态`await.ok`，也没有显示由`CONFIG_RTIO_OP_DELAY`控制的`delay.timeout`和`delay.expiry`字段。原始头文件包含它们，隐藏或条件配置并不意味着运行时不存在这些成员。页面翻译保留官方可见范围，实际布局须以构建所用头文件和配置为准。

> 译注——源码核对：本页译注以来源记录中本次读取的官方源码摘要为界。本仓库的相对源码链接用于追踪同名文件，不保证任意本地版本与滚动更新的main完全一致。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 7.4\_原页交叉引用（Cross References）

- [zephyr/rtio/sqe.h](../rtio_headers_reference/P002_RTIO提交事件头文件源码.md)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [rtio_iodev](P003_RTIO输入输出设备.md)
- [rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)
- [i3c_config_type](../hardware/P425_I3C公共接口参考.md#ga5b111bc8fa8c3bee052e621d26dcc54a)
- [rtio_signaled_t](../rtio_core_reference/P001_RTIO公共接口.md#gab254ffa4d10bfb670bacd1c47c1f8711)
- [rtio_sqe](P007_RTIO提交事件.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P006_RTIO上下文池.md) · [返回大纲](大纲.md) · [下一章](P008_RTIO完成事件标志.md)
