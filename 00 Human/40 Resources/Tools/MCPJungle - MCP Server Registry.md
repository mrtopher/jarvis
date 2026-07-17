---
type: resource
source: https://mcpjungle.com
date_clipped: "2026-07-17"
project:
tags: [tool, mcp, ai, gateway, self-hosted, open-source]
---

# MCPJungle - MCP Server Registry

## Summary
> Self-hosted, open-source **MCP gateway + central registry** for Model Context Protocol servers. Register your MCP servers once; every AI client/agent (Claude, Cursor, custom agents) connects through a single unified `/mcp` endpoint instead of scattered per-client configs. Solves config sprawl, duplicated setup, and inconsistent access control when a team runs many MCP servers. Directly relevant to the AI consulting work — a clean way to give a client one governed control point for all their agent tooling.

## Key Points
- **What:** one place to register, discover, group, and securely invoke tools across all your MCP servers.
- **Single endpoint:** clients/agents hit one gateway rather than configuring each server individually.
- **Supports** both streamable-HTTP MCP servers and STDIO-based servers.
- **Access control:** tool exposure via groups + enterprise access-control features; central monitoring of all client-server interactions.
- **Deployment:** self-hosted; registry/gateway runs on port 8080 by default.
- **Licensing:** open source (GitHub: mcpjungle/MCPJungle). Docs at docs.mcpjungle.com.
- **Fits:** dev/team use with Claude & Cursor, production AI agents needing secure MCP access, orgs wanting to centrally govern MCP usage.

## Connections
- Project: [[Client Acquisition]]
- Person: [[]]
- Company: [[]]
- Topic: MCP / AI agent infrastructure

## Link
- https://mcpjungle.com
- Docs: https://docs.mcpjungle.com/
- GitHub: https://github.com/mcpjungle/MCPJungle
