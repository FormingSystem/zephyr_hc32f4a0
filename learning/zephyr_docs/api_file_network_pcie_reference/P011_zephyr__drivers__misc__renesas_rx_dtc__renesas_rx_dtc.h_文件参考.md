---
id: learning.zephyr-docs.api-file-network-pcie-reference.page-11
title: zephyr__drivers__misc__renesas_rx_dtc__renesas_rx_dtc.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_zephyr\_\_drivers\_\_misc\_\_renesas\_rx\_dtc\_\_renesas\_rx\_dtc.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/renesas__rx__dtc_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Renesas RX数据传输控制器（DTC）驱动的头文件。

<a id="details"></a>

```c
#include <zephyr/drivers/gpio.h>
```

查看此文件的源码。

Renesas RX数据传输控制器（DTC）驱动的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 11.1\_数据结构（Data Structures）

<a id="r_st_5Ftransfer_5Finfo"></a>

```c
struct st_transfer_info
```

相关声明：[st_transfer_info](../device_power_control_model_reference/P090_st_transfer_info_结构体.md)。

传输信息（Transfer Information）结构。

<a id="r_st_5Ftransfer_5Fproperties"></a>

```c
struct st_transfer_properties
```

相关声明：[st_transfer_properties](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md)。

详细传输属性（Detailed Transfer Properties）。

<a id="r_dtc_5Ftransfer_5Fstatus"></a>

```c
struct dtc_transfer_status
```

相关声明：[dtc_transfer_status](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md)。

数据传输控制器（DTC）的传输状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 11.2\_宏定义（Macros）

<a id="define-members-0"></a>

### Renesas RX 数据传输控制器驱动定义（Renesas RX DTC driver definitions）

<a id="r_a820a787cb1c470dcb7e2a000f1a5908b"></a>

```c
#define DTC_PLACE_IN_SECTION(x)
```

