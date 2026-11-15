---
id: learning.zephyr-docs.api-file-kernel-network-reference.page-4
title: zephyr__drivers__i3c.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_zephyr\_\_drivers\_\_i3c.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/i3c_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

集成电路间接口（Inter-Integrated Circuit，I3C）驱动API的主头文件。

<a id="details"></a>

```c
#include <errno.h>
#include <stdint.h>
#include <stddef.h>
#include <zephyr/device.h>
#include <zephyr/drivers/i3c/addresses.h>
#include <zephyr/drivers/i3c/error_types.h>
#include <zephyr/drivers/i3c/ccc.h>
#include <zephyr/drivers/i3c/devicetree.h>
#include <zephyr/drivers/i3c/ibi.h>
#include <zephyr/drivers/i2c.h>
#include <zephyr/sys/slist.h>
#include <zephyr/sys/util.h>
#include <zephyr/rtio/rtio.h>
#include <zephyr/drivers/i3c/target_device.h>
#include <zephyr/drivers/i3c/hdr_ddr.h>
#include <zephyr/syscalls/i3c.h>
```

查看此文件的源码。

集成电路间接口（Inter-Integrated Circuit，I3C）驱动API的主头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 4.1\_数据结构（Data Structures）

<a id="r_i3c_5Fmsg"></a>

```c
struct i3c_msg
```

相关声明：[i3c_msg](../hardware/P395_I3C传输消息.md)。

一条I3C消息（Message）。

<a id="r_i3c_5Fconfig_5Fcontroller"></a>

```c
struct i3c_config_controller
```

相关声明：[i3c_config_controller](../hardware/P391_I3C控制器硬件配置.md)。

使I3C硬件充当控制器（Controller）的配置参数。

<a id="r_i3c_5Fconfig_5Fcustom"></a>

```c
struct i3c_config_custom
```

相关声明：[i3c_config_custom](../hardware/P393_I3C自定义硬件配置.md)。

自定义I3C配置参数（Configuration Parameters）。

<a id="r_i3c_5Fdevice_5Fid"></a>

```c
struct i3c_device_id
```

相关声明：[i3c_device_id](../hardware/P400_I3C设备匹配标识.md)。

用于匹配I3C设备的结构。

<a id="r_i3c_5Fdevice_5Fdesc"></a>

