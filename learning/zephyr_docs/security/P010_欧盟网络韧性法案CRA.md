---
id: learning.zephyr-docs.security.page-10
title: 欧盟网络韧性法案CRA
kind: reference
status: maintained
domains: [zephyr, security, documentation]
source_url: https://docs.zephyrproject.org/latest/security/standards/cyber-resilience-act.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="eu-cyber-resilience-act-cra"></a>
<a id="cra-faq"></a>

# 第10章\_欧盟网络韧性法案CRA

原文：[官方页面](https://docs.zephyrproject.org/latest/security/standards/cyber-resilience-act.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> **警告（Warning，原文）**：本文仅供参考，不构成法律意见。针对具体情况的合规指导，请咨询法律顾问。也可咨询能够提供帮助的欧盟认可实验室，参见[CRA 公告机构名单（List of Notified Bodies for CRA）](https://webgate.ec.europa.eu/single-market-compliance-space/notified-bodies/free-search?filter=notificationStatus:1,legislation:167953)。

<a id="overview"></a>

## 10.1 概览（Overview）

<a id="id1"></a>

网络韧性法案（Cyber Resilience Act，[CRA24](P008_安全文献引用.md#cra24)）是欧盟法规，为投放欧盟市场的含数字要素产品（Products with Digital Elements，PDE）规定网络安全要求。它于 **2024 年 12 月 10 日**生效。

**关键日期（Key Dates）**：

- **2026 年 6 月 11 日**：评估机构开始运作；确定市场监督机构。
- **2026 年 9 月 11 日**：制造商必须报告正在被利用的漏洞（actively exploited vulnerabilities）和严重事件（severe incidents）。
- **2027 年 12 月 11 日**：完整法规适用于自该日起投放市场的产品，以及在该日前投放市场、但此后进行实质性修改的产品。

本页说明 CRA 与两类主体的关系：在商业产品中使用 Zephyr 的制造商，以及作为开源软件管理者（open-source software steward）的 Zephyr 项目自身。

对于制造商，CRA 规定基本网络安全要求（[附件 I 第一部分](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_I)），以及漏洞处理和报告义务（[附件 I 第二部分](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_I)）。对于作为开源软件管理者的 Zephyr 项目，CRA 则规定一组专门义务，包括维护网络安全政策、报告正在被利用的漏洞及严重事件，并与市场监督机构合作。

<a id="for-manufacturers-using-zephyr"></a>

## 10.2 对使用 Zephyr 的制造商的要求（For Manufacturers Using Zephyr）

<a id="does-the-cra-apply-to-my-product"></a>

### 10.2.1 CRA 是否适用于我的产品（Does the CRA apply to my product?）

如果以商业目的将含数字要素产品（PDE）投放欧盟市场，CRA 就适用。这包括带有嵌入式软件的硬件设备，也包括独立软件产品。

含数字要素产品是连接到另一设备或网络的硬件和／或软件。产品范围还包括远程数据处理解决方案（Remote Data Processing Solution，RDPS）：它不属于产品本体，却是产品运行所必需的软件，例如手机应用或云服务。

CRA 适用于投放欧盟市场的最终产品或组件。根据[《蓝色指南》（Blue Guide）](https://single-market-economy.ec.europa.eu/news/blue-guide-implementation-product-rules-2022-published-2022-06-29_en)和[欧盟 CRA 指南（EU CRA Guidelines）](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)，产品首次在欧盟市场提供时，就属于“投放市场”（placing on the market）。在商业活动过程中，为在欧盟市场分销、消费或使用而供应产品，无论有偿还是免费，都属于“在欧盟市场提供”（making available on the market）。“投放市场”适用于一个产品系列的**每一件产品**，与开发或设计日期无关。

[欧盟 CRA 指南](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)进一步解释“投放市场”，包括独立软件、源代码发布和复杂产品等特定情况。

法规规定了一些市场领域的例外，例如医疗、汽车、航空电子、军事和备件。这些例外有严格条件，参见 CRA [第 2 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_2)。

<a id="which-category-does-my-product-belong-to"></a>

### 10.2.2 我的产品属于哪一类（Which category does my product belong to?）

CRA 按风险划分产品类别：**重要产品（Important Products）**见[附件 III](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_III)，**关键产品（Critical Products）**见[附件 IV](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_IV)。不在这两类中的产品视为**默认类别产品（Default）**，要求相对较低。

例如，默认类别产品通常可以采用自我评估（self-assessment），所需文档和保证要求较少；参见[应选择哪条合规路径](#compliance-path)。

| 类别（Category） | 简要说明（Short description） | Zephyr 使用场景示例（Example Zephyr Use Cases） |
| --- | --- | --- |
| 默认类别（Default） | 未列为“重要”或“关键”的含数字要素产品。 | Wi-Fi 智能灯泡或开关，例如通过 Thread／Wi-Fi 运行 Matter；用于个人健康管理的可穿戴活动追踪器或智能手表；蓝牙低功耗音频（Bluetooth LE audio）配件或无线传感器标签；连接 CAN 总线的温度传感器。 |
| 重要产品 I 类（Important, Class I） | 风险较高，通常面向消费者，执行安全或访问相关功能。 | 住宅用智能门锁或门禁读卡器；管理网络流量的路由器；联网报警系统或安全传感器；具备 AVA_VAN.1 保护级别的微控制器。 |
| 重要产品 II 类（Important, Class II） | 风险较高，用于企业、工业或基础设施场景，或承担具有特权的网络角色。 | 具备 AVA_VAN.2 或 AVA_VAN.3 保护级别的微控制器。 |
| 关键产品（Critical） | 一旦被攻破，可能严重影响关键基础设施或基本服务。 | 智能电表网关；硬件安全模块（Hardware Security Module，HSM）或智能卡固件。 |

**核心功能与集成组件（Core Functionality vs. Integration）**：

产品分类由最终产品的**核心功能（core functionality）**决定，而非其集成的各个组件，参见[第 7 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_7)。

- 在另一产品中集成重要或关键组件，例如安全元件（secure element）、嵌入式浏览器，**不会**自动使该产品成为重要或关键产品。
- 产品即使*能够*执行重要／关键类别中的功能，如果其核心功能不同，也**不视为**具有该类别的核心功能。

示例：

- 使用 Zephyr 构建网络防火墙时，核心功能是安全，因此产品属于重要产品 II 类。
- 使用 Zephyr 构建咖啡机，并利用 Zephyr 网络协议栈功能保护设备时，核心功能仍是制作咖啡，属于默认类别产品。

因此，设备使用 Zephyr 中与安全密切相关的功能，例如密码学或安全启动（secure boot），并不会因此被提升到更高风险类别。

详细分类见[附件 III](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_III)和[附件 IV](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_IV)。完整产品类别清单及技术说明见[实施条例（EU）2025/2392](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R2392)。

<a id="which-compliance-path-must-i-choose"></a>
<a id="compliance-path"></a>

### 10.2.3 应选择哪条合规路径（Which compliance path must I choose?）

CRA 按产品类别规定不同的符合性评估程序（conformity assessment procedure）。必须根据产品分类以及对协调标准（harmonized standards）的采用情况选择相应路径。

<a id="id4"></a>

**CRA 产品类别与评估路径（CRA Product Categories & Assessment Routes）**：

| 类别（Category） | 符合性评估程序（Conformity Assessment Procedure） | 是否需要公告机构参与（Notified Body involvement?） |
| --- | --- | --- |
| 默认类别（Default） | 模块 A，由制造商自我评估；或模块 B + 模块 C；或模块 H。 | 模块 A 不强制要求。 |
| 重要产品 I 类（Important Class I） | **只有完全采用《欧盟官方公报》所列协调标准时**才能采用模块 A；否则采用模块 B + 模块 C，或模块 H。 | 模块 A 不强制要求。 |
| 重要产品 II 类（Important Class II） | 模块 B + 模块 C，或模块 H。**不允许自我评估**。 | 是，强制要求。 |
| 关键产品（Critical） | **欧洲网络安全认证（European Cybersecurity Certification）**，例如 EUCC；或模块 B + 模块 C + 模块 H，等待授权法案进一步规定。 | 是，强制要求。 |

这里的“模块（Modules）”指[第 768/2008/EC 号决定](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008D0768)（新立法框架，New Legislative Framework）定义、并由 CRA [附件 VIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_VIII)作出调整的具体评估程序：

- [模块 A（Module A）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008D0768#d1e41-98-1)，即内部生产控制（Internal production control）：自行编制技术文档、进行风险评估并声明符合性，无需外部审核员。
- [模块 B（Module B）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008D0768#d1e288-98-1)，即 EC 型式检验（EC-type examination），加[模块 C（Module C）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008D0768#d1e439-98-1)，即符合型式（Conformity to type）：<a id="id2"></a>公告机构（Notified Body）[^nb]检查技术设计并颁发证书，这是模块 B；随后由制造商确保生产符合该型式，这是模块 C。
- [模块 H（Module H）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32008D0768#d1e1719-98-1)，即全面质量保证（Full Quality Assurance）：<a id="id3"></a>公告机构[^nb]审核涵盖设计、生产和测试的质量管理体系（Quality Management System，QMS）。

<a id="nb"></a>

[^nb]: 公告机构将于 **2026 年 6 月 11 日**前开始运作。

<a id="what-are-my-main-obligations-as-a-manufacturer"></a>

### 10.2.4 制造商的主要义务是什么（What are my main obligations as a manufacturer?）

CRA 主要在[第 13 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_13)规定产品要求和尽职调查，在[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)规定漏洞处理和报告。无论产品分类如何，以下核心义务均适用于含数字要素产品的制造商。

**风险评估（Risk assessment）**：在产品整个生命周期内评估并记录网络安全风险。

**尽职调查（Due diligence）**：集成第三方组件时履行尽职调查，包括 Zephyr 这样的开源软件。

**漏洞处理（Vulnerability handling）**：产品投放市场时处理漏洞，并在支持期内持续监测漏洞，原文概括为产品寿命或至少 5 年。漏洞处理包括识别硬件和软件漏洞，例如借助软件物料清单（Software Bill of Materials，SBOM）；评估其对产品的风险；风险不可接受时提供软件更新。

**事件报告（Incident reporting）**：报告影响产品且正在被利用的漏洞，以及影响项目基础设施的严重事件。该义务在支持期结束后仍持续存在。

**技术文档（Technical documentation）**：按[第 31 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_31)及[附件 VII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_VII)编制文档。

**符合性评估（Conformity assessment）**：按[第 32 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_32)及[附件 VIII](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#anx_VIII)进行符合性评估。

**CE 标志（CE marking）**：加贴 CE 标志并编制欧盟符合性声明（EU declaration of conformity）。

<a id="what-are-the-penalties-for-non-compliance"></a>

### 10.2.5 不合规会受到什么处罚（What are the penalties for non-compliance?）

- 违反[第 13 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_13)和[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)：最高罚款 15,000,000 欧元，或全球年度营业额的 2.5%。
- 违反其他义务：最高罚款 10,000,000 欧元，或营业额的 2%。

<a id="what-are-the-vulnerability-reporting-obligations"></a>
<a id="cra-vulnerability-reporting-obligations"></a>

### 10.2.6 漏洞报告义务有哪些（What are the vulnerability reporting obligations?）

CRA 区分“普通”漏洞与会触发[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)严格通知时限的情况。普通漏洞通过正常漏洞管理流程处理；触发严格时限的是**正在被利用的漏洞**和**严重事件**。

下表概括最低限度的报告步骤。

<a id="id5"></a>

**正在被利用的漏洞（Actively exploited vulnerabilities）**——[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)第（1）和（2）款：

| 步骤（Step） | 期限（Deadline） | 最低报告内容（Content, minimum） |
| --- | --- | --- |
| 早期预警（Early warning） | 知悉后 24 小时内 | 通过统一报告平台通知所属计算机安全事件响应团队（Computer Security Incident Response Team，CSIRT）协调方和欧盟网络安全局（ENISA），说明正在被利用的漏洞影响了产品；如已知，还应说明产品在哪些成员国提供。 |
| 漏洞通知（Vulnerability notification） | 知悉后 72 小时内 | 提供受影响产品的基本信息、利用行为与漏洞的一般性质、已采取的纠正或缓解措施，以及用户可采取的措施；适用时说明所报告信息的敏感程度。 |
| 最终报告（Final report） | 纠正或缓解措施可用后最迟 14 天 | 说明漏洞、严重程度和影响；如有，提供利用漏洞的恶意行为者信息；详细说明已提供的安全更新或其他纠正措施。 |

<a id="id6"></a>

**严重事件（Severe incidents）**——[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)第（3）至（6）款：

| 步骤（Step） | 期限（Deadline） | 最低报告内容（Content, minimum） |
| --- | --- | --- |
| 早期预警（Early warning） | 知悉后 24 小时内 | 通过统一报告平台通知所属 CSIRT 协调方和 ENISA，说明严重事件影响了产品安全；指出是否怀疑由违法或恶意行为导致；如已知，还应说明产品在哪些成员国提供。 |
| 事件通知（Incident notification） | 知悉后 72 小时内 | 提供事件性质的基本信息、初步评估，包括当时已知的影响和严重程度、已采取的纠正或缓解措施，以及用户可采取的措施；适用时说明所报告信息的敏感程度。 |
| 最终报告（Final report） | 事件通知后 1 个月内 | 详细说明事件，包括严重程度和影响、威胁类型或可能的根本原因，以及已实施和正在实施的缓解措施。 |

<a id="how-can-i-obtain-an-sbom-software-bill-of-materials"></a>

### 10.2.7 如何获取软件物料清单（How can I obtain an SBOM (Software Bill of Materials)?）

Zephyr 可以使用 `west spdx` 命令为应用自动生成软件物料清单（SBOM）。

有关配置与使用方式，参见[软件物料清单：west spdx](../west/P008_其他Zephyr扩展命令.md#west-spdx)。

<a id="how-should-i-handle-zephyr-vulnerabilities"></a>

### 10.2.8 如何处理 Zephyr 漏洞（How should I handle Zephyr vulnerabilities?）

将 Zephyr 集成到产品中的制造商仍须负责漏洞管理，并在适用时履行 CRA 报告义务。Zephyr 提供漏洞信息，制造商必须针对自己的产品评估并采取行动。

可采用以下工作流程：

1. **持续获取信息（Stay informed）**：加入[Zephyr 漏洞警报登记系统（Zephyr Vulnerability Alert Registry）](https://www.zephyrproject.org/vulnerability-registry/)，在漏洞披露时接收通知。
2. **评估影响（Assess impact）**：针对每份公告，结合 SBOM 和配置，判断受影响的 Zephyr 组件是否存在于产品中、是否可达，以及是否与产品安全相关。
3. **规划修复（Plan remediation）**：决定适当应对方式，例如应用补丁或调整配置。
4. **部署修复（Deploy fixes）**：集成、测试并部署选定修复，根据需要更新 SBOM 和产品文档。
5. **履行报告义务（Meet reporting obligations）**：如果漏洞影响产品且正在被利用，或导致严重事件，应遵守[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)时限，并按前述[漏洞报告义务](#cra-vulnerability-reporting-obligations)执行报告。

<a id="what-timelines-does-zephyr-follow-for-vulnerability-handling"></a>

### 10.2.9 Zephyr 遵循怎样的漏洞处理时间表（What timelines does Zephyr follow for vulnerability handling?）

Zephyr 运行自己的产品安全事件响应团队（Product Security Incident Response Team，PSIRT）流程，为分诊（triage）、通知和披露设定目标时间。这些是**项目时间表**，不是制造商的法定期限。

制造商在**知悉**自己的产品受到正在被利用的漏洞或严重事件影响时，即触发[第 14 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_14)的 CRA 报告义务。这个时间点可能**早于**下列某些 Zephyr 里程碑，因此可能必须在 Zephyr 修复可用或公开披露之前，就发出早期预警或事件报告。

Zephyr 使用私密 GitHub 安全公告（private security advisories）以及最长 90 天的保密期（embargo period）协调修复和披露。完整流程见[安全漏洞报告](P007_安全漏洞报告.md#reporting)，关键里程碑如下：

- **7 天内**：PSIRT 向最初报告者反馈。
- **30 天内**：通过警报登记系统通知制造商，并由项目提供修复。
- **总计最长 90 天**：安全敏感漏洞在保密期结束后公开。

<a id="do-i-need-to-report-vulnerabilities-i-find-in-zephyr"></a>

### 10.2.10 是否需要报告发现的 Zephyr 漏洞（Do I need to report vulnerabilities I find in Zephyr?）

**需要。**根据[第 13 条第（6）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#013.006)，如果发现集成到产品中的组件，包括 Zephyr，存在漏洞，就**必须**报告。此外，如果为该漏洞开发了修复，还必须分享相关代码或文档。参见[安全漏洞报告](P007_安全漏洞报告.md#reporting)。

另外，也可考虑依据[第 15 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_15)向 CSIRT 或 ENISA 自愿报告。

<a id="for-zephyr-as-an-open-source-steward"></a>

## 10.3 Zephyr 作为开源软件管理者的要求（For Zephyr as an Open Source Steward）

<a id="what-is-zephyr-s-role-under-the-cra"></a>

### 10.3.1 Zephyr 在 CRA 下承担什么角色（What is Zephyr’s role under the CRA?）

Zephyr 属于[第 3 条](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#art_3)第（14）项所述的**开源软件管理者（open-source software steward）**：系统性、持续支持开发旨在用于商业活动的含数字要素产品的法人。

Zephyr 根据第 24 条承担以下义务：

**网络安全政策（Cybersecurity policy）**：将安全政策和漏洞处理流程文档化。

**合作（Cooperation）**：与市场监督机构合作，降低风险。

**事件报告（Incident reporting）**：报告项目中正在被利用的漏洞，以及影响 Zephyr 基础设施的严重事件，范围限于 Zephyr 参与的部分。

<a id="does-the-cra-apply-to-zephyr-contributors"></a>

### 10.3.2 CRA 是否适用于 Zephyr 贡献者（Does the CRA apply to Zephyr contributors?）

**不适用。**CRA 不适用于 Zephyr 的个人贡献者，参见[序言第 18 段（Recital 18）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#rct_18)。

开发功能或修复缺陷的贡献者不受 CRA 义务约束。

<a id="how-is-zephyr-meeting-its-steward-obligations"></a>

### 10.3.3 Zephyr 如何履行管理者义务（How is Zephyr meeting its steward obligations?）

**[第 24 条第（1）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#024.001)：安全政策，已完成（Complete）**：

- 文档见[Zephyr 安全概览](P002_Zephyr安全概览.md#security-overview)。
- 漏洞报告流程见[安全漏洞报告](P007_安全漏洞报告.md#reporting)。
- 安全编码指南见[安全编码](P003_安全编码.md#secure-code)。

**[第 24 条第（2）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#024.002)：与主管机构合作，进行中（In Progress）**：

- 自 2017 年起成为注册的 CVE 编号机构（CVE Numbering Authority，CNA）。
- Zephyr 项目安全事件响应团队（PSIRT）持续运作。
- **进行中**：确定欧盟 CSIRT 协调方。

**[第 14 条第（1）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#014.001)与[第（3）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#014.003)：事件报告，进行中（In Progress）**：

- **进行中**：确定美国国家漏洞数据库（National Vulnerability Database，NVD）流程是否适用于 CSIRT／ENISA 报告。
- 计划与欧盟报告要求保持一致。

**[第 14 条第（8）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#014.008)：用户通知，已完成（Complete）**：

- 面向制造商和集成商的漏洞警报登记系统。
- CVE 发布和安全公告。

**[第 52 条第（3）款](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847#052.003)：纠正措施，已完成（Complete）**：

- 已与 CVE 主管机构建立流程。
- 通过 PSIRT 及时响应。

> 译注——状态边界：上面的完成／进行中状态来自本次读取的官方页面，描述 Zephyr 项目流程；不能据此认定某个下游产品已经完成合规评估。

<a id="external-resources"></a>

## 10.4 外部资源（External Resources）

<a id="official-cra-documentation"></a>

### 10.4.1 CRA 官方文档（Official CRA documentation）

- [欧盟 CRA 法规 2024/2847（EU CRA Regulation 2024/2847）](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847)。
- [实施条例（EU）2025/2392](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R2392)：重要及关键产品类别的技术说明。
- [ENISA CRA 要求与标准映射（Requirements-Standards Mapping）](https://www.enisa.europa.eu/publications/cyber-resilience-act-requirements-standards-mapping)。
- [欧盟委员会 CRA 常见问题（FAQ）](https://digital-strategy.ec.europa.eu/en/faqs/cyber-resilience-act-questions-and-answers)。
- [欧盟委员会 CRA 指南](https://digital-strategy.ec.europa.eu/en/library/commission-publishes-new-guidance-support-timely-cyber-resilience-act-implementation)：解答许多法规解释问题。

<a id="standards-and-technical-specifications"></a>

### 10.4.2 标准与技术规范（Standards and Technical Specifications）

相关既有标准如下。

欧洲电信标准协会（ETSI）与欧洲标准化委员会／欧洲电工标准化委员会（CEN/CENELEC）正在响应[CRA 标准化请求（Standardisation Request，M/606）](https://ec.europa.eu/growth/tools-databases/enorm/mandate/606_en)制定协调标准。

CEN/CENELEC 制定的 CRA 横向标准（horizontal standards）包括：

- **EN40000-1-1**：词汇定义（Vocabulary definition）。
- **EN40000-1-2**：开发安全设计产品（Secure by Design product）的质量流程，包括风险评估、采购尽职调查、开发、测试、验证、制造、退役等。
- **EN40000-1-3**：漏洞处理流程（Vulnerability handling process）。
- **EN40000-1-4**：安全控制（Security controls），即降低网络安全风险的技术方案；基于为 CE 无线电设备指令（Radio Equipment Directive，RED）授权法案制定的 hEN18031-x 标准。

EN40000-1-4 早期草案介绍可在 CEN/CENELEC 网站查阅：[安全控制（Security Controls）](https://www.cencenelec.eu/news-events/events/2026/2026-03-05-cra-standards-unlocked-deep-dive-session-security-controls-generic-security-requirements/)。

ETSI 公开标准草案中，针对具体产品的要求包括：

- 操作系统（Operating Systems）：prEN 304 626。
- 浏览器（Browsers）：prEN 304 617。
- 密码管理器（Password Managers）：prEN 304 618。
- 防火墙（Firewalls）：prEN 304 636。

完整草案清单及公开征求意见参与方式见[ETSI 网络韧性法案门户（Cyber Resilience Act Portal）](https://docbox.etsi.org/cyber/CYBER/Open)。

- 这些标准完成协调后，欧盟、欧洲自由贸易联盟（European Free Trade Association，EFTA）及英国公民可能可以通过[协调标准平台（Harmonized standards）](https://harmonized.standards.eu/)免费获取。

<a id="educational-resources"></a>

### 10.4.3 学习资源（Educational resources）

- [Linux 基金会：理解欧盟 CRA（Understanding the EU CRA）](https://training.linuxfoundation.org/express-learning/understanding-the-eu-cyber-resilience-act-cra-lfel1001)。
- [Linux 基金会 CRA 准备情况报告（CRA Readiness Report）](https://www.linuxfoundation.org/research/cra-readiness)。
- [Linux 基金会 CRA 合规最佳实践（CRA Compliance Best Practices）](https://www.linuxfoundation.org/research/cra-compliance-best-practices)。
- [OpenSSF CRA 指南（CRA Guidance）](https://openssf.org/public-policy/eu-cyber-resilience-act/)。

<a id="zephyr-specific-resources"></a>

### 10.4.4 Zephyr 专属资源（Zephyr-specific resources）

- [Zephyr 安全概览](P002_Zephyr安全概览.md#security-overview)。
- [安全漏洞报告](P007_安全漏洞报告.md#reporting)。
- [Zephyr 漏洞警报登记系统](https://www.zephyrproject.org/vulnerability-registry/)。
- [Zephyr 漏洞记录](P020_安全漏洞总览.md#vulnerabilities)。


> 译注——外链访问记录（2026-10-14）：原文指向的 EUR-Lex 法规与条款链接本次返回 HTTP 202，未取得可核验的条文正文及锚点；协调标准平台存在证书链验证失败，ETSI 公开草案目录的直接读取返回 403。以上原链接保留，不把网络响应当作法规内容验证。ETSI 目录和 Linux 基金会课程虽然直接读取返回 403，但网页检索工具可以读取同一目录和课程页面。

对应官方文档源码：[doc/security/standards/cyber-resilience-act.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/security/standards/cyber-resilience-act.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/security/standards/cyber-resilience-act.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：安全标准与Zephyr](P009_安全标准与Zephyr.md) · [本模块主线目录](../reading/security.md) · [全部主线](../reading/README.md) · [下一篇：ETSI_303645](P011_ETSI_303645.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P009_安全标准与Zephyr.md) · [返回大纲](大纲.md) · [下一章](P011_ETSI_303645.md)

</details>

<!-- reading-navigation:end -->
