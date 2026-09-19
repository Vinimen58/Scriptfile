#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib

LANGUAGES = [
    "Python","JavaScript","TypeScript","C","C++","C#","Java","Go","Rust","Kotlin",
    "Swift","PHP","Ruby","Dart","Lua","R","Julia","Scala","Groovy","Perl","Bash",
    "PowerShell","VB.NET","Fortran","Pascal","Ada","Elixir","Erlang","Clojure",
    "Common Lisp","Scheme","Racket","Nim","Crystal","D","Zig","Solidity","SQL",
    "MATLAB","Octave"
]

TOPICS = [
    ("aritmetica","calcular soma"),("aritmetica","calcular produto"),
    ("condicional","comparar dois valores"),("loop","somar intervalo"),
    ("loop","contar ocorrencias"),("string","inverter texto"),
    ("string","verificar palindromo"),("array","encontrar maior valor"),
    ("array","somar elementos"),("busca","busca linear"),
    ("busca","busca binaria"),("ordenacao","ordenar valores"),
    ("recursao","fatorial"),("recursao","fibonacci"),("matematica","mdc"),
    ("matematica","verificar primo"),("estrutura","pilha"),("estrutura","fila"),
    ("mapa","frequencia de valores"),("transformacao","filtrar pares")
]

LEVELS = ["iniciante","basico","intermediario","avancado","especialista"]
CONSTRAINTS = [
    "sem bibliotecas externas","priorizar legibilidade","priorizar memoria",
    "priorizar velocidade","usar funcao reutilizavel","incluir caso-limite",
    "evitar estado global","usar nomes descritivos"
]

