---
id: learning.zephyr-docs.boards-microchip.page-1
title: Flashing with Microchip MPLAB IPE
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/microchip/common/microchip-mplab-ipe-flashing.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="flashing-with-microchip-mplab-ipe"></a>

<a id="microchip-mplab-ipe-flashing"></a>

# 第1章\_使用Microchip MPLAB IPE烧录（Flashing）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/microchip/common/microchip-mplab-ipe-flashing.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Microchip器件可通过MPLAB集成编程环境（IPE / Integrated Programming Environment）编程及烧录。MPLAB IPE是独立编程工具，支持Microchip调试探针及板载调试器。它提供ipecmd命令行工具，Zephyr通过MPLAB IPE运行工具（Runner）将其集成到west flash。

本节介绍安装和配置MPLAB IPE的方法，用于将Zephyr应用烧录到Microchip目标开发板。

<a id="overview"></a>

## 概述（Overview）

MPLAB IPE为Microchip微控制器提供可用于生产的编程接口。结合Zephyr使用时，west flash调用ipecmd，将已构建固件镜像写入目标器件。

烧录过程使用Zephyr构建系统生成的Intel HEX文件：

```text
build/zephyr/zephyr.hex
```

<a id="supported-debug-tools"></a>

## 受支持调试工具（Supported Debug Tools）

MPLAB IPE支持以下调试／编程工具：


- MPLAB PICkit调试器／编程器
- MPLAB SNAP调试器／编程器
- MPLAB ICD调试器
- Microchip开发板上的PKoB、PKoB4、EDBG等板载调试器（On-Board Debuggers）

具体支持列表取决于所安装的MPLAB IPE版本及目标器件系列。

<a id="requirements"></a>

## 前置要求（Requirements）

使用MPLAB IPE烧录之前，安装并配置以下内容：


- [MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)，其中包含MPLAB IPE
- 所需Microchip器件包（Device Packs），可自动安装或通过MPLAB IPE软件包管理器（Pack Manager）安装
- 受支持的Microchip调试探针或板载调试器
- 为目标开发板构建的Zephyr固件镜像

<a id="installing-mplab-ipe"></a>

## 安装MPLAB IPE（Installing）

MPLAB IPE包含在MPLAB X IDE安装器中，安装步骤如下：


1. 从Microchip Technology网站下载[MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)安装器。
2. 解压下载的软件包并运行安装器。

  Linux下：

  ```text
  chmod +x MPLABX-vX.XX-linux-installer.sh
  sudo ./MPLABX-vX.XX-linux-installer.sh
  ```

  Windows下运行.exe安装器。
3. 安装过程中，确保从可用组件中选中MPLAB IPE。
4. 安装后确认能够访问ipecmd可执行文件。

  Linux下，ipecmd通常位于：

  ```text
  /opt/microchip/mplabx/vX.XX/mplab_platform/bin/ipecmd.sh
  ```

  Windows下：

  ```text
  C:\Program Files\Microchip\MPLABX\vX.XX\mplab_platform\bin\ipecmd.exe
  ```
5. 将ipecmd所在目录加入系统PATH。

<a id="verifying-the-installation"></a>

## 验证安装（Verifying the Installation）

运行以下命令验证MPLAB IPE安装，正常时会显示帮助菜单。

Linux下：

```text
ipecmd.sh -?
```

Windows下：

```text
ipecmd.exe -?
```

<a id="building-a-zephyr-application"></a>

## 构建Zephyr应用（Building an Application）

烧录前先构建Zephyr应用。例如，构建Blinky示例：

```text
# From the root of the zephyr repository
west build -b <board> samples/basic/blinky
```

构建成功后，HEX文件位于：

```text
build/zephyr/zephyr.hex
```

<a id="connecting-the-board"></a>

## 连接开发板（Connecting the Board）

将目标开发板的调试／编程接口连接到主机：


1. 使用USB线缆，将开发板调试USB端口连接到主机。
2. 该连接通常既为开发板供电，也连接PKoB或PKoB4等板载调试器。
3. 若使用PICkit、SNAP、ICD等外部调试探针，将其连接到开发板调试排针，再通过USB连接主机。
4. 确认开发板已供电。部分开发板除调试USB外，还需要单独供电。

注意（Note）

各开发板调试USB端口及连接器名称可能不同，具体连接方式见相应开发板文档。

<a id="flashing-with-west-flash"></a>

## 通过west flash烧录

应用构建完成且开发板已连接后，执行以下命令烧录：

```text
west flash
```

Zephyr构建系统会用适合目标器件及已连接工具的参数调用ipecmd。

若需显式指定运行工具（Runner）：

```text
west flash -r mplab_ipe
```

<a id="troubleshooting"></a>

## 故障排查（Troubleshooting）

<a id="ipecmd-is-not-found"></a>

### 找不到ipecmd（Not Found）

若west flash报告找不到ipecmd：


- 确认已安装MPLAB X IDE／MPLAB IPE。
- 确认ipecmd所在目录已加入系统PATH。

<a id="tool-is-not-detected"></a>

### 未检测到工具（Tool Is Not Detected）

若未检测到编程工具：


- 检查探针／开发板与主机之间的USB连接。
- 确认MPLAB X IDE、MPLAB IPE图形界面等其他应用没有占用调试工具。
- 确认探针固件为最新版本，必要时用MPLAB IPE图形界面更新。
- 断开并重新连接探针。
- Linux下应确认已安装Microchip工具所需udev规则。

<a id="device-is-not-recognized"></a>

### 无法识别器件（Device Is Not Recognized）

若无法识别目标器件：


- 确认MPLAB IPE已安装正确器件包。
- 打开MPLAB IPE图形界面，通过Pack Manager安装或更新软件包。
- 确认目标板已供电，调试连接牢靠。
- 确认目标器件与Zephyr开发板定义中配置的器件一致。

<a id="additional-resources"></a>

## 其他资源（Additional Resources）

更多信息见：


- [MPLAB X IDE](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)，包含MPLAB IPE
- [MPLAB IPE用户指南（User Guide）](https://ww1.microchip.com/downloads/aemDocuments/documents/DEV/ProductDocuments/UserGuides/MPLAB_IPE_Integrated_Programming_Environment_Users_Guide_50002227.pdf)

## 译注

MPLAB IPE烧录使用构建生成的HEX文件。代码中的系统安装目录属于官方工具默认路径模板，不含本仓库在作者计算机上的位置。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [mplab-x-ide](https://www.microchip.com/en-us/tools-resources/develop/mplab-x-ide)：HTTP Error 403: Forbidden。

---

[返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P002_Microchip_MPLAB_VS_Code_Debugging.md)
