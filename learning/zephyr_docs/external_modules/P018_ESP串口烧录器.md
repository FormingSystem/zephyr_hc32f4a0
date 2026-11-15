---
id: learning.zephyr-docs.external_modules.page-18
title: ESP串口烧录器
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/esp-serial-flasher.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="esp-serial-flasher"></a>
<a id="external-module-esp-serial-flasher"></a>

# 第18章\_ESP串口烧录器

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/esp-serial-flasher.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 18.1\_简介（Introduction）

ESP Serial Flasher是Espressif Systems开发维护的可移植C库，使运行嵌入式操作系统的主控微控制器能够为Espressif片上系统（System on Chip，SoC，包括ESP8266、ESP32系列）编程并与其交互。它通过统一API提供闪存操作、随机存取存储器（Random Access Memory，RAM）下载与执行、设备管理，支持通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART）、USB通信设备类抽象控制模型（USB CDC ACM）、串行外设接口（Serial Peripheral Interface，SPI）和SD输入输出（SDIO）等传输接口。

对于需要与Espressif目标交互或写入固件、又不希望依赖PC或Python运行时的Zephyr应用，该模块很有用。功能类似esptool，但针对资源受限系统优化，适合生产烧录工具、引导加载程序（Bootloader）及固件更新机制。

<a id="id2"></a>

所支持的Espressif SoC清单及更多说明见 [项目仓库](https://github.com/espressif/esp-serial-flasher)。库采用Apache License 2.0。

<a id="usage-with-zephyr"></a>

## 18.2\_在Zephyr中使用（Usage with Zephyr）

在 `west.yml` 添加项目，或新建 `zephyr/submanifests/esp-serial-flasher.yaml` 子清单，加入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: esp-serial-flasher
      url: https://github.com/espressif/esp-serial-flasher
      revision: master
      path: modules/esp-serial-flasher # adjust path or leave blank for west workspace root directory
```

> 译注——路径注释：原注释允许调整path，或省略它以使用west工作区根下的项目目录；这里仍应按west项目路径规则解析，不把库直接混入任意源码目录。

加入模块后，在应用代码包含主头文件：

```c
#include <esp_loader.h>
```

Zephyr集成提供 `espressif,esp-loader` 设备树绑定，应用设备树至少要定义一个实例，再通过chosen属性 `zephyr,esp-loader` 选择活动实例。驱动处理UART通信以及启动／复位引脚的通用输入输出（General-Purpose Input/Output，GPIO），提供闪存操作、连接设备和管理目标的高级API。

可以把目标固件镜像嵌入主控应用。将二进制文件放入 `target-firmware/`，在 `target-firmware/images.csv` 逐行记录 `<filename>;<offset>`，每行一个镜像，偏移为不带 `0x` 前缀的十六进制，例如 `app.bin;10000`。

在应用 `CMakeLists.txt` 包含Zephyr示例提供的 `bin_images_sections.cmake` 后，`create_resources()` 会将这些文件转换为C数组。在 `prj.conf` 设置 `CONFIG_ESP_SERIAL_FLASHER=y` 启用驱动。images.csv、CMake及设备树设置见项目仓库的 `examples/zephyr_example`。

若要通过Shell交互，构建同一示例并启用 `CONFIG_ESP_SERIAL_FLASHER_SHELL=y`。其 `esf` 命令组支持连接ESP目标、读写闪存、检测闪存大小、擦除闪存及读写寄存器。

<a id="reference"></a>

## 18.3\_参考资料（Reference）

<a id="id5"></a>

- [ESP Serial Flasher组件注册页](https://components.espressif.com/components/espressif/esp-serial-flasher)。
<a id="id7"></a>

- [Zephyr模块文档](https://docs.zephyrproject.org/latest/develop/modules.html)。


<a id="id3"></a>

<a id="id1"></a>

1. [源码仓库](https://github.com/espressif/esp-serial-flasher)。

<a id="id4"></a>

2. [组件入口](https://components.espressif.com/components/espressif/esp-serial-flasher)。

<a id="id6"></a>

3. [Zephyr模块说明](https://docs.zephyrproject.org/latest/develop/modules.html)。


对应官方文档源码：[doc/develop/manifest/external/esp-serial-flasher.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/esp-serial-flasher.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/esp-serial-flasher.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：emlearn机器学习](P017_emlearn机器学习.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：ExecuTorch](P019_ExecuTorch.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P017_emlearn机器学习.md) · [返回大纲](大纲.md) · [下一章](P019_ExecuTorch.md)

</details>

<!-- reading-navigation:end -->
