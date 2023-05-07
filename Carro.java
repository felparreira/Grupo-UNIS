package Unid1Code1;

//declaração da classe
public class Carro{
    private String montadora, modelo, ano, cor;

    //construtor da classe
    public Carro(String montadora, String modelo, String ano, String cor){
        this.montadora = montadora;
        this.modelo = modelo;    
        this.ano = ano;    
        this.cor = cor;
    }
    public String getMontadora() {
        return montadora ;
    }
    public void setMontadora(String montadora) {
        this.montadora = montadora;
    }

    public String getModelo() {
        return modelo ;
    }
    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String geAno() {
        return ano ;
    }
    public void setAno(String ano) {
        this.ano = ano;
    }


    public String getCor() {
        return cor ;
    }
    public void setCor(String cor) {
        this.cor = cor;
    }

    //o método main() é o metodo principal da classe
    public static void main(String[] args) {
        //O objeto chamado "meuCarro" será do tipo "Carro"
        //Os valores passados são usados pelo construtor da classe para criar o objeto

        Carro meuCarro = new Carro("Volkswagem", "Polo", "2009","Prata");

        //Testando os dados da classe, imprimindo a saída simples no terminal
        System.out.println(meuCarro.getMontadora());
        System.out.println(meuCarro.getModelo());
        System.out.println(meuCarro.geAno());
        System.out.println(meuCarro.getCor());
    }
}


