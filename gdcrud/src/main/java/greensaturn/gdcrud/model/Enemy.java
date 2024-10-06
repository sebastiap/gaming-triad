package greensaturn.gdcrud.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity(name = "Enemy")
@AllArgsConstructor
@NoArgsConstructor
@Getter
@Setter
public class Enemy {

    @Id
    @Basic(optional = false)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "seq_enemy")
    @SequenceGenerator(name="seq_enemy",sequenceName = "seq_enemy")
    @Column(name = "ID",unique=true, nullable = false)
    private Integer id;
    private String name;
    private String description;
    @Column(name = "MINLIFE", nullable = false)
    private Integer min_life;
    @Column(name = "MAXLIFE", nullable = false)
    private Integer max_life;
    private String abilities;
    private String attacks;
    private String loot;

    /*
    A FUTURO USAR ESTOS
        private String[] abilities;
    private String[] attacks;
    private String[] loot;
     */


}