FOUNDATION = r"""
CORPUS UNIVERSAL DE PROGRAMAÇÃO — EDIÇÃO MASSIVA
================================================

OBJETIVO
-------
Material sintético de estudo/pré-treinamento para um modelo de IA especializado
em programação. Parte da premissa de conhecimento zero e avança de bits e lógica
até engenharia de software, compiladores, redes, bancos de dados, sistemas
distribuídos, segurança e inteligência artificial.

PRINCÍPIO PEDAGÓGICO
--------------------
Ensinar nesta ordem:
realidade física -> representação -> bits -> números -> memória -> instruções ->
algoritmos -> sintaxe -> tipos -> estruturas de dados -> abstrações -> sistemas ->
engenharia -> especializações.

MÓDULO 1 — INFORMAÇÃO
Informação é uma representação de alguma coisa. Computadores manipulam
representações. Texto, imagens, áudio, números e programas podem ser convertidos
em sequências de bits.

MÓDULO 2 — BITS E BYTES
Bit é um dígito binário com dois estados possíveis, 0 ou 1. Oito bits formam
normalmente um byte. Estude binário, decimal, hexadecimal, complemento de dois,
overflow, endianness e unidades de armazenamento.

MÓDULO 3 — CPU E MEMÓRIA
CPU executa instruções. Memória armazena dados endereçáveis. Estude registradores,
cache, RAM, stack, heap, ponteiros, referências, memória virtual, paginação,
alocação, desalocação, garbage collection, ownership e borrowing.

MÓDULO 4 — TEXTO
Estude ASCII, Unicode, code points, grapheme clusters, UTF-8, UTF-16, UTF-32,
normalização e diferenças entre bytes, caracteres e unidades de código.

MÓDULO 5 — ALGORITMOS
Algoritmo é uma sequência finita de passos para resolver um problema. Para cada
algoritmo ensine pré-condições, pós-condições, invariantes, correção, complexidade,
casos extremos, implementação e testes.

MÓDULO 6 — LINGUAGENS
Ensine sintaxe, semântica, tipos, escopo, funções, módulos, erros, bibliotecas,
toolchain e convenções das principais linguagens de sistemas, web, mobile,
ciência, dados, hardware, automação e contratos inteligentes.

MÓDULO 7 — ESTRUTURAS DE DADOS
Arrays, vectors, listas ligadas, stacks, queues, deques, hash maps, sets, heaps,
árvores, tries, grafos, union-find, bloom filters, skip lists, segment trees,
Fenwick trees, B-trees e B+ trees.

MÓDULO 8 — COMPLEXIDADE
Big-O, Big-Theta, Big-Omega, O(1), O(log n), O(n), O(n log n), O(n²), O(n³),
O(2^n), O(n!), análise amortizada, memória e desempenho real.

MÓDULO 9 — PARADIGMAS
Imperativo, procedural, orientação a objetos, funcional, declarativo, lógico,
reativo, orientado a eventos, data-oriented, actor model, concorrência e
paralelismo.

MÓDULO 10 — COMPILADORES
Lexer, parser, AST, análise semântica, resolução de nomes, type checking, IR,
SSA, otimização, code generation, linking, loading, JIT e AOT.

MÓDULO 11 — SISTEMAS OPERACIONAIS
Processos, threads, scheduling, syscalls, memória virtual, filesystem, sinais,
IPC, sockets, sincronização, mutexes, semáforos e deadlocks.

MÓDULO 12 — REDES
Ethernet, IP, TCP, UDP, DNS, TLS, HTTP, HTTP/2, HTTP/3, QUIC, WebSocket, NAT,
ports, sockets, congestion control, timeouts, retries e idempotência.

MÓDULO 13 — BANCO DE DADOS
Modelo relacional, SQL, normalização, índices, joins, transactions, ACID,
isolation, locking, MVCC, query planner, replication, partitioning e sharding.

MÓDULO 14 — ENGENHARIA DE SOFTWARE
Requisitos, modularidade, coesão, acoplamento, abstração, encapsulamento, SOLID,
DRY, KISS, YAGNI, refatoração, code review, documentação e versionamento.

MÓDULO 15 — TESTES E DEPURAÇÃO
Unit, integration, E2E, property-based, fuzzing, mutation testing, regressão,
debuggers, logs, traces, profilers, sanitizers e análise de causa raiz.

MÓDULO 16 — SEGURANÇA
Validação de entrada, autenticação, autorização, least privilege, SQL injection,
XSS, CSRF, SSRF, path traversal, command injection, memory safety, secrets,
criptografia e segurança de dependências.

MÓDULO 17 — WEB
HTML, CSS, DOM, JavaScript, TypeScript, acessibilidade, responsividade, rendering,
HTTP, cookies, sessions, CORS, CSP, REST, GraphQL, SSR, CSR, SSG e caching.

MÓDULO 18 — CONCORRÊNCIA
Processos, threads, async, coroutines, futures, promises, goroutines, channels,
actors, atomics, locks, races, deadlocks, livelocks, starvation e memory models.

MÓDULO 19 — SISTEMAS DISTRIBUÍDOS
Latência, falhas parciais, clocks, ordering, replication, consensus, Raft, Paxos,
CAP, eventual consistency, quorum, leader election, retries, queues, Kafka,
event sourcing e CQRS.

MÓDULO 20 — DEVOPS E CLOUD
Git, CI/CD, containers, Docker, Kubernetes, Terraform, observability, métricas,
logs, traces, autoscaling, load balancing, blue-green e canary deployment.

MÓDULO 21 — IA
Álgebra linear, cálculo, probabilidade, otimização, regressão, classificação,
redes neurais, backpropagation, embeddings, CNN, RNN, attention, transformers,
tokenização, fine-tuning, LoRA, RAG, avaliação e inferência.

Cada conceito deve ser ensinado em seis fases:
1. definição; 2. intuição; 3. exemplo mínimo; 4. contraexemplo;
5. exercício; 6. aplicação real.
"""