```c
struct i3c_device_desc
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

描述I3C目标设备（Target Device）的结构。

<a id="r_i3c_5Fi2c_5Fdevice_5Fdesc"></a>

```c
struct i3c_i2c_device_desc
```

相关声明：[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

描述I3C总线上I2C设备的结构。

<a id="r_i3c_5Fdev_5Fattached_5Flist"></a>

```c
struct i3c_dev_attached_list
```

相关声明：[i3c_dev_attached_list](../hardware/P404_I3C已附接设备列表.md)。

描述控制器所连接设备（Attached Devices）的结构。

<a id="r_i3c_5Fdev_5Flist"></a>

```c
struct i3c_dev_list
```

相关声明：[i3c_dev_list](../hardware/P403_I3C已知设备列表.md)。

描述控制器已知设备（Known Devices）的结构。

<a id="r_i3c_5Fdriver_5Fconfig"></a>

```c
struct i3c_driver_config
```

相关声明：[i3c_driver_config](../hardware/P405_I3C驱动公共配置.md)。

所有I3C驱动共用此结构，预期将其置于device结构的config字段所指对象的第一个成员。

<a id="r_i3c_5Fdriver_5Fdata"></a>

```c
struct i3c_driver_data
```

相关声明：[i3c_driver_data](../hardware/P406_I3C驱动公共数据.md)。

所有I3C驱动共用此结构，预期将其置于驱动struct driver_data声明的第一个成员。

<a id="r_i3c_5Fiodev_5Fdata"></a>

```c
struct i3c_iodev_data
```

相关声明：[i3c_iodev_data](../hardware/P407_I3C输入输出设备数据.md)。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 4.2\_宏定义（Macros）

<a id="r_gadd026a36545d50ea3c043d0ebcfde95b"></a>

```c
#define I3C_OD_TLOW_MIN_NS 200
```

相关声明：[I3C_OD_TLOW_MIN_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gadd026a36545d50ea3c043d0ebcfde95b)。

开漏（Open Drain）的最大与最小时序。

<a id="r_ga7478181801369cb7ed7a7124fa9c4240"></a>

```c
#define I3C_OD_MIXED_BUS_THIGH_MAX_NS 41
```

相关声明：[I3C_OD_MIXED_BUS_THIGH_MAX_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7478181801369cb7ed7a7124fa9c4240)。

<a id="r_ga41fc93e0aba6bc1cf3540ca89e860a2b"></a>

```c
#define I3C_OD_FIRST_BC_THIGH_MIN_NS 200
```

相关声明：[I3C_OD_FIRST_BC_THIGH_MIN_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga41fc93e0aba6bc1cf3540ca89e860a2b)。

<a id="r_ga72f9fb65d218521ad006febf3dd6851b"></a>

```c
#define I3C_MSG_WRITE (0U << 0U)
```

相关声明：[I3C_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga72f9fb65d218521ad006febf3dd6851b)。

向 I3C 总线写入报文（Message）。

<a id="r_ga6ba89782a8646f96dc1f9fa3b9cd2058"></a>

```c
#define I3C_MSG_READ BIT(0)
```

相关声明：[I3C_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga6ba89782a8646f96dc1f9fa3b9cd2058)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

从 I3C 总线读取报文（Message）。

<a id="r_ga0d4ae269a53af945837d158f638d8b5c"></a>

```c
#define I3C_MSG_STOP BIT(1)
```

相关声明：[I3C_MSG_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga0d4ae269a53af945837d158f638d8b5c)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

在此消息之后发送停止条件（STOP）。

<a id="r_gad9ff03f4fdcb117b90c17d667a49c295"></a>

```c
#define I3C_MSG_RESTART BIT(2)
```

相关声明：[I3C_MSG_RESTART](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad9ff03f4fdcb117b90c17d667a49c295)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

为此报文重新启动（RESTART）I3C 事务。

<a id="r_gad827935caf8503aeaedd1aceb53d4e38"></a>

```c
#define I3C_MSG_HDR BIT(3)
```

相关声明：[I3C_MSG_HDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad827935caf8503aeaedd1aceb53d4e38)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

传输使用高数据率模式（HDR Mode）。

<a id="r_ga4147e7cdf8155d2ef7c4dc7c08e16b6a"></a>

```c
#define I3C_MSG_NBCH BIT(4)
```

相关声明：[I3C_MSG_NBCH](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

跳过 I3C 广播报头（Broadcast Header）。

<a id="r_ga735a347b1d0f431ab0c3a90f509fcbe1"></a>

```c
#define I3C_MSG_NOACK_EXPECTED BIT(5)
```

相关声明：[I3C_MSG_NOACK_EXPECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga735a347b1d0f431ab0c3a90f509fcbe1)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

预期目标设备返回否定应答（NACK）。

<a id="r_ga18aac0862826869f94e5a71670debcb0"></a>

```c
#define I3C_MSG_HDR_MODE0 BIT(0)
```

相关声明：[I3C_MSG_HDR_MODE0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga18aac0862826869f94e5a71670debcb0)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）0。

<a id="r_ga8eb3dc48237dfdb25fde40a1efa03241"></a>

```c
#define I3C_MSG_HDR_MODE1 BIT(1)
```

相关声明：[I3C_MSG_HDR_MODE1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga8eb3dc48237dfdb25fde40a1efa03241)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）1。

<a id="r_ga15cbd61e7d509c28b22fbc9e0844cb23"></a>

```c
#define I3C_MSG_HDR_MODE2 BIT(2)
```

相关声明：[I3C_MSG_HDR_MODE2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga15cbd61e7d509c28b22fbc9e0844cb23)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）2。

<a id="r_ga162fb9ab0e4ed7f8feb0e91d183a88e7"></a>

```c
#define I3C_MSG_HDR_MODE3 BIT(3)
```

相关声明：[I3C_MSG_HDR_MODE3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga162fb9ab0e4ed7f8feb0e91d183a88e7)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）3。

<a id="r_gabe45532238bc15672f6454dac70d20cf"></a>

```c
#define I3C_MSG_HDR_MODE4 BIT(4)
```

相关声明：[I3C_MSG_HDR_MODE4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gabe45532238bc15672f6454dac70d20cf)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）4。

<a id="r_gac712daa606d0c51ce523d7a687821282"></a>

```c
#define I3C_MSG_HDR_MODE5 BIT(5)
```

相关声明：[I3C_MSG_HDR_MODE5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac712daa606d0c51ce523d7a687821282)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）5。

<a id="r_ga7654c1947e13c019c24bf12712b0773b"></a>

```c
#define I3C_MSG_HDR_MODE6 BIT(6)
```

相关声明：[I3C_MSG_HDR_MODE6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga7654c1947e13c019c24bf12712b0773b)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）6。

<a id="r_ga08df1d8df82226d1f23b4cc923584672"></a>

```c
#define I3C_MSG_HDR_MODE7 BIT(7)
```

相关声明：[I3C_MSG_HDR_MODE7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga08df1d8df82226d1f23b4cc923584672)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I3C 高数据率模式（HDR Mode）7。

<a id="r_gac7386b21323d30148bd9456b9d180d7a"></a>

```c
#define I3C_MSG_HDR_DDR I3C_MSG_HDR_MODE0
```

相关声明：[I3C_MSG_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac7386b21323d30148bd9456b9d180d7a)、[I3C_MSG_HDR_MODE0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga18aac0862826869f94e5a71670debcb0)。

I3C 高数据率双倍数据率模式（HDR-DDR，Double Data Rate）。

<a id="r_gaa61322f770db296b5ab718c48ab960d3"></a>

```c
#define I3C_MSG_HDR_TSP I3C_MSG_HDR_MODE1
```

相关声明：[I3C_MSG_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaa61322f770db296b5ab718c48ab960d3)、[I3C_MSG_HDR_MODE1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga8eb3dc48237dfdb25fde40a1efa03241)。

I3C 高数据率三元符号纯总线模式（HDR-TSP，Ternary Symbol Pure-bus）。

<a id="r_gac43a2d266f3a23fd6dfa11405f3fd6f3"></a>

```c
#define I3C_MSG_HDR_TSL I3C_MSG_HDR_MODE2
```

相关声明：[I3C_MSG_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac43a2d266f3a23fd6dfa11405f3fd6f3)、[I3C_MSG_HDR_MODE2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga15cbd61e7d509c28b22fbc9e0844cb23)。

I3C 高数据率三元符号兼容传统总线模式（HDR-TSL，Ternary Symbol Legacy-inclusive-bus）。

<a id="r_ga8b2fdcb827cbd3325f124a1c615698e7"></a>

```c
#define I3C_MSG_HDR_BT I3C_MSG_HDR_MODE3
```

相关声明：[I3C_MSG_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga8b2fdcb827cbd3325f124a1c615698e7)、[I3C_MSG_HDR_MODE3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga162fb9ab0e4ed7f8feb0e91d183a88e7)。

I3C 高数据率批量传输模式（HDR-BT，Bulk Transport）。

<a id="r_gaed0df9802cc9b268abcfe4e877ebf498"></a>

```c
#define I3C_DEVICE_ID(pid)
```

相关声明：[I3C_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaed0df9802cc9b268abcfe4e877ebf498)。

根据临时标识符（PID）构造 i3c_device_id 的结构体初始化器。

<a id="r_ga42cb4edf6a099d586df14456fd98c873"></a>

```c
#define I3C_BUS_FOR_EACH_I3CDEV(bus, desc)
```

相关声明：[I3C_BUS_FOR_EACH_I3CDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga42cb4edf6a099d586df14456fd98c873)。

遍历总线上存在的全部 I3C 设备（Devices）。

<a id="r_ga450ba9021d1080f890c32624f20ba2b8"></a>

```c
#define I3C_BUS_FOR_EACH_I2CDEV(bus, desc)
```

相关声明：[I3C_BUS_FOR_EACH_I2CDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga450ba9021d1080f890c32624f20ba2b8)。

遍历总线上存在的全部 I2C 设备（Devices）。

<a id="r_gae2d038807305e9e13eab26bae1dd4624"></a>

```c
#define I3C_BUS_FOR_EACH_I3CDEV_SAFE(bus, desc, desc_s)
```

相关声明：[I3C_BUS_FOR_EACH_I3CDEV_SAFE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae2d038807305e9e13eab26bae1dd4624)。

安全地遍历总线上存在的全部 I3C 设备（Devices）。

<a id="r_ga5536141e7c7ea9dc0b1395224089ca0d"></a>

```c
#define I3C_BUS_FOR_EACH_I2CDEV_SAFE(bus, desc, desc_s)
```

相关声明：[I3C_BUS_FOR_EACH_I2CDEV_SAFE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5536141e7c7ea9dc0b1395224089ca0d)。

安全地遍历总线上存在的全部 I2C 设备（Devices）。

<a id="r_gabec5796b92d4582761bc3de456f1df27"></a>

```c
#define I3C_DT_IODEV_DEFINE(name, node_id)
```

相关声明：[I3C_DT_IODEV_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabec5796b92d4582761bc3de456f1df27)。

为总线上给定的设备树节点定义I/O设备（iodev）。

<a id="r_ga051e80ceacf87bb9ccb79357ee7bc205"></a>

```c
#define I3C_DT_INST_IODEV_DEFINE(name, inst)
```

相关声明：[I3C_DT_INST_IODEV_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga051e80ceacf87bb9ccb79357ee7bc205)。

为总线上的设备树实例定义I/O设备（iodev）。

<a id="define-members-0"></a>

### 总线特性寄存器（Bus Characteristic Register (BCR)）



<a id="r_ga91ebe41a421dc05ae7f1de1ce2dd314f"></a>

```c
#define I3C_BCR_MAX_DATA_SPEED_LIMIT BIT(0)
```

相关声明：[I3C_BCR_MAX_DATA_SPEED_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga91ebe41a421dc05ae7f1de1ce2dd314f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

最大数据速率限制位（Max Data Speed Limitation Bit）。

<a id="r_ga0c09de8a18ea1586e37d35e073ae641f"></a>

```c
#define I3C_BCR_IBI_REQUEST_CAPABLE BIT(1)
```

相关声明：[I3C_BCR_IBI_REQUEST_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0c09de8a18ea1586e37d35e073ae641f)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

带内中断请求能力位（IBI Request Capable Bit）。

<a id="r_gae119c230097cb8e1eab9fc45cafde838"></a>

```c
#define I3C_BCR_IBI_PAYLOAD_HAS_DATA_BYTE BIT(2)
```

相关声明：[I3C_BCR_IBI_PAYLOAD_HAS_DATA_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae119c230097cb8e1eab9fc45cafde838)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

带内中断有效载荷位（IBI Payload Bit）。

<a id="r_ga7b9fea89457022d8012ac25133bf63db"></a>

```c
#define I3C_BCR_OFFLINE_CAPABLE BIT(3)
```

相关声明：[I3C_BCR_OFFLINE_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7b9fea89457022d8012ac25133bf63db)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

离线能力位（Offline Capable Bit）。

<a id="r_ga69dc4a5004da568684a3c72046bba870"></a>

```c
#define I3C_BCR_VIRTUAL_TARGET BIT(4)
```

相关声明：[I3C_BCR_VIRTUAL_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga69dc4a5004da568684a3c72046bba870)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

虚拟目标支持位（Virtual Target Support Bit）。

<a id="r_ga07018705794753d0d0d65131f011e097"></a>

```c
#define I3C_BCR_ADV_CAPABILITIES BIT(5)
```

相关声明：[I3C_BCR_ADV_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga07018705794753d0d0d65131f011e097)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

高级能力位（Advanced Capabilities Bit）。

<a id="r_ga867b4b12b23c803b86b57dcc86b9e604"></a>

```c
#define I3C_BCR_DEVICE_ROLE_I3C_TARGET 0U
```

相关声明：[I3C_BCR_DEVICE_ROLE_I3C_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga867b4b12b23c803b86b57dcc86b9e604)。

设备角色：I3C 目标设备（I3C Target）。

<a id="r_ga0e64c8aa6717b96bcf9dad6c9ec7f852"></a>

```c
#define I3C_BCR_DEVICE_ROLE_I3C_CONTROLLER_CAPABLE 1U
```

相关声明：[I3C_BCR_DEVICE_ROLE_I3C_CONTROLLER_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0e64c8aa6717b96bcf9dad6c9ec7f852)。

设备角色：具备 I3C 控制器能力（I3C Controller Capable）。

<a id="r_ga25721c9963040c84b7f5bbb48bb87b44"></a>

```c
#define I3C_BCR_DEVICE_ROLE_MASK GENMASK(7U, 6U)
```

相关声明：[I3C_BCR_DEVICE_ROLE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga25721c9963040c84b7f5bbb48bb87b44)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

设备角色位移掩码（Device Role Bit Shift Mask）。

<a id="r_ga90988b26dc2f388ec7c65387a24f05af"></a>

```c
#define I3C_BCR_DEVICE_ROLE(bcr)
```

相关声明：[I3C_BCR_DEVICE_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga90988b26dc2f388ec7c65387a24f05af)。

设备角色（Device Role）。

<a id="define-members-1"></a>

### 传统虚拟寄存器（Legacy Virtual Register，LVR）。

传统虚拟寄存器（Legacy Virtual Register，LVR）。

<a id="r_ga9bf868ac6ae38e3f8ab6e5e1378bfb75"></a>

```c
#define I3C_LVR_I2C_FM_PLUS_MODE 0
```

相关声明：[I3C_LVR_I2C_FM_PLUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)。

I2C 快速模式增强版（FM+ Mode）。

<a id="r_ga053945f5f67ee3c681de2c9362e69c39"></a>

```c
#define I3C_LVR_I2C_FM_MODE 1
```

相关声明：[I3C_LVR_I2C_FM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga053945f5f67ee3c681de2c9362e69c39)。

I2C 快速模式（FM Mode）。

<a id="r_gaf073cc9ea1a68c57663c36de12554876"></a>

```c
#define I3C_LVR_I2C_MODE_MASK BIT(4)
```

相关声明：[I3C_LVR_I2C_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaf073cc9ea1a68c57663c36de12554876)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

I2C 模式指示位掩码（Mode Indicator Bitmask）。

<a id="r_gaaf759805bb5824a89612b292a4439982"></a>

```c
#define I3C_LVR_I2C_MODE(lvr)
```

相关声明：[I3C_LVR_I2C_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaaf759805bb5824a89612b292a4439982)。

I2C 模式（Mode）。

<a id="r_ga4319835ddb6b5984b21f5a5a2f14ae75"></a>

```c
#define I3C_LVR_I2C_DEV_IDX_0 0
```

相关声明：[I3C_LVR_I2C_DEV_IDX_0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga4319835ddb6b5984b21f5a5a2f14ae75)。

I2C 设备索引（Device Index）0。

<a id="r_ga02a21af4c679a81b8290beea30c8ef40"></a>

```c
#define I3C_LVR_I2C_DEV_IDX_1 1
```

相关声明：[I3C_LVR_I2C_DEV_IDX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga02a21af4c679a81b8290beea30c8ef40)。

I2C 设备索引（Device Index）1。

<a id="r_ga5950bb8ceea5fcd3ceb38c7da0d9dd68"></a>

```c
#define I3C_LVR_I2C_DEV_IDX_2 2
```

相关声明：[I3C_LVR_I2C_DEV_IDX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)。

I2C 设备索引（Device Index）2。

<a id="r_ga50fa249b36b91d56e49004548a1c7520"></a>

```c
#define I3C_LVR_I2C_DEV_IDX_MASK GENMASK(7U, 5U)
```

相关声明：[I3C_LVR_I2C_DEV_IDX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga50fa249b36b91d56e49004548a1c7520)、[GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)。

I2C 设备索引位掩码（Device Index Bitmask）。

<a id="r_gae7afa509b1d63374c551bcdaf84c5dd1"></a>

```c
#define I3C_LVR_I2C_DEV_IDX(lvr)
```

相关声明：[I3C_LVR_I2C_DEV_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae7afa509b1d63374c551bcdaf84c5dd1)。

I2C 设备索引（Device Index）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 4.3\_类型定义（Typedefs）

<a id="r_gac1df0bbb6943e1ec59c5b0dba27257fe"></a>

```c
typedef void(* i3c_callback_t) (const struct device *dev, int result, void *data)
```

相关声明：[i3c_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac1df0bbb6943e1ec59c5b0dba27257fe)、[device](../device_reference/P002_设备对象结构.md)。

I3C 异步传输请求回调（Asynchronous Transfer Request Callback）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.4\_枚举（Enumerations）

<a id="r_ga7a0d66ab45f618ca055422e2b69abe90"></a>

```c
enum i3c_bus_mode { I3C_BUS_MODE_PURE , I3C_BUS_MODE_MIXED_FAST , I3C_BUS_MODE_MIXED_LIMITED , I3C_BUS_MODE_MIXED_SLOW , I3C_BUS_MODE_MAX = I3C_BUS_MODE_MIXED_SLOW , I3C_BUS_MODE_INVALID }
```

相关声明：[i3c_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7a0d66ab45f618ca055422e2b69abe90)、[I3C_BUS_MODE_PURE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445)、[I3C_BUS_MODE_MIXED_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434)、[I3C_BUS_MODE_MIXED_LIMITED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722)、[I3C_BUS_MODE_MIXED_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a)、[I3C_BUS_MODE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697)、[I3C_BUS_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)。

I3C 总线模式（Bus Mode）。

<a id="r_ga67686f0a5d83697361c655c3fd6e61c6"></a>

```c
enum i3c_i2c_speed_type { I3C_I2C_SPEED_FM , I3C_I2C_SPEED_FMPLUS , I3C_I2C_SPEED_MAX = I3C_I2C_SPEED_FMPLUS , I3C_I2C_SPEED_INVALID }
```

相关声明：[i3c_i2c_speed_type](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga67686f0a5d83697361c655c3fd6e61c6)、[I3C_I2C_SPEED_FM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1)、[I3C_I2C_SPEED_FMPLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea)、[I3C_I2C_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967)、[I3C_I2C_SPEED_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4)。

I3C 总线下的 I2C 总线速率（Bus Speed）。

<a id="r_gae9d98642c6f249ee0e6ea0dc491b5073"></a>

```c
enum i3c_data_rate { I3C_DATA_RATE_SDR , I3C_DATA_RATE_HDR_DDR , I3C_DATA_RATE_HDR_TSL , I3C_DATA_RATE_HDR_TSP , I3C_DATA_RATE_HDR_BT , I3C_DATA_RATE_MAX = I3C_DATA_RATE_HDR_BT , I3C_DATA_RATE_INVALID }
```

相关声明：[i3c_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae9d98642c6f249ee0e6ea0dc491b5073)、[I3C_DATA_RATE_SDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9)、[I3C_DATA_RATE_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301)、[I3C_DATA_RATE_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590)、[I3C_DATA_RATE_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d)、[I3C_DATA_RATE_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed)、[I3C_DATA_RATE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725)、[I3C_DATA_RATE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)。

I3C 数据速率（Data Rate）。

<a id="r_ga5b111bc8fa8c3bee052e621d26dcc54a"></a>

```c
enum i3c_config_type { I3C_CONFIG_CONTROLLER , I3C_CONFIG_TARGET , I3C_CONFIG_CUSTOM }
```

相关声明：[i3c_config_type](../hardware/P425_I3C公共接口参考.md#ga5b111bc8fa8c3bee052e621d26dcc54a)、[I3C_CONFIG_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5)、[I3C_CONFIG_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00)、[I3C_CONFIG_CUSTOM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017)。

传给配置函数（Configure Function）的配置类型。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 4.5\_函数（Functions）

<a id="r_ga9a451379bef381c6a264a22a2282fa89"></a>

```c
struct i3c_device_desc * i3c_dev_list_find (const struct i3c_dev_list *dev_list, const struct i3c_device_id *id)
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_dev_list_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9a451379bef381c6a264a22a2282fa89)、[i3c_dev_list](../hardware/P403_I3C已知设备列表.md)、[i3c_device_id](../hardware/P400_I3C设备匹配标识.md)。

