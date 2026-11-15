---
id: learning.zephyr-docs.storage.flash-map
title: Flash分区映射
kind: reference
status: maintained
domains: [zephyr, storage]
source_url: https://docs.zephyrproject.org/latest/services/storage/flash_map/flash_map.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="flash-map-api"></a>

# 第1章\_Flash分区映射

原文：[Flash map](https://docs.zephyrproject.org/latest/services/storage/flash_map/flash_map.html)。读取日期：2026-10-12，`latest`。

`<zephyr/storage/flash_map.h>` 提供通过 `flash_area` 结构访问设备 Flash **分区（Partition）**信息的 **应用程序编程接口（Application Programming Interface，API）**。每个 `flash_area` 描述一个分区；Flash map 保存预先定义的区域，可用全局唯一的数字 ID 访问。映射由 **设备树源文件（Devicetree Source，DTS）** 文件中的 `fixed-partitions` 和 `zephyr,mapped-partition` compatible 条目生成，应用也可以在运行时创建自己的 `flash_area` 对象。本文将单个这样的分区实体称为 Flash 区域（flash area）。

## 1.1\_区域对象与访问接口

`flash_area` 包含指向 `device` 的指针，可用它通过[Flash API](../hardware/P012_Flash闪存.md)直接访问区域所在设备。每个区域由所在设备、相对于设备起点的偏移、区域大小描述；另有标识符供 `flash_area_open()` 在映射中查找区域。

`flash_area_read()`、`flash_area_write()` 等函数基本上是 Flash API 的封装，增加偏移和长度检查，把操作限制在预定义区域内。

大多数接口需要指向区域对象的指针，取得方式有两种：调用 `flash_area_open()`；或者自行定义 `flash_area` 对象，提供有效设备指针、区域在设备内的偏移和大小。

`flash_area_open()` 使用数字 ID 查找预定义对象，找到后返回其指针。对于设备树中固定分区或映射分区的节点标签，可以用 `PARTITION_ID()` 取得该 ID。

## 1.2\_与设备树的关系

Flash map 使用[设备树 API](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-api)生成的数据，尤其是[固定与映射 Flash 分区](https://docs.zephyrproject.org/latest/build/dts/api/api.html#devicetree-flash-api)信息。Zephyr 还约定了通过 MCUboot 进行[设备固件升级](https://docs.zephyrproject.org/latest/services/device_mgmt/dfu.html#dfu)时的分区名称，以及[文件系统](P007_文件系统.md)或其他[非易失存储](P012_存储服务入口.md)使用的分区。

下面片段同时为 MCUboot 和数据存储定义固定分区。为清晰起见，原文省略了部分细节：

```dts
/ {
	soc {
		flashctrl: flash-controller@deadbeef {
			flash0: flash@0 {
				compatible = "soc-nv-flash";
				reg = <0x0 0x100000>;

				partitions {
					compatible = "fixed-partitions";
					#address-cells = <0x1>;
					#size-cells = <0x1>;

					boot_partition: partition@0 {
						reg = <0x0 0x10000>;
						read-only;
					};

					storage_partition: partition@1e000 {
						reg = <0x1e000 0x2000>;
					};

					slot0_partition: partition@20000 {
						reg = <0x20000 0x60000>;
					};

					slot1_partition: partition@80000 {
						reg = <0x80000 0x60000>;
					};

					scratch_partition: partition@e0000 {
						reg = <0xe0000 0x20000>;
					};
				};
			};
		};
	};
};
```

分区偏移必须相对于其所属 Flash 存储器的起始地址。`boot_partition`、`slot0_partition`、`slot1_partition`、`scratch_partition` 是 MCUboot 使用的节点标签，但并非所有 MCUboot 配置都需要定义全部这些分区；具体见 [MCUboot 文档](https://docs.mcuboot.com)。`storage_partition` 用于文件系统或其他非易失存储 API。

将节点标签传给 `PARTITION_ID()` 即可获得数字区域 ID，例如 `PARTITION_ID(slot0_partition)`。所有 `PARTITION_*` 宏均以 DTS 节点标签作为分区标识。

如果分区已在设备树中定义，取得大小、偏移或设备并不一定要先打开区域。可分别使用 `PARTITION_SIZE()`、`PARTITION_OFFSET()`、`PARTITION_DEVICE()`，直接从节点定义取得信息。例如，`PARTITION_OFFSET(storage_partition)` 返回存储分区的偏移。

> 译注：原文这一段将打开函数写成 `flash_map_open()`，与同页其余说明及头文件中的 `flash_area_open()` 不一致，应使用后者。上例 `flash-controller@deadbeef` 是示意地址，不是 HC32 控制器地址；分区偏移也不能未经核对就用于实际擦写。

通过节点标签和 `flash_area_open()` 取得对象指针的示例如下：

```c
const struct flash_area *my_area;
int err = flash_area_open(PARTITION_ID(slot0_partition), &my_area);

if (err != 0) {
     handle_the_error(err);
} else {
     flash_area_read(my_area, ...);
}
```

> 译注：这是保留省略号和示意错误处理函数的片段，不是完整可编译应用。实际应用还应检查读写返回值。

## 1.3\_API与相关示例

接口见 [Flash 区域 API](https://docs.zephyrproject.org/latest/doxygen/html/group__flash__area__api.html)，结构见 [flash_area](https://docs.zephyrproject.org/latest/doxygen/html/structflash__area.html)。相关示例：

- [LittleFS 文件系统](P085_LittleFS文件系统示例.md)：通过文件系统 API 使用 LittleFS。
- [nRF SoC 内部存储](../driver_samples/P054_nRF内部存储示例.md#soc-flash-nrf)：通过 Flash API 操作 **片上系统（System on Chip，SoC）** Flash。

<!-- reading-navigation:start -->

**主线阅读**

[本模块主线目录](../reading/storage.md) · [全部主线](../reading/README.md) · [下一篇：非易失存储NVS](P002_非易失存储NVS.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[前置阅读：Flash驱动](../hardware/P012_Flash闪存.md) · [下一章：非易失存储NVS](P002_非易失存储NVS.md) · [返回大纲](大纲.md)

</details>

<!-- reading-navigation:end -->
