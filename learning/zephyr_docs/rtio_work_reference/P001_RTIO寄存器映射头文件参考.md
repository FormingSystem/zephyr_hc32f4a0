---
id: learning.zephyr-docs.rtio-work-reference.page-1
title: RTIO寄存器映射头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/regmap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第1章\_RTIO寄存器映射头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/regmap_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入寄存器映射、工作队列的参考与源码浏览页及相关结构体，再通过接口链接进入完整说明。源码跟踪译注与官方原文分开标示。

通过RTIO读写设备寄存器列表（Device Register Lists）的辅助函数。

<a id="details"></a>

```c
#include <zephyr/rtio/rtio.h>
```

查看此文件的源码。

通过RTIO读写设备寄存器列表（Device Register Lists）的辅助函数。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 1.1\_数据结构（Data Structures）

<a id="r_rtio_5Fregs"></a>

```c
struct rtio_regs
```

相关声明：[rtio_regs](P003_RTIO寄存器配置.md)。

用于描述RTIO操作所涉及的一组不连续内存块（Non-consecutive Memory Chunks）的结构体。

<a id="r_rtio_5Fregs_3A_3Artio_5Fregs_5Flist"></a>

```c
struct rtio_regs::rtio_regs_list
```

相关声明：[rtio_regs::rtio_regs_list](P004_RTIO寄存器列表.md)。

单个内存块的描述。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 1.2\_枚举（Enumerations）

<a id="r_aa75738a91bc261196c140a9899ef3026"></a>

```c
enum rtio_bus_type { RTIO_BUS_I2C , RTIO_BUS_SPI , RTIO_BUS_I3C }
```

