from Models import *


class DaoCategoria:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt','a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
            with open ('categoria.txt', 'r') as arq:
                cls.categoria = arq.readlines()

            # map(function ou Lambda, iterables)
            # lambda arguments : expression
                
            cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))  # remove \n do final de cada linha

            listaCategoria = []
            for i in cls.categoria:
                listaCategoria.append(Categoria(i))  
            
            return listaCategoria


class DaoVenda:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt','a') as arq:
            arq.writelines(venda.itensVendidos.nome + "|" + str(venda.itensVendidos.preco) + "|" + str(venda.itensVendidos.categoria) + "|" +
                           venda.vendedor + "|" + venda.comprador + "|" +str(venda.quantidadeVendida) + "|" + str(venda.Data))
            arq.writelines('\n')
    
    @classmethod
    def ler(cls):
        with open ('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))  # remove \n do final de cada linha
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))  # Transforma em lista
            
        listaVendas = []
        for inf_venda in cls.venda:
                listaVendas.append(Venda(inf_venda[0],inf_venda[1],inf_venda[2]),inf_venda[3],inf_venda[4],inf_venda[5],inf_venda[6])
        return listaVendas

class DaoEstoque:
    @classmethod
    def salvar(cls, produto: Produtos, quantidade):
        with open('estoque.txt','a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" +
                        produto.categoria + "|" + str(quantidade))
            arq .writelines( '\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt','r') as arq:
            cls.estoque = arq.readlines()
        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))  # remove \n do final de cada linha
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))  # Transforma em lista

        listaEstoque = []

        if len(cls.estoque) > 0:
            for infEstoque in cls.estoque:
                listaEstoque.append(Estoque(Produtos(infEstoque[0],infEstoque[1],infEstoque[2]),infEstoque[3]))
        return listaEstoque
    

class DaoFornecedor:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt','a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" +
                        fornecedor.telefone + "|" + fornecedor.categoria)
            arq .writelines( '\n')

    @classmethod
    def ler(cls):
        with open('fornecedor.txt','r') as arq:
            cls.fornecedor = arq.readlines()
        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))  # remove \n do final de cada linha
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))  # Transforma em lista

        listafornecedor = []

        if len(cls.fornecedor) > 0:
            for infFornecedor in cls.fornecedor:
                listafornecedor.append(Estoque(Fornecedor(infFornecedor[0],infFornecedor[1],infFornecedor[2]),infFornecedor[3]))
        return listafornecedor
    
class DaoPessoa:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoa.txt','a') as arq:
            arq.writelines(pessoa.nome + "|" + pessoa.telefone + "|" +
                        pessoa.cpf + "|" + pessoa.email + "|" + pessoa.endereco)
            arq .writelines( '\n')

    @classmethod
    def ler(cls):
        with open('pessoa.txt','r') as arq:
            cls.estoque = arq.readlines()
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))  # remove \n do final de cada linha
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))  # Transforma em lista

        clientes = []

        if len(cls.pessoa) > 0:
            for infPessoa in cls.pessoa:
                clientes.append(Pessoa(infPessoa[0],infPessoa[1],infPessoa[2]),infPessoa[3])
        return clientes
    
class DaoFuncionario:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt','a') as arq:
            arq.writelines(funcionario.nome + "|" + funcionario.telefone + "|" +
                        funcionario.cpf + "|" + funcionario.email + "|" + funcionario.endereco)
            arq .writelines( '\n')

    @classmethod
    def ler(cls):
        with open('funcionario.txt','r') as arq:
            cls.estoque = arq.readlines()
        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))  # remove \n do final de cada linha
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))  # Transforma em lista

        listafuncionario = []

        if len(cls.funcionario) > 0:
            for infFuncionario in cls.funcionario:
                listafuncionario.append(Pessoa(infFuncionario[0],infFuncionario[1],infFuncionario[2]),infFuncionario[3])
        return listafuncionario