def snippet(lang, task, a, b, c):
    t = task % 10
    if lang == "Python":
        s = [
            f"a,b={a},{b}\nprint(a+b)",
            f"a,b={a},{b}\nprint(a*b)",
            f"a,b={a},{b}\nprint(max(a,b))",
            f"print(sum(range(1,{a%20+2})))",
            f"x=[{a},{b},{c}]\nprint(sum(x))",
            f"s='item{a}'\nprint(s[::-1])",
            f"s='aba{a%10}aba'\nprint(s==s[::-1])",
            f"x=[{a},{b},{c}]\nprint(max(x))",
            f"x=[{a},{b},{c}]\nprint([v for v in x if v%2==0])",
            f"x=[{a},{b},{c}]\nprint(next((i for i,v in enumerate(x) if v=={b}),-1))"
        ]
        return s[t]
    if lang in ("JavaScript","TypeScript"):
        decl = "const" if lang=="JavaScript" else "const"
        return [
            f"{decl} a={a},b={b}; console.log(a+b);",
            f"{decl} a={a},b={b}; console.log(a*b);",
            f"{decl} a={a},b={b}; console.log(Math.max(a,b));",
            f"let s=0; for(let i=1;i<={a%20+1};i++) s+=i; console.log(s);",
            f"const x=[{a},{b},{c}]; console.log(x.reduce((p,v)=>p+v,0));",
            f"const s='item{a}'; console.log([...s].reverse().join(''));",
            f"const s='aba{a%10}aba'; console.log(s===[...s].reverse().join(''));",
            f"const x=[{a},{b},{c}]; console.log(Math.max(...x));",
            f"const x=[{a},{b},{c}]; console.log(x.filter(v=>v%2===0));",
            f"const x=[{a},{b},{c}]; console.log(x.indexOf({b}));"
        ][t]
    if lang == "SQL":
        return [
            f"SELECT {a}+{b} AS result;", f"SELECT {a}*{b} AS result;",
            f"SELECT CASE WHEN {a}>{b} THEN {a} ELSE {b} END AS result;",
            f"WITH RECURSIVE t(n) AS (SELECT 1 UNION ALL SELECT n+1 FROM t WHERE n<{a%20+1}) SELECT SUM(n) FROM t;",
            f"SELECT {a}+{b}+{c} AS total;", f"SELECT REVERSE('item{a}');",
            f"SELECT {a%10+1}*{a%10+1} AS square;", f"SELECT GREATEST({a},{b},{c});",
            f"SELECT v FROM (VALUES ({a}),({b}),({c})) AS t(v) WHERE MOD(v,2)=0;",
            f"SELECT CASE WHEN {b}={a} THEN 0 ELSE 1 END AS idx;"
        ][t]
    return (
        f"// Exemplo conceitual em {lang}\n"
        f"// a={a}, b={b}, c={c}\n"
        f"// objetivo: {TOPICS[task % len(TOPICS)][1]}\n"
        "// Consulte a especificação oficial da linguagem para a sintaxe de produção."
    )

def generate(path: Path, total: int):
    with path.open("w", encoding="utf-8", buffering=1024*1024) as f:
        f.write(FOUNDATION)
        f.write("\n\nLINGUAGENS COBERTAS\n===================\n")
        f.write(", ".join(LANGUAGES))
        f.write(f"\n\nINÍCIO DOS {total:,} EXEMPLOS\n".replace(",", "."))
        f.write("="*80+"\n")
        for i in range(1,total+1):
            li=(i-1)%len(LANGUAGES)
            ti=((i-1)//len(LANGUAGES))%len(TOPICS)
            lvl=LEVELS[((i-1)//(len(LANGUAGES)*len(TOPICS)))%len(LEVELS)]
            con=CONSTRAINTS[((i-1)//(len(LANGUAGES)*len(TOPICS)*len(LEVELS)))%len(CONSTRAINTS)]
            lang=LANGUAGES[li]
            cat,obj=TOPICS[ti]
            a=(i*37)%997+1
            b=(i*53)%991+1
            c=(i*97)%983+1
            h=hashlib.blake2s(f"{i}|{lang}|{ti}|{a}|{b}|{c}".encode(),digest_size=4).hexdigest()
            code=snippet(lang,ti,a,b,c)
            f.write(
                f"\n### EXEMPLO {i:07d} [{h}]\n"
                f"LINGUAGEM: {lang}\nCATEGORIA: {cat}\nNÍVEL: {lvl}\n"
                f"OBJETIVO: {obj}\nRESTRIÇÃO: {con}\n"
                f"ENTRADAS: a={a}, b={b}, c={c}\nCÓDIGO:\n{code}\n"
                "EXPLICAÇÃO: acompanhe o estado, aplique a semântica da linguagem e valide com testes.\n"
            )

if __name__ == "__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--examples",type=int,default=1_000_000)
    p.add_argument("--output",default="corpus_universal_programacao_1M_exemplos.txt")
    args=p.parse_args()
    generate(Path(args.output),args.examples)
    print(f"Criado: {args.output}")