根据 ID 查找 I3C 目标设备描述符（Target Device Descriptor）。

<a id="r_ga0e83c5a26b18acfbe7d532825a8fd54c"></a>

```c
struct i3c_device_desc * i3c_dev_list_i3c_addr_find (const struct device *dev, uint8_t addr)
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_dev_list_i3c_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0e83c5a26b18acfbe7d532825a8fd54c)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据动态地址（Dynamic Address）查找 I3C 目标设备描述符。

<a id="r_gaecbb16ce8edcd9ad7a7afcfb1251aa76"></a>

```c
struct i3c_device_desc * i3c_dev_list_i3c_static_addr_find (const struct device *dev, uint8_t addr)
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_dev_list_i3c_static_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaecbb16ce8edcd9ad7a7afcfb1251aa76)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据静态地址（Static Address）查找 I3C 目标设备描述符。

<a id="r_gafac78dca571ff7daa34fca0cfa7cc3b1"></a>

```c
struct i3c_i2c_device_desc * i3c_dev_list_i2c_addr_find (const struct device *dev, uint16_t addr)
```

相关声明：[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)、[i3c_dev_list_i2c_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gafac78dca571ff7daa34fca0cfa7cc3b1)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据地址查找 I2C 目标设备描述符（Target Device Descriptor）。

<a id="r_ga43c3268fef220faa21b81010876e69d0"></a>

```c
int i3c_dev_list_daa_addr_helper (const struct device *dev, uint64_t pid, bool must_match, bool assigned_okay, struct i3c_device_desc **target, uint8_t *addr)
```

相关声明：[i3c_dev_list_daa_addr_helper](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga43c3268fef220faa21b81010876e69d0)、[device](../device_reference/P002_设备对象结构.md)、[uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在进入动态地址分配（ENTDAA）期间查找可用地址的辅助函数。

<a id="r_ga2f176f8440d86f4ec6c94a8911a75352"></a>

```c
static int i3c_configure (const struct device *dev, enum i3c_config_type type, void *config)
```

相关声明：[i3c_configure](../hardware/P425_I3C公共接口参考.md#ga2f176f8440d86f4ec6c94a8911a75352)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_type](../hardware/P425_I3C公共接口参考.md#ga5b111bc8fa8c3bee052e621d26dcc54a)。

配置 I3C 硬件（Hardware）。

<a id="r_gaeca24930774ecc2dcbf2240d48ae19c5"></a>

```c
static int i3c_configure_controller (const struct device *dev, struct i3c_config_controller *config)
```

相关声明：[i3c_configure_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaeca24930774ecc2dcbf2240d48ae19c5)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_controller](../hardware/P391_I3C控制器硬件配置.md)。

设置 I3C 设备的控制器设备配置（Controller Device Configuration）。

<a id="r_ga7dfa33c7bdbe7e6607af61fe04bcb985"></a>

```c
static int i3c_configure_target (const struct device *dev, struct i3c_config_target *config)
```

相关声明：[i3c_configure_target](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7dfa33c7bdbe7e6607af61fe04bcb985)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_target](../hardware/P392_I3C目标硬件配置.md)。