相关声明：[rtio_bus_type](#aa75738a91bc261196c140a9899ef3026)、[RTIO_BUS_I2C](#aa75738a91bc261196c140a9899ef3026a0d014a0d843d6e8bae70039ef03fcf4a)、[RTIO_BUS_SPI](#aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3)、[RTIO_BUS_I3C](#aa75738a91bc261196c140a9899ef3026a79d24e2954651825c0919c340303fddb)。

总线类型（Bus Type）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 1.3\_函数（Functions）

<a id="r_ac660021ade3146276519b665c23aeb4e"></a>

```c
static bool rtio_is_spi (rtio_bus_type bus_type)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rtio_is_spi](#ac660021ade3146276519b665c23aeb4e)、[rtio_bus_type](#aa75738a91bc261196c140a9899ef3026)。

检查总线是否为SPI。

<a id="r_afb342104c67b6f7939412e88d673aee2"></a>

```c
static bool rtio_is_i2c (rtio_bus_type bus_type)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rtio_is_i2c](#afb342104c67b6f7939412e88d673aee2)、[rtio_bus_type](#aa75738a91bc261196c140a9899ef3026)。

检查总线是否为I2C。

<a id="r_ab2aad1556946d53016741a158ef7ad44"></a>

```c
static bool rtio_is_i3c (rtio_bus_type bus_type)
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[rtio_is_i3c](#ab2aad1556946d53016741a158ef7ad44)、[rtio_bus_type](#aa75738a91bc261196c140a9899ef3026)。

检查总线是否为I3C。

<a id="r_a3a3c3ee815644c5bb902632d4b3640ad"></a>

```c
static void rtio_read_regs_async (struct rtio *r, struct rtio_iodev *iodev, rtio_bus_type bus_type, struct rtio_regs *regs, struct rtio_iodev_sqe *iodev_sqe, const struct device *dev, rtio_callback_t complete_op_cb)
```

相关声明：[rtio_read_regs_async](#a3a3c3ee815644c5bb902632d4b3640ad)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[rtio_bus_type](#aa75738a91bc261196c140a9899ef3026)、[rtio_regs](P003_RTIO寄存器配置.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)、[device](../device_reference/P002_设备对象结构.md)、[rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)。

创建一条提交队列事件链（SQE Chain），表示用于读取寄存器的总线事务（Bus Transaction）。

## 1.4\_详细说明（Detailed Documentation）

<a id="aa75738a91bc261196c140a9899ef3026"></a>

### `rtio_bus_type`

```c
enum rtio_bus_type
```

总线类型（Bus Type）。

RTIO工作在支持RTIO的总线之上。有些RTIO操作需要按总线类型进行处理，例如`rtio_read_regs_async`。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `RTIO_BUS_I2C` | I2C总线（Inter-Integrated Circuit）。 |
| `RTIO_BUS_SPI` | SPI总线（Serial Peripheral Interface）。 |
| `RTIO_BUS_I3C` | I3C总线（Improved Inter-Integrated Circuit）。 |

<a id="afb342104c67b6f7939412e88d673aee2"></a>

### `rtio_is_i2c()`

```c
bool rtio_is_i2c ( rtio_bus_type bus_type)
```

声明属性：`inline`、`static`。

检查总线是否为I2C。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus_type` | 总线类型：I2C、SPI或I3C。 |

返回（Returns）：总线类型为I2C时返回`true`。

<a id="ab2aad1556946d53016741a158ef7ad44"></a>

### `rtio_is_i3c()`

```c
bool rtio_is_i3c ( rtio_bus_type bus_type)
```

声明属性：`inline`、`static`。

检查总线是否为I3C。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus_type` | 总线类型：I2C、SPI或I3C。 |

返回（Returns）：总线类型为I3C时返回`true`。

<a id="ac660021ade3146276519b665c23aeb4e"></a>

### `rtio_is_spi()`

```c
bool rtio_is_spi ( rtio_bus_type bus_type)
```

声明属性：`inline`、`static`。

检查总线是否为SPI。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `bus_type` | 总线类型：I2C、SPI或I3C。 |

返回（Returns）：总线类型为SPI时返回`true`。

<a id="a3a3c3ee815644c5bb902632d4b3640ad"></a>

### `rtio_read_regs_async()`

```c
void rtio_read_regs_async ( struct rtio * r, struct rtio_iodev * iodev, rtio_bus_type bus_type, struct rtio_regs * regs, struct rtio_iodev_sqe * iodev_sqe, const struct device * dev, rtio_callback_t complete_op_cb )
```

声明属性：`inline`、`static`。

创建一条提交队列事件链（SQE Chain），表示用于读取寄存器的总线事务（Bus Transaction）。

支持RTIO的总线驱动会被安排对列表中的每个寄存器执行总线读操作。

用法（Usage）：

原始示例（Example）：

```c
struct rtio_regs regs;
struct rtio_reg_list regs_list[] = {{regs_addr1, mem_addr_1, mem_len_1},
                                    {regs_addr2, mem_addr_2, mem_len_2},
                                    ...
                                   };
regs.rtio_regs_list = regs_list;
regs.rtio_regs_num = ARRAY_SIZE(regs_list);

rtio_read_regs_async(rtio,
                     iodev,
                     RTIO_BUS_SPI,
                     &regs,
                     sqe,
                     dev,
                     op_cb);
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `r` | RTIO上下文（Context）。 |
| `iodev` | 输入输出设备（I/O Device，IODEV）。 |
| `bus_type` | 总线类型：I2C、SPI或I3C。 |
| `regs` | 指向待读取寄存器列表的指针。使用SPI总线时，应设置适当的位。 |
| `iodev_sqe` | 等待操作（Await Operation）的IODEV提交。 |
| `dev` | 指向设备结构体的指针。 |
| `complete_op_cb` | 操作结束时的回调函数（Callback）。 |

## 1.5\_源码定位与版本边界

相对源码定位：[寄存器辅助头文件](../../../include/zephyr/rtio/regmap.h)、[工作队列头文件](../../../include/zephyr/rtio/work.h)、[工作队列实现](../../../subsys/rtio/rtio_workq.c)、[工作队列配置](../../../subsys/rtio/Kconfig.workq)、[核心接口](../../../include/zephyr/rtio/rtio.h)、[SQE辅助函数](../../../include/zephyr/rtio/sqe.h)及[P4队列类型](../../../include/zephyr/sys/p4wq.h)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：原示例写作`struct rtio_reg_list`，本次头文件实际声明为`struct rtio_regs_list`，多一个s；示例中的寄存器名和省略号也是示意内容。本页完整保留官方原例，不把它描述成无需修改就可编译的程序。

> 译注——源码核对：对列表中的每一项，辅助函数先准备一个1字节tiny_write发送寄存器地址，再准备一个read读取数据。前者设置TRANSACTION，使地址与读取成为一个事务；后者设置CHAINED，使下一项或末尾回调在之后执行。I2C／I3C读取条目还设置STOP和RESTART；SPI分支不自动设置读方向位，调用者必须按设备协议预先设置reg_addr。

> 译注——源码核对：非空列表N项会取得2N个读写SQE和1个末尾回调SQE，全部准备完才调用rtio_submit(r, 0)。应考虑上下文已有待提交请求以及整组2N+1个条目的容量。获取失败时通过rtio_iodev_sqe_err(iodev_sqe, -ENOMEM)报告，并调用rtio_sqe_drop_all(r)清理整个上下文待提交队列，不仅是当前寄存器列表。

> 译注——源码核对：寄存器地址在准备时复制到tiny_write的内部数组，读取目标bufp只保存引用，数据缓冲区必须在异步使用期间有效；不能因函数返回就释放。reg_addr是uint8_t，len是size_t，但read准备函数的长度参数为uint32_t；使用方应遵守实际地址和长度表示范围，不能把此辅助函数当作任意宽度寄存器地址传输器。

> 译注——源码核对：rtio_regs_num是size_t，但本次遍历变量为uint8_t。对超过255项的列表，循环变量会回绕，不能据size_t类型认为任意大列表都受支持。此处记录源码限制，没有修改官方实现。

> 译注——源码核对：末尾使用rtio_sqe_prep_callback_no_cqe，回调arg0保存dev，SQE的userdata保存传入iodev_sqe。这个末尾回调本身不再产生CQE，辅助函数也没有统一消费前面的CQE；完成报告与结果清理由调用方的complete_op_cb按协议处理。void返回和rtio_submit(r, 0)都不表示总线已经完成。原文把iodev_sqe称为await操作提交，但本辅助函数没有创建AWAIT操作，而是把该参数用于错误报告和末尾回调的关联数据。

> 译注——源码核对：rtio_is_spi／i2c／i3c只比较枚举值，不探测实际设备能力。未知bus_type在当前switch中与SPI一样不设置I2C／I3C标志，但这不代表它是已受支持的总线类型。

> 译注——源码核对：本次译注以来源记录中的官方源码摘要为界；仓库源码使用相对链接，未加入本机环境路径或实板操作前提。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 1.6\_原页交叉引用（Cross References）

- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [查看此文件的源码](P002_RTIO寄存器映射头文件源码.md)
- [rtio_regs](P003_RTIO寄存器配置.md)
- [rtio_regs::rtio_regs_list](P004_RTIO寄存器列表.md)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [device](../device_reference/P002_设备对象结构.md)
- [rtio_callback_t](../rtio_core_reference/P001_RTIO公共接口.md#ga5d5b7d440eab064918424b0261455a9f)
- [rtio_regs_list](P003_RTIO寄存器配置.md#adc88caf9fee2e0a8d5bcc83355d361dd)
- [ARRAY_SIZE](../util_reference/P001_通用工具公共接口.md#ga70c57aae3eb654e205459b4362c8089a)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="aa75738a91bc261196c140a9899ef3026a0d014a0d843d6e8bae70039ef03fcf4a"></a>
<a id="aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3"></a>
<a id="aa75738a91bc261196c140a9899ef3026a79d24e2954651825c0919c340303fddb"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>
<a id="agroup__sys-util_html_ga70c57aae3eb654e205459b4362c8089a"></a>
<a id="aregmap_8h_html_a3a3c3ee815644c5bb902632d4b3640ad"></a>
<a id="aregmap_8h_html_aa75738a91bc261196c140a9899ef3026a87c63acc8f06c06078d4f86ab65fffa3"></a>
<a id="astructrtio__regs_html"></a>
<a id="astructrtio__regs_html_adc88caf9fee2e0a8d5bcc83355d361dd"></a>
<a id="astructrtio_html"></a>

---

[返回大纲](大纲.md) · [下一章](P002_RTIO寄存器映射头文件源码.md)