相关声明：[DTC_PLACE_IN_SECTION](#a820a787cb1c470dcb7e2a000f1a5908b)。

将变量放入指定节（Section）的属性（Attribute）。

<a id="r_a9323021c339bc213862aa12aa302cf1b"></a>

```c
#define DTC_ALIGN_VARIABLE(x)
```

相关声明：[DTC_ALIGN_VARIABLE](#a9323021c339bc213862aa12aa302cf1b)。

设置变量对齐（Alignment）的属性（Attribute）。

<a id="r_a0bf33a92b64e91c91daffdd372fb8321"></a>

```c
#define DTC_SECTION_ATTRIBUTE DTC_PLACE_IN_SECTION(".dtc_vector_table")
```

相关声明：[DTC_SECTION_ATTRIBUTE](#a0bf33a92b64e91c91daffdd372fb8321)、[DTC_PLACE_IN_SECTION](#a820a787cb1c470dcb7e2a000f1a5908b)。

数据传输控制器向量表节属性（DTC Vector Table Section Attribute）。

<a id="r_a998b3e77a5d2fbd41cdc0d1006cc58d5"></a>

```c
#define DTC_VECTOR_TABLE_ENTRIES (CONFIG_NUM_IRQS)
```

相关声明：[DTC_VECTOR_TABLE_ENTRIES](#a998b3e77a5d2fbd41cdc0d1006cc58d5)。

DTC 向量条目数（Number of DTC Vector Entries）。

<a id="r_ab1b1d04710eeec628c4b9db47eeaab01"></a>

```c
#define DTC_PRV_ACT_BIT_MASK (1 << 15)
```

相关声明：[DTC_PRV_ACT_BIT_MASK](#ab1b1d04710eeec628c4b9db47eeaab01)。

DTC 活动标志（Active Flag，`DTCSTS.ACT`）的位掩码（Bit Mask）。

<a id="r_af976a02ce499ece17f4878f28e7dbc8b"></a>

```c
#define DTC_PRV_VECT_NR_MASK (0x00FF)
```

相关声明：[DTC_PRV_VECT_NR_MASK](#af976a02ce499ece17f4878f28e7dbc8b)。

DTC 激活向量编号（DTC-Activating Vector Number）的位掩码。

<a id="r_a5e430077b6d5a7d88d241a907eaaa33f"></a>

```c
#define DTC_PRV_MASK_CRAL (0xFFU)
```

相关声明：[DTC_PRV_MASK_CRAL](#a5e430077b6d5a7d88d241a907eaaa33f)。

计数器寄存器 A 低字节掩码（Counter Register A Lower Byte Mask）。

<a id="r_af371b3881a8624f0cf4ec2a8e3df7dac"></a>

```c
#define DTC_PRV_OFFSET_CRAH (8U)
```

相关声明：[DTC_PRV_OFFSET_CRAH](#af371b3881a8624f0cf4ec2a8e3df7dac)。

计数器寄存器 A 高字节偏移量（Counter Register A Upper Byte Offset）。

<a id="r_aefd0bae0ca748ccb6719ab0134d9d70b"></a>

```c
#define DTC_MAX_NORMAL_TRANSFER_LENGTH (0x10000)
```

相关声明：[DTC_MAX_NORMAL_TRANSFER_LENGTH](#aefd0bae0ca748ccb6719ab0134d9d70b)。

正常模式（NORMAL MODE）下可配置的最大传输次数。

<a id="r_a4fd7d0141f9b7f10c39146c4b80242e7"></a>

```c
#define DTC_MAX_REPEAT_TRANSFER_LENGTH (0x100)
```

相关声明：[DTC_MAX_REPEAT_TRANSFER_LENGTH](#a4fd7d0141f9b7f10c39146c4b80242e7)。

重复模式（REPEAT MODE）下每次重复的最大传输次数。

<a id="r_a19425a6e2cc8c0080c61ff61f6ad9e29"></a>

```c
#define DTC_MAX_BLOCK_TRANSFER_LENGTH (0x100)
```

相关声明：[DTC_MAX_BLOCK_TRANSFER_LENGTH](#a19425a6e2cc8c0080c61ff61f6ad9e29)。

块模式（BLOCK MODE）下每个块的最大传输次数。

<a id="r_a7ab61b801ce7972fdfc9c6f00da2df51"></a>

```c
#define DTC_MAX_BLOCK_COUNT (0x10000)
```

相关声明：[DTC_MAX_BLOCK_COUNT](#a7ab61b801ce7972fdfc9c6f00da2df51)。

块模式（BLOCK MODE）下可配置的最大传输块数。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 11.3\_类型定义（Typedefs）

<a id="r_ae69bf278e293c26a27b5752894ea3678"></a>

```c
typedef enum e_transfer_addr_mode transfer_addr_mode_t
```

相关声明：[e_transfer_addr_mode](#a0ae834acb01772fef5fd38c62486cb72)、[transfer_addr_mode_t](#ae69bf278e293c26a27b5752894ea3678)。

传输地址模式（Transfer Address Mode）。

<a id="r_af5ab2f4c329bd42eb7893a1aece381f5"></a>

```c
typedef enum e_transfer_repeat_area transfer_repeat_area_t
```

相关声明：[e_transfer_repeat_area](#abbe162d4578a4ab187a1549bcc850ca6)、[transfer_repeat_area_t](#af5ab2f4c329bd42eb7893a1aece381f5)。

重复传输模式（Repeat Transfer Mode）下重复的区域（Area）。

<a id="r_ad550861b5af9e2d116b03ddc440f6c35"></a>

```c
typedef enum e_transfer_irq transfer_irq_t
```

相关声明：[e_transfer_irq](#a56fa6d340c574db7be73de060d155b4d)、[transfer_irq_t](#ad550861b5af9e2d116b03ddc440f6c35)。

传输中断类型（Transfer Interrupt Type）。

<a id="r_a1c9f7b59f5fcfeaeb6e528c2b3b067ff"></a>

```c
typedef enum e_transfer_chain_mode transfer_chain_mode_t
```

相关声明：[e_transfer_chain_mode](#a058dc1dc14c2fc4e1be1352be860fd5d)、[transfer_chain_mode_t](#a1c9f7b59f5fcfeaeb6e528c2b3b067ff)。

<a id="r_ada156bb47034b335a8e57d7cdff02238"></a>

```c
typedef enum e_transfer_size transfer_size_t
```

相关声明：[e_transfer_size](#a81a8afa6b36f96ad966677d0efaefce0)、[transfer_size_t](#ada156bb47034b335a8e57d7cdff02238)。

传输数据大小。

<a id="r_aea0db2ddbbc3831666b0bf2bb4cc0fb5"></a>

```c
typedef enum e_transfer_mode transfer_mode_t
```

相关声明：[e_transfer_mode](#af75bb588cec15252fea99d0cf2e4a9f1)、[transfer_mode_t](#aea0db2ddbbc3831666b0bf2bb4cc0fb5)。

传输模式。

<a id="r_a93829fb00a7ef2349279986aee9f4c94"></a>

```c
typedef enum e_dtc_act_status dtc_act_status_t
```

相关声明：[e_dtc_act_status](#a5888188d6d3123522bd75b08d228b53a)、[dtc_act_status_t](#a93829fb00a7ef2349279986aee9f4c94)。

DTC 激活状态（Activation Status）。

<a id="r_a971f4055201125c15f25b4c7ba12d34e"></a>

```c
typedef struct st_transfer_info transfer_info_t
```

相关声明：[st_transfer_info](../device_power_control_model_reference/P090_st_transfer_info_结构体.md)、[transfer_info_t](#a971f4055201125c15f25b4c7ba12d34e)。

传输信息（Transfer Information）结构。

<a id="r_aa1b08c5715fd33b689643a82c63301d9"></a>

```c
typedef struct st_transfer_properties transfer_properties_t
```

相关声明：[st_transfer_properties](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md)、[transfer_properties_t](#aa1b08c5715fd33b689643a82c63301d9)。

详细传输属性（Detailed Transfer Properties）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 11.4\_枚举（Enumerations）

<a id="r_a0ae834acb01772fef5fd38c62486cb72"></a>

```c
enum e_transfer_addr_mode { TRANSFER_ADDR_MODE_FIXED = 0 , TRANSFER_ADDR_MODE_OFFSET = 1 , TRANSFER_ADDR_MODE_INCREMENTED = 2 , TRANSFER_ADDR_MODE_DECREMENTED = 3 }
```

相关声明：[e_transfer_addr_mode](#a0ae834acb01772fef5fd38c62486cb72)、[TRANSFER_ADDR_MODE_FIXED](#a0ae834acb01772fef5fd38c62486cb72abf18f9b3701e9e91f44055ee47d0ca47)、[TRANSFER_ADDR_MODE_OFFSET](#a0ae834acb01772fef5fd38c62486cb72ab8b3f8ce28fb6f7a57a1b87db0d612c2)、[TRANSFER_ADDR_MODE_INCREMENTED](#a0ae834acb01772fef5fd38c62486cb72a7665741e25c4cc78fd24745efbd2eaad)、[TRANSFER_ADDR_MODE_DECREMENTED](#a0ae834acb01772fef5fd38c62486cb72a56a87e1587844119831414f3d5e6d761)。

传输地址模式（Transfer Address Mode）。

<a id="r_abbe162d4578a4ab187a1549bcc850ca6"></a>

```c
enum e_transfer_repeat_area { TRANSFER_REPEAT_AREA_DESTINATION = 0 , TRANSFER_REPEAT_AREA_SOURCE = 1 }
```

相关声明：[e_transfer_repeat_area](#abbe162d4578a4ab187a1549bcc850ca6)、[TRANSFER_REPEAT_AREA_DESTINATION](#abbe162d4578a4ab187a1549bcc850ca6a77aeeab30b003de23742e40a57f19239)、[TRANSFER_REPEAT_AREA_SOURCE](#abbe162d4578a4ab187a1549bcc850ca6a2002ef7bbc49f7c9ebfac1618ba3c391)。

重复传输模式（Repeat Transfer Mode）下重复的区域（Area）。

<a id="r_a56fa6d340c574db7be73de060d155b4d"></a>

```c
enum e_transfer_irq { TRANSFER_IRQ_END = 0 , TRANSFER_IRQ_EACH = 1 }
```

相关声明：[e_transfer_irq](#a56fa6d340c574db7be73de060d155b4d)、[TRANSFER_IRQ_END](#a56fa6d340c574db7be73de060d155b4dada378ad830e44cc0c25d4fe2413e11de)、[TRANSFER_IRQ_EACH](#a56fa6d340c574db7be73de060d155b4da0929782b61686db69e12b3cb18175b35)。

传输中断类型（Transfer Interrupt Type）。

<a id="r_a058dc1dc14c2fc4e1be1352be860fd5d"></a>

```c
enum e_transfer_chain_mode { TRANSFER_CHAIN_MODE_DISABLED = 0 , TRANSFER_CHAIN_MODE_EACH = 2 , TRANSFER_CHAIN_MODE_END = 3 }
```

相关声明：[e_transfer_chain_mode](#a058dc1dc14c2fc4e1be1352be860fd5d)、[TRANSFER_CHAIN_MODE_DISABLED](#a058dc1dc14c2fc4e1be1352be860fd5dae974453c306b4959252905e362d75067)、[TRANSFER_CHAIN_MODE_EACH](#a058dc1dc14c2fc4e1be1352be860fd5dadab837d29a543149d35ed2fd28d8e4e8)、[TRANSFER_CHAIN_MODE_END](#a058dc1dc14c2fc4e1be1352be860fd5dab853bdecc90c476b995644c273e0ee75)。

<a id="r_a81a8afa6b36f96ad966677d0efaefce0"></a>

```c
enum e_transfer_size { TRANSFER_SIZE_1_BYTE = 0 , TRANSFER_SIZE_2_BYTE = 1 , TRANSFER_SIZE_4_BYTE = 2 }
```

相关声明：[e_transfer_size](#a81a8afa6b36f96ad966677d0efaefce0)、[TRANSFER_SIZE_1_BYTE](#a81a8afa6b36f96ad966677d0efaefce0accfeb24892ec24e42ccf14e4d4896c21)、[TRANSFER_SIZE_2_BYTE](#a81a8afa6b36f96ad966677d0efaefce0a8b6b33a085b51ea2eeed1ef119de562f)、[TRANSFER_SIZE_4_BYTE](#a81a8afa6b36f96ad966677d0efaefce0a18482bfa86e737cde78042be4db54412)。

传输数据大小。

<a id="r_af75bb588cec15252fea99d0cf2e4a9f1"></a>

```c
enum e_transfer_mode { TRANSFER_MODE_NORMAL = 0 , TRANSFER_MODE_REPEAT = 1 , TRANSFER_MODE_BLOCK = 2 , TRANSFER_MODE_REPEAT_BLOCK = 3 }
```

相关声明：[e_transfer_mode](#af75bb588cec15252fea99d0cf2e4a9f1)、[TRANSFER_MODE_NORMAL](#af75bb588cec15252fea99d0cf2e4a9f1ada90d8a89f98ff82475383b14141b08d)、[TRANSFER_MODE_REPEAT](#af75bb588cec15252fea99d0cf2e4a9f1a607c41bfd08797c08a5ee9bd4dfb9c8b)、[TRANSFER_MODE_BLOCK](#af75bb588cec15252fea99d0cf2e4a9f1aa4f65de2d9454af406f60172ff858d55)、[TRANSFER_MODE_REPEAT_BLOCK](#af75bb588cec15252fea99d0cf2e4a9f1afb43c6e62b61f0dbb9a5bcd5575e79e2)。

传输模式。

<a id="r_a5888188d6d3123522bd75b08d228b53a"></a>

```c
enum e_dtc_act_status { DTC_ACT_IDLE = 0 , DTC_ACT_CONFIGURED = 1 , DTC_ACT_IN_PROGRESS = 2 }
```

相关声明：[e_dtc_act_status](#a5888188d6d3123522bd75b08d228b53a)、[DTC_ACT_IDLE](#a5888188d6d3123522bd75b08d228b53aaf4fc44a34b910cbb4bcac8703e4b7d30)、[DTC_ACT_CONFIGURED](#a5888188d6d3123522bd75b08d228b53aab1bb6f41ed6ce9f46caa06ba7ef158c6)、[DTC_ACT_IN_PROGRESS](#a5888188d6d3123522bd75b08d228b53aa4a1afc72aa44c347439cb8557e930d74)。

DTC 激活状态（Activation Status）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 11.5\_函数（Functions）

<a id="r_a72e8a62b215ba60e4f99bca338526e4f"></a>

```c
int dtc_renesas_rx_off (const struct device *dev)
```

相关声明：[dtc_renesas_rx_off](#a72e8a62b215ba60e4f99bca338526e4f)、[device](../device_reference/P002_设备对象结构.md)。

关闭 DTC 模块（Module）。

<a id="r_aeba55fc712a1caf61abcf5c7f30e7654"></a>

```c
int dtc_renesas_rx_on (const struct device *dev)
```

相关声明：[dtc_renesas_rx_on](#aeba55fc712a1caf61abcf5c7f30e7654)、[device](../device_reference/P002_设备对象结构.md)。

开启 DTC 模块（Module）。

<a id="r_a4c7e963fd2e8a807ed6f1c1c773bc5ef"></a>

```c
int dtc_renesas_rx_configuration (const struct device *dev, uint8_t activation_irq, transfer_info_t *p_info)
```

相关声明：[dtc_renesas_rx_configuration](#a4c7e963fd2e8a807ed6f1c1c773bc5ef)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transfer_info_t](#a971f4055201125c15f25b4c7ba12d34e)。

配置 `p_info` 状态，并将 `p_info` 写入 DTC 向量表（Vector Table）。

<a id="r_ac0840ee89a1688a5212d34c5699640dc"></a>

```c
int dtc_renesas_rx_enable_transfer (uint8_t activation_irq)
```

相关声明：[dtc_renesas_rx_enable_transfer](#ac0840ee89a1688a5212d34c5699640dc)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在中断控制单元（ICU）中，为此激活源（Activation Source）启用传输。

<a id="r_aba28c80e24d2d011f0bb389feffa3da6"></a>

```c
int dtc_renesas_rx_disable_transfer (uint8_t activation_irq)
```

相关声明：[dtc_renesas_rx_disable_transfer](#aba28c80e24d2d011f0bb389feffa3da6)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

在中断控制单元（ICU）中，为此激活源（Activation Source）禁用传输。

<a id="r_a1280f41f5ad8d4b5beb79a87f5724363"></a>

```c
int dtc_renesas_rx_start_transfer (const struct device *dev, uint8_t activation_irq)
```

相关声明：[dtc_renesas_rx_start_transfer](#a1280f41f5ad8d4b5beb79a87f5724363)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

启动此激活源（Activation Source）上的传输。

<a id="r_aad7601ea771de91d82a213a528f97cb3"></a>

```c
int dtc_renesas_rx_stop_transfer (const struct device *dev, uint8_t activation_irq)
```

相关声明：[dtc_renesas_rx_stop_transfer](#aad7601ea771de91d82a213a528f97cb3)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

停止此激活源（Activation Source）上的传输。

<a id="r_ae6c70fe832e1d8873dd4240d90fe8240"></a>

```c
int dtc_renesas_rx_reset_transfer (const struct device *dev, uint8_t activation_irq, void const *p_src, void *p_dest, uint16_t const num_transfers)
```

相关声明：[dtc_renesas_rx_reset_transfer](#ae6c70fe832e1d8873dd4240d90fe8240)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

重置此激活源（Activation Source）上的传输。

<a id="r_af833ddfd2351d577c540f7daa1549717"></a>

```c
void dtc_renesas_rx_get_transfer_status (const struct device *dev, struct dtc_transfer_status *status)
```

相关声明：[dtc_renesas_rx_get_transfer_status](#af833ddfd2351d577c540f7daa1549717)、[device](../device_reference/P002_设备对象结构.md)、[dtc_transfer_status](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md)。

获取 DTC 模块的传输状态（Transfer Status），并存入 `status` 指针所指位置。

<a id="r_aa477baa206c2f80a40d473b648596b61"></a>

```c
int dtc_renesas_rx_info_get (const struct device *dev, uint8_t activation_irq, transfer_properties_t *const p_properties)
```

相关声明：[dtc_renesas_rx_info_get](#aa477baa206c2f80a40d473b648596b61)、[device](../device_reference/P002_设备对象结构.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[transfer_properties_t](#aa1b08c5715fd33b689643a82c63301d9)。

获取此次传输的信息（Transfer Information），并存入 `p_properties`。

<a id="r_af3895a9c7e54a6ba5014f54ea541ba75"></a>

```c
static ALWAYS_INLINE bool is_valid_activation_irq (uint8_t activation_irq)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[is_valid_activation_irq](#af3895a9c7e54a6ba5014f54ea541ba75)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

## 11.6\_详细说明（Detailed Documentation）

<a id="a9323021c339bc213862aa12aa302cf1b"></a>

### `DTC_ALIGN_VARIABLE`

```c
#define DTC_ALIGN_VARIABLE ( x)
```

展开值（Value）：

```c
__aligned(x)
```

设置变量对齐（Alignment）的属性（Attribute）。

<a id="a7ab61b801ce7972fdfc9c6f00da2df51"></a>

### `DTC_MAX_BLOCK_COUNT`

```c
#define DTC_MAX_BLOCK_COUNT (0x10000)
```

块模式（BLOCK MODE）下可配置的最大传输块数。

<a id="a19425a6e2cc8c0080c61ff61f6ad9e29"></a>

### `DTC_MAX_BLOCK_TRANSFER_LENGTH`

```c
#define DTC_MAX_BLOCK_TRANSFER_LENGTH (0x100)
```

块模式（BLOCK MODE）下每个块的最大传输次数。

<a id="aefd0bae0ca748ccb6719ab0134d9d70b"></a>

### `DTC_MAX_NORMAL_TRANSFER_LENGTH`

```c
#define DTC_MAX_NORMAL_TRANSFER_LENGTH (0x10000)
```

正常模式（NORMAL MODE）下可配置的最大传输次数。

重复模式（REPEAT MODE）下每次重复的最大传输次数。

<a id="a4fd7d0141f9b7f10c39146c4b80242e7"></a>

### `DTC_MAX_REPEAT_TRANSFER_LENGTH`

```c
#define DTC_MAX_REPEAT_TRANSFER_LENGTH (0x100)
```

重复模式（REPEAT MODE）下每次重复的最大传输次数。

块模式（BLOCK MODE）下每个块的最大传输次数。

<a id="a820a787cb1c470dcb7e2a000f1a5908b"></a>

### `DTC_PLACE_IN_SECTION`

```c
#define DTC_PLACE_IN_SECTION ( x)
```

展开值（Value）：

```c
__attribute__((section(x)))                                                                \
__attribute__((__used__))
```

将变量放入指定节（Section）的属性（Attribute）。

<a id="ab1b1d04710eeec628c4b9db47eeaab01"></a>

### `DTC_PRV_ACT_BIT_MASK`

```c
#define DTC_PRV_ACT_BIT_MASK (1 << 15)
```

DTC 活动标志（Active Flag，`DTCSTS.ACT`）的位掩码（Bit Mask）。

<a id="a5e430077b6d5a7d88d241a907eaaa33f"></a>

### `DTC_PRV_MASK_CRAL`

```c
#define DTC_PRV_MASK_CRAL (0xFFU)
```

计数器寄存器 A 低字节掩码（Counter Register A Lower Byte Mask）。

<a id="af371b3881a8624f0cf4ec2a8e3df7dac"></a>

### `DTC_PRV_OFFSET_CRAH`

```c
#define DTC_PRV_OFFSET_CRAH (8U)
```

计数器寄存器 A 高字节偏移量（Counter Register A Upper Byte Offset）。

<a id="af976a02ce499ece17f4878f28e7dbc8b"></a>

### `DTC_PRV_VECT_NR_MASK`

```c
#define DTC_PRV_VECT_NR_MASK (0x00FF)
```

DTC 激活向量编号（DTC-Activating Vector Number）的位掩码。

<a id="a0bf33a92b64e91c91daffdd372fb8321"></a>

### `DTC_SECTION_ATTRIBUTE`

```c
#define DTC_SECTION_ATTRIBUTE DTC_PLACE_IN_SECTION(".dtc_vector_table")
```

数据传输控制器向量表节属性（DTC Vector Table Section Attribute）。

<a id="a998b3e77a5d2fbd41cdc0d1006cc58d5"></a>

### `DTC_VECTOR_TABLE_ENTRIES`

```c
#define DTC_VECTOR_TABLE_ENTRIES (CONFIG_NUM_IRQS)
```

DTC 向量条目数（Number of DTC Vector Entries）。

<a id="a93829fb00a7ef2349279986aee9f4c94"></a>

### `dtc_act_status_t`

```c
typedef enum e_dtc_act_status dtc_act_status_t
```

DTC 激活状态（Activation Status）。

<a id="ae69bf278e293c26a27b5752894ea3678"></a>

### `transfer_addr_mode_t`

```c
typedef enum e_transfer_addr_mode transfer_addr_mode_t
```

传输地址模式（Transfer Address Mode）。

<a id="a1c9f7b59f5fcfeaeb6e528c2b3b067ff"></a>

### `transfer_chain_mode_t`

```c
typedef enum e_transfer_chain_mode transfer_chain_mode_t
```

<a id="a971f4055201125c15f25b4c7ba12d34e"></a>

### `transfer_info_t`

```c
typedef struct st_transfer_info transfer_info_t
```

传输信息（Transfer Information）结构。

<a id="ad550861b5af9e2d116b03ddc440f6c35"></a>

### `transfer_irq_t`

```c
typedef enum e_transfer_irq transfer_irq_t
```

传输中断类型（Transfer Interrupt Type）。

每次传输均产生中断（Interrupt on Each Transfer）。

<a id="aea0db2ddbbc3831666b0bf2bb4cc0fb5"></a>

### `transfer_mode_t`

```c
typedef enum e_transfer_mode transfer_mode_t
```

传输模式。

<a id="aa1b08c5715fd33b689643a82c63301d9"></a>

### `transfer_properties_t`

```c
typedef struct st_transfer_properties transfer_properties_t
```

详细传输属性（Detailed Transfer Properties）。

<a id="af5ab2f4c329bd42eb7893a1aece381f5"></a>

### `transfer_repeat_area_t`

```c
typedef enum e_transfer_repeat_area transfer_repeat_area_t
```

重复传输模式（Repeat Transfer Mode）下重复的区域（Area）。

<a id="ada156bb47034b335a8e57d7cdff02238"></a>

### `transfer_size_t`

```c
typedef enum e_transfer_size transfer_size_t
```

传输数据大小。

<a id="a5888188d6d3123522bd75b08d228b53a"></a>

### `e_dtc_act_status`

```c
enum e_dtc_act_status
```

DTC 激活状态（Activation Status）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `DTC_ACT_IDLE` | 空闲状态（Idle State）。 |
| `DTC_ACT_CONFIGURED` | 已配置状态（Configured State）。 |
| `DTC_ACT_IN_PROGRESS` | 正在进行状态（In-progress State）。 |

<a id="a0ae834acb01772fef5fd38c62486cb72"></a>

### `e_transfer_addr_mode`

```c
enum e_transfer_addr_mode
```

传输地址模式（Transfer Address Mode）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_ADDR_MODE_FIXED` | 固定模式（Fixed Mode）。 |
| `TRANSFER_ADDR_MODE_OFFSET` | 偏移模式（Offset Mode）。 |
| `TRANSFER_ADDR_MODE_INCREMENTED` | 递增模式（Incremented Mode）。 |
| `TRANSFER_ADDR_MODE_DECREMENTED` | 递减模式（Decremented Mode）。 |

<a id="a058dc1dc14c2fc4e1be1352be860fd5d"></a>

### `e_transfer_chain_mode`

```c
enum e_transfer_chain_mode
```

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_CHAIN_MODE_DISABLED` | 链式传输已禁用（Chaining Disabled）。 |
| `TRANSFER_CHAIN_MODE_EACH` | 链式传输已禁用（Chaining Disabled）。 |
| `TRANSFER_CHAIN_MODE_END` | 结束时链接（Chain at End）。 |

<a id="a56fa6d340c574db7be73de060d155b4d"></a>

### `e_transfer_irq`

```c
enum e_transfer_irq
```

传输中断类型（Transfer Interrupt Type）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_IRQ_END` | 传输结束时产生中断（Interrupt at End of Transfer）。 |
| `TRANSFER_IRQ_EACH` | 每次传输均产生中断（Interrupt on Each Transfer）。 |

<a id="af75bb588cec15252fea99d0cf2e4a9f1"></a>

### `e_transfer_mode`

```c
enum e_transfer_mode
```

传输模式。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_MODE_NORMAL` | 正常传输模式（Normal Transfer Mode）。 |
| `TRANSFER_MODE_REPEAT` | 重复传输模式（Repeat Transfer Mode）。 |
| `TRANSFER_MODE_BLOCK` | 块传输模式（Block Transfer Mode）。 |
| `TRANSFER_MODE_REPEAT_BLOCK` | 重复块传输模式（Repeat Block Transfer Mode）。 |

<a id="abbe162d4578a4ab187a1549bcc850ca6"></a>

### `e_transfer_repeat_area`

```c
enum e_transfer_repeat_area
```

重复传输模式（Repeat Transfer Mode）下重复的区域（Area）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_REPEAT_AREA_DESTINATION` | 目标区域重复（Destination Repeats）。 |
| `TRANSFER_REPEAT_AREA_SOURCE` | 源区域重复（Source Repeats）。 |

<a id="a81a8afa6b36f96ad966677d0efaefce0"></a>

### `e_transfer_size`

```c
enum e_transfer_size
```

传输数据大小。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `TRANSFER_SIZE_1_BYTE` | 1 字节传输（1-byte Transfer）。 |
| `TRANSFER_SIZE_2_BYTE` | 2 字节传输（2-byte Transfer）。 |
| `TRANSFER_SIZE_4_BYTE` | 4 字节传输（4-byte Transfer）。 |

<a id="a4c7e963fd2e8a807ed6f1c1c773bc5ef"></a>

### `dtc_renesas_rx_configuration()`

```c
int dtc_renesas_rx_configuration ( const struct device * dev, uint8_t activation_irq, transfer_info_t * p_info )
```

配置 `p_info` 状态，并将 `p_info` 写入 DTC 向量表（Vector Table）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `activation_irq` | 激活源（Activation Source）。 |
| `p_info` | 传输信息（Transfer Info）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |

<a id="aba28c80e24d2d011f0bb389feffa3da6"></a>

### `dtc_renesas_rx_disable_transfer()`

```c
int dtc_renesas_rx_disable_transfer ( uint8_t activation_irq)
```

在中断控制单元（ICU）中，为此激活源（Activation Source）禁用传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `activation_irq` | 激活源（Activation Source）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |

<a id="ac0840ee89a1688a5212d34c5699640dc"></a>

### `dtc_renesas_rx_enable_transfer()`

```c
int dtc_renesas_rx_enable_transfer ( uint8_t activation_irq)
```

在中断控制单元（ICU）中，为此激活源（Activation Source）启用传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `activation_irq` | 激活源（Activation Source）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |

<a id="af833ddfd2351d577c540f7daa1549717"></a>

### `dtc_renesas_rx_get_transfer_status()`

```c
void dtc_renesas_rx_get_transfer_status ( const struct device * dev, struct dtc_transfer_status * status )
```

获取 DTC 模块的传输状态（Transfer Status），并存入 `status` 指针所指位置。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `status` | DTC 状态（Status）。 |

<a id="aa477baa206c2f80a40d473b648596b61"></a>

### `dtc_renesas_rx_info_get()`

```c
int dtc_renesas_rx_info_get ( const struct device * dev, uint8_t activation_irq, transfer_properties_t *const p_properties )
```

获取此次传输的信息（Transfer Information），并存入 `p_properties`。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `activation_irq` | 激活源中断请求编号（Activation Source IRQ Number）。 |
| `p_properties` | 指向结构体的指针，用于接收驱动特定传输属性（Driver-specific Transfer Properties）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |

<a id="a72e8a62b215ba60e4f99bca338526e4f"></a>

### `dtc_renesas_rx_off()`

```c
int dtc_renesas_rx_off ( const struct device * dev)
```

关闭 DTC 模块（Module）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="aeba55fc712a1caf61abcf5c7f30e7654"></a>

### `dtc_renesas_rx_on()`

```c
int dtc_renesas_rx_on ( const struct device * dev)
```

开启 DTC 模块（Module）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |

<a id="ae6c70fe832e1d8873dd4240d90fe8240"></a>

### `dtc_renesas_rx_reset_transfer()`

```c
int dtc_renesas_rx_reset_transfer ( const struct device * dev, uint8_t activation_irq, void const * p_src, void * p_dest, uint16_t const num_transfers )
```

重置此激活源（Activation Source）上的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `activation_irq` | 激活源中断请求编号（Activation Source IRQ Number）。 |
| `p_src` | 指向传输源地址（Source Address）的指针。 |
| `p_dest` | 指向传输目标地址（Destination Address）的指针。 |
| `num_transfers` | 要传输的数据单元数量（Number of Data Units）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |

<a id="a1280f41f5ad8d4b5beb79a87f5724363"></a>

### `dtc_renesas_rx_start_transfer()`

```c
int dtc_renesas_rx_start_transfer ( const struct device * dev, uint8_t activation_irq )
```

启动此激活源（Activation Source）上的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `activation_irq` | 激活源（Activation Source）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |
| `-EACCES` | DTC 向量表（Vector Table）中的此激活源（Activation Source）尚未配置时。 |

<a id="aad7601ea771de91d82a213a528f97cb3"></a>

### `dtc_renesas_rx_stop_transfer()`

```c
int dtc_renesas_rx_stop_transfer ( const struct device * dev, uint8_t activation_irq )
```

停止此激活源（Activation Source）上的传输。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `dev` | DTC 设备实例（Device Instance）。 |
| `activation_irq` | 激活源（Activation Source）。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时返回。 |
| `-EINVAL` | 激活源（Activation Source）无效时。 |
| `-EACCES` | DTC 向量表（Vector Table）中的此激活源（Activation Source）尚未配置时。 |

<a id="af3895a9c7e54a6ba5014f54ea541ba75"></a>

### `is_valid_activation_irq()`

```c
ALWAYS_INLINE bool is_valid_activation_irq ( uint8_t activation_irq)
```

声明属性：`static`。

DTC 向量条目数（Number of DTC Vector Entries；原文前导字符为 `<`）。


## 11.7\_原页交叉引用（Cross References）

- [zephyr/drivers/gpio.h](../gpio_driver_reference/P002_GPIO驱动头文件源码.md)
- [查看此文件的源码。](../api_source_reference/P711_renesas_rx_dtc.h_源码浏览.md)
- [st_transfer_info](../device_power_control_model_reference/P090_st_transfer_info_结构体.md)
- [st_transfer_properties](../device_power_control_model_reference/P091_st_transfer_properties_结构体.md)
- [dtc_transfer_status](../device_power_control_model_reference/P006_dtc_transfer_status_结构体.md)
- [device](../device_reference/P002_设备对象结构.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="a5888188d6d3123522bd75b08d228b53aaf4fc44a34b910cbb4bcac8703e4b7d30"></a>
<a id="a5888188d6d3123522bd75b08d228b53aab1bb6f41ed6ce9f46caa06ba7ef158c6"></a>
<a id="a5888188d6d3123522bd75b08d228b53aa4a1afc72aa44c347439cb8557e930d74"></a>
<a id="a0ae834acb01772fef5fd38c62486cb72abf18f9b3701e9e91f44055ee47d0ca47"></a>
<a id="a0ae834acb01772fef5fd38c62486cb72ab8b3f8ce28fb6f7a57a1b87db0d612c2"></a>
<a id="a0ae834acb01772fef5fd38c62486cb72a7665741e25c4cc78fd24745efbd2eaad"></a>
<a id="a0ae834acb01772fef5fd38c62486cb72a56a87e1587844119831414f3d5e6d761"></a>
<a id="a058dc1dc14c2fc4e1be1352be860fd5dae974453c306b4959252905e362d75067"></a>
<a id="a058dc1dc14c2fc4e1be1352be860fd5dadab837d29a543149d35ed2fd28d8e4e8"></a>
<a id="a058dc1dc14c2fc4e1be1352be860fd5dab853bdecc90c476b995644c273e0ee75"></a>
<a id="a56fa6d340c574db7be73de060d155b4dada378ad830e44cc0c25d4fe2413e11de"></a>
<a id="a56fa6d340c574db7be73de060d155b4da0929782b61686db69e12b3cb18175b35"></a>
<a id="af75bb588cec15252fea99d0cf2e4a9f1ada90d8a89f98ff82475383b14141b08d"></a>
<a id="af75bb588cec15252fea99d0cf2e4a9f1a607c41bfd08797c08a5ee9bd4dfb9c8b"></a>
<a id="af75bb588cec15252fea99d0cf2e4a9f1aa4f65de2d9454af406f60172ff858d55"></a>
<a id="af75bb588cec15252fea99d0cf2e4a9f1afb43c6e62b61f0dbb9a5bcd5575e79e2"></a>
<a id="abbe162d4578a4ab187a1549bcc850ca6a77aeeab30b003de23742e40a57f19239"></a>
<a id="abbe162d4578a4ab187a1549bcc850ca6a2002ef7bbc49f7c9ebfac1618ba3c391"></a>
<a id="a81a8afa6b36f96ad966677d0efaefce0accfeb24892ec24e42ccf14e4d4896c21"></a>
<a id="a81a8afa6b36f96ad966677d0efaefce0a8b6b33a085b51ea2eeed1ef119de562f"></a>
<a id="a81a8afa6b36f96ad966677d0efaefce0a18482bfa86e737cde78042be4db54412"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P010_zephyr__drivers__pcie__endpoint__pcie_ep.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P012_zephyr__usb__class__usb_hub.h_文件参考.md)