设置 I3C 设备的目标设备配置（Target Device Configuration）。

<a id="r_ga807877923755aeb5a065e054fb42946d"></a>

```c
static int i3c_config_get (const struct device *dev, enum i3c_config_type type, void *config)
```

相关声明：[i3c_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga807877923755aeb5a065e054fb42946d)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_type](../hardware/P425_I3C公共接口参考.md#ga5b111bc8fa8c3bee052e621d26dcc54a)。

获取 I3C 硬件配置（Hardware Configuration）。

<a id="r_ga96cd903b4a676c5943c43cc7b27af867"></a>

```c
static int i3c_config_get_controller (const struct device *dev, struct i3c_config_controller *config)
```

相关声明：[i3c_config_get_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga96cd903b4a676c5943c43cc7b27af867)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_controller](../hardware/P391_I3C控制器硬件配置.md)。

获取 I3C 设备的控制器设备配置（Controller Device Configuration）。

<a id="r_ga8ef11af673e94646806e093504cfb01f"></a>

```c
static int i3c_config_get_target (const struct device *dev, struct i3c_config_target *config)
```

相关声明：[i3c_config_get_target](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8ef11af673e94646806e093504cfb01f)、[device](../device_reference/P002_设备对象结构.md)、[i3c_config_target](../hardware/P392_I3C目标硬件配置.md)。

获取 I3C 设备的目标设备配置（Target Device Configuration）。

<a id="r_ga7b23e08b10a09bde4e87328d6915aa25"></a>

```c
static int i3c_recover_bus (const struct device *dev)
```

相关声明：[i3c_recover_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7b23e08b10a09bde4e87328d6915aa25)、[device](../device_reference/P002_设备对象结构.md)。

尝试恢复 I3C 总线（Bus Recovery）。

<a id="r_ga042d1a3315f040562534ce08306b329c"></a>

```c
int i3c_attach_i3c_device (struct i3c_device_desc *target)
```

