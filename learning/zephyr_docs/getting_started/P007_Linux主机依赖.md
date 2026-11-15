---
id: learning.zephyr-official-intro.linux
title: Linux 主机依赖
kind: engineering
status: maintained
domains: [zephyr, documentation]
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 本文件为中文翻译；章节编号、导航和明确标出的译注为本地新增。 -->

# 第7章\_Linux主机依赖

原文：[Install Linux Host Dependencies](https://docs.zephyrproject.org/latest/develop/getting_started/installation_linux.html)。译文基线：2026-10-12 的 `latest` 页面。

本页提供 Ubuntu、Fedora、Clear Linux 和 Arch Linux 的说明。对于非滚动发行版，包管理器提供的软件可能不满足全部版本需求；遇到这种情况，按后面的补充说明从其他来源取得软件。

> 原文说明：如果处于企业防火墙之后，可能需要先配置访问互联网的代理。部分工具读取 `http_proxy`、`https_proxy` 环境变量，另一些工具使用各自配置文件，尤其是 apt 和 Git。

> 译注：本页按来源保留各发行版和历史命令。它是平台参考页，不是要求执行所有分支；其中 CMake 3.21.1 示例与同批入门指南的最低版本 3.28.0 已冲突，相关位置明确标注，不能直接用于搭建最新环境。

## 7.1\_更新操作系统

确保主机系统已经更新。在对应发行版的 Linux 终端中，只执行匹配的分支。

Ubuntu：

```bash
sudo apt-get update
sudo apt-get upgrade
```

Fedora：

```bash
sudo dnf upgrade
```

Clear Linux：

```bash
sudo swupd update
```

Arch Linux：

```bash
sudo pacman -Syu
```

## 7.2\_安装所需工具与依赖

下列说明同时安装 Ninja 与 Make；实际上只需要其中一个。

### 7.2.1\_Ubuntu

```bash
sudo apt-get install --no-install-recommends git cmake ninja-build gperf \
  ccache dfu-util device-tree-compiler wget \
  python3-dev python3-pip python3-setuptools python3-tk python3-wheel xz-utils file \
  make gcc gcc-multilib g++-multilib libsdl2-dev libmagic1
```

> 译注：这里保留补充页的包列表；前章 Ubuntu 24.04 主线额外明确了 `python3-venv`，并提示 ARM64 可能需要去掉 multilib 包。若按前章创建虚拟环境，应遵循前章完整列表，不用本页的旧列表覆盖它。

### 7.2.2\_Fedora

```bash
sudo dnf group install development-tools c-development
sudo dnf install cmake ninja-build gperf dfu-util dtc wget which \
  python3-pip python3-tkinter xz file python3-devel SDL2-devel \
  libusb1-devel
```

### 7.2.3\_Clear Linux

```bash
sudo swupd bundle-add c-basic dev-utils dfu-util dtc \
  os-core-dev python-basic python3-basic python3-tcl
```

Clear Linux 侧重本机性能和安全，而非交叉编译。因此，它默认向所有用户的环境导出一组编译器和链接器标志，这些标志会导致 Zephyr 的 CMake 构建系统警告或失败。

要清除其中的 C/C++ 标志，原文要求以 root 身份执行下列命令，然后退出登录并重新登录：

```bash
echo 'unset CFLAGS CXXFLAGS' >> /etc/profile.d/unset_cflags.sh
```

此命令会为系统上的所有用户取消这些 C/C++ 标志。每个 Linux 发行版的 Bash 初始化文件相互加载关系都不同，较为复杂且可能演变，Clear Linux 也不例外。需要更灵活的方案时，可从 `/usr/share/defaults/etc/profile` 中的逻辑入手。

> 译注：该发行版分支按官方页面保留，不代表本次重新验证了发行版维护状态或软件仓库可用性。

### 7.2.4\_Arch Linux

```bash
sudo pacman -S git cmake ninja gperf ccache dfu-util dtc wget \
    python-pip python-setuptools python-wheel tk xz file make which
```

## 7.3\_检查与更新主要工具

包管理器执行成功后，仍需核对实际找到的版本。最低要求参见[入门指南](P002_入门指南.md#install-dependencies)。

### 7.3.1\_CMake

Zephyr 要求较新的 CMake。先运行 `cmake --version` 检查。旧版本可以通过以下方式更新：

**方式一：Ubuntu 的 Kitware 软件源。** 按 [Kitware 第三方 apt 仓库](https://apt.kitware.com/)说明添加软件源，随后使用 apt 安装更新版本。

**方式二：从 CMake 项目站点下载打包的安装程序。** 这不会卸载已有版本。原文示例如下：

> 译注：下列两组 `3.21.1` 命令是 **过时的原文示例，仅供对照，不应作为当前安装步骤执行**。该版本低于当前入门指南要求的 3.28.0。实际选包请从 CMake 官方下载页选择满足当前 Zephyr 版本要求的版本和主机架构。

```bash
cd ~
wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
chmod +x cmake-3.21.1-Linux-x86_64.sh
sudo ./cmake-3.21.1-Linux-x86_64.sh --skip-license --prefix=/usr/local
hash -r
```

如果安装脚本将 CMake 放到了 `PATH` 中的新位置，可能需要 `hash -r` 清除 shell 缓存的命令位置。

**方式三：使用官方预构建程序。** 到 [CMake Downloads](https://cmake.org/download/) 获取。原文另给出将 3.21.1 安装到 `~/bin/cmake` 的示例，同样属于上述过时示例：

```bash
mkdir $HOME/bin/cmake && cd $HOME/bin/cmake
wget https://github.com/Kitware/CMake/releases/download/v3.21.1/cmake-3.21.1-Linux-x86_64.sh
yes | sh cmake-3.21.1-Linux-x86_64.sh | cat
echo "export PATH=$PWD/cmake-3.21.1-Linux-x86_64/bin:\$PATH" >> $HOME/.zephyrrc
```

**方式四：使用 pip3。** 原文命令为：

```bash
pip3 install --user cmake
```

这不会卸载旧 CMake，新版本安装到 `~/.local/bin`，因此需要把该目录加入 `PATH`。另见[Python 与 pip](P003_入门之后.md#python-and-pip)。

> 译注：此命令属于用户级安装分支，不应附加到已激活的虚拟环境步骤中；若系统报告受外部管理的 Python 环境错误，应回到虚拟环境或发行版支持的安装方式。

**方式五：检查发行版测试版或不稳定版的软件包仓库。** 其中可能有更新包。

**方式六：Ubuntu 使用 snap。** 原文给出的命令为：

```bash
sudo snap install cmake
```

更新之后，再次运行 `cmake --version`，确认终端找到的是新版本。也可考虑卸载包管理器提供的旧版本以避免冲突；`whereis cmake` 可用于寻找其他已安装版本。

### 7.3.2\_设备树编译器

需要较新的设备树编译器（Device Tree Compiler，DTC）。运行 `dtc --version` 检查；若版本太旧，可以从源码构建较新版本，或安装 **软件开发工具包（Software Development Kit，SDK）** 并使用其附带的版本。

### 7.3.3\_Python

需要较新的 Python 3。运行 `python3 --version` 检查。

版本过旧时，可以从源码构建较新 Python，或使用发行版包管理器提供的回移版本。建议用虚拟环境隔离这一 Python 环境，以免干扰系统 Python。

## 7.4\_安装Zephyr SDK

Zephyr SDK 包含各受支持架构的工具链，以及定制的 QEMU、OpenOCD 等主机工具。

强烈建议使用 SDK，在一些场景下它甚至是必需的，例如某些架构的 QEMU 测试。

安装步骤见 [Zephyr SDK 安装指南的 Linux 分支](https://docs.zephyrproject.org/latest/develop/toolchains/zephyr_sdk.html)。

## 7.5\_不使用SDK工具链构建

SDK 为方便使用而提供，包含 Zephyr 各目标架构的工具链；用它构建应用或运行测试时，无须额外指定相关工具标志。除了交叉编译器，它还提供预构建主机工具。

也可以使用[工具链文档](https://docs.zephyrproject.org/latest/develop/toolchains/index.html)中列出的其他工具链，替代 SDK 中的工具链。

如果想把 SDK 的预构建主机工具与其他来源的工具链组合使用，必须将 `ZEPHYR_SDK_INSTALL_DIR` 设为 SDK 安装目录。若不使用 SDK 的预构建主机工具，则必须取消该环境变量：

```bash
unset ZEPHYR_SDK_INSTALL_DIR
```

> 译注：这是一条有条件的替代路线，不是正常 SDK 安装的必做收尾。取消变量只改变当前 shell 的环境；原文并未在此要求卸载 SDK。

---

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：术语表](P006_术语表.md) · [本模块主线目录](../reading/getting_started.md) · [全部主线](../reading/README.md) · [下一篇：macOS 补充配置](P008_macOS补充配置.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章：术语表](P006_术语表.md) · [返回大纲](大纲.md) · [下一章：macOS补充配置](P008_macOS补充配置.md)

</details>

<!-- reading-navigation:end -->
