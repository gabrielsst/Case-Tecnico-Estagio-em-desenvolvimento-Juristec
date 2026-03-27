SELECT 
    c.nome,
    p.assunto,
    p.data_abertura
FROM clientes c
INNER JOIN processos p
    ON c.id_cliente = p.id_cliente
WHERE c.estado = 'SP'
  AND p.data_abertura >= DATE '2023-01-01'
  AND p.data_abertura < DATE '2024-01-01';