相关声明：[i3c_attach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga042d1a3315f040562534ce08306b329c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

挂接 I3C 设备（Attach Device）。

<a id="r_gae6c8e8612368808117f4fce960e43769"></a>

```c
int i3c_reattach_i3c_device (struct i3c_device_desc *target, uint8_t old_dyn_addr)
```

相关声明：[i3c_reattach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae6c8e8612368808117f4fce960e43769)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

重新挂接 I3C 设备（Reattach Device）。

<a id="r_ga6db9688cc7e9d34404717ae753751579"></a>

```c
int i3c_detach_i3c_device (struct i3c_device_desc *target)
```

相关声明：[i3c_detach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga6db9688cc7e9d34404717ae753751579)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

解除挂接 I3C 设备（Detach Device）。

<a id="r_gac10ab0c78a581bf8284b9cc3a30c92cf"></a>

```c
static bool i3c_is_i3c_device_attached (struct i3c_device_desc *target)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_is_i3c_device_attached](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac10ab0c78a581bf8284b9cc3a30c92cf)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

检查 I3C 设备是否已挂接到总线（Attached to the Bus）。

<a id="r_ga5e69aaed50f99418c7123f652555ae20"></a>

```c
int i3c_attach_i2c_device (struct i3c_i2c_device_desc *target)
```

相关声明：[i3c_attach_i2c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5e69aaed50f99418c7123f652555ae20)、[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

挂接 I2C 设备（Attach Device）。

<a id="r_ga8e8de45499bff02cac4c59c1758ec0a7"></a>

```c
int i3c_detach_i2c_device (struct i3c_i2c_device_desc *target)
```

相关声明：[i3c_detach_i2c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8e8de45499bff02cac4c59c1758ec0a7)、[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

解除挂接 I2C 设备（Detach Device）。

<a id="r_ga489c2c5f18e92421642d2316c317dbd9"></a>

```c
static bool i3c_is_i2c_device_attached (struct i3c_i2c_device_desc *target)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_is_i2c_device_attached](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga489c2c5f18e92421642d2316c317dbd9)、[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

检查 I2C 设备是否已挂接到总线（Attached to the Bus）。

<a id="r_gabb54c0e85d0f5e8585391f9e5c20d4b6"></a>

```c
static int i3c_do_daa (const struct device *dev)
```

相关声明：[i3c_do_daa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabb54c0e85d0f5e8585391f9e5c20d4b6)、[device](../device_reference/P002_设备对象结构.md)。

在 I3C 总线上执行动态地址分配（Dynamic Address Assignment）。

<a id="r_gaa6d5445489bfc8611c98b93f49305862"></a>

```c
int i3c_do_ccc (const struct device *dev, struct i3c_ccc_payload *payload)
```

相关声明：[i3c_do_ccc](../hardware/P425_I3C公共接口参考.md#gaa6d5445489bfc8611c98b93f49305862)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)。

向总线发送通用命令码（CCC）。

<a id="r_ga779f8dd18d361175ea0d38fe3de16ef6"></a>

```c
int i3c_do_ccc_cb (const struct device *dev, struct i3c_ccc_payload *payload, i3c_callback_t cb, void *userdata)
```

相关声明：[i3c_do_ccc_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga779f8dd18d361175ea0d38fe3de16ef6)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)、[i3c_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac1df0bbb6943e1ec59c5b0dba27257fe)。

向总线异步发送通用命令码（CCC），带回调。

<a id="r_ga067c0f1e3c9abb6ef34ce48cb7e45cb8"></a>

```c
int i3c_transfer (struct i3c_device_desc *target, struct i3c_msg *msgs, uint8_t num_msgs)
```

相关声明：[i3c_transfer](../hardware/P394_I3C传输接口.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_msg](../hardware/P395_I3C传输消息.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

从控制器向 I3C 目标设备执行数据传输（Data Transfer）。

<a id="r_ga354eb19c5134f1a4df291005d0f6622a"></a>

```c
int i3c_transfer_cb (struct i3c_device_desc *target, struct i3c_msg *msgs, uint8_t num_msgs, i3c_callback_t cb, void *userdata)
```

相关声明：[i3c_transfer_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga354eb19c5134f1a4df291005d0f6622a)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_msg](../hardware/P395_I3C传输消息.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i3c_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac1df0bbb6943e1ec59c5b0dba27257fe)。

从控制器向 I3C 目标设备执行带回调的异步数据传输（Asynchronous Data Transfer）。

<a id="r_ga10a3963b749cc667a03975889d618d1b"></a>

```c
static struct i3c_device_desc * i3c_device_find (const struct device *dev, const struct i3c_device_id *id)
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_device_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga10a3963b749cc667a03975889d618d1b)、[device](../device_reference/P002_设备对象结构.md)、[i3c_device_id](../hardware/P400_I3C设备匹配标识.md)。

查找已注册的 I3C 目标设备（Target Device）。

<a id="r_gac8c77e43fc7c06701437e799739507ee"></a>

```c
static int i3c_ibi_hj_response (const struct device *dev, bool ack)
```

相关声明：[i3c_ibi_hj_response](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gac8c77e43fc7c06701437e799739507ee)、[device](../device_reference/P002_设备对象结构.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

确认或拒绝带内中断热加入请求（IBI HJ Requests），即发送 ACK 或 NACK。

<a id="r_ga2546ae3b345b9271a3962c40ce38f73e"></a>

```c
static int i3c_ibi_crr_response (struct i3c_device_desc *target, bool ack)
```

相关声明：[i3c_ibi_crr_response](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga2546ae3b345b9271a3962c40ce38f73e)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

确认或拒绝带内中断控制器角色请求（IBI Controller Role Requests），即发送 ACK 或 NACK。

<a id="r_ga516c656231efd07429402c37643eca66"></a>

```c
static int i3c_ibi_raise (const struct device *dev, struct i3c_ibi *request)
```

相关声明：[i3c_ibi_raise](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga516c656231efd07429402c37643eca66)、[device](../device_reference/P002_设备对象结构.md)、[i3c_ibi](../hardware/P397_I3C带内中断请求.md)。

发起带内中断（In-Band Interrupt，IBI）。

<a id="r_ga7625ef0313ded1f638a6eb44395b02c0"></a>

```c
static int i3c_ibi_enable (struct i3c_device_desc *target)
```

相关声明：[i3c_ibi_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7625ef0313ded1f638a6eb44395b02c0)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

启用目标设备的带内中断（IBI）。

<a id="r_ga037e156404324262694b4a5403821adc"></a>

```c
static int i3c_ibi_disable (struct i3c_device_desc *target)
```

相关声明：[i3c_ibi_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga037e156404324262694b4a5403821adc)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

禁用目标设备的带内中断（IBI）。

<a id="r_ga1a23e2ca2afb7cf371f523dcbcd7724f"></a>

```c
static int i3c_ibi_has_payload (struct i3c_device_desc *target)
```

相关声明：[i3c_ibi_has_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga1a23e2ca2afb7cf371f523dcbcd7724f)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

检查目标设备的带内中断（IBI）是否具有有效载荷（Payload）。

<a id="r_ga6c09d19ab1c7c19db4d085a30066345e"></a>

```c
static int i3c_device_is_ibi_capable (struct i3c_device_desc *target)
```

相关声明：[i3c_device_is_ibi_capable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga6c09d19ab1c7c19db4d085a30066345e)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

检查设备是否具备带内中断能力（IBI Capable）。

<a id="r_ga537c1e2dafe3df1a5758e535beb323ea"></a>

```c
static int i3c_device_is_controller_capable (struct i3c_device_desc *target)
```

相关声明：[i3c_device_is_controller_capable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga537c1e2dafe3df1a5758e535beb323ea)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

检查目标设备是否具备控制器能力（Controller Capable）。

<a id="r_gaa3b61aa9813ccb0df80562b0829d95dd"></a>

```c
static int i3c_write (struct i3c_device_desc *target, const uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaa3b61aa9813ccb0df80562b0829d95dd)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 I3C 目标设备写入指定数量的数据（Data）。

<a id="r_gaba39bd08ab50c5737ba617f4d27c3541"></a>

```c
static int i3c_read (struct i3c_device_desc *target, uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaba39bd08ab50c5737ba617f4d27c3541)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 I3C 目标设备读取指定数量的数据（Data）。

<a id="r_ga3da2e99b667eab4fd92f5c0e1b57a8ea"></a>

```c
static int i3c_write_read (struct i3c_device_desc *target, const void *write_buf, size_t num_write, void *read_buf, size_t num_read)
```

相关声明：[i3c_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga3da2e99b667eab4fd92f5c0e1b57a8ea)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

先写入再读取 I3C 目标设备的数据（Write Then Read）。

<a id="r_ga3e4d985a784618efad67f8550f715115"></a>

```c
static int i3c_burst_read (struct i3c_device_desc *target, uint8_t start_addr, uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga3e4d985a784618efad67f8550f715115)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 I3C 目标设备的内部地址（Internal Address）读取多个字节。

<a id="r_gaee773f95fcaf6cb88ced47f5c512c78c"></a>

```c
static int i3c_burst_write (struct i3c_device_desc *target, uint8_t start_addr, const uint8_t *buf, uint32_t num_bytes)
```

相关声明：[i3c_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaee773f95fcaf6cb88ced47f5c512c78c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

向 I3C 目标设备的内部地址（Internal Address）写入多个字节。

<a id="r_ga87c1f23c94d37dfbaa22e4679fb8130a"></a>

```c
static int i3c_reg_read_byte (struct i3c_device_desc *target, uint8_t reg_addr, uint8_t *value)
```

相关声明：[i3c_reg_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga87c1f23c94d37dfbaa22e4679fb8130a)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

读取 I3C 目标设备的内部寄存器（Internal Register）。

<a id="r_gaf7033eb93fd3779ffa98eb83e5a1a1b1"></a>

```c
static int i3c_reg_write_byte (struct i3c_device_desc *target, uint8_t reg_addr, uint8_t value)
```

相关声明：[i3c_reg_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaf7033eb93fd3779ffa98eb83e5a1a1b1)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

写入 I3C 目标设备的内部寄存器（Internal Register）。

<a id="r_ga4e0488ff21cbe99b206c115017473ed9"></a>

```c
static int i3c_reg_update_byte (struct i3c_device_desc *target, uint8_t reg_addr, uint8_t mask, uint8_t value)
```

相关声明：[i3c_reg_update_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga4e0488ff21cbe99b206c115017473ed9)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

更新 I3C 目标设备的内部寄存器（Internal Register）。

<a id="r_ga61098371d2492a3f35c0fa779a88b348"></a>

```c
void i3c_dump_msgs (const char *name, const struct i3c_msg *msgs, uint8_t num_msgs, struct i3c_device_desc *target)
```

相关声明：[i3c_dump_msgs](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga61098371d2492a3f35c0fa779a88b348)、[i3c_msg](../hardware/P395_I3C传输消息.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

转储 I3C 报文（Message）。

<a id="r_ga9af9191a5ab2e5e2ea0478520721171d"></a>

```c
int i3c_bus_init (const struct device *dev, const struct i3c_dev_list *i3c_dev_list)
```

相关声明：[i3c_bus_init](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9af9191a5ab2e5e2ea0478520721171d)、[device](../device_reference/P002_设备对象结构.md)、[i3c_dev_list](../hardware/P403_I3C已知设备列表.md)、[i3c_dev_list](../hardware/P403_I3C已知设备列表.md)。

执行总线初始化（Bus Initialization）的通用辅助函数。

<a id="r_gaac5d10b8f42a6a069e0ac15cc7263db8"></a>

```c
int i3c_device_basic_info_get (struct i3c_device_desc *target)
```

相关声明：[i3c_device_basic_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaac5d10b8f42a6a069e0ac15cc7263db8)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备基本信息（Basic Information），并更新设备描述符。

<a id="r_ga4e4a7e9408bd2f43602367bc9fe4f81e"></a>

```c
int i3c_device_adv_info_get (struct i3c_device_desc *target)
```

相关声明：[i3c_device_adv_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga4e4a7e9408bd2f43602367bc9fe4f81e)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备高级信息（Advanced Information），并更新设备描述符。

<a id="r_ga39a760d8ba759f9443689fc954eb3d4b"></a>

```c
static int i3c_device_info_get (struct i3c_device_desc *target)
```

相关声明：[i3c_device_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga39a760d8ba759f9443689fc954eb3d4b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备全部信息（All Information），并更新设备描述符。

<a id="r_ga125e18a08f4b16efbb3f27297a1de13c"></a>

```c
enum i3c_bus_mode i3c_bus_mode (const struct i3c_dev_list *dev_list)
```

相关声明：[i3c_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7a0d66ab45f618ca055422e2b69abe90)、[i3c_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga125e18a08f4b16efbb3f27297a1de13c)、[i3c_dev_list](../hardware/P403_I3C已知设备列表.md)。

根据总线上的 I2C 设备确定 I3C 总线模式（Bus Mode）。

<a id="r_ga149d70b1c2e02e19782aa21a94b13684"></a>

```c
bool i3c_bus_has_sec_controller (const struct device *dev)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_bus_has_sec_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga149d70b1c2e02e19782aa21a94b13684)、[device](../device_reference/P002_设备对象结构.md)。

检查总线是否具有次级控制器（Secondary Controller）。

<a id="r_ga14ec397e1c82b79302f7eff6022660ae"></a>

```c
int i3c_bus_rstdaa_all (const struct device *dev)
```

相关声明：[i3c_bus_rstdaa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga14ec397e1c82b79302f7eff6022660ae)、[device](../device_reference/P002_设备对象结构.md)。

复位总线上的全部设备，并清除其动态地址（Dynamic Addresses）。

<a id="r_ga2ae8b79140ddceebd071e0891a0ac824"></a>

```c
int i3c_bus_setdasa (struct i3c_device_desc *desc, uint8_t dynamic_addr)
```

相关声明：[i3c_bus_setdasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga2ae8b79140ddceebd071e0891a0ac824)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

使用设备的静态地址为其分配动态地址（Dynamic Address）。

<a id="r_ga55ba4babddb31ed83ad3fab5adce2f18"></a>

```c
int i3c_bus_setnewda (struct i3c_device_desc *desc, uint8_t dynamic_addr)
```

相关声明：[i3c_bus_setnewda](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga55ba4babddb31ed83ad3fab5adce2f18)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为设备分配新的动态地址（Dynamic Address）。

<a id="r_gab6735824952836a1ac06745b21e2b534"></a>

```c
int i3c_bus_setaasa (const struct device *dev)
```

相关声明：[i3c_bus_setaasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab6735824952836a1ac06745b21e2b534)、[device](../device_reference/P002_设备对象结构.md)。

将总线上全部设备的静态地址用作动态地址（Dynamic Addresses）。

<a id="r_gac8c0ec6eb11030183be10fb541e1e561"></a>

```c
int i3c_bus_getbcr (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getbcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac8c0ec6eb11030183be10fb541e1e561)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备的总线特性寄存器（Bus Characteristics Register，BCR）。

<a id="r_gaab2801ccc00e9891269709ecc34f4f7c"></a>

```c
int i3c_bus_getdcr (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getdcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaab2801ccc00e9891269709ecc34f4f7c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备的设备特性寄存器（Device Characteristics Register，DCR）。

<a id="r_ga129bab2c352fd08b62c352d916c7307c"></a>

```c
int i3c_bus_getpid (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getpid](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga129bab2c352fd08b62c352d916c7307c)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备的临时标识符（Provisional ID，PID）。

<a id="r_ga5483ce25f70cae032ed5935483102c0f"></a>

```c
int i3c_bus_getmrl (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5483ce25f70cae032ed5935483102c0f)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备的最大读取长度（Maximum Read Length，MRL）。

<a id="r_ga8d4da712075ee05896bcd7dde49cd827"></a>

```c
int i3c_bus_getmwl (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8d4da712075ee05896bcd7dde49cd827)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取设备的最大写入长度（Maximum Write Length，MWL）。

<a id="r_ga6fbb9bec228b7dc310c5724c3530bebd"></a>

```c
int i3c_bus_setmrl (struct i3c_device_desc *desc, uint16_t mrl, uint8_t ibi_len)
```

相关声明：[i3c_bus_setmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga6fbb9bec228b7dc310c5724c3530bebd)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

设置设备的最大读取长度（Maximum Read Length，MRL）。

<a id="r_ga8002de8239c4a0d1178fba27092a1254"></a>

```c
int i3c_bus_setmwl (struct i3c_device_desc *desc, uint16_t mwl)
```

相关声明：[i3c_bus_setmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8002de8239c4a0d1178fba27092a1254)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置设备的最大写入长度（Maximum Write Length，MWL）。

<a id="r_ga28278e90417b01d7cb18a301f906f6ae"></a>

```c
int i3c_bus_setmrl_all (const struct device *dev, uint16_t mrl, uint8_t ibi_len, bool has_ibi_size)
```

相关声明：[i3c_bus_setmrl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga28278e90417b01d7cb18a301f906f6ae)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置总线上全部设备的最大读取长度（Maximum Read Length，MRL）。

<a id="r_gad3a4bf3cfc1b150c19ff1186cc8e3e2a"></a>

```c
int i3c_bus_setmwl_all (const struct device *dev, uint16_t mwl)
```

相关声明：[i3c_bus_setmwl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gad3a4bf3cfc1b150c19ff1186cc8e3e2a)、[device](../device_reference/P002_设备对象结构.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置总线上全部设备的最大写入长度（Maximum Write Length，MWL）。

<a id="r_ga8d4356b56d8414e62b5a9931ffc7ab8b"></a>

```c
int i3c_bus_getacccr (struct i3c_device_desc *desc)
```

相关声明：[i3c_bus_getacccr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8d4356b56d8414e62b5a9931ffc7ab8b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

获取活动控制器动态地址（Active Controller's Dynamic Address，ACCCR）。

<a id="r_ga554e0c4fa3e6855f431521ae42313216"></a>

```c
int i3c_bus_deftgts (const struct device *dev)
```

相关声明：[i3c_bus_deftgts](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga554e0c4fa3e6855f431521ae42313216)、[device](../device_reference/P002_设备对象结构.md)。

发送通用命令码（CCC）DEFTGTS。

<a id="r_gaaf7736a8895de826f7fac1a9ecf0d7ea"></a>

```c
uint8_t i3c_odd_parity (uint8_t p)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[i3c_odd_parity](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaaf7736a8895de826f7fac1a9ecf0d7ea)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

计算奇校验（Odd Parity）。

<a id="r_gaedf58fdd96f38f103f8defe221427b6f"></a>

```c
int i3c_device_controller_handoff (struct i3c_device_desc *target, bool requested)
```

相关声明：[i3c_device_controller_handoff](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaedf58fdd96f38f103f8defe221427b6f)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

执行控制器交接（Controller Handoff）。

<a id="r_ga221ab7abe735ddee881c002b934ee138"></a>

```c
void i3c_sec_handoffed (struct k_work *work)
```

相关声明：[i3c_sec_handoffed](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga221ab7abe735ddee881c002b934ee138)、[k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)。

控制权（Controllership）移交给自身时的回调。

<a id="r_gab8e12d10528686040707f4aae502df98"></a>

```c
struct i3c_device_desc * i3c_device_desc_alloc (void)
```

相关声明：[i3c_device_desc](../hardware/P401_I3C设备描述符.md)、[i3c_device_desc_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab8e12d10528686040707f4aae502df98)。

为 I3C 设备描述符（Device Descriptor）分配内存。

<a id="r_ga25bfef54bb7bdc387ce0997ed0120739"></a>

```c
void i3c_device_desc_free (struct i3c_device_desc *desc)
```

相关声明：[i3c_device_desc_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga25bfef54bb7bdc387ce0997ed0120739)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

释放 I3C 设备描述符（Device Descriptor）的内存。

<a id="r_gaf2c8afec987322be8dfd4fb053fac61b"></a>

```c
bool i3c_device_desc_in_pool (struct i3c_device_desc *desc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_device_desc_in_pool](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaf2c8afec987322be8dfd4fb053fac61b)、[i3c_device_desc](../hardware/P401_I3C设备描述符.md)。

报告 I3C 设备描述符是否来自内存块池（Memory Slab）。

<a id="r_ga16b9ba6480ac807ff8b9268d6cffa577"></a>

```c
struct i3c_i2c_device_desc * i3c_i2c_device_desc_alloc (void)
```

相关声明：[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)、[i3c_i2c_device_desc_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga16b9ba6480ac807ff8b9268d6cffa577)。

为 I3C 总线的 I2C 设备描述符（Device Descriptor）分配内存。

<a id="r_ga61ead89539fe3556f5e6e30eae5e71a3"></a>

```c
void i3c_i2c_device_desc_free (struct i3c_i2c_device_desc *desc)
```

相关声明：[i3c_i2c_device_desc_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga61ead89539fe3556f5e6e30eae5e71a3)、[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

释放 I3C 总线的 I2C 设备描述符（Device Descriptor）的内存。

<a id="r_gabfebceaa3e6f6f255352b8dcc3e7f9b1"></a>

```c
bool i3c_i2c_device_desc_in_pool (struct i3c_i2c_device_desc *desc)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[i3c_i2c_device_desc_in_pool](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabfebceaa3e6f6f255352b8dcc3e7f9b1)、[i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)。

报告 I3C 总线的 I2C 设备描述符是否来自内存块池（Memory Slab）。

<a id="r_ga909d531941cd81850f4a05c51646690d"></a>

```c
void i3c_iodev_submit_fallback (const struct device *dev, struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[i3c_iodev_submit_fallback](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga909d531941cd81850f4a05c51646690d)、[device](../device_reference/P002_设备对象结构.md)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

后备提交实现（Fallback Submit Implementation）。

<a id="r_ga3b612267e71202094fb4adab64ffd61c"></a>

```c
static void i3c_iodev_submit (struct rtio_iodev_sqe *iodev_sqe)
```

相关声明：[i3c_iodev_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga3b612267e71202094fb4adab64ffd61c)、[rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)。

通过实时输入输出（RTIO）向 I3C 设备提交请求。

<a id="r_gab46a231442a7bf60e7e28ca2f52d25fc"></a>

```c
struct rtio_sqe * i3c_rtio_copy (struct rtio *r, struct rtio_iodev *iodev, const struct i3c_msg *msgs, uint8_t num_msgs)
```

相关声明：[rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)、[i3c_rtio_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab46a231442a7bf60e7e28ca2f52d25fc)、[rtio](../rtio_model_reference/P001_RTIO上下文.md)、[rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)、[i3c_msg](../hardware/P395_I3C传输消息.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

将 i3c_msgs 复制为一组实时输入输出（RTIO）请求。

<a id="header-var-members"></a>
<a id="var-members"></a>

## 4.6\_变量（Variables）

<a id="r_gace1f8f10af2d87bb5a17441645030833"></a>

```c
const struct rtio_iodev_api i3c_iodev_api
```

相关声明：[rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)、[i3c_iodev_api](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gace1f8f10af2d87bb5a17441645030833)。


## 4.7\_原页交叉引用（Cross References）

- [errno.h](../error_reference/P005_错误号头文件源码.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/device.h](../device_reference/P008_设备模型头文件源码.md)
- [zephyr/drivers/i3c/addresses.h](../api_source_supplement_reference/P003_addresses.h_源码浏览.md)
- [zephyr/drivers/i3c/error_types.h](../api_source_reference/P233_error_types.h_源码浏览.md)
- [zephyr/drivers/i3c/ccc.h](../api_source_supplement_reference/P023_ccc.h_源码浏览.md)
- [zephyr/drivers/i3c/devicetree.h](../api_source_reference/P157_devicetree.h_源码浏览.md)
- [zephyr/drivers/i3c/ibi.h](../api_source_reference/P332_ibi.h_源码浏览.md)
- [zephyr/drivers/i2c.h](../i2c_driver_reference/P002_I2C驱动头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [zephyr/sys/util.h](../util_reference/P003_通用工具头文件源码.md)
- [zephyr/rtio/rtio.h](../rtio_core_reference/P003_RTIO核心头文件源码.md)
- [zephyr/drivers/i3c/target_device.h](../api_source_reference/P854_target_device.h_源码浏览.md)
- [zephyr/drivers/i3c/hdr_ddr.h](../api_source_reference/P313_hdr_ddr.h_源码浏览.md)
- [查看此文件的源码。](../api_source_network_reference/P008_i3c.h_源码浏览.md)
- [i3c_msg](../hardware/P395_I3C传输消息.md)
- [i3c_config_controller](../hardware/P391_I3C控制器硬件配置.md)
- [i3c_config_custom](../hardware/P393_I3C自定义硬件配置.md)
- [i3c_device_id](../hardware/P400_I3C设备匹配标识.md)
- [i3c_device_desc](../hardware/P401_I3C设备描述符.md)
- [i3c_i2c_device_desc](../hardware/P402_I3C总线上的I2C设备描述符.md)
- [i3c_dev_attached_list](../hardware/P404_I3C已附接设备列表.md)
- [i3c_dev_list](../hardware/P403_I3C已知设备列表.md)
- [i3c_driver_config](../hardware/P405_I3C驱动公共配置.md)
- [i3c_driver_data](../hardware/P406_I3C驱动公共数据.md)
- [i3c_iodev_data](../hardware/P407_I3C输入输出设备数据.md)
- [I3C_OD_TLOW_MIN_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gadd026a36545d50ea3c043d0ebcfde95b)
- [I3C_OD_MIXED_BUS_THIGH_MAX_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7478181801369cb7ed7a7124fa9c4240)
- [I3C_OD_FIRST_BC_THIGH_MIN_NS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga41fc93e0aba6bc1cf3540ca89e860a2b)
- [I3C_MSG_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga72f9fb65d218521ad006febf3dd6851b)
- [I3C_MSG_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga6ba89782a8646f96dc1f9fa3b9cd2058)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [I3C_MSG_STOP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga0d4ae269a53af945837d158f638d8b5c)
- [I3C_MSG_RESTART](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad9ff03f4fdcb117b90c17d667a49c295)
- [I3C_MSG_HDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gad827935caf8503aeaedd1aceb53d4e38)
- [I3C_MSG_NBCH](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga4147e7cdf8155d2ef7c4dc7c08e16b6a)
- [I3C_MSG_NOACK_EXPECTED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga735a347b1d0f431ab0c3a90f509fcbe1)
- [I3C_MSG_HDR_MODE0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga18aac0862826869f94e5a71670debcb0)
- [I3C_MSG_HDR_MODE1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga8eb3dc48237dfdb25fde40a1efa03241)
- [I3C_MSG_HDR_MODE2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga15cbd61e7d509c28b22fbc9e0844cb23)
- [I3C_MSG_HDR_MODE3](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga162fb9ab0e4ed7f8feb0e91d183a88e7)
- [I3C_MSG_HDR_MODE4](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gabe45532238bc15672f6454dac70d20cf)
- [I3C_MSG_HDR_MODE5](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac712daa606d0c51ce523d7a687821282)
- [I3C_MSG_HDR_MODE6](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga7654c1947e13c019c24bf12712b0773b)
- [I3C_MSG_HDR_MODE7](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga08df1d8df82226d1f23b4cc923584672)
- [I3C_MSG_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac7386b21323d30148bd9456b9d180d7a)
- [I3C_MSG_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaa61322f770db296b5ab718c48ab960d3)
- [I3C_MSG_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gac43a2d266f3a23fd6dfa11405f3fd6f3)
- [I3C_MSG_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga8b2fdcb827cbd3325f124a1c615698e7)
- [I3C_DEVICE_ID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaed0df9802cc9b268abcfe4e877ebf498)
- [I3C_BUS_FOR_EACH_I3CDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga42cb4edf6a099d586df14456fd98c873)
- [I3C_BUS_FOR_EACH_I2CDEV](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga450ba9021d1080f890c32624f20ba2b8)
- [I3C_BUS_FOR_EACH_I3CDEV_SAFE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae2d038807305e9e13eab26bae1dd4624)
- [I3C_BUS_FOR_EACH_I2CDEV_SAFE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5536141e7c7ea9dc0b1395224089ca0d)
- [I3C_DT_IODEV_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabec5796b92d4582761bc3de456f1df27)
- [I3C_DT_INST_IODEV_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga051e80ceacf87bb9ccb79357ee7bc205)
- [I3C_BCR_MAX_DATA_SPEED_LIMIT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga91ebe41a421dc05ae7f1de1ce2dd314f)
- [I3C_BCR_IBI_REQUEST_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0c09de8a18ea1586e37d35e073ae641f)
- [I3C_BCR_IBI_PAYLOAD_HAS_DATA_BYTE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae119c230097cb8e1eab9fc45cafde838)
- [I3C_BCR_OFFLINE_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7b9fea89457022d8012ac25133bf63db)
- [I3C_BCR_VIRTUAL_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga69dc4a5004da568684a3c72046bba870)
- [I3C_BCR_ADV_CAPABILITIES](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga07018705794753d0d0d65131f011e097)
- [I3C_BCR_DEVICE_ROLE_I3C_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga867b4b12b23c803b86b57dcc86b9e604)
- [I3C_BCR_DEVICE_ROLE_I3C_CONTROLLER_CAPABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0e64c8aa6717b96bcf9dad6c9ec7f852)
- [I3C_BCR_DEVICE_ROLE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga25721c9963040c84b7f5bbb48bb87b44)
- [GENMASK](../util_reference/P001_通用工具公共接口.md#ga58530d20924859d16358c7400c37738d)
- [I3C_BCR_DEVICE_ROLE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga90988b26dc2f388ec7c65387a24f05af)
- [I3C_LVR_I2C_FM_PLUS_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9bf868ac6ae38e3f8ab6e5e1378bfb75)
- [I3C_LVR_I2C_FM_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga053945f5f67ee3c681de2c9362e69c39)
- [I3C_LVR_I2C_MODE_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaf073cc9ea1a68c57663c36de12554876)
- [I3C_LVR_I2C_MODE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaaf759805bb5824a89612b292a4439982)
- [I3C_LVR_I2C_DEV_IDX_0](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga4319835ddb6b5984b21f5a5a2f14ae75)
- [I3C_LVR_I2C_DEV_IDX_1](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga02a21af4c679a81b8290beea30c8ef40)
- [I3C_LVR_I2C_DEV_IDX_2](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5950bb8ceea5fcd3ceb38c7da0d9dd68)
- [I3C_LVR_I2C_DEV_IDX_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga50fa249b36b91d56e49004548a1c7520)
- [I3C_LVR_I2C_DEV_IDX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae7afa509b1d63374c551bcdaf84c5dd1)
- [i3c_callback_t](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac1df0bbb6943e1ec59c5b0dba27257fe)
- [device](../device_reference/P002_设备对象结构.md)
- [i3c_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7a0d66ab45f618ca055422e2b69abe90)
- [I3C_BUS_MODE_PURE](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a879f2e1337e50df0df804b870ceb6445)
- [I3C_BUS_MODE_MIXED_FAST](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a913a67b18c3020d393ffab9edc970434)
- [I3C_BUS_MODE_MIXED_LIMITED](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90ab64e923c332404da70d0b8266827a722)
- [I3C_BUS_MODE_MIXED_SLOW](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90ad86533c65d9685bed06110056a0fd31a)
- [I3C_BUS_MODE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90aa078a6108abc5f5783b4113b4b475697)
- [I3C_BUS_MODE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga7a0d66ab45f618ca055422e2b69abe90a67e56000ca21354d218d48f26a95b36c)
- [i3c_i2c_speed_type](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga67686f0a5d83697361c655c3fd6e61c6)
- [I3C_I2C_SPEED_FM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6af3e68696cdca6bd202bff26fa804d3e1)
- [I3C_I2C_SPEED_FMPLUS](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6ae28e3d134dd27348a45704402b49cbea)
- [I3C_I2C_SPEED_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6aa1826e175d88c25e26d09f044bd7c967)
- [I3C_I2C_SPEED_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga67686f0a5d83697361c655c3fd6e61c6a9e4ffc7ed1f2ceed97944cda0cf547c4)
- [i3c_data_rate](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae9d98642c6f249ee0e6ea0dc491b5073)
- [I3C_DATA_RATE_SDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a7da0e8024e49d704c7f11e6f64e739c9)
- [I3C_DATA_RATE_HDR_DDR](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a7a18220be49deea188c386398846d301)
- [I3C_DATA_RATE_HDR_TSL](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073ab20f2392a5729800a329b4b4a0a4e590)
- [I3C_DATA_RATE_HDR_TSP](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a583fe54dd65bd7805a747cfe7ec9663d)
- [I3C_DATA_RATE_HDR_BT](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073ae6d5eb001045596bc01a8b26fdbf52ed)
- [I3C_DATA_RATE_MAX](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a4b8e5152ac9e2a54fad142cc47b13725)
- [I3C_DATA_RATE_INVALID](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ggae9d98642c6f249ee0e6ea0dc491b5073a511dd2b924d1d423adbaa841b941748a)
- [i3c_config_type](../hardware/P425_I3C公共接口参考.md#ga5b111bc8fa8c3bee052e621d26dcc54a)
- [I3C_CONFIG_CONTROLLER](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aaab2bdda67e4aa91f8fd43c110e2a25e5)
- [I3C_CONFIG_TARGET](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aa0304077c1d277f6a0f80424879474d00)
- [I3C_CONFIG_CUSTOM](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gga5b111bc8fa8c3bee052e621d26dcc54aa8decc53824153bb2582c9ce0e9b47017)
- [i3c_dev_list_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9a451379bef381c6a264a22a2282fa89)
- [i3c_dev_list_i3c_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga0e83c5a26b18acfbe7d532825a8fd54c)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [i3c_dev_list_i3c_static_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaecbb16ce8edcd9ad7a7afcfb1251aa76)
- [i3c_dev_list_i2c_addr_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gafac78dca571ff7daa34fca0cfa7cc3b1)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [i3c_dev_list_daa_addr_helper](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga43c3268fef220faa21b81010876e69d0)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [i3c_configure](../hardware/P425_I3C公共接口参考.md#ga2f176f8440d86f4ec6c94a8911a75352)
- [i3c_configure_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaeca24930774ecc2dcbf2240d48ae19c5)
- [i3c_configure_target](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7dfa33c7bdbe7e6607af61fe04bcb985)
- [i3c_config_target](../hardware/P392_I3C目标硬件配置.md)
- [i3c_config_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga807877923755aeb5a065e054fb42946d)
- [i3c_config_get_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga96cd903b4a676c5943c43cc7b27af867)
- [i3c_config_get_target](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8ef11af673e94646806e093504cfb01f)
- [i3c_recover_bus](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga7b23e08b10a09bde4e87328d6915aa25)
- [i3c_attach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga042d1a3315f040562534ce08306b329c)
- [i3c_reattach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gae6c8e8612368808117f4fce960e43769)
- [i3c_detach_i3c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga6db9688cc7e9d34404717ae753751579)
- [i3c_is_i3c_device_attached](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac10ab0c78a581bf8284b9cc3a30c92cf)
- [i3c_attach_i2c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5e69aaed50f99418c7123f652555ae20)
- [i3c_detach_i2c_device](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8e8de45499bff02cac4c59c1758ec0a7)
- [i3c_is_i2c_device_attached](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga489c2c5f18e92421642d2316c317dbd9)
- [i3c_do_daa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabb54c0e85d0f5e8585391f9e5c20d4b6)
- [i3c_do_ccc](../hardware/P425_I3C公共接口参考.md#gaa6d5445489bfc8611c98b93f49305862)
- [i3c_ccc_payload](../hardware/P417_I3C通用命令传输载荷.md)
- [i3c_do_ccc_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga779f8dd18d361175ea0d38fe3de16ef6)
- [i3c_transfer](../hardware/P394_I3C传输接口.md#ga067c0f1e3c9abb6ef34ce48cb7e45cb8)
- [i3c_transfer_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga354eb19c5134f1a4df291005d0f6622a)
- [i3c_device_find](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga10a3963b749cc667a03975889d618d1b)
- [i3c_ibi_hj_response](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#gac8c77e43fc7c06701437e799739507ee)
- [i3c_ibi_crr_response](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga2546ae3b345b9271a3962c40ce38f73e)
- [i3c_ibi_raise](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga516c656231efd07429402c37643eca66)
- [i3c_ibi](../hardware/P397_I3C带内中断请求.md)
- [i3c_ibi_enable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga7625ef0313ded1f638a6eb44395b02c0)
- [i3c_ibi_disable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga037e156404324262694b4a5403821adc)
- [i3c_ibi_has_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga1a23e2ca2afb7cf371f523dcbcd7724f)
- [i3c_device_is_ibi_capable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga6c09d19ab1c7c19db4d085a30066345e)
- [i3c_device_is_controller_capable](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__ibi.html#ga537c1e2dafe3df1a5758e535beb323ea)
- [i3c_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaa3b61aa9813ccb0df80562b0829d95dd)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [i3c_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaba39bd08ab50c5737ba617f4d27c3541)
- [i3c_write_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga3da2e99b667eab4fd92f5c0e1b57a8ea)
- [i3c_burst_read](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga3e4d985a784618efad67f8550f715115)
- [i3c_burst_write](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaee773f95fcaf6cb88ced47f5c512c78c)
- [i3c_reg_read_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga87c1f23c94d37dfbaa22e4679fb8130a)
- [i3c_reg_write_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#gaf7033eb93fd3779ffa98eb83e5a1a1b1)
- [i3c_reg_update_byte](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga4e0488ff21cbe99b206c115017473ed9)
- [i3c_dump_msgs](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__transfer__api.html#ga61098371d2492a3f35c0fa779a88b348)
- [i3c_bus_init](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga9af9191a5ab2e5e2ea0478520721171d)
- [i3c_device_basic_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaac5d10b8f42a6a069e0ac15cc7263db8)
- [i3c_device_adv_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga4e4a7e9408bd2f43602367bc9fe4f81e)
- [i3c_device_info_get](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga39a760d8ba759f9443689fc954eb3d4b)
- [i3c_bus_mode](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga125e18a08f4b16efbb3f27297a1de13c)
- [i3c_bus_has_sec_controller](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga149d70b1c2e02e19782aa21a94b13684)
- [i3c_bus_rstdaa_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga14ec397e1c82b79302f7eff6022660ae)
- [i3c_bus_setdasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga2ae8b79140ddceebd071e0891a0ac824)
- [i3c_bus_setnewda](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga55ba4babddb31ed83ad3fab5adce2f18)
- [i3c_bus_setaasa](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab6735824952836a1ac06745b21e2b534)
- [i3c_bus_getbcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gac8c0ec6eb11030183be10fb541e1e561)
- [i3c_bus_getdcr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaab2801ccc00e9891269709ecc34f4f7c)
- [i3c_bus_getpid](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga129bab2c352fd08b62c352d916c7307c)
- [i3c_bus_getmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga5483ce25f70cae032ed5935483102c0f)
- [i3c_bus_getmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8d4da712075ee05896bcd7dde49cd827)
- [i3c_bus_setmrl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga6fbb9bec228b7dc310c5724c3530bebd)
- [i3c_bus_setmwl](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8002de8239c4a0d1178fba27092a1254)
- [i3c_bus_setmrl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga28278e90417b01d7cb18a301f906f6ae)
- [i3c_bus_setmwl_all](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gad3a4bf3cfc1b150c19ff1186cc8e3e2a)
- [i3c_bus_getacccr](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga8d4356b56d8414e62b5a9931ffc7ab8b)
- [i3c_bus_deftgts](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga554e0c4fa3e6855f431521ae42313216)
- [i3c_odd_parity](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaaf7736a8895de826f7fac1a9ecf0d7ea)
- [i3c_device_controller_handoff](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaedf58fdd96f38f103f8defe221427b6f)
- [i3c_sec_handoffed](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga221ab7abe735ddee881c002b934ee138)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [i3c_device_desc_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab8e12d10528686040707f4aae502df98)
- [i3c_device_desc_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga25bfef54bb7bdc387ce0997ed0120739)
- [i3c_device_desc_in_pool](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gaf2c8afec987322be8dfd4fb053fac61b)
- [i3c_i2c_device_desc_alloc](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga16b9ba6480ac807ff8b9268d6cffa577)
- [i3c_i2c_device_desc_free](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga61ead89539fe3556f5e6e30eae5e71a3)
- [i3c_i2c_device_desc_in_pool](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gabfebceaa3e6f6f255352b8dcc3e7f9b1)
- [i3c_iodev_submit_fallback](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga909d531941cd81850f4a05c51646690d)
- [rtio_iodev_sqe](../rtio_model_reference/P005_RTIO设备提交条目.md)
- [i3c_iodev_submit](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#ga3b612267e71202094fb4adab64ffd61c)
- [rtio_sqe](../rtio_model_reference/P007_RTIO提交事件.md)
- [i3c_rtio_copy](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gab46a231442a7bf60e7e28ca2f52d25fc)
- [rtio](../rtio_model_reference/P001_RTIO上下文.md)
- [rtio_iodev](../rtio_model_reference/P003_RTIO输入输出设备.md)
- [rtio_iodev_api](../rtio_model_reference/P004_RTIO设备函数表.md)
- [i3c_iodev_api](https://docs.zephyrproject.org/latest/doxygen/html/group__i3c__interface.html#gace1f8f10af2d87bb5a17441645030833)

<a id="I3C_BCR"></a>
<a id="I3C_LVR"></a>
<a id="header-details"></a>

---

[上一章](P003_zephyr__bluetooth__conn.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P005_zephyr__net__ieee802154_frame.h_文件参考.md)
