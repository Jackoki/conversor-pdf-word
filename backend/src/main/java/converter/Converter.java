package converter;

import java.nio.file.Path;

import javax.management.RuntimeErrorException;

import org.springframework.stereotype.Component;

@Component
public class Converter {
    public void convert(Path pathInputArchive, Path pathOutputArchive) {
        try {
            ProcessBuilder processBuilder = new ProcessBuilder("soffice", "--headless", "--convert-to", "docx", "--outdir", pathOutputArchive.toString(), pathInputArchive.toString());
            executeProcess(processBuilder);
        }

        catch (Exception e){
            throw new RuntimeException("Falha durante a conversão", e);
        }
    }

    private void executeProcess(ProcessBuilder processBuilder) throws Exception {
        Process process = processBuilder.start();
        int exitCode = process.waitFor();

        if(exitCode != 0) {                
            throw new RuntimeException("Falha ao executar o processo de conversão");
        }
    }
}
