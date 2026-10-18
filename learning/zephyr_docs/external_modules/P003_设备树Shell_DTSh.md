---
id: learning.zephyr-docs.external_modules.page-3
title: 设备树Shell_DTSh
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/dtsh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="dtsh"></a>
<a id="external-module-dtsh"></a>

# 第3章\_设备树Shell\_DTSh

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/dtsh.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 3.1\_简介（Introduction）

[DTSh](https://dottspina.github.io/dtsh/handbook.html) 是交互式设备树源文件（Devicetree Source，DTS）查看工具，提供类似Shell的命令行界面（Command-Line Interface，CLI），可以：

- 方便地浏览和可视化设备树（Devicetree）。
- 根据总线协议、绑定（Binding）、生成的中断请求（Interrupt Request，IRQ）、内存大小或sensor、PWM等关键词寻找节点；PWM为脉宽调制（Pulse-Width Modulation）。
- 将命令输出重定向到文本、HTML或SVG文件，记录硬件配置或做笔记；HTML为超文本标记语言，SVG为可缩放矢量图形。
- 使用上下文自动补全、命令历史、语义高亮及用户配置文件。
- 通过脚本运行，即使用批处理模式（Batch Mode）。

此Zephyr模块把DTSh作为west扩展（Extension）加入工作区。

<a id="usage-with-zephyr"></a>

## 3.2\_在Zephyr中使用（Usage with Zephyr）

安装DTSh模块时，需要定义自己的清单文件，或通过子清单引入。

例如，沿用[Zephyr入门指南](https://docs.zephyrproject.org/latest/develop/getting_started/)的目录布局，新建 `zephyrproject/zephyr/submanifests/dtsh.yaml`，内容如下：

```yaml
manifest:
  projects:
    - name: dtsh
      url: https://github.com/dottspina/dtsh.git
      revision: zephyr
      path: modules/tools/dtsh
      west-commands: scripts/west-commands.yml
```

然后更新工作区并安装DTSh依赖：

```bash
west update dtsh
west packages -m dtsh pip --install
```

**注意：**`west update dtsh` 会获取[DTSh项目](https://github.com/dottspina/dtsh)的全部标签（Tag）。这些标签不指向此Zephyr模块的版本，在这里应忽略它们。

<a id="the-west-command"></a>

## 3.3\_west命令（The West command）

安装完成后，该项目／模块应提供 `west dtsh` 命令。原文交互示例如下：

```text
$ west build
$ west dtsh
dtsh (0.2.5-zephyr): Shell-like interface with Devicetree
How to exit: q, or quit, or exit, or press Ctrl-D

/
> cd &flash_controller

/soc/flash-controller@4001e000
> find -E --also-known-as (image|storage).* --format NKd -T
                             Also Known As               Description
                             ───────────────────────────────────────────────────────────────────────────────────
flash-controller@4001e000    flash_controller            Nordic NVMC (Non-Volatile Memory Controller)
└── flash@0                  flash0                      Flash node
    └── partitions                                       This binding is used to describe fixed partitions…
        ├── partition@c000   image-0, slot0_partition    Each child node of the fixed-partitions node represents…
        ├── partition@82000  image-1, slot1_partition    Each child node of the fixed-partitions node represents…
        └── partition@f8000  storage, storage_partition  Each child node of the fixed-partitions node represents…
```

> 译注——示例界面：`$` 与 `>` 是主机Shell及DTSh提示符；How to exit列出q、quit、exit或Ctrl-D等退出方式。`cd &flash_controller` 按节点标签进入闪存控制器；后续find命令查找别名匹配image或storage的节点。Also Known As为节点别名，Description为说明；NVMC是非易失性存储器控制器（Non-Volatile Memory Controller），Flash node为闪存节点，fixed partitions为固定分区。原树中的Nordic节点、地址、image-0、image-1和storage属于示例设备树，不要求读者工程具有相同布局；以 `/soc` 开头的是树内节点路径。

完整west命令用法可运行 `west dtsh -h` 查看。

**注意：**推荐安装到默认相对位置 `modules/tools/dtsh`。如果使用其他位置，应在运行 `west dtsh` 之前设置 `ZEPHYR_BASE` 环境变量。

<a id="reference"></a>

## 3.4\_参考资料（Reference）

- [DTSh项目](https://github.com/dottspina/dtsh)。
- [DTSh手册](https://dottspina.github.io/dtsh/handbook.html)。
- [DTSh的Zephyr模块分支](https://github.com/dottspina/dtsh/tree/zephyr)。


对应官方文档源码：[doc/develop/manifest/external/dtsh.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/dtsh.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/dtsh.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CANopenNode协议栈](P002_CANopenNode协议栈.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：LZ4压缩](P004_LZ4压缩.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P002_CANopenNode协议栈.md) · [返回大纲](大纲.md) · [下一章](P004_LZ4压缩.md)

</details>

<!-- reading-navigation:end -->
